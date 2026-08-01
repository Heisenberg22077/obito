# v2026.3 Practitioner’s Pass — Research and Release Audit

**Audit date:** 2026-08-01  
**Branch:** `feat/v2026.3-practitioners-pass`  
**Target:** `genspark_ai_developer`  
**Edition:** 2026.3 Practitioner’s Pass

## 1. Scope and method

This audit covers the additive practitioner route, Module 1 pacing, project requirements, career operations, practitioner books, production standards, coursepage alignment, and release hygiene. The governing rule was **expand rather than replace**: preserve the academic/research spine while making the application route explicit about its speed/depth trade-off.

External links were checked with:

```bash
curl -ILs -A "Mozilla/5.0" --max-time 15
```

Classification follows the repository convention:

- **PASS:** HTTP 2xx or 3xx.
- **WARN:** 401/403/405/429 where the resource is known but rejects automated requests.
- **FAIL:** 404, DNS failure, or connection failure in active curriculum content.

The release-gate scan covers `README.md` and all files under `coursepages/`. Historical source/audit records are scanned separately because they intentionally retain rejected URLs as evidence. Every unique URL introduced by this pass is recorded in [`VERIFICATION.md`](VERIFICATION.md).

## 2. Editorial result

### Practitioner route and academic trade-off

The new six-phase fast lane targets 6–9 months at 12–18 focused hours per week:

1. Python that works.
2. Math intuition first.
3. Classical ML overview.
4. Mechanical understanding through NumPy implementations.
5. AI Engineer application stack.
6. Production wrap.

It is not presented as equivalent to the full academic route. The README states that proof literacy, measure theory, abstract linear algebra, and derivation-heavy deep learning are deferred, and tells learners when to return. The full route and protected resources remain available beside it.

### Module 1 evidence

The two required Scrimba articles were fetched and reviewed:

- **How to Learn Python: A Beginner’s Guide (2026):** supports four phases—Foundations (weeks 1–4), Working Python (weeks 5–8), Real-World Python (weeks 9–14), and Specialisation (months 4–6+). It distinguishes 9–12 month entry-level readiness from basic syntax acquisition, requires phase-matched projects, recommends two hours building per hour watching, tells learners to rebuild from memory, and restricts AI assistants from bypassing understanding.
- **Best Free Python Courses for Beginners in 2026:** compares eight routes by depth and format: Scrimba, CS50P, Helsinki, freeCodeCamp, Python for Everybody, the official tutorial, Google’s Python Class, and *Automate the Boring Stuff*. This became the README’s eight-course selection matrix rather than an instruction to complete all eight.

The editorial term **fluency illusion** names the failure mode in which generated code feels familiar but cannot be reproduced or debugged independently.

### Video evidence and timestamps

Automated YouTube subtitle download was bot-blocked, so semantic analysis was used and timestamp claims were checked against the analysed media:

| Source | Evidence used |
|---|---|
| *How to Become an ML Engineer* | Math intuition at **01:13–02:16**; from-scratch NumPy at **05:01–05:20**; production wrap at **07:28–07:42**; GenAI application work at **08:31–09:04**. |
| *The Only 7 Books You Need to Become an AI Engineer* | Applications-oriented AI Engineer identity at **00:52–01:12**. |
| Career-transition practitioner interview | Real projects and organisations **01:56–02:02**; networking/cold outreach **01:15–01:24**, **01:34–01:39**, and **02:03–02:11**; internal locus of control **03:03–03:24**; apply without checking every box **03:31–03:47**; one-to-two-year expectation **03:54–04:05**; sustainable **18/24/36-month** transition **04:52–04:59**; interviews/failure as data **04:59–05:08**; community accountability **06:04–06:32**. The video does **not** state “70%”; that threshold is clearly an editorial rule of thumb, not a direct quotation. |

## 3. Project and production enforcement

Every M1–M25 module now has a mandatory project or inherits an existing project list. The common definition of done requires:

