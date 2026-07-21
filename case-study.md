# Fixera Core Case Study

## Problem

Small-business operations were split across chats, notes, spreadsheets, memory, and manual decisions. That made it hard to keep jobs, clients, costs, and follow-up in one coherent operational record.

Fixera Core was built to turn that scattered work into a practical internal system that could hold the operational state of the business without exposing private production data.

## Constraints

- Private production data had to stay private.
- The system had to fit a real small-business context, not a sandbox.
- It had to work local-first on the Mac runtime with SQLite as the source of truth.
- Human review had to remain in the loop for important decisions.
- The system could not rely on autonomous execution.
- Rollout had to be gradual, with validation before each status change and no big-bang rewrite.

## System Built

Fixera Core models operational work as a pipeline rather than a set of disconnected tools.

In the private operational system, Notion is the active input surface for jobs. The intake path maps those jobs into the core job model and stores them in SQLite. Lifecycle changes are reviewed against canonical states before acceptance. Costs, labor, and price are captured on the job record. Profit is treated as derived analysis rather than a source ledger. Reporting refreshes produce snapshots, and the decision layer reads existing data to produce prioritized, read-only outputs.

This public repository documents that design at a public-safe level. It does not include the private runtime, private schema, private migrations, or the deployable backend implementation.

The public-safe representation in this repository focuses on the parts a reviewer can evaluate directly:

- intake and normalization
- canonical job lifecycle control
- derived profit calculation
- refresh-driven reporting
- read-only decision support
- public/private evidence separation

At the system level, the private design allows the business to move from intake to operational state to financial summary to decision support without collapsing everything into free text.

## Representative Flow

The flagship evidence package is here:

[public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/)

It shows one synthetic service job moving through a representative flow:

1. A Notion-originated job arrives.
2. The intake path normalizes it into the core job model.
3. SQLite is documented as the canonical record layer in the private system.
4. Lifecycle review is represented as a controlled transition step.
5. Hours, materials, and price are captured on the job.
6. `profit_analysis` is illustrated as a derived field.
7. Reporting refresh is represented as a downstream step.
8. The decision layer is shown as read-only review support.

The supporting files in that package are:

- `synthetic-job.json`
- `lead-event-example.json`
- `validation.md`
- `provenance.md`

Additional public evidence:

- [public-proof/diagrams/architecture-v1.md](public-proof/diagrams/architecture-v1.md)
- [public-proof/diagrams/workflow-v1.md](public-proof/diagrams/workflow-v1.md)
- [public-proof/manifest/evidence-manifest.md](public-proof/manifest/evidence-manifest.md)

## Key Engineering Decisions

- SQLite-first operational model. The private system was designed around SQLite as the canonical operational database and system of record.
- Canonical lifecycle states. Job status was designed as a controlled lifecycle rather than free text.
- Review before status transition. The private system uses controlled lifecycle handling instead of arbitrary updates.
- Derived profit layer. `profit_analysis` is documented as derived from job-related inputs rather than treated as source truth.
- Read-only decision support. The decision layer is described as ranking and surfacing actions without auto-executing them.
- Public/private evidence boundary. The portfolio publishes synthetic and sanitized evidence only, while the private production repository stays private.
- Evidence package discipline. The public repository includes explicit provenance, validation notes, and automated public-evidence checks so the sample cannot be mistaken for a production export.

## Tradeoffs

- The private `fixera-core` repository remains private, so the public case study relies on synthetic examples and sanitized evidence.
- The public package is intentionally narrower than the production system; it shows representative structure rather than the full implementation.
- Lead-to-job attribution is not overstated. The current public evidence supports workflow and decision-support discussion, but not a full closed-loop attribution proof.
- The local-first design favors ownership, simplicity, and direct control over cloud polish or broader platform abstraction.

## Evidence

- Representative operational flow: [public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/)
- Architecture view: [public-proof/diagrams/architecture-v1.md](public-proof/diagrams/architecture-v1.md)
- Evidence boundary: [public-proof/manifest/evidence-manifest.md](public-proof/manifest/evidence-manifest.md)
- Validation and provenance: [public-proof/examples/representative-operational-flow/validation.md](public-proof/examples/representative-operational-flow/validation.md), [public-proof/examples/representative-operational-flow/provenance.md](public-proof/examples/representative-operational-flow/provenance.md)

## What This Demonstrates

This project documents how I model operational work as a stateful system instead of a pile of notes and manual steps.

It shows operational modeling, lifecycle control, and financial attribution in a real small-business context through public-safe documentation and synthetic evidence. It also shows how to add automation with guardrails, keep decision support read-only, and preserve a clear boundary between private production evidence and public-safe portfolio material.

The main takeaway is practical system design: define the real state, control review boundaries, derive outputs from operational records, and keep the human responsible for the final decision.
