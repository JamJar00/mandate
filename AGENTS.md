# AGENTS.md

## Project Overview
This project is a linter that checks project setup to ensure good quality foundations. It checks things like whether language-specific linters are present, README files exists and other best practices

Checks are written in `src/mandate/check_providers/` and tests are written in `tests/scenarios` split by examples that meet the desired checks in `passes` and examples that fail the desired checks in `failures`. And templates used in fixes are stored in `src/mandate/templates/`

When adding a new check it must also be added to `src/mandate/check_providers/__init__.py` to ensure it is included

## Build and Test Commands
- Run commands withing poetry, e.g. `poetry run pytest`
- When new checks are added the output of `poetry run generate_docs` should be added to the `README.md` file to ensure documentation is up to date

## Code Style Guidelines
- Prefer double quotes to single quotes

## Testing Instructions
Always generate tests for new check providers. Run them once you have generated new tests

## Security Considerations
