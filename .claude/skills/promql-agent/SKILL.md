---
name: promql-agent
description: Use to ask the local promql-agent CLI for Prometheus/Loki/Grafana answers. Trigger when the user asks about metrics, logs, alerts, system health, or PromQL/LogQL queries.
---

# promql-agent

Run from repo root. No API server needed — the CLI calls tools directly.

## Commands

- `uv run promql-agent -q "<question>"` — natural language query
- `uv run promql-agent --health` — system health report
- `uv run promql-agent --tools-health` — check Prometheus/Loki/Grafana connectivity
- `uv run promql-agent --incident "<alert>" "<severity>"` — incident workflow
- `uv run promql-agent --demo` — tool demo

## Setup

`cp .env.example .env.local` and set `LLAMA_API_KEY` (and optional `PROMETHEUS_URL`, `LOKI_URL`, `GRAFANA_URL`).

## When to use

Prefer the CLI over reading raw exporter output. Always run `--tools-health` first if a query fails — usually a missing endpoint env var.
