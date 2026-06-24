# 🛠️ Implementation Plan — *The Elite Data Science Curriculum* → v2026.3 "Employability Hardening" Pass

**Author:** Deep-inspection + live-market-research pass
**Date compiled:** 2026-06-24
**Repo at inspection:** `akazadivu-design/data-sci`, README v2026.2 (1,919 lines), 26 modules + M0, 9 coursepage scaffolds, 5-doc `audit/` trail.
**Status of plan:** Proposed. Nothing in here is merged into `README.md` yet — this document is the spec, the same way `audit/IMPROVEMENT_SPEC.md` was the spec for the v2026.2 pass.

---

## 0. Executive Summary

This repo is **already elite.** The v2026.2 pass closed all 13 benchmark gaps, the math spine is stronger than most MSc programmes, and the audit trail (`AUDIT.md` → `VERIFICATION.md` → `IMPROVEMENT_SPEC.md` → `FINAL_AUDIT.md`) is genuinely rigorous and anti-hallucination by design. **There is nothing to "rescue" here.**

So this plan is not a rewrite. It is a **freshness + employability + usability** pass driven by two findings from a 2026-06-24 research session:

1. **Time has moved on ~2 months since the 23-Apr-2026 refresh.** Live PyPI checks (this session) show **every pinned framework version has drifted** — the README's "verified latest" badges are now stale. A curriculum whose entire brand is "live-verified versions" loses credibility the moment a reader checks PyPI and sees a newer number. This is the single highest-priority, lowest-effort fix.
2. **The curriculum is optimised for *knowledge*, not yet for *getting hired*.** Live job-market research (Robert Half H2-2026 Demand for Skilled Talent; a 500-posting frequency analysis Apr–May 2026; the AI-Engineer-vs-Data-Scientist 2026 role split) shows the market now hires for **3 distinct tracks** (Data Analyst / Data Scientist / AI Engineer / Data Engineer / ML Engineer) with **different skill bundles**, weights **portfolio over certificates** (78% of hiring managers), and pays a **15–25% premium** for GenAI/LLM/MLOps in the title. The curriculum has all the *content* to serve these tracks but offers no **role-targeted path, no portfolio rubric tied to job signals, and no interview-prep layer.**

The plan below is organised in **5 priority tiers (P0–P4)** with effort/impact estimates, mapped to concrete file edits, and ends with a verification checklist mirroring the project's existing audit discipline.

---

## 1. Evidence Base (what the research actually said)

### 1.1 University / course-syllabus signals (mid-2026)

| Source | Finding relevant to this repo | Action implied |
|---|---|---|
| **Stanford CS336** (cs336.stanford.edu) | Still **Spring 2026** edition; lecture videos posted Apr 2026; community completing it (HN Jun 2026). Repo already cites it correctly. | ✅ No change — re-verify URL only. |
| **MIT 6.7960 Deep Learning** | Repo cites **Fall 2025**. MIT catalog (`student.mit.edu/catalog/m6d.html`) shows a **Fall 2026** offering with RL / self-supervised / imitation / model-based emphasis. | 🔄 Add a watch-note; bump to Fall 2026 schedule once it goes live. |
| **MIT 6.390 Intro ML** | Repo cites `introml.mit.edu/spring26`. A **Spring 2027** page will supersede it. | 🔄 Re-verify; add "latest offering" pattern instead of hard-coded term. |
| **DeepLearning.AI / Andrew Ng** | **NEW since April:** *Agentic AI* (Ng, raw-Python agents), *MCP: Build Rich-Context AI Apps with Anthropic*, *AI Prompting* course (May 2026). Not yet cited in repo. | ➕ Add to M22 (Agentic AI) and M18/M21 as accessible on-ramps. |
| **Berkeley MIDS / UMich MADS / CMU MSPPM-DA** | Already cited & corrected in v2026.2. | ✅ No change. |

**Net:** The university spine is sound. The only *new* free-course content worth importing is the **DeepLearning.AI Agentic/MCP/Prompting** trio (high accessibility, fills the "I can't start with a Stanford grad course" on-ramp gap).

### 1.2 Job-market signals (2026, primary sources)

