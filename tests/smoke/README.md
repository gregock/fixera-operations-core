# Public Validation Notes

This repository does not publish executable production smoke tests.

That is intentional: the public package contains documentation, diagrams, and synthetic JSON, not the private runtime or production code.

## Current Public Checks

- manual review against the evidence manifest
- JSON validation for the synthetic examples
- link and privacy review before publication

## Publication Rule

Only add executable smoke output if future public artifacts become executable and the output can be published without logs, paths, secrets, or production data.
