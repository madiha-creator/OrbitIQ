# Contributing to Aura Field Safety Co-Pilot

## 1. Pick a task

Open `TASKS.md`, find an `unclaimed` SKU in your area, and put your name in the Owner column via a small PR (or claim it by commenting on the matching GitHub Issue, if issues are enabled from the templates in `.github/ISSUE_TEMPLATE`).

## 2. Branch naming

```
<area>/<sku>-short-description
```
Examples:
```
backend/be-002-conversation-state
audio/aud-003-mic-capture
safety/saf-002-threshold-check
```

## 3. Where your code goes

Work inside the folder matching your task area (`audio/`, `backend/`, `frontend/`, `data/`, `safety/`, `integrations/`, `qa/`, `docs/`). Each folder has its own `README.md` describing what belongs there and how it plugs into the rest of the system — read it before starting.

## 4. Commits & PRs

- Reference the SKU in your commit messages and PR title, e.g. `[BE-002] Add conversation state tracking`.
- Keep PRs scoped to one SKU where possible.
- In the PR description, note any new environment variables, dependencies, or interfaces other tasks will need to know about (e.g. a new tool schema, a new DB table).
- Tag a reviewer from a neighboring area if your change touches a shared interface (e.g. Backend ↔ Safety, Backend ↔ Data).

## 5. Shared interfaces to keep in sync

These cut across multiple areas — coordinate in the PR or in `docs/` if you change them:
- The `tools[]` schema sent in `session.update` (Backend + Data + Safety + Integrations all define tools that live here).
- The incident report schema (Data defines it; Frontend, Integrations, and Backend all read/write it).
- The audit log format (Backend defines it; QA and Docs depend on it).

## 6. Environment variables

Do not commit secrets. Add any new environment variable your task needs to `.env.example` (create one if it doesn't exist yet) with a placeholder value, and document it in `docs/`.

## 7. Testing

If your task has a corresponding QA task (see `TASKS.md`), coordinate with whoever owns it so your feature is testable (expose hooks, mock endpoints, etc. as needed).
