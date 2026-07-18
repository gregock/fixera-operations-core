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

Notion is the active input surface for jobs. The Notion sync path maps those jobs into the canonical Core job model and stores them in SQLite. Job lifecycle changes are validated against canonical states before they are accepted. Costs, labor, and job price are captured on the job record. Profit is derived in `profit_analysis` rather than treated as a source ledger. Refresh writes dashboard snapshots, and the decision layer reads only existing data to produce prioritized, read-only outputs.

The public-safe representation in this repository focuses on the parts a reviewer can actually evaluate:

- intake and normalization
- canonical job lifecycle control
- derived profit calculation
- refresh-driven reporting
- read-only decision support
- public/private evidence separation

At the system level, that means the business can move from intake to operational state to financial summary to decision support without collapsing everything into free text.

## Representative Flow

The flagship evidence package is here:

[public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/)

It shows one synthetic service job moving through the full flow:

1. A Notion-originated job arrives.
2. The sync layer normalizes it into the Core job model.
3. SQLite stores it as the canonical record.
4. Lifecycle validation keeps status changes within allowed transitions.
5. Hours, materials, and price are captured on the job.
6. `profit_analysis` is recomputed from the job inputs.
7. Refresh writes snapshots for the dashboard.
8. The decision layer produces a prioritized action when the evidence supports it.

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

- SQLite-first operational model. The private docs describe SQLite as the canonical operational database and the system of record.
- Canonical lifecycle states. Job status is not free text; it is a controlled lifecycle with defined allowed transitions.
- Validation before status transition. Notion sync and lifecycle helpers enforce transitions instead of accepting arbitrary updates.
- Derived profit layer. `profit_analysis` is computed from job-related inputs rather than treated as source truth.
- Read-only decision support. The decision layer ranks and surfaces actions, but does not execute them automatically.
- Public/private evidence boundary. The portfolio publishes synthetic and sanitized evidence only, while the private production repository stays private.
- Evidence package discipline. The public repository includes explicit provenance and validation notes so the sample cannot be mistaken for a production export.

## Tradeoffs

- The private `fixera-core` repository remains private, so the public case study has to rely on synthetic examples and sanitized evidence.
- The public package is intentionally narrower than the production system; it shows one representative flow instead of every subsystem.
- Lead-to-job attribution is not overstated. The current evidence supports decision support and job lifecycle modeling, but not a fully closed attribution story.
- The local-first design favors ownership, simplicity, and direct control over cloud polish or broader platform abstraction.

## Evidence

- Representative operational flow: [public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/)
- Architecture view: [public-proof/diagrams/architecture-v1.md](public-proof/diagrams/architecture-v1.md)
- Evidence boundary: [public-proof/manifest/evidence-manifest.md](public-proof/manifest/evidence-manifest.md)
- Validation and provenance: [public-proof/examples/representative-operational-flow/validation.md](public-proof/examples/representative-operational-flow/validation.md), [public-proof/examples/representative-operational-flow/provenance.md](public-proof/examples/representative-operational-flow/provenance.md)

## What This Demonstrates

This project demonstrates how I model operational work as a stateful system instead of a pile of notes and manual steps.

It shows operational modeling, lifecycle control, and financial attribution in a live small-business context. It also shows how to add automation with guardrails, keep decision support read-only, and preserve a clear boundary between private production evidence and public-safe portfolio material.

The main takeaway is practical system design: define the real state, validate transitions, derive outputs from the state, and keep the human responsible for the final decision.
