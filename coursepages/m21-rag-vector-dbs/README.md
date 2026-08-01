# Module 21 — RAG, Vector DBs & Retrieval Systems

> **Status:** v2026.3 Practitioner’s Pass · full spec in the root [README.md § Module 21](../../README.md#module-21).

## Why this module exists

Retrieval-Augmented Generation is the single most-deployed LLM pattern in production (Menlo Ventures Oct 2025: >70% of enterprise LLM deployments). Getting chunking + retrieval + reranking + evaluation right is the difference between a demo and a product. Closes Gap #5.

## Primary anchors (P1-verified)

| Resource | Role | Link |
|---|---|---|
| Pinecone Learning Center | Free RAG/vector primer | <https://www.pinecone.io/learn/> |
| LlamaIndex docs | Practical cookbook | <https://docs.llamaindex.ai/> |
| LangChain RAG tutorial | Framework walkthrough | <https://python.langchain.com/docs/tutorials/rag/> |
| pgvector | Postgres vector extension | <https://github.com/pgvector/pgvector> |
| Qdrant | Rust vector DB | <https://qdrant.tech/> |
| Weaviate | Open-source vector DB | <https://weaviate.io/> |
| Milvus | Distributed vector DB | <https://milvus.io/> |
| LanceDB | Embedded, Lance-format vector DB | <https://lancedb.com/> |
| ColBERT | Late-interaction retrieval | <https://github.com/stanford-futuredata/ColBERT> |
| Ragas | RAG evaluation framework | — see `github.com/explodinggradients/ragas` |
| Anthropic — Contextual Retrieval (Sep 2024) | SOTA chunking technique | <https://www.anthropic.com/news/contextual-retrieval> |
| Microsoft GraphRAG (2024) | Graph-based RAG | <https://github.com/microsoft/graphrag> |

## Practitioner decision gate

1. Use **zero/few-shot prompting** when the model already has the needed knowledge and only instruction, format, or reasoning behaviour must improve.
2. Use **RAG** for private, changing, attributable, or access-controlled knowledge; score retrieval and generation separately.
3. Use **fine-tuning/PEFT** to change repeated behaviour, style, structure, or task performance—not merely to inject facts.
4. Combine approaches only after ablations justify quality, latency, cost, security, maintenance, and rollback trade-offs.

## Mandatory mini-projects

1. Build a RAG over your own PDFs: chunking → pgvector → BGE reranker → answer-with-citations; measure Ragas faithfulness + context precision.
2. Hybrid search A/B: BM25-only vs dense-only vs hybrid-with-RRF; measure nDCG@10 on a labelled query set.
3. GraphRAG on a technical corpus; compare multi-hop accuracy vs vanilla RAG.
4. Add a CI eval gate over a versioned query set and adversarial tests for direct/indirect prompt injection, poisoned documents, source-ACL bypass, and data exfiltration.

**Definition of done:** tests for retrieval, citations, abstention, ACLs, and failure paths; `README` with architecture and limitations; short results memo with quality, latency, and cost. **Production stretch:** deploy with tracing and alert on eval regressions.

## Prerequisites

- Module 18 (LLMs, tokenisation), Module 11 (embeddings, cosine similarity, PCA/SVD), Module 8a (SQL metadata filters + hybrid search)
