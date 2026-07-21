# Public Validation Notes

This repository does not publish executable production smoke tests.

That is intentional: the public package contains documentation, diagrams, synthetic JSON, and public-evidence validation only, not the private runtime or deployable production code.

## Current Public Checks

- manual review against the evidence manifest
- JSON validation for the synthetic examples
- link and privacy review before publication
- `python -m scripts.validate_public_evidence`
- `python -m unittest discover -s tests -p "test_*.py"`

## Publication Rule

The executable checks in this repository validate only the public evidence package.
They do not claim to validate the private production backend.