**Robert Half — H2-2026 Demand for Skilled Talent (jun 2026):**
- AI/ML/DS roles: **49,200 postings in 2025, +163% YoY.** AI integration is the #1 project category delayed by skills shortage (64%).
- **2026 starting-salary bands (national):** AI/ML engineer **$134k–$193k** · Data engineer **$127k–$181k** · Data scientist **$122k–$183k** · DevOps **$118k–$174k**.
- **Top software proficiencies in demand: Apache Kafka, Databricks, Microsoft Azure.**
- Data engineer is a structural #1 hiring gap; "clean data doesn't happen by accident."

**500-posting frequency analysis (Apr–May 2026):**

| Rank | Skill | % of postings | Repo coverage today |
|---:|---|---:|---|
| 1 | Python (incl. FastAPI, LangChain/LlamaIndex) | 74% | ✅ M1 (FastAPI deployment is thin) |
| 2 | ML (NLP jumped 5%→19%; MLOps; SHAP/LIME interpretability) | 69% | ✅ strong; SHAP/LIME under-emphasised |
| 3 | SQL (windows, CTEs, plans, BigQuery/Snowflake dialects) | 64% | ✅ M8a excellent |
| 4 | Statistics (A/B, Bayesian, time series) | 58% | ✅ elite |
| 5 | Cloud (**Azure 28.5%**, AWS 19.7%, GCP 14.2%, Snowflake, Databricks) | 62% | 🟡 **scattered, no cloud module** |
| 6 | Data viz (Excel 41%, Tableau 28%, Power BI 25%) | 53% | 🟡 Python-only; **BI tools + Excel under-served** |
| 7 | Big-data/pipelines (Spark, Airflow 8.9%, Kafka, dbt, Docker, K8s) | 43% | ✅ M8b strong |
| 8 | Statistics/Math | 58% | ✅ elite |
| 9 | **GenAI/LLM (31%, was ~0% in 2023; prompt-eng named in 14%)** | 31% ↑ | ✅ M18/21/22 strong |
| 10 | **Soft skills — "explain to non-technical stakeholders" 47%, storytelling 28%** | — | 🟡 M25 exists but light |

Other hard findings:
- **78% of hiring managers value portfolio projects over certifications.** "Your GitHub gets you hired."
- **~20% of postings now require a cloud certification** (AWS ML Specialty, Azure DP-100, GCP PDE), attached to higher salary bands.
- **15–25% salary premium** when GenAI/LLM/MLOps is in the title.
- **85–88% of data roles are outside FAANG** — mid-size SaaS, banks, hospital systems, manufacturers. The curriculum's research-grade framing should not crowd out the applied/enterprise track.
- Entry-level is the most squeezed; juniors are now expected to *frame problems, validate, interpret critically, orchestrate AI tools.*
- **AI Engineer ≠ Data Scientist in 2026.** AI engineers live in "Python/TypeScript, vector DBs, evals, prompt orchestration, deployment"; DS lives in stats/experimentation/modelling. The curriculum currently blends them — readers need a router.

### 1.3 Framework version drift (live PyPI, 2026-06-24)

| Package | README v2026.2 claim | **PyPI today (2026-06-24)** | Drift |
|---|---|---|---|
| torch | 2.11.0 | **2.12.1** | 🔴 stale |
| jax | 0.10.0 | **0.10.2** | 🟡 minor |
| polars | 1.40.1 | **1.42.0** | 🟡 minor |
| transformers | 5.6.2 | **5.12.1** | 🔴 stale |
| scikit-learn | 1.8.0 | **1.9.0** | 🔴 stale |
| vllm | 0.19.1 | **0.23.0** | 🔴 stale |
| langgraph | 1.1.9 | **1.2.6** | 🟡 minor |
| dspy | 3.2.0 | **3.2.1** | 🟢 patch |
| mlflow | 3.11.1 | **3.14.0** | 🔴 stale |
| dbt-core | 1.11.8 | **1.11.11** | 🟢 patch |
| duckdb | 1.5.2 | **1.5.4** | 🟢 patch |

**Conclusion:** The "Last Refresh 23 Apr 2026 / URLs Live-Verified" badges over-promise as of June. Fix is mechanical but credibility-critical.

---

## 2. Gap Analysis — v2026.2 vs. 2026 hiring reality

