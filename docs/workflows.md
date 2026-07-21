# Workflows

This document explains the public-safe workflows demonstrated by Fixera Core.

## Ingestion

- A job enters from the intake surface.
- The job is normalized into the internal model.
- The lifecycle state is represented as a controlled review step before acceptance.
- The canonical record is then described as the source for reporting and downstream decision support in the private system.

## Reporting

- Job fields are stored in SQLite.
- Costs, labor, and price are captured on the job.
- Profit is derived from recorded inputs.
- Reporting refresh generates snapshots.
- Derived outputs are treated as runtime artifacts, not source truth.

## Decision support

- The decision layer reads existing data only.
- Actions are ranked and surfaced for review.
- The system does not auto-execute operational decisions.
- The decision layer is explicitly read-only and is not allowed to mutate job state.

## Representative Path

The public sample package illustrates this sequence:

1. synthetic job or lead-like evidence is introduced
2. the record is normalized
3. lifecycle review accepts or rejects the transition
4. the job record is represented in the canonical model
5. profit is derived
6. reporting refresh writes snapshots
7. decision support consumes the existing state
8. the human operator remains responsible for the final action

## Boundary rule

The workflow description stays abstract so the repository can explain the private system design without exposing production history, private backend code, or sensitive records.
