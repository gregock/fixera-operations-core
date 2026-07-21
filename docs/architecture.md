# Architecture

This document describes the public-safe architecture of Fixera Core.

## High-level shape

The private Fixera Core system was designed as a local-first operational system for a service business.

The private design uses:

- Notion as the active intake surface for jobs
- SQLite as the canonical operational store
- controlled lifecycle handling
- a refresh layer to generate summaries and dashboard outputs
- read-only decision support for prioritization

This public repository documents the same shape at a safer resolution:

- source events enter through an intake layer
- canonical job records are stored in SQLite
- lifecycle transitions are represented as controlled review steps
- profit is derived from job inputs rather than written as a source ledger
- refresh produces dashboard snapshots and supporting reports
- the decision layer reads existing data only

## Core flow

1. A job enters through the intake layer.
2. The job is normalized into the internal record shape.
3. Lifecycle transitions are represented as controlled review steps.
4. Costs, labor, and price are stored on the job record.
5. Profit is derived from the recorded inputs.
6. Refresh generates reporting snapshots.
7. The decision layer surfaces prioritized actions without executing them automatically.

## Design choices

- SQLite keeps the system simple and local-first.
- Canonical states prevent free-text drift.
- Derived outputs reduce duplication and keep the source of truth clear.
- Read-only decisions preserve human control.
- Explicit evidence boundaries keep public artifacts synthetic and reviewable.
- Diagrams and sample JSON are separate from explanatory text so reviewers can inspect the system from multiple angles.

## Public boundary

This portfolio edition documents the system structure without exposing production data, production databases, private backend code, credentials, customer records, or sensitive operational details.
The public diagrams may retain abstracted runtime component names and artifact categories where they help explain the architecture without exposing deployable private implementation.
