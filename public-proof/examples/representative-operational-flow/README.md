# Representative Operational Flow

This package shows one sanitized Fixera Core flow end to end:
an operational service job arrives through Notion, is normalized into the core job model, moves through the lifecycle, picks up cost and labor data, produces derived profit data, and finally reaches the dashboard decision layer.

Why this scenario:
- It uses only verified system behavior.
- It is representative of the live backend because Notion sync, job lifecycle enforcement, financial attribution, and decision support are all implemented.
- It avoids the still-open lead-to-job attribution gap as the main story spine.

Timeline:
1. Notion job arrives as the active input surface.
2. Notion Sync Agent maps the page into the canonical Core job model.
3. The job is upserted into SQLite with Notion page ID as the external key.
4. Lifecycle validation keeps status changes within allowed transitions.
5. Hours, materials, and price data are captured on the job record.
6. `profit_analysis` is recomputed from the job-related inputs.
7. Refresh writes snapshots and the dashboard renders the outputs.
8. The decision layer consumes the evidence and produces a prioritized action when page-level signals justify it.

How the files fit together:
- `synthetic-job.json` is the synthetic example record.
- `validation.md` explains which tests and validation rules enforce the workflow.
- `provenance.md` maps each major section of the JSON to verified private sources and describes the sanitization applied.
- This README is the short guide to the package.

Read this package in order:
1. Scenario and timeline here.
2. Synthetic record in `synthetic-job.json`.
3. Enforcement evidence in `validation.md`.
4. Traceability details in `provenance.md`.
