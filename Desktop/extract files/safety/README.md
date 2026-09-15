# Safety Logic (SAF-*)

The safety layer that runs underneath both conversation modes, on every finalized turn.

## Tasks
- **SAF-001** — Define safe-range reference data per procedure/parameter
- **SAF-002** — Implement `check_safety_threshold` — flags unsafe spoken readings
- **SAF-003** — Implement `check_safety_status` — blocks reporting while worker is exposed
- **SAF-004** — Define decision boundaries: automatic vs confirm vs supervisor-approve vs never

## Notes
- `check_safety_threshold` and `check_safety_status` are called by Backend on every finalized turn, in either mode — keep their interfaces stable or coordinate changes with `backend/`.
- SAF-004's decision boundaries feed directly into Backend's confirmation-gate logic (BE-004).
