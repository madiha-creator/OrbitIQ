# Backend (BE-*, plus AUD-002, INT-*)

Node.js / Python service that mediates between the frontend, the AssemblyAI Voice Agent API, and downstream systems.

## Tasks
- **BE-001** — Design `session.update` payload: system_prompt, greeting, tools, voice
- **BE-002** — Build conversation state tracking (current step / report fields / confirmation status)
- **BE-003** — Implement `tool.call` → `tool.result` round trip, incl. interrupted-reply handling
- **BE-004** — Build confirmation-gate logic before any write action
- **BE-005** — Build audit history logging (what was said, changed, confirmed, created)
- **AUD-002** — Token-minting route (`GET /v1/token`, Bearer auth)
- **INT-001** — `log_maintenance_entry` write to Salesforce/Jira/SQL
- **INT-002** — `create_near_miss` write + idempotency handling
- **INT-003** — `notify_safety_contact` per site policy
- **INT-004** — `draft_corrective_action` proposal flow

## Notes
- Every write action (maintenance log, near-miss report, notification, corrective action) must pass through the confirmation gate (BE-004) first.
- The audit log (BE-005) should capture enough to reconstruct: what the worker said, what changed, what was confirmed, and what was created — QA and Docs depend on this format.
