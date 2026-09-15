# Testing/QA (QA-*)

## Tasks
- **QA-001** — Test interruption handling end-to-end (correcting a report field mid-flow)
- **QA-002** — Test interruption handling mid-procedure-step playback
- **QA-003** — Test safety-sentinel triggering on out-of-range spoken values
- **QA-004** — Test session resume after disconnect (30s window)

## Notes
- These tests depend on Backend's state tracking (BE-002) and audit log (BE-005) being in place — coordinate timing with whoever owns those.
