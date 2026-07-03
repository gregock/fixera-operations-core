# Architecture Diagram v1

This is a sanitized public view of the private production architecture behind `fixera-core`.
It shows the verified runtime shape without exposing real paths, domains, credentials, customer data, or operational incidents.

```mermaid
flowchart LR
  subgraph EXT[External Sources and Sinks]
    notion[Notion]
    ga4[Google Analytics]
    gsc[Google Search Console]
    visitors[Website visitors]
    telegram[Telegram]
    launchd[macOS launchd]
    backup[Backup target]
  end

  subgraph CORE[Fixera Core on macOS]
    api[FastAPI runtime / API]
    ingest[Ingestion modules]
    refresh[Refresh / reporting]
    ops[Ops automation]
  end

  subgraph STORE[Storage and Runtime Artifacts]
    sqlite[(SQLite database)]
    leads[leads_log.jsonl]
    snapshots[dashboard snapshots]
    history[dashboard history]
    logs[runtime logs]
  end

  subgraph OUT[Outputs]
    browser[Dashboard browser]
    views[Operator views]
    alerts[Alerts / notifications]
    backups[Backups]
  end

  notion --> ingest
  ga4 --> ingest
  gsc --> ingest
  visitors --> api
  telegram --> api
  launchd --> ops

  api --> sqlite
  api --> leads
  ingest --> sqlite
  ingest --> leads
  refresh --> sqlite
  refresh --> snapshots
  refresh --> history
  refresh --> logs
  ops --> logs
  ops --> alerts
  ops --> backup

  sqlite --> refresh
  leads --> refresh
  snapshots --> browser
  snapshots --> views
  history --> views
  logs --> views
  alerts --> telegram
  backups --> backup
  browser --> views
```

Notes:
- The diagram is intentionally compact and single-page.
- It represents the private production architecture in sanitized form.