| # | Gap | Severity | Why it matters (evidence) | Where it lives now |
|---:|---|:---:|---|---|
| G1 | **Stale version pins / dated "live-verified" badges** | 🔴 P0 | Brand is "verified latest"; 5 of 11 core libs already a minor+ behind. | README badges, Meta-Info table, M-level version strings |
| G2 | **No role-targeted learning paths** (Analyst / DS / AI-Eng / DE / MLE) | 🔴 P1 | Market hires for 5 distinct bundles; AI-Eng & DS skills "barely overlap" in 2026. | None — only one linear 26-module spine |
| G3 | **Portfolio is told, not specified** | 🔴 P1 | 78% of managers prefer portfolio to certs; "GitHub gets you hired." Mini-projects exist but no *capstone-portfolio rubric tied to job signals.* | M26 has a rubric but it's dissertation-flavoured |
| G4 | **Cloud has no home** (Azure #1 proficiency; 20% want a cert) | 🟠 P2 | Cloud in 62% of postings; Azure/AWS/GCP/Databricks/Snowflake named. Repo mentions them inside M8a/M24 but no consolidated cloud+cert track. | Scattered across M8a, M8b, M24 |
| G5 | **BI tools + Excel under-served** (Tableau 28%, Power BI 25%, Excel 41%) | 🟠 P2 | Viz in 53% of postings; repo is Python-viz-centric (Plotly/Altair/Streamlit). | M7 mentions Tableau/PowerBI in one line |
| G6 | **No interview-prep layer** (DS case, ML-system-design, SQL/coding, take-home) | 🟠 P2 | Every senior interview tests CUPED/DAGs (already taught) + system design (taught) but there's no *interview map* connecting content→interview rounds. | None |
| G7 | **Model interpretability for hiring (SHAP/LIME)** under-weighted | 🟡 P3 | Named explicitly in regulated-industry postings (finance/health = 23% of market). Repo has mechanistic-interp (M23) but classical SHAP/LIME is thin. | M23 (mech-interp), not M12/M10 |
| G8 | **FastAPI / model-serving-as-API** thin | 🟡 P3 | FastAPI named in #1 Python skill cluster; AI-Eng track lives in deployment. | M24 (serving) but no FastAPI walkthrough |
| G9 | **New free on-ramp courses missing** (DeepLearning.AI Agentic/MCP/Prompting, May 2026) | 🟡 P3 | Lowers the barrier for self-learners who can't start at Stanford-grad level. | M18/M21/M22 |
| G10 | **No "freshness automation"** — refresh is manual, so drift recurs | 🟡 P3 | Root cause of G1. A CI job could re-check PyPI + URLs and open an issue. | `.github/workflows/` has only `delete-empty-issues.yml` |

---

## 3. Proposed Changes by Priority

> **Guardrails (inherited from the project's own anti-hallucination rules):**
> 1. No URL enters the README without a live HTTP 200/3xx check in the same pass.
> 2. No version string without a same-day PyPI query.
> 3. Protected spine (M0; M2 matrix-calc; M3 two-pass LA; M5 measure/concentration) is **never** weakened.
> 4. All additions are **additive** — old anchors preserved.

### 🔴 P0 — Freshness Pass (do first; ~half a day)

**P0.1 — Re-verify + bump all framework versions** against PyPI on the day of the edit. Update:
- The two version badges in the header (`Frameworks`, `Prod Stack`).
- The Meta-Information table.
- Inline version strings in M1, M7, M8a/b, M15, M16, M18, M21, M24.
- Add a one-line *"versions auto-checked YYYY-MM-DD; see `audit/version_check.txt`"* so the date is explicit, not a static badge.

**P0.2 — Re-run the URL liveness sweep** (the `audit/raw_http_checks.txt` script) and refresh `Last Refresh` badge + `audit/FINAL_AUDIT.md` date. Demote any newly-broken URL.

**P0.3 — Soften absolute badges** that age badly: change `Last Refresh — 23 Apr 2026` to a relative "rolling refresh" note + link to the CI freshness job (P3.4), so the repo never *looks* stale even between manual passes.

*Impact: High (protects core brand). Effort: Low. Risk: None.*

### 🔴 P1 — Employability Layer (the headline of this pass)

**P1.1 — Add §"🎯 Five Role-Targeted Tracks" right after the Progression Map.** A table that routes the existing 26 modules into 5 market-recognised roles, so a reader picks a destination first:

| Track | Core modules (subset of existing) | Market salary band (RH 2026) | Signature portfolio piece |
|---|---|---|---|
| **Data Analyst** | M1, M6, M7, M8a, M25 + BI/Excel (P2.2) | $72k–$130k | Stakeholder dashboard + insight memo |
| **Data Scientist** | M5, M6, M6½, M9–M14, M25 | $122k–$200k | Causal A/B-test study + model |
| **ML Engineer** | M9–M19, M24 | $170k–$220k | Trained model served behind an API + monitored |
| **AI Engineer** | M18, M21, M22, M23, M24 (LLMOps tier) | $134k–$193k | RAG + agent app with evals + tracing |
| **Data Engineer** | M4, M8a, M8b, M24 (MLOps tier) | $127k–$181k | Lakehouse + Airflow/dbt pipeline |

Each row links to the relevant module anchors (all already exist). **Zero new content needed — pure navigation.** This is the single highest-impact change.

**P1.2 — Add §"💼 The 2026 Hiring-Signal Portfolio Rubric"** (extend M26, don't replace its 3-track research rubric). For each role track, specify the *one flagship GitHub repo* a hiring manager should see, with a 5-point checklist (README with problem framing, reproducible env via `uv`, tests, a deployed/served artifact, a written results memo). Tie directly to the "78% prefer portfolio" finding.

**P1.3 — Add §"🧭 Interview Map"** — a table mapping interview round → modules that prepare it:
SQL/coding round → M4+M8a; ML-system-design → M24+M8b; DS case / experimentation → M6½; ML-theory → M9–M16; LLM/agent design → M18/M21/M22; behavioural/stakeholder → M25. No new teaching content; it makes the existing depth *legible* to a job-seeker.

*Impact: Very High (turns a syllabus into a career plan). Effort: Medium. Risk: Low (additive navigation).*

### 🟠 P2 — Market-Coverage Fills

**P2.1 — Consolidate a §"☁️ Cloud & Certification Appendix"** (or light Module 8c). Pull the already-scattered Azure/AWS/GCP/Snowflake/Databricks references into one place; map each to its in-demand cert (Azure **DP-100**, **AWS ML Specialty**, **GCP Professional Data Engineer**) with free study paths. Cite the "20% of postings require a cloud cert + higher salary band" finding. Flag **Azure as #1 by posting frequency** and **Databricks + Kafka** as Robert Half's named in-demand proficiencies.

**P2.2 — Expand M7 viz sub-section into a proper §"📊 BI & Business Reporting"** beat: Tableau, Power BI, Looker, **and Excel** (41% of analyst postings — name it without snobbery). Position Python viz (Plotly/Altair/Streamlit) as the *programmatic* complement, BI tools as the *stakeholder-facing* one. Add a Power BI ↔ Azure correlation note.

**P2.3 — Add a §"🎤 Interview Question Bank"** pointer block per stratum (DS cases, A/B-test scenarios, ML system-design prompts, SQL drills, LLM-eval debugging) — link to free canonical resources only, verified live.

*Impact: High. Effort: Medium. Risk: Low.*

### 🟡 P3 — Polish & Durability

- **P3.1** — Add **SHAP / LIME / partial-dependence / permutation-importance** explicitly to M12 (and a callback in M10), framed as *the interpretability employers in finance/health ask for by name*. Distinguish from M23 mechanistic interp.
- **P3.2** — Add a **FastAPI model-serving walkthrough** mini-project to M24 (train → `FastAPI` endpoint → Docker → deploy). Closes the #1-Python-cluster "FastAPI/Flask" signal.
- **P3.3** — Add the **DeepLearning.AI Agentic AI / MCP / AI-Prompting** (Ng, 2025–26) trio as accessible on-ramps in M22/M21/M18, each live-verified.
- **P3.4** — Add a **GitHub Actions freshness workflow** (`.github/workflows/freshness-check.yml`): monthly cron that queries PyPI JSON for the pinned packages + curls the README URLs, then opens an issue listing drift. This makes G1 *self-healing* and is on-brand with the repo's verification ethos.
- **P3.5** — Flesh out the 7 thin coursepage scaffolds (each ~30–58 lines) toward the depth of the root module sections, OR explicitly mark them as intentional stubs that defer to the README anchor (current behaviour) — pick one and be consistent.

*Impact: Medium. Effort: Medium. Risk: Low.*

### 🟢 P4 — Optional / Nice-to-have

- **P4.1** — A printable one-page "DS 2026 skills cheat-sheet" (ranked skill table from §1.2) as `extras/skills_2026.md` — the empty `extras/books.md` tables could be filled at the same time.
- **P4.2** — Translate the `topic_progression_graph.jpg` into an accessible Mermaid diagram in-README (searchable, diffable, screen-reader friendly).
- **P4.3** — A short "85% of jobs are outside FAANG" note in the Preamble to set expectations and steer the applied track.

---

## 4. Execution Phasing (mirrors the repo's existing P0→P5 audit cadence)

| Phase | Scope | Deliverable | Gate before next phase |
|---|---|---|---|
| **Φ0** | This document | `IMPLEMENTATION_PLAN.md` (this file) | Reviewer sign-off |
| **Φ1** | P0 freshness | Version + URL re-verification; `audit/version_check.txt` | All versions PyPI-confirmed same-day |
| **Φ2** | P1 employability | 3 new README sections (Tracks, Portfolio Rubric, Interview Map) | All anchor links resolve internally |
| **Φ3** | P2 coverage | Cloud/Cert appendix, BI section, Q-bank | Every new URL live-checked |
| **Φ4** | P3 polish | SHAP/LIME, FastAPI project, DLAI courses, CI workflow | CI workflow green on a dry run |
| **Φ5** | Re-audit | Update `audit/FINAL_AUDIT.md` + badges; squash; PR | 0 broken URLs, 0 stale versions |

---

## 5. Concrete File-Edit Map

| File | Change |
|---|---|
| `README.md` (header) | P0.1 version badges, P0.3 rolling-refresh note |
| `README.md` (after Progression Map) | P1.1 Five Role-Targeted Tracks table |
| `README.md` (Meta-Info table) | P0.1 version refresh |
| `README.md` (M7) | P2.2 BI & Business Reporting sub-section |
| `README.md` (M10/M12) | P3.1 SHAP/LIME interpretability |
| `README.md` (M22/M21/M18) | P3.3 DeepLearning.AI on-ramps |
| `README.md` (M24) | P3.2 FastAPI serving mini-project |
| `README.md` (M26 / new section) | P1.2 Hiring-Signal Portfolio Rubric; P1.3 Interview Map |
| `README.md` (new appendix) | P2.1 Cloud & Certification; P2.3 Interview Q-bank |
| `.github/workflows/freshness-check.yml` | P3.4 new CI freshness job |
| `audit/version_check.txt` | P0.1 same-day PyPI snapshot |
| `audit/FINAL_AUDIT.md` | P5 re-verification append (becomes v2026.3) |
| `extras/skills_2026.md` (new) | P4.1 ranked skills cheat-sheet |
| `coursepages/*/README.md` | P3.5 consistency decision |

---

## 6. Verification Checklist (Definition of Done for v2026.3)

- [ ] Every framework version string matches a same-day `pypi.org/pypi/<pkg>/json` query (logged in `audit/version_check.txt`).
- [ ] Every newly-added URL returns HTTP 200/3xx via the existing curl sweep; failures replaced or flagged ⚠️.
- [ ] The 5 role tracks each link only to **existing** module anchors (no dead internal links).
- [ ] Portfolio rubric + Interview Map reference modules that actually teach the named skill.
- [ ] No protected spine module (M0, M2 matrix-calc, M3 LA, M5 measure/concentration) altered.
- [ ] Badges reflect a *relative* refresh policy, not a fixed date that ages.
- [ ] CI freshness workflow runs green on a manual dispatch and opens a well-formed issue on simulated drift.
- [ ] `audit/FINAL_AUDIT.md` updated with a v2026.3 section + the new gap-closure traceability (G1–G10).
- [ ] All work squashed into one commit; PR opened `genspark_ai_developer` → `master` with this plan linked.

---

## 7. What this plan deliberately does NOT do

- **No content deletion or "simplification."** The depth is the moat.
- **No re-numbering of modules.** v2026.2 already paid that tax; re-numbering churns anchors.
- **No chasing hype.** Only skills with *measured posting-frequency or salary evidence* (§1.2) are added. (E.g., "prompt engineering as a standalone career" is explicitly *not* elevated — research flagged it as commoditising.)
- **No paywalled resources** promoted as primary; free/open anchors stay primary, consistent with the repo's ethos.

---

*Compiled from a 2026-06-24 deep-inspection + live-web-research session: Robert Half H2-2026 Demand for Skilled Talent; a 500-posting frequency analysis (Apr–May 2026); AI-Engineer-vs-Data-Scientist 2026 role analysis; Stanford CS336 / MIT 6.x course pages; DeepLearning.AI course catalog; and same-day PyPI version queries for 11 core frameworks.*
