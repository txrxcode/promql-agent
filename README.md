# promql-agent

CLI agent for Prometheus, Loki, and Grafana. Ask in natural language, get queries and answers from your stack.

## Quickstart

```bash
uv sync
cp .env.example .env.local
uv run promql-agent -q "What is the current CPU usage?"
```

## CLI

```bash
uv run promql-agent -q "show recent error logs"
uv run promql-agent --health
uv run promql-agent --tools-health
uv run promql-agent --incident "HighCPU" "critical"
uv run promql-agent --demo
```

| Flag | Description |
|------|-------------|
| `-q, --question` | Natural language question |
| `-a, --agent` | Agent type (default: `sre_agent`) |
| `--health` | System health report |
| `--demo` | Run tools demo |
| `--tools-health` | Tool connectivity check |
| `--incident NAME SEV` | Trigger incident workflow |

## How it works

Question → plan action → select tools (LangGraph) → generate PromQL/LogQL → execute → summarize.

## Layout

- `cli.py`, `pyproject.toml` — root entry.
- `backend/app/` — agent, tools, services.
- `demo-grafana-promethues-forked-edited/` — local Prometheus + Loki + Grafana stack.
- `frontend/` — optional Next.js UI (side support).
- `litmus-choa-test/` — chaos experiments.

## License

MIT
