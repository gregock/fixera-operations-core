# Provenance

This file maps the synthetic JSON sections to verified private sources and explains how the values were sanitized.

## Intake

- Verified private sources:
  - [core/notion_sync.py](/Users/gregorioescola/code/fixera-core/core/notion_sync.py#L77)
  - [db/models.py](/Users/gregorioescola/code/fixera-core/db/models.py#L171)
  - [data-integration.md](/Users/gregorioescola/code/fixera-core/docs/active/data-integration.md#L142)
  - [dashboard-backend.md](/Users/gregorioescola/code/fixera-core/docs/active/dashboard-backend.md#L396)
- Transformation applied:
  - Reduce the live import shape to a single synthetic service job.
  - Keep only fields that are already supported by the job model and sync path.
- Sanitization applied:
  - Replace the real Notion page ID with a fictional ID.
  - Remove any real client name, address, notes, or source payload.
  - Use a generic service title and a public-safe landing path.

## Lifecycle

- Verified private sources:
  - [core/job_lifecycle.py](/Users/gregorioescola/code/fixera-core/core/job_lifecycle.py#L5)
  - [fixera-core-job-lifecycle-design.md](/Users/gregorioescola/code/fixera-core/docs/active/fixera-core-job-lifecycle-design.md#L84)
  - [test_job_lifecycle.py](/Users/gregorioescola/code/fixera-core/tests/test_job_lifecycle.py#L72)
- Transformation applied:
  - Collapse the full lifecycle contract into one clean status path for a single example job.
- Sanitization applied:
  - Use canonical status names only.
  - Avoid showing any actual operator corrections or private workflow history.

## Cost capture

- Verified private sources:
  - [db/models.py](/Users/gregorioescola/code/fixera-core/db/models.py#L171)
  - [pipeline.md](/Users/gregorioescola/code/fixera-core/docs/active/pipeline.md#L94)
  - [fixera-core-financial-domain-design.md](/Users/gregorioescola/code/fixera-core/docs/active/fixera-core-financial-domain-design.md#L37)
- Transformation applied:
  - Use the job model fields that already capture price, hours, and materials cost.
- Sanitization applied:
  - Use rounded fictional amounts.
  - Do not include any real supplier, expense, or payment detail.

## Profit summary

- Verified private sources:
  - [db/models.py](/Users/gregorioescola/code/fixera-core/db/models.py#L315)
  - [core/profit_engine.py](/Users/gregorioescola/code/fixera-core/core/profit_engine.py#L32)
  - [fixera-core-financial-domain-design.md](/Users/gregorioescola/code/fixera-core/docs/active/fixera-core-financial-domain-design.md#L123)
- Transformation applied:
  - Express the derived profit layer as a compact per-job summary.
- Sanitization applied:
  - Use fictional revenue and cost figures that fit the documented schema.
  - Keep the example free of account identifiers and tax details.

## Decision output

- Verified private sources:
  - [decision-layer.md](/Users/gregorioescola/code/fixera-core/docs/active/decision-layer.md#L40)
  - [core/growth_engine.py](/Users/gregorioescola/code/fixera-core/core/growth_engine.py#L1)
  - [test_growth_engine_enrichment.py](/Users/gregorioescola/code/fixera-core/tests/test_growth_engine_enrichment.py#L11)
- Transformation applied:
  - Convert the documented growth-report contract into one representative action block.
- Sanitization applied:
  - Use synthetic page metrics and a fictional generated timestamp.
  - Do not reference live traffic, live leads, or real profit rows.
