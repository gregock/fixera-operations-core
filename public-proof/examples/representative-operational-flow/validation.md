# Validation

This package is grounded in existing Fixera Core validation rather than invented behavior.

What the tests prove:

- [tests/test_job_lifecycle.py](/Users/gregorioescola/code/fixera-core/tests/test_job_lifecycle.py#L8) proves the canonical lifecycle states exist, valid transitions are accepted, invalid transitions are rejected, and admin correction paths are controlled.
- [tests/test_notion_sync_transition_enforcement.py](/Users/gregorioescola/code/fixera-core/tests/test_notion_sync_transition_enforcement.py#L12) proves Notion sync uses lifecycle validation, preserves non-status fields on an invalid transition, and fails visibly when the incoming status cannot be mapped.
- [tests/test_financial_foundation.py](/Users/gregorioescola/code/fixera-core/tests/test_financial_foundation.py#L24) proves the financial model separates account scope, transaction type, transfer linkage, and derived profit storage.
- [tests/test_financial_foundation.py](/Users/gregorioescola/code/fixera-core/tests/test_financial_foundation.py#L156) proves the seeded business and personal accounts exist and remain idempotent.
- [tests/test_lead_signal.py](/Users/gregorioescola/code/fixera-core/tests/test_lead_signal.py#L9) proves the clean lead layer canonicalizes landing pages and skips blank values.
- [tests/test_growth_engine_enrichment.py](/Users/gregorioescola/code/fixera-core/tests/test_growth_engine_enrichment.py#L10) proves the decision layer can carry page registry enrichment into action output.

What the implementation docs add:

- [projects_state.md](/Users/gregorioescola/code/fixera-core/docs/active/projects_state.md#L9) documents the live macOS runtime, launchd scheduling, snapshot history, and current operational gaps.
- [pipeline.md](/Users/gregorioescola/code/fixera-core/docs/active/pipeline.md#L15) documents the full traffic → leads → jobs → profit → reporting → decisions flow and its current boundary.
- [decision-layer.md](/Users/gregorioescola/code/fixera-core/docs/active/decision-layer.md#L6) documents the exact action contract and the read-only decision rule.

What this means for the synthetic job:

- The synthetic record is not a captured production export.
- It is a compact example built to match the verified schema, lifecycle rules, financial boundary, and decision-layer contract.
- The workflow is enforced by existing tests and runtime documentation, not by the artifact itself.
