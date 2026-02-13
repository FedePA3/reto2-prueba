# Repository Guidelines

## Project Structure & Module Organization
This repository follows a simple MVC-style layout for the EDA course challenge:
- `main.py`: program entry point; launches the console view.
- `App/view.py`: CLI menu, user interaction, and output formatting.
- `App/logic.py`: data loading, requirement handlers (`req_1` to `req_6`), and timing helpers.
- `Data/`: input CSV datasets used by the application.
- `DataStructures/`: supporting ADT package area.
- `Docs/`: deliverables (report templates and final documentation).

Keep business logic in `App/logic.py`; avoid placing processing code in the view layer.

## Build, Test, and Development Commands
- `python -m pip install -r requirements.txt`: install project dependencies.
- `python main.py`: run the interactive CLI locally.
- `pytest -q`: execute automated tests.

If no tests exist yet, add them first under `tests/` and then run `pytest -q`.

## Coding Style & Naming Conventions
- Follow Python PEP 8 with 4-space indentation.
- Use `snake_case` for functions/variables and keep module names lowercase.
- Preserve the template contract names (`new_logic`, `load_data`, `req_1` ... `req_6`) unless the team agrees on a refactor.
- Keep functions focused and side effects explicit; view prints, logic computes.
- Add short docstrings for non-trivial functions.

## Testing Guidelines
Use `pytest` (already pinned in `requirements.txt`).
- Place tests in `tests/`.
- Name files `test_*.py` and test functions `test_*`.
- Prioritize coverage for data loading and each requirement function.
- Include edge cases (empty inputs, invalid options, missing files).

Example:
```bash
pytest -q tests/test_logic.py
```

## Commit & Pull Request Guidelines
Git history shows short, direct commit messages (often in Spanish), e.g., `Update README.md`.
- Prefer imperative, scoped messages: `feat: implement req_2 filtering`.
- Keep commits focused by concern (logic, view, docs).
- PRs should include: summary, changed files, test evidence (`pytest` output), and linked task/requirement.
- For CLI output changes, include a short terminal transcript or screenshot in the PR description.
