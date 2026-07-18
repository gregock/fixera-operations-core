# Fixera Core Portfolio Edition

Fixera Core is a local-first operations and intelligence backend for a real service business.

It models jobs, costs, lifecycle state, reporting, and decision support as one coherent operational system instead of a set of disconnected notes, spreadsheets, and manual follow-up steps.

This public Portfolio Edition shows the engineering behind the private production system without exposing operational data, private business context, runtime artifacts, or sensitive configuration.

The production system, live database, runtime configuration, customer records, and operational history are not included in this repository.

## What This Demonstrates

This project is meant to show practical backend judgment: how to define the source of truth, protect state transitions, derive useful outputs, and keep automation accountable.

- local-first backend design with SQLite as the canonical operational store
- stateful job lifecycle modeling with validation before status changes
- derived financial reporting instead of duplicated source ledgers
- refresh-driven dashboard outputs and public-safe evidence packaging
- read-only decision support that ranks actions without executing them automatically

## What Is Included

- an index of the public evidence set in `public-proof/`
- a public-safe case study of the core operational system
- a sanitized architecture diagram
- a sanitized workflow diagram
- synthetic sample JSON for job and lead-like evidence
- a promotion manifest that explains what can and cannot be published
- validation and provenance notes for the synthetic sample package

## Repository Map

- [case-study.md](case-study.md) - public case study and engineering narrative
- [docs/architecture.md](docs/architecture.md) - public-safe architecture summary
- [docs/workflows.md](docs/workflows.md) - public-safe workflow summary
- [docs/safety-boundaries.md](docs/safety-boundaries.md) - publication and privacy boundary
- [public-proof/README.md](public-proof/README.md) - index of the public evidence package
- [public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/) - synthetic job and lead examples
- [public-proof/diagrams/architecture-v1.md](public-proof/diagrams/architecture-v1.md) - sanitized architecture diagram
- [public-proof/diagrams/workflow-v1.md](public-proof/diagrams/workflow-v1.md) - sanitized workflow diagram
- [public-proof/manifest/evidence-manifest.md](public-proof/manifest/evidence-manifest.md) - evidence promotion contract

What it is:
- a curated public showcase of architecture, workflows, and engineering decisions
- a stable public companion to the private production repository
- an evidence-first portfolio repository for technical review

What it is not:
- a clone of `fixera-core`
- a fork of `fixera-core`
- a second product
- a place for production data, secrets, logs, or operational history

The private `fixera-core` repository remains the production source of truth.
This repository only receives public-safe evidence and explanatory artifacts that can be shared safely.

## Review Bar

The goal is not to imply that this is a full export of production.
The goal is to make the public repository strong enough for technical review by showing:

- the real system shape
- the real boundary between canonical state and derived outputs
- the real lifecycle and decision-support model
- the real public-safe evidence trail
