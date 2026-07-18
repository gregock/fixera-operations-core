# Evidence Manifest

This document is the contract for promoting private evidence into the public Portfolio Edition.

Scope:
- source system: `fixera-core` only
- destination repo: `fixera-core-portfolio`
- allowed output: synthetic, sanitized, or mock evidence only

Rules:
- do not copy production data directly
- do not expose secrets, credentials, client records, or private operational details
- keep artifacts stable, minimal, and public-safe
- use the smallest transformation needed to make the evidence shareable

Promotion standard:
- each artifact must name its private source, transformation rule, redaction rule, public destination, and verification method
- if a source cannot be sanitized cleanly, do not publish it

## Artifact Register

| Artifact name | Private source | Transformation rule | Redaction rule | Public destination | Verification method |
| --- | --- | --- | --- | --- | --- |
| Synthetic job and lead/event JSON | Private job, lead/event records, and schema shape from `fixera-core` | Rebuild as small synthetic payloads that preserve representative field shapes and states | Remove names, emails, phone numbers, IDs, timestamps tied to real activity, and any business-sensitive values | `public-proof/examples/representative-operational-flow/` | Manual review against public docs and JSON validation that confirms only synthetic values are present |
| Architecture diagram | Private architecture notes, service boundaries, and runtime layout | Redraw as a simplified public architecture view with only stable system components and data flows | Omit internal hosts, private networks, deployment secrets, and runtime-only details | `public-proof/diagrams/` | Cross-check against `docs/architecture.md` and confirm all labels are public-safe |
| Workflow diagram | Private workflow notes and operational flow descriptions | Convert into a public workflow map that shows stages, handoffs, and decision points without operational specifics | Remove client names, exception cases tied to real incidents, and internal tooling references | `public-proof/diagrams/` | Review against `docs/workflows.md` and confirm the flow is abstracted from production cases |
| Sanitized/mock dashboard screenshot | Private dashboard view or UI capture from `fixera-core` | Recreate as a mock or heavily sanitized screenshot that demonstrates layout and purpose only | Blur or replace all live data, identifiers, metrics, and account details; no raw captures with private content | `public-proof/screenshots/` | Visual inspection plus metadata check that the image is mock or sanitized |
| Public validation notes | Local public-artifact checks and lightweight verification notes | Document only the checks that validate public samples, diagrams, and publication boundaries | Exclude production test fixtures, environment secrets, operational logs, and private runtime output | `tests/smoke/README.md` | Record the public checks used before publication |

Use this manifest as the gate for future public evidence.
It is a process contract, not an evidence store.

## Current Public Set

- one synthetic job record
- one synthetic lead/event record
- one sanitized architecture diagram
- one sanitized workflow diagram
- provenance and validation notes for the sample package

Anything beyond that should be added only if it can be published without exposing production data or operational history.
