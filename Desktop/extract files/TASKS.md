# Task Breakdown

Each task has a SKU (code) for assignment and tracking. Prefix indicates area: **AUD**=Audio/Voice, **BE**=Backend, **FE**=Frontend, **DAT**=Data/Retrieval, **SAF**=Safety Logic, **INT**=Integrations, **QA**=Testing/QA, **DOC**=Docs.

Fill in **Owner** and **Status** as the team claims tasks (Status: `unclaimed` / `in progress` / `in review` / `done`).

| SKU | Task | Area | Owner | Status |
|---|---|---|---|---|
| AUD-001 | Set up AssemblyAI API key + secure server-side storage | Audio/Voice | | unclaimed |
| AUD-002 | Build token-minting backend route (GET /v1/token, Bearer auth) | Audio/Voice | | unclaimed |
| AUD-003 | Implement mic capture: AudioWorklet, Float32→PCM16→base64, 24kHz | Audio/Voice | | unclaimed |
| AUD-004 | Implement audio playback buffer for reply.audio (no sleep-scheduling) | Audio/Voice | | unclaimed |
| AUD-005 | Tune turn detection (vad_threshold, interruption_delay) for frequent interruptions | Audio/Voice | | unclaimed |
| BE-001 | Design session.update payload: system_prompt, greeting, tools, voice | Backend | | unclaimed |
| BE-002 | Build conversation state tracking (current step / report fields / confirmation status) | Backend | | unclaimed |
| BE-003 | Implement tool.call → tool.result round trip, incl. interrupted-reply handling | Backend | | unclaimed |
| BE-004 | Build confirmation-gate logic before any write action | Backend | | unclaimed |
| BE-005 | Build audit history logging (what was said, changed, confirmed, created) | Backend | | unclaimed |
| SAF-001 | Define safe-range reference data per procedure/parameter | Safety Logic | | unclaimed |
| SAF-002 | Implement check_safety_threshold — flags unsafe spoken readings | Safety Logic | | unclaimed |
| SAF-003 | Implement check_safety_status — blocks reporting while worker is exposed | Safety Logic | | unclaimed |
| SAF-004 | Define decision boundaries: automatic vs confirm vs supervisor-approve vs never | Safety Logic | | unclaimed |
| DAT-001 | Build/index vector database of technical manuals | Data/Retrieval | | unclaimed |
| DAT-002 | Implement query_manual_db similarity search + safe-range context return | Data/Retrieval | | unclaimed |
| DAT-003 | Design incident report schema with field-status tags | Data/Retrieval | | unclaimed |
| DAT-004 | Implement get_missing_fields adaptive follow-up logic | Data/Retrieval | | unclaimed |
| DAT-005 | Build embedding + similarity search for incident pattern matching | Data/Retrieval | | unclaimed |
| INT-001 | Implement log_maintenance_entry write to Salesforce/Jira/SQL | Integrations | | unclaimed |
| INT-002 | Implement create_near_miss write + idempotency handling | Integrations | | unclaimed |
| INT-003 | Implement notify_safety_contact per site policy | Integrations | | unclaimed |
| INT-004 | Implement draft_corrective_action proposal flow | Integrations | | unclaimed |
| FE-001 | Build mode-aware app UI: procedure-step view / report-field view | Frontend | | unclaimed |
| FE-002 | Build live transcript + safety-alert banner UI | Frontend | | unclaimed |
| FE-003 | Build text/keyboard fallback input path | Frontend | | unclaimed |
| FE-004 | Build supervisor review UI: approve/edit/reject actions | Frontend | | unclaimed |
| QA-001 | Test interruption handling end-to-end (correcting a report field mid-flow) | Testing/QA | | unclaimed |
| QA-002 | Test interruption handling mid-procedure-step playback | Testing/QA | | unclaimed |
| QA-003 | Test safety-sentinel triggering on out-of-range spoken values | Testing/QA | | unclaimed |
| QA-004 | Test session resume after disconnect (30s window) | Testing/QA | | unclaimed |
| DOC-001 | Write example system prompt and tool schema reference for the team | Docs | | unclaimed |
| DOC-002 | Document decision boundaries and escalation rules for reviewers | Docs | | unclaimed |

## Suggested known assignment

- **Backend (BE-001–005, AUD-001–002, INT-001–004):** Madeha — session config, state tracking, tool.call/result handling, confirmation gates, audit log, token minting, DB writes.

Everyone else: claim your SKU(s) above by editing this table in a PR, or by commenting on the matching GitHub Issue (see `.github/ISSUE_TEMPLATE`).
