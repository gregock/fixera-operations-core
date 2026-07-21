# Safety Boundaries

This document defines what stays out of the public Portfolio Edition.

## Do not publish

- production data
- production databases
- deployable private backend code
- secrets
- credentials
- logs
- backups
- internal incident notes
- private configuration
- sensitive operational details
- raw operational exports

## Public-safe material

- architecture diagrams
- abstracted runtime component names and artifact categories when needed for explanation
- synthetic sample data
- workflow summaries
- sanitized validation notes
- boundary explanations

## Review rule

If a file would reveal a real client, a live operational event, deployable private implementation, or sensitive runtime detail, it belongs in the private repository instead.
