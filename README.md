# Fixera Core Portfolio Edition

Fixera Core was designed and used privately as a local-first operations system for a real service business.
The private system organizes jobs, costs, lifecycle state, reporting, and decision support as one coherent operational model instead of scattered notes, spreadsheets, and manual follow-up.

This repository is a public-safe architecture and system-design case study, not the deployable production backend.
It documents the system structure, operating model, and evidence boundary without publishing production data, private backend code, private configuration, customer records, or operational history.

The public repository does not independently reproduce the production runtime.
It includes architecture documentation, diagrams, a public evidence manifest, synthetic example records, and lightweight checks for the public evidence package itself.

## Operational Problem

The underlying private system was built for a small service business that needed durable operational records instead of fragmented coordination across chats, notes, spreadsheets, and memory.
The design goal was a database-first internal system that could keep job state, task coordination, pricing context, document organization, review history, and reporting aligned.

## What This Public Case Study Demonstrates

This public case study is meant to show practical systems judgment:

- how the private system was structured around persistent operational records
- how lifecycle control and review boundaries were designed
- how reporting and decision support were separated from source records
- how public-safe evidence can be published without exposing production data

The included synthetic examples illustrate representative record shapes and workflow stages.
They do not claim to be production exports or executable proof of the private runtime.

## Main Workflows Designed

- intake and normalization of operational requests
- persistent job and task coordination
- lifecycle review and status control
- pricing and cost capture concepts
- reporting and derived operational summaries
- read-only decision support for human review

## System-Design Principles

- database-first operational modeling
- explicit separation between source records and derived outputs
- controlled review points instead of free-form state mutation
- local-first ownership and operational simplicity
- public/private evidence discipline

## What Is Included

- an index of the public evidence set in `public-proof/`
- a public-safe case study of the underlying operational system
- a sanitized architecture diagram
- a sanitized workflow diagram
- synthetic sample JSON for job and lead-like evidence
- a promotion manifest that explains what can and cannot be published
- validation and provenance notes for the synthetic sample package
- a lightweight validator and test suite for the public evidence package

## What Remains Private

- the deployable production backend
- production SQLite databases and runtime artifacts
- private backend code, schema, migrations, and production tests
- credentials, environment configuration, and infrastructure details
- customer records, documents, and operational history

## Inspecting The Evidence

Start with these files:

- [case-study.md](case-study.md) - public narrative of the private system design and the evidence boundary
- [docs/architecture.md](docs/architecture.md) - public-safe architecture summary
- [docs/workflows.md](docs/workflows.md) - public-safe workflow summary
- [docs/safety-boundaries.md](docs/safety-boundaries.md) - publication and privacy boundary
- [public-proof/README.md](public-proof/README.md) - index of the public evidence package
- [public-proof/examples/representative-operational-flow/](public-proof/examples/representative-operational-flow/) - synthetic representative examples
- [public-proof/diagrams/architecture-v1.md](public-proof/diagrams/architecture-v1.md) - sanitized architecture diagram
- [public-proof/diagrams/workflow-v1.md](public-proof/diagrams/workflow-v1.md) - sanitized workflow diagram
- [public-proof/manifest/evidence-manifest.md](public-proof/manifest/evidence-manifest.md) - evidence promotion contract

## Validation

Run the full public check from the repository root:

```bash
python -m scripts.check
```

That command runs:

- the unittest suite for the public validator
- the public evidence validator itself

What it proves:

- required public evidence files exist
- the synthetic JSON samples parse and contain required markers
- manifest references resolve to real files
- the committed public package does not include obvious prohibited runtime artifacts

What it does not prove:

- the private production backend implementation
- production schema or migrations
- production smoke tests
- production runtime behavior

## My Role

I designed and built the underlying operational workflows and system structure for the private Fixera operations core.
That work included job lifecycle design, persistent record strategy, task coordination concepts, pricing and history modeling, document organization, operational review flow, and the public-safety boundary for evidence publication.

The private deployable backend, production data model implementation, and operational runtime remain outside this public repository.

## AI-Assisted Development

I use AI as a tool for architecture exploration, implementation support, debugging, validation design, documentation, and iteration.
I remain responsible for requirements, architecture, operational decisions, evidence boundaries, and accepting or rejecting generated changes.

## Review Bar

The goal is not to imply that this repository is a full export of production.
The goal is to make the public repository strong enough for technical review by showing:

- the system shape and design intent of the private operational platform
- the boundary between source records and derived outputs
- the lifecycle and review model
- the public-safe evidence trail and validation discipline
