# Public Proof

This folder contains the public-safe evidence set for `fixera-core`.

## Current Evidence

- `diagrams/` - sanitized architecture and workflow diagrams
- `examples/` - representative synthetic operational flows
- `manifest/` - the promotion contract for public evidence

## Useful Links

- [Repository overview](../README.md)
- [Case study](../case-study.md)
- [Architecture](../docs/architecture.md)
- [Workflows](../docs/workflows.md)
- [Safety boundaries](../docs/safety-boundaries.md)
- [Representative operational flow](examples/representative-operational-flow/README.md)
- [Evidence manifest](manifest/evidence-manifest.md)

## Publication Notes

- Synthetic JSON samples are kept inside `examples/representative-operational-flow/` so the data, validation notes, and provenance stay together.
- `sample-json/` exists only as a publication rule note, not as the active sample location.
- Screenshots and smoke-output captures are not part of the current public evidence package.
- Future screenshots or smoke outputs should be added only when they can be sanitized cleanly and add real review value.

## Rule Set

- keep everything synthetic or sanitized
- do not commit production data
- do not commit secrets or credentials
- do not commit runtime logs or private operational history

## Current Evidence Package

- synthetic job sample
- synthetic lead/event sample
- architecture diagram
- workflow diagram
- validation and provenance notes

Use this folder as the public boundary for what can be reviewed outside the private production repository.
