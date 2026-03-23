# Contributing to KNApSAcK-AI

## Team Workflow

- **CS track:** owns `knapsack/chem/`, `knapsack/ml/`, all model `src/` folders
- **Biology track:** owns `docs/DATA_DICTIONARY.md`, domain validation, notebook review
- **Joint:** `knapsack/db/`, all `docs/` except DATA_DICTIONARY, `README.md`

## Branch Strategy

```
main          ← stable, never push directly
dev           ← integration branch
feature/xxx   ← one branch per feature or project phase
```

Always open a pull request from `feature/xxx` → `dev`, never directly to `main`.

## Commit Message Format

```
[scope] short description (max 72 chars)

scope = init | data | model | eval | app | docs | fix | refactor | test
```

Examples:
- `[data] add SMILES coverage audit for activity_db`
- `[model] bioguard baseline RF, macro F1=0.71`
- `[docs] update roadmap with Tier 2 timelines`

## Code Style

- Formatter: `black` (line length 88)
- Linter: `ruff`
- Run before committing: `black . && ruff check .`

## Adding a New Project

1. Create `projects/<name>/` using the standard structure
2. Add a `PROJECT_CHARTER.md` before writing any code
3. Add project to `README.md` status table
4. Reuse `knapsack/` library functions — do not duplicate logic