- a runnable deliverable;
- automated critical-path and failure-case tests;
- a README covering setup, architecture, usage, and limitations;
- a short evidence-based results memo; and
- at least one production stretch such as Docker, CI, tracking, monitoring, or deployment.

M24 and the Production Toolchain now share a Minimum Production Bar: typed package code, pinned environments, lint/type/test gates, reproducible data/model/prompt versions, non-root containers, CI, deployment, secrets and rollback, tracked artifacts, architecture/system cards, structured telemetry, SLI/SLOs, drift/security checks, prompt-injection tests, ACLs, human escalation, budgets, sandboxing, and a kill switch.

M21 and M22 add evaluation pipelines and adversarial prompt-injection/tool-abuse scenarios. The zero-shot → RAG → fine-tuning gate selects the least complex intervention that satisfies knowledge freshness, behaviour, attribution, security, latency, cost, maintenance, and rollback constraints.

## 4. Career-market evidence

Twelve postings were live-checked on 2026-08-01. The sample is directional evidence, not a claim that one vacancy represents an entire profession.

| Family | Posting sample | HTTP | Repeated evidence |
|---|---|:---:|---|
| AI Engineer | Healx; Infinite PL; Kobie | 200 each | Python, foundation-model APIs, RAG, agents/tool use, evals, injection/PII defences, tracing, deployment. |
| ML Engineer | Bumble; Spear AI; PayU | 200 each | ML frameworks, end-to-end ownership, CI/CD, containers/cloud, serving, evaluation, observability. |
| Data Scientist / analytics | HighLevel; Foodsmart; Airalo | 200 each | SQL, experimentation/causal inference, Python/R, product/growth metrics, stakeholder decisions. |
| Data Engineer | RAVL; Breakwater Technology; SteerBridge | 200 each | Python/SQL, orchestration, distributed processing, warehouses/lakehouses, quality, governance, operations. |

An expired WHOOP posting and a rejected Luxury Presence posting were not used in the final sample. Airalo and SteerBridge were checked as live replacements.

The resulting Career Operations section treats applications as an observable feedback system: control weekly action, apply near a 70% evidence match, conduct targeted outreach, turn interviews into skill-gap data, solve real organisational problems, and use community accountability. It reconciles **9–12 months** for initial Python/portfolio readiness with **18–36 months** for a full transition; neither is stated as a guarantee.

## 5. Practitioner shelf evidence

All paid print/ebook recommendations are explicitly optional. Free courses, libraries, samples, and author material remain valid substitutes.

| Group | Edition / identifier checked | Availability result | Mapping |
|---|---|---|---|
| *Automate the Boring Stuff with Python* | 3rd ed. (2025), ISBN 978-1-7185-0340-3 | Publisher and free online edition PASS | M1; practitioner routes |
| *Software Engineering for Data Scientists* | O’Reilly 2024, ISBN 978-1-098-13620-8 | WARN: publisher blocks automated checks | M1, M7, M24 |
| Manga Guides | Statistics 978-1-59327-189-3; Linear Algebra 978-1-59327-413-9; Calculus 978-1-59327-194-7 | Publisher pages PASS | M5, M3, M2 |
| StatQuest illustrated guides | ML 979-8986924007; NN/AI 979-8303440616 | Store PASS | M9–M12, M15–M18 |
| *Build a Large Language Model (From Scratch)* | Manning 2024, ISBN 978-1-63343-716-6 | Publisher PASS | M16, M18 |
| *AI Engineering* | O’Reilly 2025, ISBN 978-1-098-16630-4 | WARN: publisher blocks automated checks | M18, M21–M24 |
| *Generative AI System Design Interview* | 2024, ISBN 978-1-73604-914-3 | Course/book page PASS | M21–M24, Career Operations |

The pre-existing academic shelf was preserved.

## 6. Framework snapshots

PyPI JSON was the source of truth on 2026-08-01:

| Package | Verified version | Endpoint |
|---|---:|---|
| Streamlit | **1.60.0** | `https://pypi.org/pypi/streamlit/json` |
| CrewAI | **1.15.5** | `https://pypi.org/pypi/crewai/json` |

