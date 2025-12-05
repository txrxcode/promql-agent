# promql-agent

CLI-first agent for Prometheus, Loki, Grafana. Run everything from repo root.

## Commands

- Install: `uv sync`
- Run: `uv run promql-agent -q "<question>"`
- Health: `uv run promql-agent --health`
- Tool health: `uv run promql-agent --tools-health`
- Tests: `uv run pytest`

## Layout

- `cli.py` — entry point
- `backend/app/agents/` — agent logic
- `backend/app/tools/` — Prometheus/Loki/Grafana clients
- `backend/app/services/` — LLM service

## Conventions

- No web API. CLI invokes tools directly.
- Env vars in `.env.local` (see `.env.example`).
- Frontend (`frontend/`) is optional side support — do not add features there unless asked.
