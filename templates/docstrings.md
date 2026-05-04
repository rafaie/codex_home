# Docstring Standard

Use Google-style docstrings for Python code where the docstring reduces maintenance risk.

## Required
- Public modules, classes, functions, and methods.
- CLI entrypoints and command handlers.
- Data models, schemas, provider/client wrappers, and integration boundaries.
- Non-trivial private helpers with business rules, branching, side effects, or surprising constraints.
- Shared test fixtures/helpers used across files.

## Usually not required
- Trivial properties and one-line wrappers.
- Tiny local closures.
- Obvious test helpers used in one file.
- Generated code.
- Code where a docstring would only repeat the function name.

## Format
Use Google-style sections as applicable:
- `Args:`
- `Returns:`
- `Raises:`
- `Yields:`
- `Examples:`

## Example

```python
def normalize_score(raw_score: float, minimum: float, maximum: float) -> float:
    """Normalize a raw score into the 0.0 to 1.0 range.

    Args:
        raw_score: Score before normalization.
        minimum: Lower bound of the original score range.
        maximum: Upper bound of the original score range.

    Returns:
        Normalized score between 0.0 and 1.0.

    Raises:
        ValueError: If maximum is less than or equal to minimum.
    """
```

## Enforcement
- Prefer `ruff` pydocstyle rules when the repo already uses Ruff.
- Otherwise configure `[commands].docstrings` in `codex.toml`.
- Treat docstring lint as optional until the project enables the command.