Versions are snapshots, not permanent pins. The curriculum requires environment pinning inside projects and re-verification when a learner starts the relevant module.

## 7. Link, anchor, and architecture checks

### Active external links

Final active-curriculum scan on 2026-08-01:

```text
active_files=8 urls=311 statuses={'200': 299, '302': 1, '403': 11}
```

Result: **300 PASS, 11 WARN, 0 FAIL**. The WARN set consists of bot-gated publisher, university, or platform pages; no active 404/DNS failure remains.

The initial full-repository scan reported ten 404s and two DNS failures. Classification found that several were historical audit evidence intentionally documenting bad source claims, while active failures were repaired. Examples include migrated MIT OCW pages, Cambridge’s current Velleman page, a stable Princeton archive, a DOI for the experimentation book, DTU’s Matrix Cookbook record, an Internet Archive copy released by MacKay, and the NBER record for the Angrist–Krueger paper. The final all-Markdown scan found **334 HTTP 200, 1 HTTP 302, 16 HTTP 403, 1 HTTP 405, 4 historical 404, and 2 historical DNS failures** across 358 unique URLs; all six failures occur only in audit/spec evidence, not active curriculum content.

### Local links and stable anchors

Before creation of this file, the local checker reported one expected issue: the Refresh Log linked to this not-yet-created audit. The final check scanned **15 Markdown files** and reported **0 missing local files or anchors**.

The 27 visible roadmap entries and module numbering were preserved, including M0, M6½, M8a/M8b, and M21–M26. Required explicit anchors remain in place, including:

- `#module-6-half`
- `#module-21`
- `#module-22`
- `#module-24`

Coursepage links point back to these stable README anchors. The README remains authoritative; coursepages provide module-specific operational detail. This preserves the README↔coursepage/PDF architecture mapping rather than creating a second curriculum.

## 8. Deliberate non-changes

- Did not delete, weaken, or substitute the elite academic content in M0, M2, M3, M5, M9–M13, or M15.
- Did not renumber modules or normalise away M6½ and M8a/M8b.
- Did not claim the fast lane provides research-level mathematical mastery.
- Did not make optional paid books prerequisites.
- Did not recommend RAG, agents, or fine-tuning by default; each is gated by a simpler-first decision rule.
- Did not silently erase historical failed URLs from prior audits; they remain evidence of rejected source claims and are excluded from the active release gate.
- Did not treat an AI-generated implementation as evidence that a learner can independently reproduce, test, or debug it.

## 9. Six-category self-score

| Category | Score | Evidence |
|---|:---:|---|
| Academic integrity and preservation | **5/5** | Additive edits, explicit trade-offs, protected modules and numbering retained. |
| Practitioner route and Python pedagogy | **5/5** | Six-phase lane, four-phase M1 pacing, eight-route matrix, tutorial escape, disciplined AI use. |
| Project-based learning | **5/5** | M1–M25 coverage plus one reusable tests/README/memo/production completion bar. |
| Career relevance and evidence | **4.5/5** | Twelve live postings across four role families; posting volatility is acknowledged. |
| Production AI, security, and evaluation | **5/5** | Minimum Production Bar, intervention decision gate, evals, injection/tool controls, observability. |
| Verification and repository hygiene | **4.5/5** | Every introduced URL logged; active scan has zero failures; bot-gated warnings and historical failures are explicit. |

**Release threshold:** all six categories are at or above 4/5.

## 10. Next-pass recommendations

1. **Automate link classification in CI.** Scan active curriculum separately from historical audits, cache results, retry transient failures, and fail only on active 404/DNS errors.
2. **Add machine-checkable project manifests.** A small schema per module could record deliverable, tests, dataset/license, deployment, evals, and production stretch without bloating the prose.
3. **Refresh labour-market evidence quarterly.** Replace expired postings, retain anonymised requirement counts, and segment expectations by geography and seniority to reduce survivorship and senior-role bias.
