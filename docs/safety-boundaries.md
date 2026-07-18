# Safety Boundaries

This document defines what stays out of the public Portfolio Edition.

## Do not publish

- production data
- secrets
- credentials
- logs
- backups
- internal incident notes
- private infrastructure references
- raw operational exports

## Public-safe material

- architecture diagrams
- synthetic sample data
- workflow summaries
- sanitized validation notes
- boundary explanations

## Review rule

If a file would reveal a real client, a live operational event, or the private runtime shape, it belongs in the private repository instead.
