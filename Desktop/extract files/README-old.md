# Aura Field Safety Co-Pilot

Hands-free voice AI agent for frontline field workers (technicians, mechanics, warehouse staff, medical device operators), built on the **AssemblyAI Voice Agent API**.

## The Idea

A voice agent that rides along with a field worker whose hands are occupied with physical equipment. It guides them step-by-step through procedures, flags unsafe readings in real time, and captures near-miss or maintenance events by voice — checking each one against historical patterns before routing a confirmed report to a supervisor.

## The Problem

Field workers can't safely stop to consult a manual or type a log while hands-on with equipment. When something goes wrong, the reporting process is slow enough that details fade or the report never gets filed. Both problems share a root cause: the interface between a physically-occupied worker and the systems that need their information is broken.

## How It Works

One voice session, two conversation patterns the agent switches between based on what the worker says:

| | Guided Field Ops | Safety Reporting |
|---|---|---|
| **Trigger** | "Aura, walk me through …" | "I need to report a near miss…" |
| **Pattern** | Step-by-step, agent-led, waits for confirmation before advancing | Worker-led narrative, agent asks adaptive follow-ups |
| **Output** | Logged maintenance entry + completed procedure | Confirmed report + supervisor pattern signal |

A safety layer runs underneath both modes: it blocks the agent from collecting a report while the worker is still exposed to a hazard, and it flags any spoken reading that falls outside a known safe range, without needing to be asked.

## Architecture

```
[Worker — Mobile App / Wearable Headset]
Continuous or push-to-talk mic capture
AudioWorklet -> Float32 -> PCM16 (24kHz) -> base64
        |
        v
[App Frontend]
- Procedure-step view OR report-field view
- Live transcript + safety alert banner
- Text/keyboard fallback (accessibility)
        |
        v
[Backend — Node.js / Python]
- Mints short-lived token (GET /v1/token, Bearer auth)
- Safety layer: runs on every finalized turn, either mode
- Field Ops tools: manual lookup, step advance, maintenance log
- Reporting tools: missing-field check, similarity search,
  report creation, notifications, corrective-action drafts
- Confirmation gates + supervisor-approval rules
- Full audit history log
        |
        v
[AssemblyAI Voice Agent API]
wss://agents.assemblyai.com/v1/ws
- session.update: system_prompt, greeting, tools[], voice,
  turn_detection tuned for frequent interruptions
- Streams: transcript.user, reply.audio, transcript.agent,
  reply.done, tool.call
        |
        v
[Worker's Speaker/Headset] <- reply.audio (base64 PCM16, 24kHz)
safety warnings interrupt normal playback

[Backend, downstream]
-> Vector DB (technical manuals) for procedure retrieval
-> Embedding + similarity search for incident pattern matching
-> Maintenance DB (Salesforce / Jira / SQL)
-> Safety dashboard + supervisor review UI + notifications
```

## Tool Calls

| Tool | Purpose |
|---|---|
| `check_safety_status()` | Gates reporting; confirms the worker isn't still exposed |
| `check_safety_threshold(parameter, value, context)` | Flags an unsafe reading in either mode |
| `query_manual_db(procedure, step, parameter)` | Vector search over technical manuals |
| `get_next_step(procedure, current_step)` | Advances only on explicit confirmation |
| `log_maintenance_entry(component, action, condition, technician_id)` | Structured DB write |
| `get_missing_fields(schema_state)` | Drives adaptive report follow-up |
| `search_similar_reports(embedding, filters)` | Semantic similarity against prior incidents |
| `create_near_miss(report, idempotency_key)` | Writes the confirmed report |
| `notify_safety_contact(report_id, site_policy)` | Notifies the correct role per policy |
| `draft_corrective_action(report_id, pattern_signal)` | Proposes a fix for supervisor approval |

## Repo Structure

Each top-level folder maps to a task area (see `TASKS.md` for the full SKU breakdown). Put your work in the matching folder and open a PR — see `CONTRIBUTING.md`.

```
audio/         AUD-*  Mic capture, audio playback, turn detection
backend/       BE-*   Session config, state tracking, tool round-trips, confirmation gates, audit log
safety/        SAF-*  Safe-range reference data, safety threshold/status checks, decision boundaries
data/          DAT-*  Vector DB, manual lookup, report schema, missing-field logic, similarity search
integrations/  INT-*  Writes to Salesforce/Jira/SQL, near-miss creation, notifications, corrective actions
frontend/      FE-*   Mode-aware UI, transcript/alert banner, keyboard fallback, supervisor review UI
qa/            QA-*   Interruption tests, safety-sentinel tests, session-resume tests
docs/          DOC-*  System prompt reference, tool schema reference, escalation rules
```

## Getting Started

1. Clone the repo and check `TASKS.md` for your assigned SKU(s).
2. Work inside the matching folder — each has its own `README.md` with more detail.
3. Open a PR referencing your SKU (e.g. `[BE-002] Build conversation state tracking`).
4. See `CONTRIBUTING.md` for branch naming and PR conventions.
