# Audio/Voice (AUD-*)

Client-side audio pipeline: capture, playback, and turn-detection tuning for the AssemblyAI Voice Agent WebSocket.

## Tasks
- **AUD-001** — Set up AssemblyAI API key + secure server-side storage
- **AUD-002** — Build token-minting backend route (`GET /v1/token`, Bearer auth) *(shared with Backend — see backend/)*
- **AUD-003** — Implement mic capture: AudioWorklet, Float32 → PCM16 → base64, 24kHz
- **AUD-004** — Implement audio playback buffer for `reply.audio` (no sleep-scheduling)
- **AUD-005** — Tune turn detection (`vad_threshold`, `interruption_delay`) for frequent interruptions

## Notes
- Audio in/out is 24kHz PCM16, base64-encoded over the WebSocket (`wss://agents.assemblyai.com/v1/ws`).
- Safety warnings must be able to interrupt normal `reply.audio` playback — coordinate with `safety/` on how an interrupt signal is surfaced.
