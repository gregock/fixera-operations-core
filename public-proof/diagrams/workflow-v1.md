# Workflow Diagram v1

This is a sanitized public view of the job-to-decision workflow in `fixera-core`.
It shows the lifecycle shape without exposing production records or private operational details.

```mermaid
flowchart LR
  intake[Job intake]
  normalize[Normalize record]
  validate[Validate lifecycle transition]
  store[Store in SQLite]
  derive[Derive profit_analysis]
  refresh[Run refresh]
  snapshot[Write dashboard snapshots]
  decide[Read-only decision support]
  review[Human review]

  intake --> normalize --> validate --> store --> derive --> refresh --> snapshot --> decide --> review
  validate --> review
  decide --> review
```

Notes:
- The workflow is intentionally linear and public-safe.
- It represents the operational sequence, not a literal production trace.
