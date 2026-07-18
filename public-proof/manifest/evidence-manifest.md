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
| Synthetic lead/event JSON | Private lead/event records and schema from `fixera-core` | Rebuild as a small synthetic payload that preserves field shapes and representative states | Remove names, emails, phone numbers, IDs, timestamps tied to real activity, and any business-sensitive values | `public-proof/sample-json/` | Manual review against schema and a diff check that confirms only synthetic values are present |
| Architecture diagram | Private architecture notes, service boundaries, and runtime layout | Redraw as a simplified public architecture view with only stable system components and data flows | Omit internal hosts, private networks, deployment secrets, and runtime-only details | `public-proof/diagrams/` | Cross-check against `docs/architecture.md` and confirm all labels are public-safe |
| Workflow diagram | Private workflow notes and operational flow descriptions | Convert into a public workflow map that shows stages, handoffs, and decision points without operational specifics | Remove client names, exception cases tied to real incidents, and internal tooling references | `public-proof/diagrams/` | Review against `docs/workflows.md` and confirm the flow is abstracted from production cases |
| Sanitized/mock dashboard screenshot | Private dashboard view or UI capture from `fixera-core` | Recreate as a mock or heavily sanitized screenshot that demonstrates layout and purpose only | Blur or replace all live data, identifiers, metrics, and account details; no raw captures with private content | `public-proof/screenshots/` | Visual inspection plus metadata check that the image is mock or sanitized |
| Optional validation/smoke output | Local public-artifact checks and lightweight verification scripts | Capture only the result of checks that validate public samples, diagrams, or screenshots | Exclude production test fixtures, environment secrets, and operational logs | `tests/smoke/` | Record a short pass/fail summary showing the public artifact set was verified |

Use this manifest as the gate for future public evidence.
It is a process contract, not an evidence store.

## Current Public Set

- one synthetic job record
- one synthetic lead/event record
- one sanitized architecture diagram
- one sanitized workflow diagram
- provenance and validation notes for the sample package

Anything beyond that should be added only if it can be published without exposing production data or operational history.
