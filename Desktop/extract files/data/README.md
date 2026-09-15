# Data/Retrieval (DAT-*)

Vector search, report schema, and similarity matching.

## Tasks
- **DAT-001** — Build/index vector database of technical manuals
- **DAT-002** — Implement `query_manual_db` similarity search + safe-range context return
- **DAT-003** — Design incident report schema with field-status tags
- **DAT-004** — Implement `get_missing_fields` adaptive follow-up logic
- **DAT-005** — Build embedding + similarity search for incident pattern matching

## Notes
- The incident report schema (DAT-003) is shared: Frontend renders it, Integrations writes it, Backend tracks its fill-state. Post any schema change in the PR description and tag those areas.
