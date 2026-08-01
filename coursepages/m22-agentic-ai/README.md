# Module 22 — Agentic AI (LangGraph, CrewAI, MCP & A2A)

> **Status:** v2026.3 Practitioner’s Pass · full spec in the root [README.md § Module 22](../../README.md#module-22).

## Why this module exists

2025 was the "year of the agent" and 2026 is the year of *reliable* agents. Every 2026 senior AI-engineer interview covers LangGraph + MCP + SWE-bench. Closes Gap #4 of the benchmark PDF.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Hugging Face AI Agents Course (free, certified) | Primary course | <https://huggingface.co/learn/agents-course/> |
| Berkeley LLM Agents MOOC | University course | <https://llmagents-learning.org/> |
| Anthropic — Building Effective Agents (Dec 2024) | Canonical patterns article | <https://www.anthropic.com/research/building-effective-agents> |
| LangGraph | Stateful multi-agent framework | <https://www.langchain.com/langgraph> |
| CrewAI **1.15.5** (PyPI checked 2026-07-26) | Role-based orchestration; use only when explicit roles improve measured outcomes | <https://docs.crewai.com/> · <https://pypi.org/pypi/crewai/json> |
| smolagents (Hugging Face) | ~1000 LOC code-agents | <https://github.com/huggingface/smolagents> |
| Model Context Protocol | LLM↔tool/data open standard | <https://modelcontextprotocol.io/> |
| MCP 2025-06-18 spec | Latest MCP revision | <https://modelcontextprotocol.io/specification/2025-06-18> |
| MCP reference servers | Filesystem, GitHub, Postgres, Slack, etc. | <https://github.com/modelcontextprotocol/servers> |
| GAIA benchmark | General assistant eval | <https://huggingface.co/gaia-benchmark> |
| SWE-bench | Real GitHub issues eval | <https://www.swebench.com/> |
| E2B / Daytona / Modal | Agent sandboxing | <https://e2b.dev/> · <https://www.daytona.io/> · <https://modal.com/> |

## Selection rule

Start with a prompt, then a deterministic workflow, and adopt a full agent only when an evaluated task requires dynamic tool choice or recovery. Use the M21 gate for zero-shot vs RAG vs fine-tuning; agent orchestration does not remove the need for that decision.

## Mandatory mini-projects

1. Build an MCP server that exposes a small SQL DB; connect it to Claude Desktop or Cursor; run 10 queries.
2. LangGraph multi-agent researcher: planning → parallel web-search → synthesis → citation-checking; trace with LangSmith.
3. Run a minimal agent on 5 SWE-bench instances; measure pass@1 vs pass@10.
4. Add a versioned CI scenario suite covering task success, valid tool calls, cost/latency budgets, human escalation, direct/indirect prompt injection, poisoned tool output, PII/secret exfiltration, unsafe retries, and irreversible-action approval gates.

**Definition of done:** typed tool schemas, unit/integration/eval tests, least-privilege allowlists, sandboxing, audit logs, kill switch, `README`, and results memo. **Production stretch:** deploy with tracing, regression alerts, and a human-approval path.

## Prerequisites

- Module 18 (LLMs, tool-use, function calling), Module 21 (retrieval)
