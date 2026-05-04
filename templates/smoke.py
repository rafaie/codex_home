#!/usr/bin/env python3
"""Smoke harness template (live-first, no UI).

This is a starter script for downstream repos. It executes tiny smoke scenarios
through subprocess entrypoints, writes a required artifact bundle, classifies
failures, and returns standardized exit codes.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - template fallback
    yaml = None

ARTIFACT_VERSION = "1"

EXIT_CODES = {
    "pass": 0,
    "config_error": 10,
    "fixture_error": 10,
    "auth": 10,
    "permission_error": 10,
    "artifact_error": 12,
    "subprocess_error": 20,
    "network_error": 22,
    "timeout": 23,
    "rate_limit": 24,
    "quota_exceeded": 25,
    "provider_error": 26,
    "invalid_response": 30,
    "parse_error": 30,
    "schema_error": 40,
    "invariant_error": 41,
    "golden_mismatch": 50,
    "budget_exceeded": 55,
    "internal_error": 60,
}

PRIORITY = [
    "artifact_error",
    "config_error",
    "fixture_error",
    "auth",
    "permission_error",
    "quota_exceeded",
    "rate_limit",
    "network_error",
    "timeout",
    "provider_error",
    "subprocess_error",
    "invalid_response",
    "parse_error",
    "schema_error",
    "invariant_error",
    "golden_mismatch",
    "budget_exceeded",
    "internal_error",
]

DEFAULT_TIME_BUDGET_SEC = 60
DEFAULT_MAX_REQUESTS = 6
DEFAULT_MAX_TOKENS = 256
DEFAULT_MAX_TOKENS_TOTAL = 1200


@dataclass
class CaseResult:
    case_id: str
    status: str
    failure_bucket: str
    secondary_buckets: list[str]
    elapsed_sec: float
    entrypoint: list[str]
    fixture: str | None
    returncode: int | None
    stdout: str
    stderr: str
    parsed_output: dict[str, Any] | list[Any] | None
    validation: dict[str, Any]


def _has_live_credentials() -> bool:
    if os.getenv("SMOKE_LIVE") == "1":
        return True
    keys = [
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GOOGLE_API_KEY",
        "AZURE_OPENAI_API_KEY",
    ]
    return any(bool(os.getenv(k)) for k in keys)


def _default_mode() -> str:
    return "live" if _has_live_credentials() else "offline"


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Run smoke scenarios and write artifacts.")
    p.add_argument("--mode", choices=["live", "offline"], default=None)
    p.add_argument("--run-profile", choices=["manual", "nightly", "both"], default="manual")
    p.add_argument("--work-item", default=None)
    p.add_argument("--feature", default=None, help="Deprecated alias for --work-item.")
    p.add_argument("--scenario", default=None)
    p.add_argument("--providers", default=None)
    p.add_argument("--max-cases", type=int, default=1)
    p.add_argument("--seed", type=int, default=1337)
    p.add_argument("--time-budget-sec", type=int, default=None)
    p.add_argument("--max-requests", type=int, default=None)
    p.add_argument("--max-tokens", type=int, default=None)
    p.add_argument("--max-tokens-total", type=int, default=None)
    p.add_argument("--cost-ceiling-usd", type=float, default=None)
    p.add_argument("--temperature", type=float, default=0.0)
    p.add_argument("--output-dir", default=None)
    p.add_argument("--redact-secrets", choices=["true", "false"], default="true")
    p.add_argument("--record", action="store_true", help="Intentionally update goldens.")
    p.add_argument("--registry", default="spec/smoke_registry.yaml")
    return p


def _now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def _redact(text: str, enabled: bool) -> str:
    if not enabled:
        return text
    redacted = text
    sensitive_env_names = (
        "API_KEY",
        "TOKEN",
        "SECRET",
        "PASSWORD",
        "CREDENTIAL",
        "PRIVATE_KEY",
    )
    for name, value in os.environ.items():
        if not value or len(value) < 8:
            continue
        if any(marker in name.upper() for marker in sensitive_env_names):
            redacted = redacted.replace(value, "REDACTED")

    patterns = [
        r"Bearer\s+[A-Za-z0-9._~+/=-]+",
        r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*['\"]?[^'\"\s,}]+",
        r"sk-[A-Za-z0-9_-]{16,}",
        r"gh[pousr]_[A-Za-z0-9_]{20,}",
    ]
    for pattern in patterns:
        redacted = re.sub(pattern, "REDACTED", redacted)
    return redacted


def _load_registry(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"Registry not found: {path}")
    if yaml is None:
        raise RuntimeError("PyYAML is required to parse smoke_registry.yaml")
    content = _safe_read(path)
    data = yaml.safe_load(content) or {}
    if not isinstance(data, dict):
        raise ValueError("Registry content must be a mapping")
    return data


def _matches_mode(scenario: dict[str, Any], mode: str) -> bool:
    scenario_mode = str(scenario.get("mode") or "both").lower()
    return scenario_mode in ("both", "any") or scenario_mode == mode


def _matches_profile(scenario: dict[str, Any], run_profile: str) -> bool:
    scenario_profile = str(scenario.get("run_profile") or "both").lower()
    if run_profile == "both":
        return True
    return scenario_profile in ("both", run_profile)


def _select_scenarios(
    data: dict[str, Any],
    work_item: str | None,
    scenario: str | None,
    max_cases: int,
    mode: str,
    run_profile: str,
) -> list[dict[str, Any]]:
    scenarios = data.get("scenarios", [])
    if not isinstance(scenarios, list):
        return []
    out: list[dict[str, Any]] = []
    for s in scenarios:
        if not isinstance(s, dict):
            continue
        if not s.get("enabled", True):
            continue
        scenario_work_item = s.get("work_item") or s.get("feature")
        if work_item and scenario_work_item != work_item:
            continue
        if scenario and s.get("id") != scenario:
            continue
        if not _matches_mode(s, mode):
            continue
        if not _matches_profile(s, run_profile):
            continue
        out.append(s)
    return out[: max(1, max_cases)]


def _scenario_budget_values(scenarios: list[dict[str, Any]], key: str) -> list[Any]:
    values: list[Any] = []
    for scenario in scenarios:
        budgets = scenario.get("budgets") or {}
        if isinstance(budgets, dict) and budgets.get(key) is not None:
            values.append(budgets[key])
    return values


def _resolve_int_budget(
    cli_value: int | None,
    scenarios: list[dict[str, Any]],
    key: str,
    default: int,
) -> int:
    if cli_value is not None:
        return cli_value
    values = [int(v) for v in _scenario_budget_values(scenarios, key) if isinstance(v, (int, float))]
    return min(values) if values else default


def _resolve_float_budget(
    cli_value: float | None,
    scenarios: list[dict[str, Any]],
    key: str,
) -> float | None:
    if cli_value is not None:
        return cli_value
    values = [
        float(v)
        for v in _scenario_budget_values(scenarios, key)
        if isinstance(v, (int, float))
    ]
    return min(values) if values else None


def _command_string() -> str:
    return " ".join(shlex.quote(part) for part in sys.argv)


def _provider_stats(scenarios: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    stats: dict[str, dict[str, Any]] = {}
    for scenario in scenarios:
        providers = scenario.get("providers") or []
        if not isinstance(providers, list) or not providers:
            key = "unspecified"
            stats.setdefault(key, {"provider": None, "model": None, "cases": 0})
            stats[key]["cases"] += 1
            continue
        for provider_entry in providers:
            if not isinstance(provider_entry, dict):
                continue
            provider = provider_entry.get("provider")
            model = provider_entry.get("model")
            key = f"{provider or 'unknown'}:{model or 'unknown'}"
            stats.setdefault(key, {"provider": provider, "model": model, "cases": 0})
            stats[key]["cases"] += 1
    return stats


def _selected_ids(scenarios: list[dict[str, Any]]) -> list[str]:
    return [str(s.get("id", "unknown")) for s in scenarios]


def _fixture_paths(scenarios: list[dict[str, Any]]) -> list[str]:
    fixtures = []
    for scenario in scenarios:
        fixture = scenario.get("dataset_fixture")
        if fixture:
            fixtures.append(str(fixture))
    return fixtures


def _detect_bucket(stderr: str, returncode: int | None, timed_out: bool) -> str:
    text = stderr.lower()
    if timed_out:
        return "timeout"
    if returncode not in (None, 0):
        if "rate" in text and "limit" in text:
            return "rate_limit"
        if "quota" in text:
            return "quota_exceeded"
        if "auth" in text or "unauthorized" in text or "forbidden" in text:
            return "auth"
        if "network" in text or "dns" in text or "connection" in text:
            return "network_error"
        return "subprocess_error"
    return "pass"


def _run_case(scenario: dict[str, Any], timeout_sec: int, redact_secrets: bool) -> CaseResult:
    case_id = str(scenario.get("id", "unknown"))
    fixture = scenario.get("dataset_fixture")
    entrypoint = (scenario.get("entrypoint") or {}).get("cmd")
    if not isinstance(entrypoint, list) or not entrypoint:
        return CaseResult(
            case_id=case_id,
            status="failed",
            failure_bucket="config_error",
            secondary_buckets=[],
            elapsed_sec=0.0,
            entrypoint=[],
            fixture=str(fixture) if fixture else None,
            returncode=None,
            stdout="",
            stderr="missing entrypoint.cmd in scenario",
            parsed_output=None,
            validation={"schema": False, "invariants": False},
        )

    start = time.perf_counter()
    timed_out = False
    try:
        proc = subprocess.run(
            entrypoint,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            check=False,
            cwd=(scenario.get("entrypoint") or {}).get("cwd") or ".",
        )
        rc = proc.returncode
        stdout = _redact(proc.stdout, redact_secrets)
        stderr = _redact(proc.stderr, redact_secrets)
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        rc = None
        stdout = _redact(exc.stdout or "", redact_secrets)
        stderr = _redact(exc.stderr or "", redact_secrets)
    elapsed = time.perf_counter() - start

    bucket = _detect_bucket(stderr, rc, timed_out)
    parsed_output: dict[str, Any] | list[Any] | None = None
    validation = {"schema": False, "invariants": False}

    # Fail closed for template consumers: successful subprocess execution is not
    # enough; smoke must also produce structurally valid output.
    if bucket == "pass":
        try:
            parsed_output = json.loads(stdout) if stdout.strip() else None
        except json.JSONDecodeError:
            bucket = "parse_error"

    if bucket == "pass":
        validation["schema"] = isinstance(parsed_output, (dict, list))
        if not validation["schema"]:
            bucket = "schema_error"

    if bucket == "pass":
        validation["invariants"] = bool(parsed_output)
        if not validation["invariants"]:
            bucket = "invariant_error"

    status = "passed" if bucket == "pass" else "failed"

    return CaseResult(
        case_id=case_id,
        status=status,
        failure_bucket=bucket,
        secondary_buckets=[],
        elapsed_sec=elapsed,
        entrypoint=entrypoint,
        fixture=str(fixture) if fixture else None,
        returncode=rc,
        stdout=stdout,
        stderr=stderr,
        parsed_output=parsed_output,
        validation=validation,
    )


def _ensure_dirs(base: Path) -> tuple[Path, Path]:
    cases_dir = base / "cases"
    base.mkdir(parents=True, exist_ok=True)
    cases_dir.mkdir(parents=True, exist_ok=True)
    return base, cases_dir


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _pick_exit_bucket(buckets: list[str]) -> str:
    if not buckets:
        return "pass"
    unique = set(buckets)
    for bucket in PRIORITY:
        if bucket in unique:
            return bucket
    return "internal_error"


def _write_run_level_failure(
    output_dir: Path,
    bucket: str,
    mode: str,
    run_profile: str,
    work_item: str | None,
    errors: list[str],
    start_ts: float,
) -> None:
    case_id = bucket
    case_payload = {
        "case_id": case_id,
        "status": "failed",
        "failure_bucket": bucket,
        "secondary_buckets": [],
        "input_pointer": None,
        "input_hash": None,
        "request_params": {},
        "entrypoint": [],
        "fixture": None,
        "returncode": None,
        "elapsed_sec": 0.0,
        "raw_response": None,
        "parsed_output": None,
        "validation": {"schema": False, "invariants": False},
        "stdout": "",
        "stderr": "\n".join(errors),
    }
    _write_json(output_dir / "cases" / f"{case_id}.json", case_payload)
    _write_json(
        output_dir / "summary.json",
        {
            "artifact_version": ARTIFACT_VERSION,
            "status": "failed",
            "mode": mode,
            "run_profile": run_profile,
            "work_item": work_item,
            "command": _command_string(),
            "artifact_path": str(output_dir),
            "selected_scenarios": [],
            "fixtures": [],
            "provider_stats": {},
            "budgets": {
                "time_budget_sec": DEFAULT_TIME_BUDGET_SEC,
                "max_requests": DEFAULT_MAX_REQUESTS,
                "max_tokens": DEFAULT_MAX_TOKENS,
                "max_tokens_total": DEFAULT_MAX_TOKENS_TOTAL,
                "cost_ceiling_usd": None,
                "requests_used": 0,
                "time_budget_exceeded": False,
            },
            "record": False,
            "counts": {bucket: 1},
            "failure_bucket": bucket,
            "errors": errors,
            "cases_total": 0,
            "case_artifacts": [str(output_dir / "cases" / f"{case_id}.json")],
        },
    )
    _write_json(
        output_dir / "timing.json",
        {
            "wall_clock_sec": time.perf_counter() - start_ts,
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "cmd": _command_string(),
        },
    )


def main() -> int:
    args = _build_parser().parse_args()
    mode = args.mode or _default_mode()
    run_profile = args.run_profile
    work_item = args.work_item or args.feature
    start_ts = time.perf_counter()

    output_dir = Path(args.output_dir or f"artifacts/smoke/{_now_stamp()}")
    _ensure_dirs(output_dir)

    logs: list[str] = []
    errors: list[str] = []
    logs.append(f"mode={mode}")

    try:
        registry = _load_registry(Path(args.registry))
    except FileNotFoundError as exc:
        errors.append(str(exc))
        bucket = "config_error"
        _write_run_level_failure(output_dir, bucket, mode, run_profile, work_item, errors, start_ts)
        (output_dir / "stdout.txt").write_text("\n".join(logs) + "\n", encoding="utf-8")
        (output_dir / "stderr.txt").write_text("\n".join(errors) + "\n", encoding="utf-8")
        return EXIT_CODES[bucket]
    except Exception as exc:  # pragma: no cover - template guard
        errors.append(str(exc))
        bucket = "internal_error"
        _write_run_level_failure(output_dir, bucket, mode, run_profile, work_item, errors, start_ts)
        (output_dir / "stdout.txt").write_text("\n".join(logs) + "\n", encoding="utf-8")
        (output_dir / "stderr.txt").write_text("\n".join(errors) + "\n", encoding="utf-8")
        return EXIT_CODES[bucket]

    selected = _select_scenarios(
        registry,
        work_item,
        args.scenario,
        args.max_cases,
        mode,
        run_profile,
    )
    if not selected:
        errors.append("No enabled scenarios matched filters")

    effective_time_budget_sec = _resolve_int_budget(
        args.time_budget_sec,
        selected,
        "time_budget_sec",
        DEFAULT_TIME_BUDGET_SEC,
    )
    effective_max_requests = _resolve_int_budget(
        args.max_requests,
        selected,
        "max_requests",
        DEFAULT_MAX_REQUESTS,
    )
    effective_max_tokens = int(args.max_tokens or DEFAULT_MAX_TOKENS)
    effective_max_tokens_total = _resolve_int_budget(
        args.max_tokens_total,
        selected,
        "max_tokens_total",
        DEFAULT_MAX_TOKENS_TOTAL,
    )
    effective_cost_ceiling_usd = _resolve_float_budget(
        args.cost_ceiling_usd,
        selected,
        "cost_ceiling_usd",
    )

    case_buckets: list[str] = []
    requests_used = 0
    budget_exceeded = False
    case_artifacts: list[str] = []
    run_deadline = start_ts + float(effective_time_budget_sec)
    for scen in selected:
        if requests_used >= effective_max_requests:
            budget_exceeded = True
            errors.append(
                f"max_requests exceeded: used={requests_used}, limit={effective_max_requests}"
            )
            case_buckets.append("budget_exceeded")
            break
        if time.perf_counter() > run_deadline:
            budget_exceeded = True
            errors.append(
                f"time_budget_sec exceeded before case execution: limit={effective_time_budget_sec}"
            )
            case_buckets.append("budget_exceeded")
            break

        timeout_sec = int(((scen.get("request_defaults") or {}).get("timeout_sec") or 20))
        remaining_sec = run_deadline - time.perf_counter()
        case_timeout_sec = min(timeout_sec, max(1, int(remaining_sec)))
        result = _run_case(scen, case_timeout_sec, args.redact_secrets == "true")
        requests_used += 1
        case_buckets.append(result.failure_bucket)
        case_path = output_dir / "cases" / f"{result.case_id}.json"
        request_params = scen.get("request_defaults") or {}
        _write_json(
            case_path,
            {
                "case_id": result.case_id,
                "status": result.status,
                "failure_bucket": result.failure_bucket,
                "secondary_buckets": result.secondary_buckets,
                "input_pointer": result.fixture,
                "input_hash": None,
                "request_params": request_params if isinstance(request_params, dict) else {},
                "entrypoint": result.entrypoint,
                "fixture": result.fixture,
                "returncode": result.returncode,
                "elapsed_sec": result.elapsed_sec,
                "raw_response": result.stdout,
                "stdout": result.stdout,
                "stderr": result.stderr,
                "parsed_output": result.parsed_output,
                "validation": result.validation,
            },
        )
        case_artifacts.append(str(case_path))
        if time.perf_counter() > run_deadline:
            budget_exceeded = True
            errors.append(
                f"time_budget_sec exceeded after case execution: limit={effective_time_budget_sec}"
            )
            case_buckets.append("budget_exceeded")
            break

    if errors and not case_buckets:
        case_buckets.append("config_error")
        case_path = output_dir / "cases" / "config_error.json"
        _write_json(
            case_path,
            {
                "case_id": "config_error",
                "status": "failed",
                "failure_bucket": "config_error",
                "secondary_buckets": [],
                "input_pointer": None,
                "input_hash": None,
                "request_params": {},
                "entrypoint": [],
                "fixture": None,
                "returncode": None,
                "elapsed_sec": 0.0,
                "raw_response": None,
                "stdout": "",
                "stderr": "\n".join(errors),
                "parsed_output": None,
                "validation": {"schema": False, "invariants": False},
            },
        )
        case_artifacts.append(str(case_path))

    chosen_bucket = _pick_exit_bucket(case_buckets)

    if case_buckets and not case_artifacts:
        case_path = output_dir / "cases" / f"{chosen_bucket}.json"
        _write_json(
            case_path,
            {
                "case_id": chosen_bucket,
                "status": "failed",
                "failure_bucket": chosen_bucket,
                "secondary_buckets": [],
                "input_pointer": None,
                "input_hash": None,
                "request_params": {},
                "entrypoint": [],
                "fixture": None,
                "returncode": None,
                "elapsed_sec": 0.0,
                "raw_response": None,
                "stdout": "",
                "stderr": "\n".join(errors),
                "parsed_output": None,
                "validation": {"schema": False, "invariants": False},
            },
        )
        case_artifacts.append(str(case_path))

    counts: dict[str, int] = {}
    for b in case_buckets:
        counts[b] = counts.get(b, 0) + 1

    summary = {
        "artifact_version": ARTIFACT_VERSION,
        "status": "passed" if chosen_bucket == "pass" and not errors else "failed",
        "mode": mode,
        "run_profile": run_profile,
        "work_item": work_item,
        "scenario": args.scenario,
        "providers_override": args.providers,
        "command": _command_string(),
        "artifact_path": str(output_dir),
        "selected_scenarios": _selected_ids(selected),
        "fixtures": _fixture_paths(selected),
        "provider_stats": _provider_stats(selected),
        "budgets": {
            "time_budget_sec": effective_time_budget_sec,
            "max_requests": effective_max_requests,
            "max_tokens": effective_max_tokens,
            "max_tokens_total": effective_max_tokens_total,
            "cost_ceiling_usd": effective_cost_ceiling_usd,
            "requests_used": requests_used,
            "time_budget_exceeded": budget_exceeded,
        },
        "record": bool(args.record),
        "counts": counts,
        "failure_bucket": chosen_bucket,
        "errors": errors,
        "cases_total": len(selected),
        "case_artifacts": case_artifacts,
    }

    _write_json(output_dir / "summary.json", summary)
    (output_dir / "stdout.txt").write_text("\n".join(logs) + "\n", encoding="utf-8")
    (output_dir / "stderr.txt").write_text("\n".join(errors) + "\n", encoding="utf-8")
    _write_json(
        output_dir / "timing.json",
        {
            "wall_clock_sec": time.perf_counter() - start_ts,
            "started_at_utc": datetime.now(timezone.utc).isoformat(),
            "cmd": _command_string(),
        },
    )

    return EXIT_CODES.get(chosen_bucket, EXIT_CODES["internal_error"])


if __name__ == "__main__":
    raise SystemExit(main())
