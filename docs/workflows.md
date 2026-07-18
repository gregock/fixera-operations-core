# Workflows

This document explains the public-safe workflows demonstrated by Fixera Core.

## Ingestion

- A job enters from the intake surface.
- The job is normalized into the internal model.
- The lifecycle state is checked before the record is accepted.
- The canonical record is then used for reporting and downstream decision support.

## Reporting

- Job fields are stored in SQLite.
- Costs, labor, and price are captured on the job.
- Profit is derived from recorded inputs.
- Refresh generates reporting snapshots.
- Derived outputs are treated as runtime artifacts, not source truth.

## Decision support

- The decision layer reads existing data only.
- Actions are ranked and surfaced for review.
- The system does not auto-execute operational decisions.
- The decision layer is explicitly read-only and is not allowed to mutate job state.

## Representative Path

The public sample package models this sequence:

1. synthetic job or lead-like evidence is introduced
2. the record is normalized
3. lifecycle validation accepts or rejects the transition
4. the job record is stored in the canonical model
5. profit is derived
6. refresh writes snapshots
7. decision support consumes the existing state
8. the human operator remains responsible for the final action

## Boundary rule

The workflow description stays abstract so the repository can explain the system without exposing production history or sensitive records.
