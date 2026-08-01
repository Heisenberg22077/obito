<div align="center">

# Data Science & AI Roadmap

### A rigorous, free-first path from foundations to production AI

[![Edition](https://img.shields.io/badge/2026.3-Practitioner's%20Pass-6f42c1)](#refresh-log)
[![Modules](https://img.shields.io/badge/modules-27-6f42c1)](#roadmap)
[![Level](https://img.shields.io/badge/level-beginner%20to%20advanced-0969da)](#who-this-is-for)
[![Resources](https://img.shields.io/badge/resources-free--first-1a7f37)](#how-to-use-this-roadmap)
[![License](https://img.shields.io/badge/license-CC%20BY--SA%204.0-lightgrey)](LICENSE.md)

**Mathematics · Statistics · Machine Learning · Data Engineering · Deep Learning · LLMs · Production AI**

[Start here](#start-here) · [Choose a track](#choose-your-track) · [Practitioner fast lane](#practitioner-track) · [Browse modules](#roadmap) · [Career operations](#career-operations) · [Books](#books) · [Toolchain](#toolchain) · [Progress tracker](#progress-tracker)

</div>

---

## Goal

This roadmap turns high-quality university syllabi and open learning resources into one prerequisite-aware curriculum. It is designed to help you:

- build strong mathematical, statistical, and programming foundations;
- learn classical machine learning before jumping to frontier models;
- ship real systems with data engineering, MLOps, RAG, agents, and evaluation;
- finish with a portfolio-ready research, systems, or applied capstone.

The curriculum is detailed by design, but the navigation is intentionally simple: **choose a track, follow the modules in order, and build as you learn.**

<a id="refresh-log"></a>
## Refresh log

### July 2026 — v2026.3 Practitioner's Pass

This pass adds a parallel 6–9 month practitioner on-ramp without removing the academic spine: intuition-first mathematics, a phase-based Python plan, mandatory shipped projects, an applications-focused AI Engineer identity, career operations grounded in 12 live job postings, a practitioner book shelf, and a minimum production bar. Source claims and new URLs are recorded in [`audit/AUDIT_v2026.3.md`](audit/AUDIT_v2026.3.md) and [`audit/VERIFICATION.md`](audit/VERIFICATION.md).

## Who this is for

- **Beginners** who want a complete path and are willing to fill prerequisite gaps.
- **Data analysts and data scientists** strengthening statistics, experimentation, and modelling.
- **ML and AI engineers** building production-grade model and LLM systems.
- **Experienced practitioners** using individual modules for focused study or interview review.
- **Research-oriented learners** preparing for graduate-level machine learning work.

> **Expected commitment:** roughly 24–36 months at 20–25 hours per week for the complete path. You do not need to complete every module for a role-focused track.

## How to use this roadmap

1. **Take the [math diagnostic](#math-diagnostic).** Complete Module 0 if any foundation is weak.
2. **Choose a destination** in the role-track table below instead of studying everything by default.
3. **Respect prerequisites.** Each module states what you should know before starting.
4. **Use one primary course and one primary book.** Treat the remaining links as alternatives or references.
5. **Build every mandatory project.** Passive course completion is not enough.
6. **Track your work** with the [progress checklist](#progress-tracker).
7. **Finish with a capstone** that matches your intended role.

<a id="start-here"></a>
## Start here

Use the shortest entry point that matches your current experience. You can return to the full curriculum whenever you need more depth.

| If you are... | Start with | Then continue to |
|---|---|---|
| **New to programming and data** | [Microsoft Data Science for Beginners](#companion-curricula), then [M1](#module-1) | [M5](#module-5) → [M6](#module-6) → [M7](#module-7) → [M8a](#module-8a) |
| **Comfortable with Python, new to ML** | [Microsoft ML for Beginners](#companion-curricula) alongside [M9](#module-9) | M9 → [M10](#module-10) → [M11](#module-11) → [M12](#module-12) |
| **An analyst moving into data science** | [M5](#module-5) → [M6](#module-6) → [M7](#module-7) | [M9](#module-9) → [M14](#module-14) → [M25](#module-25) |
| **An ML practitioner moving into production AI** | [M8b](#module-8b) and [M24](#module-24) | [M18](#module-18) → [M21](#module-21) → [M22](#module-22) → [M23](#module-23) |
| **Preparing for research** | [Math diagnostic](#math-diagnostic) | Follow M0–M18 in order, then [M23](#module-23) and the [research capstone](#module-26) |

> **First milestone:** complete one small project before collecting more resources. The Microsoft companion courses below supply guided lessons, quizzes, assignments, and solutions; this roadmap supplies the deeper prerequisite and production sequence.

## Choose your track

| Track | Recommended modules | Portfolio outcome |
|---|---|---|
| **Data Analyst** | M1 → M6 → M7 → M8a → M25 → M26 | Reproducible analysis, dashboard, and stakeholder memo |
| **Data Scientist** | M1–M7 → M9–M14 → M25 → M26 | Validated model plus causal or experimental evaluation |
| **Data Engineer** | M1 → M4 → M7 → M8a → M8b → M24 → M26 | Tested batch/streaming data platform with observability |
| **ML Engineer** | M1–M12 → M15–M17 → M24 → M26 | Model served behind an API with CI, monitoring, and SLOs |
| **AI Engineer (model/research depth)** | M1 → M8a → M15–M18 → M21–M24 → M26 | Evaluated RAG or agent system plus model-training depth, tracing, and guardrails |
| **AI Engineer (Applications)** | M1 → M7 → M8a → intuition passes in M2/M3/M5 → M18 → M21–M24 → M26 | Production application on GPT/Claude/Llama-class foundation models: prompting, RAG, agents, evals, and secure deployment. Primary text: [Chip Huyen, *AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) ⚠️ publisher bot-gated; ISBN 978-1-098-16630-4 |
| **Research / PhD prep** | M0–M18 → M23 → M26 Research Track | Reproducible paper, ablations, and public research artifact |

<a id="practitioner-track"></a>
## 🚀 Practitioner Track (Fast Lane)

**Target:** 6–9 months at 12–18 focused hours/week. This is a shipping-first route to junior applied ML/AI work, not a compressed research degree. It follows the practical sequence described in [“How to Become an ML Engineer”](https://www.youtube.com/watch?v=UZ_rK9gzVSc) (math intuition at 01:13–02:16; from-scratch NumPy at 05:01–05:20; production wrap at 07:28–07:42; GenAI at 08:31–09:04) and the applications-focused role definition in [“The Only 7 Books You Need to Become an AI Engineer”](https://www.youtube.com/watch?v=Pr9oRVtAqCM) (00:52–01:12).

| Phase | Approx. time | Sequence and exit evidence |
|---|---:|---|
| **1. Python that works** | 6–8 weeks | Complete the M1 phases below: [Scrimba Learn Python](https://scrimba.com/learn-python-c03) for an interactive start, *Automate the Boring Stuff* for useful scripts, then CS50P or Helsinki for depth. Ship a tested file-I/O CLI and API app. |
| **2. Math intuition first** | 3–5 weeks | Use the ⚡ alternatives in M0/M2/M3/M5: 3Blue1Brown, StatQuest, and the Manga Guides. Explain gradients, vectors/eigenvectors, distributions, and Bayes in plain language; compute toy examples. Defer proofs—do not pretend you completed them. |
| **3. Classical ML overview** | 5–7 weeks | Work at scikit-learn level through M9–M12: baselines, leakage-safe pipelines, cross-validation, regression/classification/clustering/trees, calibration, and error analysis. Ship one churn-prediction dashboard with a decision memo. |
| **4. Mechanical understanding** | 3–4 weeks | Implement **logistic regression**, **K-Means**, and a **decision tree** from scratch with NumPy. Use the `__init__` → internal helpers (for logistic regression, `sigmoid`) → `fit` → `predict` class pattern; test against scikit-learn on fixed toy data. |
| **5. AI Engineer stack** | 6–9 weeks | M18 → M21 → M22 → M23: prompting, the zero-shot/RAG/fine-tuning decision, retrieval, agents/tool use, eval pipelines, and prompt-injection defenses. Ship a cited RAG assistant over your own notes. |
| **6. Production wrap** | 4–6 weeks | M24: move out of a loose notebook into typed Python, pytest, Docker, CI/CD, MLflow or W&B tracking, monitoring, and one deployment target (AWS is one option, not a requirement). Publish architecture, evals, cost/latency, and failure analysis. |

> **Trade-off:** this route buys fast feedback and portfolio evidence by postponing proof literacy, measure theory, abstract linear algebra, and derivation-heavy deep learning. Return to full M0/M2/M3/M5 before research work, before claiming mathematical mastery, or when M13+ derivations become opaque. The academic route remains the stronger preparation for research and theory-heavy roles.

> **Operating rule:** implement first, then use libraries; deploy before polishing. AI assistants may tutor, explain errors, and review your work, but must not perform the cognitive step you are trying to learn. Otherwise you create the **fluency illusion**: generated code feels familiar even though you cannot reproduce or debug it.

## Roadmap

### Foundations

- [🚀 Practitioner Track (Fast Lane)](#practitioner-track)
- [Math diagnostic and remediation](#math-diagnostic)
- [M0 — Mathematical maturity: pre-calculus, logic, and proof](#module-0)
- [M1 — Programming foundations and computational thinking](#module-1)
- [M2 — Calculus, matrix calculus, and convex optimisation](#module-2)
- [M3 — Linear algebra](#module-3)
- [M4 — Discrete mathematics, algorithms, and data structures](#module-4)
- [M5 — Probability theory](#module-5)

### Statistics and data systems

- [M6 — Statistical inference](#module-6)
- [M6½ — Causal inference and experimentation](#module-6-half)
- [M7 — Data wrangling, EDA, and visualisation](#module-7)
- [M8a — Databases, SQL, and warehouses](#module-8a)
- [M8b — Distributed data and streaming systems](#module-8b)

### Classical machine learning

- [M9 — Regression](#module-9)
- [M10 — Classification and kernel methods](#module-10)
- [M11 — Unsupervised learning and dimensionality reduction](#module-11)
- [M12 — Trees, ensembles, and boosting](#module-12)

### Probabilistic and deep learning

- [M13 — Bayesian inference, graphical models, and MCMC](#module-13)
- [M14 — Sequence modelling and time series](#module-14)
- [M15 — Deep learning foundations](#module-15)
- [M16 — Representation learning, transformers, and generative models](#module-16)
- [M17 — Reinforcement learning and decision-making](#module-17)

### Frontier and production AI

- [M18 — Large language models, RLHF, and alignment](#module-18)
- [M21 — RAG, vector databases, and retrieval](#module-21)
- [M22 — Agentic AI, MCP, and A2A](#module-22)
- [M23 — AI safety, interpretability, evaluations, and policy](#module-23)
- [M24 — MLOps, LLMOps, and AgentOps](#module-24)
- [M25 — Product data science and communication](#module-25)
- [M26 — Capstone: research, systems, or applied](#module-26)

### Reference sections

- [Career Operations](#career-operations)
- [Practitioner Shelf](#practitioner-shelf)
- [Core textbook list](#books)
- [Production toolchain](#toolchain)
- [Progress tracker](#progress-tracker)
- [Acknowledgements and sources](#acknowledgements)
- [Verification and audit trail](audit/FINAL_AUDIT.md)

## Curriculum at a glance

| Stage | Modules | Main outcome |
|---|---|---|
| **Foundations** | M0–M5 | Proof literacy, Python, calculus, linear algebra, algorithms, probability |
| **Statistics & data** | M6–M8b | Inference, experimentation, EDA, SQL, warehouses, distributed systems |
| **Classical ML** | M9–M12 | Regression, classification, unsupervised learning, ensembles |
| **Probabilistic & deep learning** | M13–M17 | Bayesian modelling, time series, neural networks, transformers, RL |
| **Frontier & production** | M18, M21–M25 | LLMs, RAG, agents, safety, evaluation, MLOps, product thinking |
| **Capstone** | M26 | A public, reproducible portfolio project |

<a id="companion-curricula"></a>
## Guided companion curricula

The two Microsoft curricula below are strong, actively maintained beginner companions. They use the lesson-table navigation, short projects, quizzes, assignments, and solution folders that make a large subject easier to enter. Use their repository root links to follow the newest default-branch content; the reviewed commits provide a dated audit trail.

| Curriculum | Best for | Current scope | Reviewed upstream snapshot |
|---|---|---|---|
| [Microsoft Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) | A gentle, project-based introduction before the statistics and data modules | 10 weeks · 20 lessons · data ethics, SQL/NoSQL, Python, preparation, visualisation, lifecycle, cloud, and communication | [`4d2ac42`](https://github.com/microsoft/Data-Science-For-Beginners/commit/4d2ac427ad6f022e73a75c4f46a28bbb7978ec3f), reviewed 2026-07-24 |
| [Microsoft ML for Beginners](https://github.com/microsoft/ML-For-Beginners) | Hands-on classical ML practice alongside M9–M14 and M17 | 12 weeks · 26 lessons · regression, classification, clustering, NLP, time series, reinforcement learning, and responsible ML | [`d0d0ea2`](https://github.com/microsoft/ML-For-Beginners/commit/d0d0ea2b2d22cddca31f9c6d108df7daa87a1b46), reviewed 2026-07-24 |

### Where the Microsoft lessons fit

| This roadmap | Guided lesson groups | How to use them |
|---|---|---|
| [M1 Programming](#module-1), [M5 Probability](#module-5), [M6 Statistics](#module-6) | [Defining data science and introductory statistics](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction) | Use as an accessible first pass; keep this roadmap's exercises for mathematical depth. |
| [M7 Wrangling, EDA, and visualisation](#module-7) | [Working with data](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) and [data visualisation](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/3-Data-Visualization) | Complete the guided notebooks, then rebuild one analysis with validation and a reproducible pipeline. |
| [M8a Databases and SQL](#module-8a) | [Relational and NoSQL lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/2-Working-With-Data) | Use lessons 5–6 for practice before advanced SQL, query plans, warehousing, and dbt. |
| [M9 Regression](#module-9) | [Regression lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/2-Regression) and [model web app](https://github.com/microsoft/ML-For-Beginners/tree/main/3-Web-App) | Pair the projects with this roadmap's derivations, diagnostics, regularisation, and cross-validation. |
| [M10 Classification](#module-10) | [Classification lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/4-Classification) | Practise model comparison, then add calibration, leakage checks, and error analysis. |
| [M11 Unsupervised learning](#module-11) | [Clustering lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/5-Clustering) | Use for a visual K-means project before PCA, mixture models, and manifold learning. |
| [M14 Time series](#module-14) | [Time-series lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/7-TimeSeries) | Start with ARIMA and SVR, then continue to probabilistic forecasting and foundation models. |
| [M16 Representation learning](#module-16) | [Introductory NLP lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP) | Treat these as classical NLP prerequisites before transformers and generative models. |
| [M17 Reinforcement learning](#module-17) | [Reinforcement-learning lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/8-Reinforcement) | Use the Q-learning projects as the practical on-ramp to modern deep and offline RL. |
| [M23 Safety](#module-23), [M24 Operations](#module-24), [M25 Product DS](#module-25) | [ML in the wild](https://github.com/microsoft/ML-For-Beginners/tree/main/9-Real-World), [data-science lifecycle](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/4-Data-Science-Lifecycle), and [cloud lessons](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/5-Data-Science-In-Cloud) | Use for case studies; follow this roadmap for current evaluation, governance, MLOps, and communication depth. |

> **Selection rule:** use the Microsoft courses when you want a guided beginner lesson or a small practice project. Use the primary university courses and books in each module when you need formal depth. The companion courses supplement this roadmap; they do not replace its mathematics, deep learning, data engineering, or production-AI modules.

### Suggested study rhythm

For each module, use a simple four-step loop:

1. **Learn** — complete the primary course or lecture sequence.
2. **Read** — work through the listed primary text and exercises.
3. **Implement** — reproduce core algorithms without relying only on high-level APIs.
4. **Ship** — complete the module project with tests, documentation, and a short results memo.

> **Portfolio rule for every M1–M25 project:** publish a concrete, runnable deliverable. The definition of done is (1) automated tests for the critical path and at least one failure case, (2) a `README` with setup, architecture, usage, and limitations, and (3) a short results memo with evidence, errors, and next steps. Add at least one production stretch—Docker, CI, experiment tracking, monitoring, or deployment. **A messy project on the internet beats a perfect project on your laptop.** Existing multi-project lists below use this same completion bar.

> **Resource policy:** free and open resources are preferred. Some books are listed as optional references when no equivalent open source is as strong.

---

# 🟩 FOUNDATION STRATUM — Modules 0–5

> These six modules establish the non-negotiable mathematical and programming substrate. **A weakness in any one will cause silent failure later** — e.g., a shaky grasp of eigenvalues cripples PCA, a shaky grasp of chain rule cripples backprop, a shaky grasp of `∀ / ∃ / ⟹` cripples your ability to read a single PRML proof.

---

<a id="math-diagnostic"></a>
## 🩺 Math-Foundations Diagnostic & Remediation Map

> **Why this section exists:** Most self-learners fail at Modules 9–17 not because ML is hard, but because they skipped (or mis-sequenced) one of *six* prerequisite skills. Below is a **15-question, 60-minute diagnostic** plus a **remediation table** so you can fix the weakness *before* it metastasises.

### Step 1 — Take the 15-question self-diagnostic (free, 60 min)

Pick **one** of these freely-available diagnostic instruments — each maps cleanly to the 6 strands you must master:

| # | Strand | Diagnostic instrument | Pass bar | Remediation if you fail → |
|---|---|---|---|---|
| 1 | **Pre-calculus & algebra** | [MIT 18.01 practice exam (first 10 questions)](https://ocw.mit.edu/courses/18-01-single-variable-calculus-fall-2006/pages/exams/) | 8/10 | Module **0a** (Khan Academy Pre-Calc) |
| 2 | **Trigonometry & complex numbers** | [Paul's Online Trig diagnostic](https://tutorial.math.lamar.edu/) | 7/10 | Module **0a** (Khan Academy Trig + Euler's formula) |
| 3 | **Proof writing & logic** | [Velleman *How To Prove It* §1.5 exercises](https://www.cambridge.org/highereducation/books/how-to-prove-it/6D2965D625C6836CD4A785A2C843B3DA) | 4/5 | Module **0b** (Hammack *Book of Proof* + Velleman + Lean tutorial) |
| 4 | **Single-variable calculus** | [MIT 18.01SC Final Exam](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/pages/final-exam/) | 70 % | Module **2** (full) |
| 5 | **Linear algebra (computational)** | [MIT 18.06 Quiz 1](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/exams/) | 70 % | Module **3** (full) |
| 6 | **Probability sense** | [Harvard Stat 110 Practice Strategic Practice 1–3](https://stat110.hsites.harvard.edu/) | 70 % | Module **5** (full) |

### Step 2 — Use the remediation paths

* **Score < 50 %:** Do **Module 0** end-to-end (≈ 6–10 weeks at 10 hrs/week) before touching Module 2.
* **Score 50–70 %:** Spot-fix using the per-topic links inside Module 0a / 0b.
* **Score > 70 %:** Skip Module 0; you are ready for Module 1 + 2 in parallel.

### Step 3 — Adopt the **Math Maturity Operating Manual**

Independent of *which* topic, every elite programme (MIT, Cambridge, Harvard) implicitly assumes you have these **seven habits**:

1. **Quantifier discipline** — when you read "for every / there exists", you can write it as `∀ / ∃` and negate it correctly.
2. **Definition-unfolding** — given a theorem, you can rewrite each term to its primitive definition before reasoning.
3. **Counter-example reflex** — when you doubt a claim, you immediately try `n=0`, `n=1`, the empty set, the singleton, and the constant function.
4. **Proof-template recall** — induction, contradiction, contrapositive, direct, construction, pigeonhole — each as a *template* you can fill in.
5. **Notation hygiene** — distinguish `=` (equal), `:=` (defined-as), `≡` (congruent / identical), `≈` (approximately), `∼` (asymptotic), `∝` (proportional).
6. **Computational verification** — every symbolic claim you make is sanity-checked in **SymPy** (algebra) or **NumPy** (numerical) within 5 minutes.
7. **Lean / proof-assistant exposure** — *not required*, but doing one chapter of [Velleman's *How To Prove It With Lean*](https://djvelleman.github.io/HTPIwL/) **changes how you read every subsequent definition** for the rest of your career.

> **Cited source for habits 1–6:** Cambridge IB Discrete Mathematics + Harvard Math 22a "Reasoning, Proof, and Linear Algebra" course handbooks (2025–26).

---

<a id="module-0"></a>
## Module 0: Mathematical Maturity Bridge — Pre-Calculus, Logic & Proof

> **Status:** Optional **only** if you scored > 70 % on every diagnostic above. Otherwise: **mandatory**.

* **The Tutor's "Why":** No university teaches *the leap* from procedural high-school math to definition-driven university math — they assume you already made it. The result: 60 %+ of self-learners stall at Module 5 (probability proofs) or Module 9 (regression assumptions). Cambridge's IB CST course explicitly assumes "Mathematics for Natural Sciences" maturity; MIT 6.7960 assumes 18.05 + a proof course; Harvard CS 1810 assumes Math 22a (linear algebra **with proofs**). **This module IS that proof course, compressed and free.**

* **Strict Prerequisites:** Working knowledge of high-school algebra (solve linear and quadratic equations).

> **⚡ Intuition-First Alternative (Practitioner Track):** You may defer M0b while you build the first practitioner projects. Use the visuals-first approach of [3Blue1Brown](https://www.3blue1brown.com/), the plain-language style of [StatQuest](https://www.youtube.com/@statquest), and the relevant Manga Guide examples to learn what notation is saying before formal proof. **What you give up:** quantifier discipline, theorem reading, and the ability to verify claims rather than merely recognize them. **Come back:** before research work and before M13+ derivations. There is no honest “intuition-only” substitute for learning to write a proof.

### Sub-module 0a — Pre-Calculus & Trigonometry Refresher (≈ 2–4 weeks)

* **Exhaustive Topic List:**
  * **Numbers:** ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ; absolute value as distance; intervals; surds and rationalising.
  * **Algebra:** factorisation (difference of squares, sum/difference of cubes), polynomial long division, partial fractions, exponent and log laws, change-of-base formula, **completing the square** (the single most-cited identity in regression).
  * **Functions:** domain/range, composition, invertibility, even/odd, increasing/decreasing, piecewise, absolute value, floor/ceiling.
  * **Conic sections:** circle, ellipse, parabola, hyperbola — equations and parametrisations (you'll see them again in Gaussians and SVMs).
  * **Trigonometry:** unit circle, radian measure, six trig functions, identities (Pythagorean, sum/difference, double-angle, half-angle, product-to-sum), inverse trig, polar coordinates.
  * **Complex numbers:** Cartesian and polar form, **Euler's formula `eⁱᶿ = cos θ + i sin θ`** (the bridge to Fourier transforms in M3), De Moivre's theorem, roots of unity.
  * **Sequences & series:** arithmetic and geometric, sum formulas (you will re-derive these in MGFs in M5).
  * **Limits — informal:** ε-δ intuition, one-sided limits, infinite limits, limits at infinity.

* **2026 Resources:**
  * **Primary (free):** [Khan Academy Precalculus](https://www.khanacademy.org/math/precalculus) — 10 units, ≈ 40 hours, includes mastery quizzes.
  * **Alternative (free, MIT-quality):** [MIT 18.01SC Single Variable Calculus](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — a structured calculus review with videos, notes, exams, and solutions; pair it with Khan Precalculus above if algebra or trigonometry is weak.
  * **Reading:** Stewart *Calculus, Early Transcendentals* (9th ed.) — Appendix A (numbers), Appendix B (coordinate geometry), Appendix C (graphs), §1.1–§1.5 (functions and models).
  * **Computational verification:** every identity must be checked in **SymPy** within 1 line (e.g., `sympy.simplify(sin(x)**2 + cos(x)**2 - 1)`).

### Sub-module 0b — Logic, Proof & Mathematical Vernacular (≈ 4–6 weeks · CORE)

* **Exhaustive Topic List:**
  * **Propositional logic:** truth tables, conjunction `∧`, disjunction `∨`, negation `¬`, implication `⟹`, biconditional `⟺`, **converse / contrapositive / inverse** (and which are logically equivalent).
  * **Predicate logic:** universal `∀`, existential `∃`, **negating quantified statements** (`¬∀x P(x) ≡ ∃x ¬P(x)` — the single most error-prone identity in undergraduate maths).
  * **Sets:** ∅, ∈, ⊆, ⊊, ∪, ∩, complement, Cartesian product, power set, Russell's paradox (and why ZFC patches it).
  * **Functions formally:** as relations satisfying functional dependence; injection, surjection, bijection; image and pre-image; composition; inverse function theorem (statement only).
  * **Relations:** reflexive, symmetric, transitive, equivalence relations, partitions, partial and total orders.
  * **Cardinality:** finite, countably infinite (ℕ ∼ ℤ ∼ ℚ), uncountable (ℝ via Cantor's diagonal); pigeonhole as a corollary.
  * **Proof techniques (with at least 3 worked examples each):**
    1. **Direct proof** — e.g., sum of two evens is even.
    2. **Proof by contradiction** — e.g., √2 is irrational; there are infinitely many primes.
    3. **Proof by contrapositive** — e.g., if `n²` is even then `n` is even.
    4. **Proof by mathematical induction** (weak and strong) — e.g., `Σk=1ⁿ k = n(n+1)/2`; well-ordering principle.
    5. **Proof by construction** — e.g., explicitly construct a bijection ℕ → ℤ.
    6. **Proof by cases** — e.g., triangle inequality.
    7. **Pigeonhole principle** — e.g., among any 13 people, two share a birth-month.
  * **Number theory primer:** divisibility, gcd, Euclidean algorithm (with extended version), Bezout's identity, modular arithmetic, Fermat's little theorem, Chinese Remainder Theorem (used in cryptography and hashing).
  * **Combinatorial identities:** Pascal's rule, hockey-stick identity, Vandermonde's identity (you will re-encounter all three in Stat 110 Lec 1–2).
  * **(Optional) Lean 4 first contact:** prove `∀ n : ℕ, n + 0 = n` interactively. *Not required for the curriculum but a 10× force-multiplier on every later module's confidence.*

* **2026 Resources:**
  * **Primary text (free, CC-BY):** [_Book of Proof_ (Hammack, **3rd Edition, 2018; revised 2025**)](https://richardhammack.github.io/BookOfProof/) — chapters 1–10. Open Textbook Initiative-approved; used at 50+ universities.
  * **Companion text:** [_How to Prove It: A Structured Approach_ (Velleman, **3rd Edition, Cambridge 2019**)](https://www.cambridge.org/highereducation/books/how-to-prove-it/6D2965D625C6836CD4A785A2C843B3DA) — chapters 1–6 + the new **[*How to Prove It With Lean* (Velleman, 2024)](https://djvelleman.github.io/HTPIwL/)** companion (free, browser-based).
  * **Discrete-math companion:** [_Mathematics for Computer Science_ (Lehman, Leighton, Meyer — MIT 6.042J, **2024 edition free PDF**)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/resources/mit6_042js15_textbook/) — chapters 1–5 (Proofs, Induction, Number Theory).
  * **Video course:** [Stanford CS103 Mathematical Foundations of Computing — full lecture notes](https://web.stanford.edu/class/cs103/) (publicly mirrored).
  * **Free online interactive course:** [_Introduction to Mathematical Thinking_ (Keith Devlin — Coursera, evergreen)](https://www.coursera.org/learn/mathematical-thinking) — Stanford-led, free audit.
  * **Practical implementation:** **SymPy 1.13+** for symbolic verification; **Lean 4 + Mathlib** (optional) — `lean4-web` runs in browser, no install needed.

* **Outcome:** When you finish Module 0b you can **read any theorem statement in Stat 110 / 18.06 / CS 1810 and re-state it formally before attempting the proof.** That single skill is the difference between a frustrated learner and an MIT-track one.

* **Suggested Pace:** 6 weeks at 10 hrs/week = 60 hrs total; or 12 weeks at 5 hrs/week. **Do not skip the exercises** — Hammack provides 600+ with hints, and *doing 200 of them* is the entire point of this module.

---

<a id="module-1"></a>
## Module 1: Programming Foundations & Computational Thinking

* **The Tutor's "Why":** All 2026 data-science work is Python-first (with selective Polars/R/Julia). You cannot derive a gradient if you cannot write a loop. This module is the gateway — master it, or every subsequent module becomes guesswork.

* **Strict Prerequisites:** High-school algebra. A working laptop with VS Code installed.

* **Official Pacing — four phases:**

  | Phase | Time | Skills and mandatory milestone |
  |---|---:|---|
  | **1. Foundations** | Weeks 1–4 | Types, control flow, functions, collections, strings, debugging → ship a number-guessing game **and** calculator. |
  | **2. Working Python** | Weeks 5–8 | Comprehensions, standard library, files, exceptions, packages, `uv` → ship a file-I/O CLI such as an expense tracker, notes manager, password generator, or downloads organiser. |
  | **3. Real-World Python** | Weeks 9–14 | HTTP/APIs, JSON, scraping, OOP, pytest, Git/GitHub → ship a weather CLI, Reddit scraper, Spotify analyser, or Discord bot that stores results. |
  | **4. Specialisation** | Months 4–6+ | Choose web/data/AI/automation; build **2–3 deployed portfolio projects**. Ladder options: Flask blog with auth → pretrained-HF sentiment analyser → stock dashboard → RAG chatbot over your own notes. |

  **Honest timing:** approximately 4–8 weeks for basics, 3–6 months for useful programs, and 9–12 months for entry-level job readiness when the learner also builds a portfolio. These estimates assume consistent part-time study; prior programming experience can shorten them.

* **Exhaustive Topic List:**
  * **[Harvard CS50P · Week 0]**: Functions, variables, types (int/float/str), `print`, formatted strings, conditionals, boolean expressions.
  * **[Harvard CS50P · Week 1]**: Conditionals, `match` statement, flow control, truthy/falsy semantics.
  * **[Harvard CS50P · Week 2]**: Loops (`for`, `while`), iterables, `break`/`continue`, `enumerate`, `zip`.
  * **[Harvard CS50P · Week 3]**: Exceptions, `try/except/else/finally`, raising custom exceptions, `assert`.
  * **[Harvard CS50P · Week 4]**: Libraries, `import`, `pip`, standard library tour (`random`, `statistics`, `sys`, `pathlib`).
  * **[Harvard CS50P · Week 5]**: Unit testing, `pytest`, test-driven development, fixtures, parametrise.
  * **[Harvard CS50P · Week 6]**: File I/O, CSV, JSON, binary files, context managers (`with`), PIL/Pillow basics.
  * **[Harvard CS50P · Week 7]**: Regular expressions, `re.search/match/sub/findall`, character classes, anchors, lookaheads.
  * **[Harvard CS50P · Week 8]**: Object-Oriented Programming: classes, `__init__`, attributes, methods, `@classmethod`, `@staticmethod`, `@property`, inheritance, `super()`, dunder methods (`__str__`, `__repr__`, `__eq__`).
  * **[Harvard CS50P · Week 9]**: `et cetera` — set/dict comprehensions, generators (`yield`), decorators, `*args`/`**kwargs`, type hints (`typing` module, 2026 `|` syntax).
  * **[IITM BSCS1001 — Computational Thinking]**: Algorithmic decomposition, state machines, invariants, correctness proofs (loop invariants), complexity intuition (counting ops).
  * **[IITM BSCS1002 — Programming in Python]**: Python interpreter model, memory model (reference semantics), mutability vs immutability, scope (LEGB), closures, iterators vs generators vs async generators.
  * **[MIT 6.0001 (archived edX)]**: Branching, iteration, string manipulation, recursion (factorial, Fibonacci, Towers of Hanoi), debugging methodology, efficiency (big-O informal intro), tuples, lists, aliasing, cloning, mutating, dictionaries.
  * **[MIT 6.0002]**: Optimisation problems, knapsack, graph-theoretic models, dynamic programming motivation, random walks, Monte Carlo simulation, sampling + confidence, experimental data curve-fitting, statistical myths.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS50P](https://cs50.harvard.edu/python/) · [MIT 6.0001 on OCW](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)
  * **Research sources:** [Scrimba — *Best Free Python Courses for Beginners in 2026*](https://scrimba.com/articles/best-free-python-courses-for-beginners-in-2026/) · [Scrimba — *How to Learn Python: A Beginner's Guide (2026)*](https://scrimba.com/articles/how-to-learn-python-a-beginners-guide-2026/)
  * **Required Reading (Latest 2026 Editions):**
    * _Fluent Python_ (**3rd Edition, 2025**) — Luciano Ramalho — chapters 1–6, 9 (closures/decorators), 17 (iterators).
    * _Python Crash Course_ (**4th Edition, 2025**) — Eric Matthes — for absolute beginners only.
  * **Practical Implementation:** **Python 3.12+** (pattern matching, improved error messages, per-interpreter GIL awareness). IDE: **VS Code** with `ms-python.python`, `charliermarsh.ruff`, `ms-python.mypy-type-checker`. Dependency manager: **`uv`** (2024-released, now standard).

* **🛠 Modern Python Tooling:**
  * **Type hints + mypy/pyright + Pydantic v2** — every production ML codebase uses typed Python. Learn: `TypedDict`, `Protocol`, `Generic`, `Annotated`, `TYPE_CHECKING`; [Pydantic v2 docs](https://docs.pydantic.dev/) ✅ for data-validation and settings management.
  * **[`uv` — Astral's ultra-fast package manager (0.11.7, Apr 2026)](https://docs.astral.sh/uv/)** ✅ — replaces `pip`/`pip-tools`/`virtualenv`/`pipx`/`poetry`. Learn `uv init`, `uv add`, `uv run`, `uv lock`, `uv tool install`.
  * **`async`/`asyncio` + `anyio`** — required for serving LLM APIs (M24), streaming pipelines (M8b), and batching tokeniser calls. Read [Python docs asyncio](https://docs.python.org/3/library/asyncio.html) ✅ + *Fluent Python* ch 19–21.
  * **Git + GitHub Actions CI** — pre-commit hooks, branch-protection, conventional commits, GitHub Actions workflows for test/lint/build.
  * **`pytest` + `hypothesis` (property-based testing)** — [hypothesis docs](https://hypothesis.readthedocs.io/) ✅. Every ML engineer at FAANG writes property-based tests for numerical code; learn the `@given` decorator and shrinking.
  * **`ruff` + `pyright`** for lint + typecheck; **`pre-commit`** to run them on every commit.

* **Free Python Course Matrix:**

  | Resource | Time | Format | Certificate | Project practice | Best for |
  |---|---:|---|---|---|---|
  | [Scrimba Learn Python](https://scrimba.com/learn-python-c03) | 5.6 h | Interactive scrims, 58 parts | Free completion certificate | Built throughout | First-week active practice |
  | [Harvard CS50P](https://cs50.harvard.edu/python/) | ≈100 h / 10 weeks | Lectures + problem sets | Free audit; paid verified edX certificate | 9 problem sets + final | Academic depth and problem solving |
  | [Helsinki Python MOOC 2026](https://programming-26.mooc.fi/) | 200+ h / 14 parts | Text + auto-graded exercises | Exam/ECTS route subject to course rules | Hundreds of exercises | Maximum exercise volume |
  | [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) | ≈300 h estimate | Text + projects | Free | 5 required projects | Project certificate; **legacy track is no longer actively updated**—check the [current Python certifications](https://www.freecodecamp.org/news/python-curriculum-is-live/) |
  | [Python for Everybody](https://www.coursera.org/specializations/python) | ≈32 h audit estimate | Video + reading | No certificate in audit mode | Graded work is paid | Gentle university-style sequence |
  | [Official Python Tutorial](https://docs.python.org/3/tutorial/) | Self-paced | Canonical reference | No | None | Accurate companion/reference, not hand-holding |
  | [Google's Python Class](https://developers.google.com/edu/python) | ≈10 h | Text + videos + exercises | No | Exercises | Existing programmers moving quickly |
  | [*Automate the Boring Stuff*](https://automatetheboringstuff.com/) | Self-paced | Free online book | No | Automation scripts | Immediate, useful wins |

  **Recommended pairing:** Scrimba → *Automate the Boring Stuff* → CS50P **or** Helsinki. Red flags when evaluating alternatives: Python 2 as the primary language, no projects, or no OOP coverage.

> **📚 How to actually study this module — tutorial-hell escape protocol:** Build before you feel ready. After each lesson, close it and rebuild the idea from a blank file. Budget **two hours building for each hour watching**. Clone a small open-source Python project; run it, read it, break it, and fix it. Use a study cohort, code review partner, local meetup, or learning community for weekly accountability. Difficulty is not a sign to collect another tutorial; it is the practice.

> **AI-use policy — avoid the fluency illusion:** In Phases 1–2, type the code yourself. Cursor, Claude, Copilot, and ChatGPT may explain an error, ask you guiding questions, generate extra exercises, or review code **after your attempt**. They may not author the solution you are learning to produce. Before accepting AI help, write your hypothesis; afterward, close the answer and reproduce the fix from memory.

* **📦 Module Project (mandatory) — API-powered weather CLI:** Build a CLI with typed functions, error handling, caching, and tests around mocked HTTP responses. **Definition of done:** public repo; `README` with setup and example output; pytest suite including failure paths; short results/lessons memo; tagged release. **Stretch:** Dockerfile + GitHub Actions test workflow. Ship before polishing—a messy project on the internet beats a perfect project on your laptop.

---

<a id="module-2"></a>
## Module 2: Single-Variable & Multivariable Calculus + Matrix Calculus & Convex Optimisation

* **The Tutor's "Why":** Gradients, backpropagation, maximum-likelihood estimation, and Bayes-rule derivations all live or die on calculus. You will not understand *why* SGD converges without it. Harvard's CS 1810 (2026) explicitly requires AM 22a (calc + lin alg). **Crucially, every modern paper denotes gradients in *matrix-calculus* notation (Jacobians, Hessians, vector-by-matrix derivatives) — and 90 % of self-learners have never seen this formalism.** This module fixes that gap.

* **Strict Prerequisites:** Module 0 (proof literacy) + Module 1 (so you can verify integrals with SymPy).

> **⚡ Intuition-First Alternative (Practitioner Track):** Start with [3Blue1Brown's *Essence of Calculus*](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr), calculus explanations from [StatQuest](https://www.youtube.com/@statquest), and [*The Manga Guide to Calculus*](https://nostarch.com/releases/manga_calculus.html) (optional paid book). Practise derivatives, gradients, and convex-loss sketches on toy functions; use autodiff to check them. **What you give up:** ε–δ proof literacy, convergence arguments, full matrix-calculus derivations, and KKT depth. **Come back:** before research, optimisation-heavy interviews, or when M13+/M15 derivations stop being intelligible.

* **Exhaustive Topic List:**
  * **[MIT 18.01.1x · Differentiation]**: Limits and continuity (ε-δ definition), derivative as a limit, power/product/quotient/chain rules, trig derivatives, exponential and log derivatives, implicit differentiation, linear/quadratic approximations, related rates, Mean Value Theorem, L'Hôpital's rule, optimisation (first/second derivative tests), Newton's method.
  * **[MIT 18.01.2x · Integration]**: Antiderivatives, Fundamental Theorem of Calculus (both parts + proofs), u-substitution, integration by parts, trigonometric integrals, partial fractions, improper integrals, Riemann sums, numerical integration (trapezoidal, Simpson's rule), applications (areas, volumes of revolution, arc length, surface area, centre of mass, work).
  * **[MIT 18.01.3x · Coordinate Systems & Infinite Series]**: Polar coordinates, parametric curves, conic sections, sequences, series convergence tests (ratio, root, integral, comparison, alternating series), power series, Taylor & Maclaurin series (**with remainder bounds — used in Newton's-method convergence and stochastic-gradient analysis**), complex numbers, Euler's formula.
  * **[MIT 18.02 · Multivariable Calculus]**: Vectors in ℝⁿ, dot and cross products, lines and planes, vector-valued functions, partial derivatives, tangent planes, total differential, **gradient vector & directional derivatives** (the foundation of gradient descent), chain rule (multivariable), **Hessian matrix** (used in Newton's method and second-order optimisers), Lagrange multipliers (→ SVM dual), double/triple integrals, change of variables, Jacobian determinant, vector fields, line integrals, Green's theorem, Stokes' theorem, divergence theorem.
  * **[IITM BSMA1001 — Math for DS I]**: Function basics, domain/range, piecewise functions, composition, inverse functions; limits; differentiation applied to business problems; definite vs indefinite integration; matrix-vector product as linear combination (preview of M3).
  * **[IITM BSMA1003 — Math for DS II]**: Vector calculus for optimisation, constrained optimisation, Lagrange multipliers with KKT conditions, convex functions, Jensen's inequality, convex optimisation preview.
  * **[Cambridge Data Science — Wischik]**: Calculus of variations (used in variational inference, M13).
  * **[MIT 18.063 / 18.S096 · Matrix Calculus for Machine Learning, IAP 2023 + Jan 2026 — Edelman & Johnson]**: **Differentials in the language of linear maps** (the *correct* modern view that subsumes both numerator-layout and denominator-layout conventions); derivatives of vector-valued functions of vectors (Jacobians); derivatives of scalar-valued functions of matrices (gradients); derivatives of matrix-valued functions of matrices (4-tensors / Kronecker products); chain rule as composition of linear maps; **forward-mode and reverse-mode automatic differentiation** (the operational foundation of every DL framework); cost analysis of forward-vs-reverse AD (matrix-multiplication-cost argument); derivatives through SVD, eigendecomposition, matrix inverse, determinant, log-determinant, trace, Frobenius norm; **adjoint method** for differentiating through ODE/PDE solutions (used in Neural ODEs and diffusion solvers, M16).
  * **[Stanford EE364A · Convex Optimization I — Boyd & Vandenberghe (Lectures 1–10) — *promoted from Module 9 to here as a foundation*]**: Convex sets (hyperplanes, half-spaces, polyhedra, balls, ellipsoids, norm cones, positive semi-definite cone), operations preserving convexity, convex functions (definition via secant inequality, first- and second-order conditions, Jensen's inequality), epigraph, sub-level sets, conjugate function, **convex optimisation problems** (LP, QP, QCQP, SOCP, SDP — and *which ML problems map to each*), Lagrangian duality, **KKT conditions** (the single most-cited result in classical ML), strong vs weak duality, complementary slackness, perturbation analysis. **Why here, not later:** every regression / SVM / logistic / GLM proof in Modules 9–14 *assumes* this material.
  * **[The Matrix Cookbook — Petersen & Pedersen, 2024 update]** + **[Parr & Howard "The Matrix Calculus You Need For Deep Learning" (arXiv:1802.01528, 2024 revision)]** as *daily-reference* lookup PDFs.

* **2026 Resources:**
  * **Primary Course Link:** [MITx 18.01.1x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.1x/) · [18.01.2x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.2x/) · [18.01.3x](https://mitxonline.mit.edu/courses/course-v1:MITxT+18.01.3x/) · [MIT OCW 18.02SC Multivariable](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)
  * **Matrix-Calculus track:** [MIT 18.S096 / 18.063 — Matrix Calculus for ML (IAP 2023 + Jan 2026)](https://github.com/mitmath/matrixcalc) — full lecture notes, video, problem sets *all open* on GitHub.
  * **Convex-Optimisation track:** [Stanford EE364A — Boyd, lectures + slides + book](https://web.stanford.edu/class/ee364a/) · [Free PDF of *Convex Optimization* (Boyd & Vandenberghe, Cambridge 2004, 6th printing 2023)](https://stanford.edu/~boyd/cvxbook/) · YouTube lecture series (re-recorded **Spring 2024**).
  * **Required Reading (Latest 2026 Editions):**
    * _Calculus: Early Transcendentals_ (**9th Edition, 2025 reprint**) — James Stewart — chapters 1–12.
    * **[Recommended freely-available alternative]** _Active Calculus_ (Boelkins et al., **2024 edition, free online**) — used at 80+ liberal-arts colleges.
    * **[Free, MIT-quality, 2024-revised]** Strang & Herman _Calculus, Vol 1–3_ (OpenStax, free PDF) — explicit OCW companion.
    * _Mathematics for Machine Learning_ — Deisenroth, Faisal, Ong (**book PDF last updated December 2025**) — Chapters 5 (Vector Calculus), 6 (Probability), **7 (Continuous Optimization)**. [mml-book.com](https://mml-book.com/) — **explicitly recommended by Harvard CS 1810 (2026)**.
    * ***The Matrix Cookbook*** — Petersen & Pedersen (2012 release) — [DTU publication page](https://www2.compute.dtu.dk/pubdb/pubs/3274-full.html) with the freely available manuscript.
    * **Parr & Howard** "The Matrix Calculus You Need For Deep Learning" — free on arXiv `1802.01528` (revised); also as an HTML web-book at [explained.ai/matrix-calculus](https://explained.ai/matrix-calculus/).
    * **Boyd & Vandenberghe** _Convex Optimization_ (Cambridge 2004; **6th printing 2023**, free PDF as above) — chapters 1–5 mandatory; 6–11 optional and revisited in M9–M11.
    * 3Blue1Brown: [_Essence of Calculus_ playlist (16 videos, ≈ 3 hrs)](https://www.youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) — required visual intuition.
    * **[Imperial College "Mathematics for Machine Learning" Coursera Specialization (Deisenroth, Cooper, Page — last refreshed Mar 2025)](https://www.coursera.org/specializations/mathematics-machine-learning)** — three courses: Linear Algebra · Multivariable Calculus · PCA. Free audit. *Pedagogically the gentlest on-ramp.*
  * **Practical Implementation:** **SymPy 1.13+** for symbolic verification; **JAX 0.7+** `jax.grad` / `jax.jacrev` / `jax.jacfwd` / `jax.hessian` for automatic differentiation — learn these NOW as you'll need them for all of M15+. **`cvxpy` 1.5+** for convex optimisation modelling (DCP), **`autograd`** as a teaching aid for hand-coding back-prop. Optionally explore **`Zygote.jl`** in Julia for source-to-source AD intuition.

* **Suggested Sequencing (16 weeks at 10 hrs/week):**
  1. Weeks 1–4: Single-variable calc (18.01.1x + 18.01.2x).
  2. Weeks 5–6: Series + Taylor (18.01.3x).
  3. Weeks 7–10: Multivariable (18.02 SC), with daily SymPy verification.
  4. Weeks 11–13: **Matrix calculus** (MIT 18.063 + Parr-Howard) — *the highest-leverage 3 weeks in the whole curriculum*.
  5. Weeks 14–16: **Convex optimisation** (EE364A Lectures 1–10) — write 5 small `cvxpy` programs (LP, LASSO, SVM, portfolio, max-likelihood logistic).

* **🧠 Automatic Differentiation Theory (2026.2 NEW sub-section):** Understanding AutoDiff is non-negotiable for M15+.
  * **Forward-mode (JVP — Jacobian-Vector Product):** Propagate dual numbers `(x, ẋ)` through the computational graph. Cost: O(n) extra for n inputs. Best when **inputs ≪ outputs** (rare in ML).
  * **Reverse-mode (VJP — Vector-Jacobian Product):** Forward pass builds a tape/graph; backward pass propagates cotangents. Cost: O(n) extra for n outputs. This is **backpropagation**. Best when **outputs ≪ inputs** (always true in ML: scalar loss, millions of parameters).
  * **Mixed-mode:** For Hessian-vector products (`Hv = ∇(∇L · v)`) used in second-order optimisers, Newton-CG, and natural gradient — apply forward-over-reverse or reverse-over-forward.
  * **Checkpointing:** Trade compute for memory by recomputing activations during backward pass (used in FSDP / gradient-checkpointing in M15).
  * **Practical:** `jax.grad`, `jax.jvp`, `jax.vjp`, `jax.jacrev`, `jax.jacfwd`, `jax.hessian`; `torch.autograd.grad`, `torch.func.vmap`, `torch.func.jacrev`; all cross-reference the [MIT 18.063 matrix-calc notes](https://github.com/mitmath/matrixcalc) already cited above.

* **📦 Module Project (mandatory) — constraint-based meal planner:** Express nutrition, budget, allergy, and preference constraints; solve them with `cvxpy`; explain feasibility and sensitivity. **Definition of done:** tested feasible and infeasible cases, reproducible environment, `README`, and results memo. **Production stretch:** containerise the solver and run tests in CI.

---

<a id="module-3"></a>
## Module 3: Linear Algebra — Computational, Geometric & Abstract

* **The Tutor's "Why":** *Every* modern ML algorithm — from linear regression to attention heads in GPT-class transformers — is a composition of matrix operations. Strang's 18.06 is the global gold standard for the *computational* view; Axler's *Linear Algebra Done Right* (**4th edition, 2024, freely available**) is the gold standard for the *abstract / proof-based* view that PRML, Bishop 2024, and Cambridge MLMI implicitly assume. **You need both.** Cambridge's MLMI Module 1 requires eigendecomposition mastery before week 3.

* **Strict Prerequisites:** Module 0b (proof literacy) + Module 2 (partial derivatives for matrix calculus).

> **⚡ Intuition-First Alternative (Practitioner Track):** Complete [3Blue1Brown's *Essence of Linear Algebra*](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab), selected [StatQuest](https://www.youtube.com/@statquest) PCA/linear-model explanations, and [*The Manga Guide to Linear Algebra*](https://nostarch.com/linearalgebra) (optional paid book), then manipulate small matrices in NumPy. **What you give up:** abstract vector-space and spectral-theorem proofs plus numerical-analysis depth. **Come back:** before research, M13+ derivations, or any work where conditioning and factorisation choices affect correctness.

* **🧭 Suggested Two-Pass Pedagogy:**
  * **Pass 1 — Computational (5 weeks):** Strang 18.06 + 3Blue1Brown — focus on *doing* row-reduction, computing eigenvalues, running SVD on toy matrices. Goal: numerical fluency.
  * **Pass 2 — Abstract (4 weeks):** Axler 4e (Chapters 1–7, skipping Chapter 8 if PhD-track is not the goal) — focus on *proving* spectral theorem, why SVD always exists, why orthogonal projection minimises distance. Goal: theoretical confidence.
  * **Pass 3 — Applications (3 weeks):** Strang's *Linear Algebra and Learning from Data* + Townsend's *Linear Algebra for Data Science* (Cambridge 2024) — focus on *the eight matrix factorisations of ML* (LU, QR, eigendecomposition, SVD, Cholesky, polar, NMF, randomised SVD).

* **Exhaustive Topic List:**
  * **[MIT 18.06 · Strang]**: Systems of linear equations, Gaussian elimination, LU factorisation, vector spaces, subspaces (column space, null space, row space, left null space — the "four fundamental subspaces"), rank-nullity theorem, linear independence, basis, dimension, orthogonality, Gram-Schmidt process, QR decomposition, projections, least squares (normal equations), determinants (cofactor expansion, properties), **eigenvalues and eigenvectors** (characteristic polynomial, diagonalisation), **Singular Value Decomposition (SVD)** (full and reduced forms, Eckart-Young theorem, pseudoinverse), positive-definite matrices (Cholesky), similar matrices, Jordan form, complex matrices (Hermitian, unitary), fast Fourier transform as a change of basis, linear transformations, applications to graphs (Laplacian), applications to differential equations (matrix exponential).
  * **[Axler — *Linear Algebra Done Right* 4e (2024) · *abstract pass*]**: Vector spaces *axiomatically* (no a-priori reference to ℝⁿ), subspaces, sums and direct sums, linear independence, basis, dimension; **linear maps as the central object** (kernel, image, the fundamental theorem of linear algebra); polynomials over ℂ (the algebraic backbone of eigentheory); eigenvalues, eigenvectors, **invariant subspaces, generalised eigenspaces**; **inner-product spaces** (axioms, Cauchy-Schwarz, triangle inequality, orthonormal bases via Gram-Schmidt, orthogonal complements, orthogonal projection as best approximation); **operators on inner-product spaces** (self-adjoint, normal, **the Spectral Theorem — proven without determinants**, polar decomposition, **SVD via the spectral theorem**); positive operators and isometries; trace and determinant *properly* defined (via characteristic polynomial coefficients, not as the Leibniz formula).
  * **[3Blue1Brown — Essence of Linear Algebra (16 videos, evergreen)]**: Geometric intuition for determinants as signed-volume scaling, eigenvectors as invariant directions, change of basis as relabelling, **dot product as the dual of a linear map** (the trick that makes attention "queries · keys" feel inevitable).
  * **[IITM BSMA1003]**: Matrix rank via row reduction, solvability of linear systems, null space / column space correspondence, linear maps, basis transformations, symmetric matrices and spectral theorem.
  * **[Harvard CS 1810 prereq (AM 22a / Math 21b)]**: Inner product spaces, orthogonal complement, projection matrices `P = A(AᵀA)⁻¹Aᵀ`, quadratic forms, positive semi-definiteness as condition for convex loss.
  * **[Cambridge Data Science — Wischik, Lec 2-3 "Feature Spaces"]**: Vector spaces as abstract objects, bases, inner products, orthonormal bases, projection onto subspace, **"model fitting as projection"** (critical insight for understanding linear regression), design of features, basis functions (polynomial, Fourier, radial).
  * **[Cambridge MLMI 1]**: Eigendecomposition as diagonalisation, SVD applications to dimensionality reduction and image compression.
  * **[Strang & Drineas/Mahoney — *Numerical Linear Algebra at scale*]**: Condition number κ(A) and numerical-stability intuition, **why floating-point matters** (catastrophic cancellation; why you never `(AᵀA)⁻¹Aᵀy` in practice — use `np.linalg.lstsq` or QR), **randomised SVD** (Halko-Martinsson-Tropp, 2011 — the algorithm Hugging Face uses for embedding compression), iterative methods (power iteration, Lanczos, Arnoldi → ARPACK), **Krylov subspaces** as preview of conjugate-gradient.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 18.06 OCW SC version (Strang, 2011) — evergreen](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/) · [3Blue1Brown EoLA](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
  * **Abstract / Proof Track:** [_Linear Algebra Done Right_ — Axler, **4th Edition, Springer 2024, FREE PDF + Kindle**](https://linear.axler.net/) — the cleanest abstract treatment ever written; 400 pp.; includes worked solutions.
  * **Applications-first Track:** [_Linear Algebra for Data Science, Machine Learning, and Signal Processing_ — Hero/Fessler/Townsend (Cambridge, 2024, hardback)](http://www.cambridge.org/highereducation/isbn/9781009418140) — explicitly cross-references PCA, SVD-of-images, low-rank approximation.
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Linear Algebra_ (**6th Edition, 2023**) — Gilbert Strang. Companion to 18.06.
    * _Linear Algebra and Learning from Data_ (**2019; 2025 reprint with errata**) — Strang — specifically written for ML era; covers randomised SVD, NMF, neural-net Jacobians.
    * ***Linear Algebra Done Right* (Axler, 4e, 2024)** — chapters 1–7 mandatory for proof maturity.
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapters 2, 3, 4.
    * **[*Numerical Linear Algebra* — Trefethen & Bau (SIAM, 1997, 25th-anniversary printing 2022)]** — for any student going into systems / scaling (M19).
  * **Free interactive notebooks:** [`fastai/numerical-linear-algebra` — Rachel Thomas USF (2019, still gold-standard, all-Jupyter)](https://github.com/fastai/numerical-linear-algebra) — covers SVD, randomised methods, PageRank, compressed sensing in 12 lectures.
  * **Practical Implementation:** **NumPy 2.x** (`np.linalg.eig`, `np.linalg.svd`, `np.linalg.solve`, `np.linalg.lstsq`). **SciPy 1.14+** for sparse linear algebra (`scipy.sparse.linalg`, ARPACK eigensolvers, `splu`). Use **`jax.numpy`** for GPU-accelerated linear algebra once comfortable. **`einops` 0.8+** to write tensor operations in *index notation* — once you internalise this, you can read every transformer paper without effort.

* **Mandatory mini-projects (do **all five**):**
  1. **PCA on MNIST from scratch** using only `np.linalg.svd` — recover 95 % variance in `k` components, plot `k`.
  2. **Image compression** via truncated SVD on a single greyscale photo — show MSE-vs-rank curve.
  3. **PageRank** as power iteration on the link-matrix — verify on a 5-node toy graph by hand.
  4. **Linear regression two ways** — `(AᵀA)⁻¹Aᵀy` *vs* `np.linalg.lstsq` *vs* QR *vs* SVD; compare numerical errors on Hilbert matrices (κ ≈ 10¹⁵).
  5. **Spectral clustering** on the two-moons dataset — Laplacian eigenmaps in 30 lines.

* **🔢 Numerical Linear Algebra (2026.2 NEW sub-section):** Production ML code that gets this wrong silently corrupts training.
  * **Factorisations used in ML:** LU (solving Ax=b), Cholesky (SPD systems, Gaussian MLE, KFAC), QR (least-squares, Gram-Schmidt, Arnoldi), **Householder reflections** (numerically stable QR — the *right* way), SVD (low-rank approx, pseudoinverse, PCA), **randomised SVD** (Halko-Martinsson-Tropp — standard for embedding compression at scale).
  * **Iterative solvers:** Conjugate Gradient (CG) for large sparse SPD systems, Lanczos/Arnoldi for dominant eigenvalues, GMRES for non-symmetric. These matter for Gaussian-Process inversion (M13), natural gradient (M17), and implicit differentiation through optimisation (M15).
  * **Condition number & stability:** Why `np.linalg.lstsq(A, b)` beats `np.linalg.inv(A.T @ A) @ A.T @ b` by 10+ orders of magnitude on ill-conditioned designs. Read *Trefethen & Bau* Lectures 12–16.
  * **Floating-point traps:** catastrophic cancellation, log-sum-exp trick, Kahan summation, mixed-precision (bf16/fp16/fp8) for DL.

---

<a id="module-4"></a>
## Module 4: Discrete Math, Algorithms & Data Structures

* **The Tutor's "Why":** Interviews for FAANG/quant/research roles test DSA rigorously; beyond that, you cannot design feature pipelines (hashing, bloom filters) or understand graph ML without it. **Cambridge ML & Bayesian Inference (2025-26) explicitly lists Discrete Mathematics as a prerequisite.**

* **Strict Prerequisites:** Module 1 (can write and debug Python).

* **Exhaustive Topic List:**
  * **[OSSU baseline / GaTech Algorithms I]**: ArrayList implementation, singly/doubly linked lists, stacks, queues, circular buffers, amortised analysis of dynamic arrays.
  * **[OSSU baseline / GaTech Algorithms II]**: Binary trees, BST operations (insert, delete, search, traversal — in/pre/post-order, level-order), heaps (min-heap, max-heap, heapsort, priority queue), skip lists, hashmaps (open addressing vs chaining, load factor, rehashing, perfect hashing).
  * **[GaTech Algorithms III]**: Self-balancing trees — AVL (rotations, balance factor), 2-4 trees, red-black trees, B-trees (used in databases — Module 8), divide-and-conquer (master theorem, merge sort, quicksort, strassen matrix multiplication).
  * **[GaTech Algorithms IV]**: Pattern matching (Boyer-Moore, KMP, Rabin-Karp), graph algorithms (BFS, DFS, topological sort), **Dijkstra's shortest path**, Bellman-Ford, **Minimum Spanning Tree (Prim's, Kruskal's)**, dynamic programming (LCS, edit distance, knapsack, matrix-chain multiplication), NP-completeness, approximation algorithms.
  * **[IITM BSCS2002 — PDSA in Python]**: Complexity analysis (O, Ω, Θ), master theorem proofs, graph representations (adjacency list/matrix), topological sort with DFS, DAG shortest paths, strongly connected components (Tarjan, Kosaraju).
  * **[Cambridge Discrete Math]**: Proof techniques (induction, contradiction, contrapositive), set theory, relations, equivalence classes, partial orders, functions (injection, surjection, bijection), counting (permutations, combinations, inclusion-exclusion, pigeonhole), recurrence relations, generating functions (preview of MGFs in M5), graph theory (Euler paths, Hamiltonian cycles, planarity, chromatic number), elementary number theory (gcd, Euclidean algorithm, modular arithmetic — used in cryptography and hashing).
  * **[Cambridge ML & Real-World Data · Topic 3]**: **Social networks analysis** — properties of networks (degree, diameter), betweenness centrality, clustering using betweenness centrality, detection of cliques in unstructured networks.
  * **[2026.2 addendum — Randomised & Streaming Algorithms]**: **Bloom filters** (false-positive rate calculus, counting bloom, cuckoo filter), **MinHash / locality-sensitive hashing (LSH)** (Jaccard similarity estimation for dedup and near-duplicate detection, used in LLM pre-training data pipelines), **HyperLogLog** (cardinality estimation), **Count-Min Sketch** (frequency estimation for streaming), **reservoir sampling** (uniform sampling from a stream of unknown length), **randomised quicksort**, **Karger's min-cut**. *All of these appear in modern data-engineering interviews (M8a/M8b).*
  * **[Amortised Analysis]**: Aggregate / accounting / potential methods applied to dynamic arrays, splay trees, union-find with path-compression — the mental model behind *"why Python `list.append` is O(1) amortised"*.
  * **[Approximation Algorithms]**: PTAS / FPTAS definitions, vertex-cover 2-approximation, set-cover greedy log-factor, k-means approximation, **primal-dual schema** — relevant for NP-hard pipeline-scheduling problems (M8b).

* **2026 Resources:**
  * **Primary Course Link:** [GaTech DSA I-IV on edX](https://www.edx.org/learn/data-structures/the-georgia-institute-of-technology-data-structures-algorithms-i-arraylists-linkedlists-stacks-and-queues) (Java) **OR** [MIT 6.006 Introduction to Algorithms OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (Python — **more aligned with 2026 workflow**).
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Algorithms_ (**4th Edition, 2022**) — Cormen, Leiserson, Rivest, Stein (CLRS) — the canonical reference.
    * _Algorithm Design Manual_ (**3rd Edition, 2020**) — Skiena — for problem-solving intuition.
    * _Concrete Mathematics_ (**2nd Edition**) — Graham, Knuth, Patashnik — for discrete-math depth.
  * **Practical Implementation:** Pure Python + `collections` (deque, defaultdict, Counter), **`sortedcontainers`**, **`networkx` 3.x** for graph algorithms, **LeetCode** + **Codeforces** for practice.

* **📦 Module Project (mandatory) — route-planner benchmark:** Implement BFS, Dijkstra, and A* over the same graph; document complexity and benchmark runtime/memory on reproducible inputs. **Definition of done:** correctness/property tests, `README`, and results memo. **Production stretch:** expose the planner through a containerised API with CI.

---

<a id="module-5"></a>
## Module 5: Probability Theory — The Language of Uncertainty

* **The Tutor's "Why":** Harvard's Joe Blitzstein (Stat 110) calls probability "the soul of statistics." In 2026, every ML model is a probability distribution — diffusion models are score-matched Gaussians; LLMs are autoregressive categoricals; Bayesian networks are joint PMFs. This is **the** pivotal module.

* **Strict Prerequisites:** Modules 2 and 3 (integration for continuous RVs; matrices for multivariate distributions).

> **⚡ Intuition-First Alternative (Practitioner Track):** Use [StatQuest](https://www.youtube.com/@statquest) for distributions, Bayes, likelihood, and uncertainty; pair it with [*The Manga Guide to Statistics*](https://nostarch.com/releases/manga_statistics.html) (optional paid book) and visual probability simulations in NumPy. 3Blue1Brown's visual style is useful for the linear-algebra/calculus dependencies. **What you give up:** measure-theoretic definitions, concentration proofs, and convergence arguments. **Come back:** before Bayesian research, theoretical ML, or M13+ derivations; simulation intuition does not license formal probability claims.

* **Exhaustive Topic List:** *(Blitzstein's 34-lecture Stat 110 is the spine; everything else confirms or extends it.)*
  * **[Harvard STAT 110 · Lec 1]**: Probability and Counting — sample spaces, events, naïve definition of probability, multiplication rule, permutations, combinations, binomial coefficient identities.
  * **[STAT 110 · Lec 2]**: Story proofs, axioms of probability (Kolmogorov), inclusion-exclusion.
  * **[STAT 110 · Lec 3]**: Birthday problem, properties of probability (monotonicity, Bonferroni).
  * **[STAT 110 · Lec 4-6]**: Conditional probability, Law of Total Probability, Bayes' Theorem, **Monty Hall**, **Simpson's Paradox**.
  * **[STAT 110 · Lec 7-8]**: Gambler's ruin, random variables, CDF, PMF.
  * **[STAT 110 · Lec 9-10]**: **Expectation** — linearity of expectation (with non-independent RVs!), indicator RVs, fundamental bridge.
  * **[STAT 110 · Lec 11]**: **Poisson distribution** — Poisson paradigm, Poisson approximation to binomial.
  * **[STAT 110 · Lec 12-13]**: Discrete vs continuous RVs, **Uniform**, **Normal** (standard and general), 68-95-99.7 rule, universality of the uniform.
  * **[STAT 110 · Lec 14]**: Location, scale, **LOTUS** (Law of the Unconscious Statistician).
  * **[STAT 110 · Lec 16]**: **Exponential distribution** — memorylessness, connection to Poisson process.
  * **[STAT 110 · Lec 17-18]**: **Moment Generating Functions (MGFs)** — uniqueness, computing moments, MGF of sums of independent RVs.
  * **[STAT 110 · Lec 19]**: **Joint, conditional, and marginal distributions**, independence, transformations.
  * **[STAT 110 · Lec 20]**: **Multinomial**, Cauchy (and why its mean doesn't exist).
  * **[STAT 110 · Lec 21]**: **Covariance and Correlation**, Cauchy-Schwarz.
  * **[STAT 110 · Lec 22]**: Transformations of random variables, **convolutions** (sum of RVs).
  * **[STAT 110 · Lec 23]**: **Beta distribution** — conjugate prior for binomial (preview of M13).
  * **[STAT 110 · Lec 24]**: **Gamma distribution**, Poisson process in detail, arrival times.
  * **[STAT 110 · Lec 25-27]**: **Order statistics**, **conditional expectation** as an RV, Adam's law (E[E[Y|X]] = E[Y]), Eve's law (law of total variance).
  * **[STAT 110 · Lec 28]**: **Inequalities** — Markov, Chebyshev, Cauchy-Schwarz, Jensen, Chernoff bounds.
  * **[STAT 110 · Lec 29]**: **Law of Large Numbers** (weak and strong), **Central Limit Theorem** (statement and MGF proof).
  * **[STAT 110 · Lec 30]**: **Chi-squared**, **Student-t**, **Multivariate Normal** (mean vector, covariance matrix, conditional MVN).
  * **[STAT 110 · Lec 31-33]**: **Markov chains** — transition matrix, stationary distribution, reversibility, convergence (detailed balance preview for MCMC).
  * **[STAT 110 · Lec 34]**: A look ahead — Brownian motion, martingales.
  * **[MIT 6.431x / MicroMasters C1]**: Complements Stat 110 with a more engineering-flavoured treatment — probability spaces, conditioning as information update, Bayesian vs frequentist views introduced, discrete/continuous RVs, multiple RVs, derived distributions, convergence in probability vs distribution vs almost sure, Bernoulli process, Poisson process, elementary queueing, hidden random processes.
  * **[IITM BSMA1002 · Week 1-12]**: Types of data and scales of measurement (nominal/ordinal/interval/ratio), descriptive vs inferential statistics; frequency distributions; measures of central tendency (mean/median/mode) with formal definitions; measures of dispersion (range, variance, standard deviation, IQR); five-number summary and boxplots; association (contingency tables, Pearson correlation, point-biserial correlation); counting principles (addition/multiplication rule, factorials); permutations and combinations; probability (events, axioms); conditional probability, multiplication rule, independence, law of total probability, Bayes' theorem; random variables (PMF, CDF); expectation and variance of discrete RVs; Bernoulli trials, binomial, Poisson; continuous RVs (uniform, exponential).
  * **[Cambridge Data Science — Wischik · "Handling probability models"]**: PDF and CDF manipulation, Bayes's rule, **Monte Carlo estimation** (first rigorous introduction), empirical distribution as a function.
  * **[Cambridge Data Science — Wischik · "Random processes"]**: Markov chains (discrete time), **stationarity and drift analysis**, processes with memory, learning a random process from data.

* **Critical Additions (April 2026):**
  * **Concentration inequalities for ML — beyond Chebyshev:** **Hoeffding's inequality** (the workhorse of generalisation bounds), **McDiarmid's bounded-differences inequality**, **Bernstein's inequality**, **sub-Gaussian** and **sub-exponential** random variables, ψ-Orlicz norms, **Bernstein-Chernoff bound for VC-dimension** (the 1971 Vapnik-Chervonenkis result that started statistical learning theory). Without these you cannot read a single PAC-learning theorem in M9.
  * **Information theory primer (the overlap with probability):** **entropy `H(X) = −Σ p log p`**, joint and conditional entropy, **mutual information `I(X;Y)`**, **KL divergence `D_KL(P‖Q)` and Jensen's inequality**, cross-entropy (the loss function of every classifier and every LM), **f-divergences** (TV, JS, Hellinger), **Fano's inequality** (lower bounds for classification error). Cited from MIT 6.7960 Wk 5–6 (Information Theory) and Cover & Thomas Ch 1–2.
  * **Measure-theoretic bridge — *taught minimally so you can read PML2 (Murphy 2023)*:** σ-algebras (Borel), measurable functions, Lebesgue integral *vs* Riemann (why we need it: integrating discontinuous limits), **Radon-Nikodym derivative `dν/dμ`** (the *correct* definition of "density"), almost-sure convergence vs convergence in probability vs in distribution vs in `L²` (the four convergence types every probabilist mixes up), pushforward measures, **dominated and monotone convergence theorems** (used implicitly every time you swap an integral and a limit in MCMC analysis). **Goal:** read Wasserman *All of Statistics* Ch 21 or Murphy PML2 Ch 1 without panic — *not* to do measure-theoretic exercises.
  * **Probability in code — *do these three concretely*:** (1) **inverse-CDF sampling** for any 1-D distribution, hand-coded; (2) **rejection sampling** + **importance sampling** with diagnostics (effective sample size); (3) **Monte-Carlo integration** of a 5-D integral with confidence-interval analysis.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard Stat 110 full playlist (Blitzstein, 34 lectures)](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo) · [Handouts & problems](https://stat110.hsites.harvard.edu/) (browser only — `curl` is bot-gated) · [MITx 6.431x](https://micromasters.mit.edu/ds/)
  * **Required Reading (Latest 2026 Editions):**
    * _Introduction to Probability_ (**2nd Edition, 2019; 2024 reprint**) — Joseph Blitzstein & Jessica Hwang — [free PDF](https://projects.iq.harvard.edu/stat110/home) — **chapters 1-12 cover-to-cover**. This is the primary text.
    * _Introduction to Probability_ (**2nd Edition, 2008**) — Bertsekas & Tsitsiklis — companion to 6.431x.
    * **[_Introduction to Probability for Data Science_ — Stanley H. Chan (Michigan Publishing, 2021/2023, FREE PDF + HTML)](https://probability4datascience.com/)** — *the* book that bridges Stat-110-style probability to Python/MATLAB code; hundreds of worked computational examples; **adopted by 30+ US engineering programmes** (incl. Purdue, Michigan).
    * _Mathematics for Machine Learning_ — Deisenroth et al. — Chapter 6.
    * **[_Information Theory, Inference, and Learning Algorithms_ — David MacKay (Cambridge 2003, **free PDF**)](https://archive.org/details/MackayInformationTheoryFreeEbookReleasedByAuthor)** — a singular masterpiece; chapters 1–6 give the cleanest entropy/MI exposition in any language.
    * **[_High-Dimensional Probability_ — Roman Vershynin (Cambridge 2018, **free draft online**)](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html)** — *the* reference for sub-Gaussian, concentration, and random matrices; chapters 1–3 sufficient for ML purposes.
    * **(Optional, PhD-track only)** _Probability with Martingales_ — David Williams (Cambridge 1991), or _Measure, Integral and Probability_ — Capinski & Kopp (Springer 2nd ed., 2014) — for the measure-theoretic complement after Stat 110.
  * **Practical Implementation:** **SciPy 1.14+** `scipy.stats` (every distribution you'll need); **NumPy** `np.random.Generator` (modern PCG64 / Philox RNG, **default since NumPy 1.17**); begin using **`distrax`** (JAX) or **`torch.distributions`** (PyTorch) for *differentiable* distributions — you'll need these in M13. **`tensorflow_probability` 0.24+** (JAX-substrate) for advanced bijectors (used in normalising flows, M16).

* **Suggested Pace (12 weeks at 10 hrs/week):**
  * Weeks 1–8: Stat 110 lectures 1–28 + Blitzstein-Hwang exercises 1–10 from each chapter.
  * Weeks 9–10: Concentration inequalities + information-theory primer (MacKay Ch 1–6 + Vershynin Ch 1–2).
  * Weeks 11–12: Stat 110 lectures 29–34 + measure-theoretic bridge (Wasserman Ch 21 *or* Capinski-Kopp Ch 1–4 if PhD-track).
  * **Capstone exercise:** write a 30-line script that empirically demonstrates the CLT, the Hoeffding bound, and the Galton-Watson process, all in one notebook. *If you can do this without help, you have actually learned probability.*

* **📦 Module Project (mandatory) — uncertainty simulator:** Build an interactive simulator for Bayes updates, the CLT, and concentration bounds; compare empirical coverage with theory. **Definition of done:** deterministic statistical tests, `README`, and results memo. **Production stretch:** deploy the app with monitoring for invalid inputs.

---

# 🟨 CORE STATISTICS STRATUM (Modules 6–8)

---

<a id="module-6"></a>
## Module 6: Statistical Inference

* **The Tutor's "Why":** This is where mathematics meets reality. Every p-value in a Nature paper, every A/B test at Meta, every FDA drug approval, hinges on the concepts in this module. Harvard STAT 111 and MIT 18.6501x are the twin pillars.

* **Strict Prerequisites:** Module 5 (must know MGFs, CLT, joint distributions).

* **Exhaustive Topic List:**
  * **[Harvard STAT 111 / MIT 18.6501x]**: Statistical models (parametric, non-parametric, semi-parametric); estimators and their properties — unbiasedness, consistency, efficiency, sufficiency (Neyman-Fisher factorisation), completeness, Rao-Blackwell theorem, Lehmann-Scheffé theorem; Cramér-Rao lower bound.
  * **[MIT 18.6501x]**: **Maximum Likelihood Estimation** — construction, invariance, asymptotic normality, Fisher information, observed vs expected information; **Method of Moments**; delta method.
  * **[MIT 18.6501x]**: **Parametric hypothesis testing** — null vs alternative, Type I / Type II errors, power, size, Neyman-Pearson lemma, Likelihood Ratio Test (Wilks' theorem), Wald test, score test.
  * **[MIT 18.6501x]**: Confidence intervals — construction by pivoting, Wald CIs, likelihood-based CIs, bootstrap CIs.
  * **[MIT 18.6501x]**: Goodness-of-fit tests — chi-squared test, Kolmogorov-Smirnov test, Anderson-Darling.
  * **[MIT 18.6501x]**: Linear regression inference — Gauss-Markov theorem proof, sampling distribution of β̂, ANOVA decomposition (SST = SSR + SSE), F-test for nested models.
  * **[Harvard CS109A · Lec 7 "Probability"]**: Review of Stat 110 concepts in regression context.
  * **[Harvard CS109A · Lec 8 "Inference in Regression and Hypothesis Testing"]**: t-tests for regression coefficients, confidence vs prediction intervals, multiple testing issues (Bonferroni, Holm, Benjamini-Hochberg FDR).
  * **[Harvard CS109A · Lec 21 "Experimental Design"]**: Randomisation, blocking, factorial designs, power analysis (a priori sample size computation), **causal inference preview** (ATE, ATT), Simpson's paradox revisited.
  * **[Cambridge Data Science · "Inference"]**: **Bayesianism** vs **frequentism** — epistemic vs aleatory uncertainty. Frequentist confidence intervals construction. Hypothesis testing as decision rule. **Bootstrap resampling** (non-parametric bootstrap, parametric bootstrap, block bootstrap for time series).
  * **[IITM BSMA1004 — Statistics for Data Science II]**: Sampling distributions (χ², t, F); estimation (point and interval); tests for one/two means/proportions/variances; paired t-test; McNemar's test; non-parametric tests (sign, Wilcoxon, Mann-Whitney, Kruskal-Wallis); contingency tables (χ² test of independence); ANOVA (one-way, two-way, with and without interaction); simple and multiple linear regression hypothesis testing.
  * **[Harvard CS 1810]**: Estimators — **Maximum a Posteriori (MAP)** as the Bayesian regularised counterpart to MLE.

* **2026 Resources:**
  * **Primary Course Link:** [MITx 18.6501x Fundamentals of Statistics](https://www.edx.org/course/fundamentals-of-statistics) · [Harvard STAT 111 course page](https://beta.my.harvard.edu/course/STAT110/2025-Fall/001)
  * **Required Reading (Latest 2026 Editions):**
    * _All of Statistics_ (**2nd printing, Springer 2004**, still canonical) — Larry Wasserman — chapters 6–15.
    * _Statistical Inference_ (**2nd Edition**) — Casella & Berger — the rigorous graduate-level reference.
    * _An Introduction to Statistical Learning with Python (ISLP)_ (**2023, 2025 reprint**) — James, Witten, Hastie, Tibshirani, Taylor — Chapters 2-3.
  * **Practical Implementation:** **`statsmodels` 0.14+** for classical inference (OLS, GLM, ANOVA), **`pingouin`** for modern stats API, **`scipy.stats`** for tests. Use **R 4.4+** with `{tidyverse}`, `{broom}`, `{infer}` for when you need publication-grade stats.

* **➡️ Cross-ref note (NEW v2026.2):** A/B testing, experimental design, and causal inference have been promoted out of this module into a **dedicated Module 6½ — Causal Inference & Experimentation** (directly below) because every senior-DS interview at Meta / Netflix / Booking / Uber tests this material in depth.

* **📦 Module Project (mandatory) — reproducible inference lab:** Analyse one public dataset with estimator diagnostics, confidence intervals, power analysis, multiple-testing control, and bootstrap checks. **Definition of done:** simulation/unit tests, `README`, and decision-focused results memo. **Production stretch:** schedule the analysis in CI and publish the report artifact.

---

<a id="module-6-half"></a>
## Module 6½: Causal Inference & Experimentation

* **The Tutor's "Why":** In 2026, this is the #1 differentiator between a *junior ML engineer* and a *senior data scientist*. Netflix, Meta, Uber, Booking, Airbnb, and every product-data-science org hires specifically for causal-inference fluency. Berkeley MIDS dedicates an entire course to it ([DATA 241 · Causal Inference](https://www.ischool.berkeley.edu/courses/datasci/241) ✅). MIT 14.387 *Mostly Harmless Big Data* covers the econometric half. **Correlation≠causation is not a slogan — it is a formal theorem (Pearl's do-calculus).** This module closes the single largest production-DS gap identified in the April 2026 benchmark PDF.

* **Strict Prerequisites:** Module 5 (joint distributions, conditional expectation), Module 6 (hypothesis testing, CIs, bootstrap).

* **Exhaustive Topic List:**
  * **A/B Testing Foundations:** Randomisation as the identification strategy, potential outcomes framework (Rubin/Neyman), ATE / ATT / CATE / LATE estimands, sample-size and MDE (minimum detectable effect) calculations, one-sided vs two-sided tests, Type I/II control, **sequential testing & always-valid p-values** (Howard et al. 2021), **group-sequential designs** with O'Brien-Fleming/Pocock boundaries, **CUPED variance reduction** (Deng et al. Microsoft 2013 — the single most impactful variance-reduction trick), stratified randomisation, cluster-randomised experiments.
  * **Interference & Network Effects:** **SUTVA violations**, switchback experiments (Uber/Lyft), **spillover** in social networks, ego-cluster randomisation, graph-cluster randomisation, synthetic control for marketplace platforms.
  * **Multiple Testing:** Bonferroni, Holm-Bonferroni, Hochberg, **Benjamini-Hochberg FDR control**, Storey's q-values, sequential multiple testing.
  * **Resampling-Based Inference:** Non-parametric bootstrap (Efron), parametric bootstrap, block bootstrap for time-series, **permutation tests** (exact inference under the null), conformal inference preview (M9).
  * **Bayesian A/B Testing:** Beta-Binomial for conversion rates, Normal-Normal for continuous metrics, **expected loss / expected regret stopping rules**, multi-armed bandits (Thompson sampling, UCB) as a replacement for fixed-horizon A/B tests.
  * **Causal Graphs & do-Calculus:** Directed Acyclic Graphs (DAGs), **d-separation** criterion, Markov equivalence classes, **Pearl's do-operator** and the three rules of do-calculus, confounders / mediators / colliders, **M-bias** and **butterfly-bias** (colliders you didn't know you conditioned on), identifiability.
  * **Adjustment Strategies:** **Backdoor criterion** (sufficient-adjustment sets), **frontdoor criterion**, **instrumental variables (IV)** and the LATE theorem (Imbens-Angrist), **2SLS**, **Difference-in-Differences (DiD)** and parallel-trends assumption, **Regression Discontinuity Design (RDD)** sharp and fuzzy, **Synthetic Control Method** (Abadie et al.), **matching** (exact, Mahalanobis, propensity-score, CEM).
  * **Modern Causal ML:** **Double/Debiased ML** (Chernozhukov et al. 2018) as the bridge to high-dimensional confounders, **Causal Forests** (Wager & Athey) for heterogeneous treatment effects, **doubly-robust estimators** (AIPW, TMLE), **meta-learners** (S-, T-, X-, R-, DR-learner), **uplift modelling** for marketing.
  * **Python Stack:** [DoWhy](https://github.com/py-why/dowhy) ✅ (end-to-end causal workflow), [EconML](https://econml.azurewebsites.net/) ✅ (Microsoft, heterogeneous TE), [CausalML](https://causalml.readthedocs.io/) ✅ (Uber, uplift), [Pyro](https://pyro.ai/) (probabilistic programming for causal models), `statsmodels` IV/2SLS, `linearmodels` (panel/IV).

* **2026 Resources:**
  * **Primary Course (free):** [Brady Neal — *Introduction to Causal Inference*, Fall 2020 (YouTube + lecture notes; still the gold-standard free course)](https://www.bradyneal.com/causal-inference-course) ✅
  * **Econometric track:** [MIT 14.387 — *Applied Econometrics (Mostly Harmless Big Data)*, Fall 2014 OCW](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) ✅
  * **Harvard CAUSALab** — [course materials + *What If* book](https://www.hsph.harvard.edu/causal/) ✅
  * **Practical book (free, 2024):** [Matheus Facure — *Causal Inference for the Brave and True*](https://matheusfacure.github.io/python-causality-handbook/landing-page.html) ✅ — every chapter is a runnable notebook.
  * **Required Reading:**
    * Hernán & Robins — [*Causal Inference: What If* (free PDF, 2024 revision)](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf) ✅
    * Pearl, Glymour & Jewell — *Causal Inference in Statistics: A Primer* (Wiley 2016).
    * Pearl — *Causality: Models, Reasoning, and Inference* (Cambridge 2e, 2009) — the reference.
    * **Kohavi, Tang & Xu** — [*Trustworthy Online Controlled Experiments*](https://doi.org/10.1017/9781108653985) ✅ (Cambridge 2020) — **the industrial A/B-testing bible**.
  * **Communities / living resources:** [exp-platform.com](https://exp-platform.com/) ✅ (Ron Kohavi's blog + papers from Microsoft ExP platform), [Statistical Modeling, Causal Inference & Social Science (Gelman blog)](https://statmodeling.stat.columbia.edu/), Pearl's *UCLA Causality Blog*.

* **📋 Mandatory mini-projects:**
  1. **Design + simulate an A/B test** with CUPED variance reduction — show the % reduction in required sample size.
  2. **Fit an IV regression** on a realistic dataset (e.g., [NLSY or Angrist-Krueger 1991 compulsory-schooling](https://www.nber.org/papers/w3572)) — reproduce the returns-to-education estimate.
  3. **Use DoWhy end-to-end**: model → identify → estimate → refute — on a confounded synthetic dataset; show refutation tests (placebo, random common cause, unobserved-confounder sensitivity).
  4. **Causal Forest on lalonde / criteo-uplift**: estimate CATEs, plot HTE heatmap, produce a targeting policy + its evaluation via doubly-robust off-policy estimation.

---

<a id="module-7"></a>
## Module 7: Data Wrangling, EDA & Visualisation

* **The Tutor's "Why":** "The data scientist spends 80% of their time on data preparation" is a cliché because it's true. Harvard CS109A dedicates **three full weeks** to this before any modelling.

* **Strict Prerequisites:** Module 1 (Python).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 1 "Introduction to CS109A"]**: The data-science life-cycle (CRISP-DM revisited for 2026), question framing, translating business problems into statistical ones.
  * **[Harvard CS109A · Lec 2 "Introduction to PANDAS and EDA"]**: `DataFrame` / `Series` model, indexing (`.loc`, `.iloc`), filtering, `groupby`-`apply`-`combine`, `merge`/`join`/`concat`, `melt`/`pivot`/`stack`/`unstack`, datetime handling, categorical dtype, missing-value representations.
  * **[Harvard CS109A · Lab 1 "Data formats, sources, and scraping"]**: Web scraping with BeautifulSoup, Requests session management, handling JS-rendered pages with Playwright, API consumption (REST, GraphQL, OAuth), handling CSV/TSV/JSON/JSONL/Parquet/Arrow/Avro.
  * **[Harvard CS109A · Lab 2 "Pandas & EDA 2"]**: Outlier detection (z-score, IQR rule, isolation forest preview), distributional plots (histogram binning strategies — Freedman-Diaconis, Sturges, Scott), QQ plots, log-transforms, Box-Cox transforms.
  * **[Harvard CS109A · Lec 9 "Missing Data & Imputation"]**: MCAR / MAR / MNAR taxonomy (Rubin 1976), listwise/pairwise deletion, mean/median/mode imputation, **k-NN imputation**, **MICE (Multivariate Imputation by Chained Equations)**, multiple imputation, domain-specific imputation.
  * **[Harvard CS109A · Lec 12 "Visualization"]**: Grammar of graphics (Wilkinson), Cleveland-McGill perceptual hierarchy (position > length > angle > area > colour), Tufte's principles (data-ink ratio, small multiples), choropleth vs cartogram, interactive dashboards.
  * **[Harvard CS109A · Lec 13 "Ethics"]**: Fairness in data collection, selection bias, survivorship bias, historical bias, measurement bias, informed consent, differential privacy preview.
  * **[IITM BSMS2001 — Business Data Management]**: Real-world data in business context, Excel-to-Python migration, data warehousing vs data lakes, ETL vs ELT, slowly-changing dimensions.
  * **[IITM BSMS2002 — Business Analytics]**: Descriptive / diagnostic / predictive / prescriptive analytics framework, KPIs, dashboarding, **Tableau / PowerBI** vs **Streamlit / Dash / Plotly**.
  * **[MIT 15.773 — Hands-on DL]**: Data-centric AI — **data augmentation**, weak supervision, active learning preview, label noise.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109A 2021 schedule](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) (latest public) · Lectures 1, 2, 9, 12, 13, 21.
  * **Required Reading (Latest 2026 Editions):**
    * _Python for Data Analysis_ (**3rd Edition, 2022**) — Wes McKinney (pandas creator) — chapters 5–10.
    * _Storytelling with Data_ — Cole Nussbaumer Knaflic — communication principles.
    * _Fundamentals of Data Visualization_ — Claus Wilke — [free online](https://clauswilke.com/dataviz/).
  * **Practical Implementation:** **Polars 1.x** (fastest DataFrame library of 2026, Arrow-native, lazy evaluation) as primary; **pandas 2.2+** with PyArrow backend for compatibility. **`matplotlib 3.9+`**, **`seaborn 0.13+`**, **`plotly 5.x`**, **`altair 5.x`**, and **`great_tables`** for publication-grade tables. **`ydata-profiling`** (formerly pandas-profiling) for automated EDA.

* **🔧 Modern Data Tooling:**
  * **[Polars 1.40+](https://pola.rs/)** ✅ — the pandas successor; Rust-powered, Arrow-native, lazy frames, query optimiser. Learn `pl.LazyFrame`, `pl.col`, `pl.Expr`, expression-based group-by, streaming engine.
  * **[DuckDB 1.5+](https://duckdb.org/)** ✅ — "SQLite for analytics." In-process OLAP over Parquet/Arrow; zero-config; faster than pandas on anything > 100MB. Perfect for EDA on 100-GB datasets from a laptop.
  * **[Great Expectations](https://greatexpectations.io/)** ✅ + **[Pandera](https://pandera.readthedocs.io/)** ✅ — schema + data-quality validation; declarative expectations; catch data drift before it reaches models.
  * **[Plotly 5.x](https://plotly.com/python/)** ✅ + **[Altair 5.x](https://altair-viz.github.io/)** ✅ + **[Observable Plot](https://observablehq.com/plot/)** ✅ — the modern grammar-of-graphics ecosystem; Plotly for interactivity, Altair for Vega-Lite precision.
  * **Dashboards:** **[Streamlit](https://streamlit.io/)** ✅ for ML demos, **[Gradio](https://www.gradio.app/)** ✅ for HF-style model UIs, **[Evidently](https://www.evidentlyai.com/)** ✅ for data-drift dashboards.
  * **Feature Engineering Discipline:** Target encoding with K-fold smoothing, **train-test leakage** (temporal, group, target-leak from future aggregates), time-based features (lag, rolling, expanding windows), cyclical encoding (sin/cos of hour/month), **sklearn Pipelines + ColumnTransformer** as the *only* correct way to avoid leakage. Reference: [*Feature Engineering for Machine Learning* — Zheng & Casari (O'Reilly 2018)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/).

* **📦 Module Project (mandatory) — public-data EDA dashboard:** Ingest, validate, clean, and visualise a public dataset; make one defensible recommendation and disclose data limitations. **Definition of done:** schema/transform tests, `README`, and results memo. **Production stretch:** deploy a Streamlit dashboard with CI.

---

<a id="module-8a"></a>
## Module 8a: Databases, SQL & Warehouses

* **The Tutor's "Why":** In 2026, data rarely fits in RAM. IITM dedicates a full diploma-level course (BSCS2001) + two specialisation courses to this. You need SQL fluency for 90% of industry jobs. **Module 8 has been split in v2026.2** into **M8a (Databases, SQL & Warehouses)** here, and **M8b (Distributed Data & Streaming)** directly below — because the 2026 production data stack (Spark + Iceberg + Airflow + Kafka + dbt) is a full module in its own right and cannot share airtime with SQL fundamentals.

* **Strict Prerequisites:** Module 4 (hashing, trees, randomised/streaming algos).

* **Exhaustive Topic List:**
  * **[IITM BSCS2001 — DBMS (Prof. P.P. Das)]**: Relational model (tuples, relations, schemas, keys — super/primary/candidate/foreign), relational algebra (selection σ, projection π, union, intersection, difference, Cartesian product, join variants, division), **SQL DDL** (CREATE, ALTER, DROP), **SQL DML** (SELECT/INSERT/UPDATE/DELETE), JOINs (inner, left/right/full outer, cross, self, lateral), subqueries (correlated vs uncorrelated), CTEs (recursive and non-recursive), window functions (`OVER`, `PARTITION BY`, `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER`), set operations (UNION, INTERSECT, EXCEPT), views, indexes (B-tree, hash, bitmap, covering), transactions and **ACID properties**, isolation levels (read uncommitted/committed, repeatable read, serialisable), concurrency control (two-phase locking, MVCC), recovery (WAL, ARIES), normalisation (1NF/2NF/3NF/BCNF/4NF/5NF), functional dependencies, Armstrong's axioms.
  * **Advanced SQL (2026 Industry Interview Canon):** Query plans (EXPLAIN ANALYZE), cost-based optimisation, partitioning (range/list/hash), bitmap indexes, covering indexes, **recursive CTEs** for hierarchical data, **LATERAL joins**, **PIVOT / UNPIVOT**, **MERGE / UPSERT**, JSON/JSONB queries (Postgres), array types, `PERCENTILE_CONT`, `QUALIFY` clause (Snowflake/BQ), approximate aggregations (`APPROX_COUNT_DISTINCT` powered by HyperLogLog).
  * **[OSSU baseline — Coursera DB Specialisation]**: Data warehouse concepts (star schema, snowflake schema, fact/dimension tables), OLAP cubes, slice/dice/drill-down/roll-up, **SCD Type 0/1/2/3/6**, ETL vs ELT pipeline design, **Kimball dimensional modelling**, Data Vault 2.0 (preview).
  * **Cloud Warehouses (2026 production stack):** **Snowflake** (warehouses, virtual warehouses, time travel, zero-copy clone), **BigQuery** (slot-based pricing, BI-engine, materialised views), **Amazon Redshift**, **Databricks SQL Warehouse**, **DuckDB** (single-node), **ClickHouse** (OLAP, real-time).
  * **[dbt — Data Build Tool](https://docs.getdbt.com/)** ✅: models, sources, tests (`unique`, `not_null`, `accepted_values`, relationships), **macros** (Jinja templating), **incremental models** (with `unique_key`, late-arriving facts), **snapshots** (SCD Type 2 automation), **packages** (`dbt_utils`, `dbt_expectations`), exposures, metrics, MetricFlow integration.
  * **[OSSU — MongoDB path]**: Document databases, BSON, sharding, replica sets, aggregation pipeline ($match, $group, $project, $lookup, $unwind), indexing strategies.

* **2026 Resources:**
  * **Primary Course Link:** [IITM BSCS2001 course page](https://study.iitm.ac.in/ds/course_pages/BSCS2001.html) · [Stanford CS145 Intro to Databases](https://web.stanford.edu/class/cs145/) ✅ · [Databricks Academy](https://www.databricks.com/learn/training/home) (free path) · [dbt Learn](https://learn.getdbt.com/) ✅ (free dbt Fundamentals course).
  * **Required Reading (Latest 2026 Editions):**
    * _Designing Data-Intensive Applications_ — Martin Kleppmann (2017; 2026 revised edition in progress) — chapters 1–4, 10–11.
    * _Database System Concepts_ (**7th Edition, 2019**) — Silberschatz, Korth, Sudarshan.
    * **The Kimball Group** — [*The Data Warehouse Toolkit* (3e)](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/) ✅ — the dimensional-modelling bible.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ (O'Reilly 2022) — Chapters 5–8 for the DB/warehouse half.
  * **Practical Implementation:** **PostgreSQL 17** (with `pgvector` extension), **DuckDB 1.5+**, **SQLAlchemy 2.x** with async, **dbt-core 1.11.8**, **sqlmesh** (dbt alternative), **Snowflake** or **BigQuery** free-tier for cloud practice.

* **📦 Module Project (mandatory) — analytics warehouse:** Model an open dataset as facts/dimensions in Postgres or DuckDB, transform it with dbt, and answer five stakeholder questions with tested SQL. **Definition of done:** dbt tests, query-plan evidence, `README`, and results memo. **Production stretch:** orchestrate refreshes and add data-quality monitoring.

---

<a id="module-8b"></a>
## Module 8b: Distributed Data & Streaming Systems

* **The Tutor's "Why":** Every senior-DS / MLE interview in 2026 covers Spark, Kafka, Airflow, and the lakehouse pattern. Closing this is closing Gap #2 in the benchmark PDF — the single largest production gap. Joe Reis (*Fundamentals of Data Engineering*) and the DataExpert free bootcamp are the two canonical on-ramps.

* **Strict Prerequisites:** Module 4 (randomised / streaming algos, hashing), Module 8a (SQL fluency), Module 1 (async Python).

* **Exhaustive Topic List:**
  * **Storage & File Formats:** **Parquet** (columnar, predicate pushdown, row-groups, page-level statistics), **Apache Arrow** (in-memory columnar, zero-copy IPC), **ORC**, **Avro** (schema evolution), object storage (S3 / GCS / Azure Blob), **lakehouse table formats** — [Apache Iceberg](https://iceberg.apache.org/) ✅ (hidden partitioning, snapshot isolation, time travel, MERGE INTO), [Delta Lake](https://delta.io/) ✅ (ACID on data lake, Z-ordering, vacuum), [Apache Hudi](https://hudi.apache.org/) (streaming upserts).
  * **Distributed Compute:** **Apache Spark 3.5+** — RDDs, DataFrames, Dataset API, Catalyst optimiser, Tungsten execution, **Adaptive Query Execution (AQE)**, broadcast joins vs sort-merge, skew-handling, partitioning and bucketing, caching strategies, PySpark idioms, Spark SQL, MLlib (legacy), **Structured Streaming** (micro-batches, triggers, watermarks). **[Ray Data](https://docs.ray.io/en/latest/data/data.html)** ✅ + **[Dask](https://www.dask.org/)** ✅ as Python-native alternatives. **[Apache Beam](https://beam.apache.org/)** as the portable API.
  * **Orchestration:** **[Apache Airflow](https://airflow.apache.org/)** ✅ — DAGs, operators, sensors, XComs, task groups, dynamic task mapping, backfills, SLAs. **[Dagster](https://dagster.io/)** ✅ — asset-oriented orchestration, software-defined assets, declarative scheduling. **[Prefect](https://www.prefect.io/)** ✅ — Pythonic flows, deployments, agents.
  * **Streaming:** **[Apache Kafka](https://kafka.apache.org/)** ✅ — brokers, topics, partitions, consumer groups, offsets, ISR, **exactly-once semantics**, Kafka Streams, Kafka Connect, Schema Registry (Avro/Protobuf). **[Redpanda](https://redpanda.com/)** ✅ (Kafka-compatible, C++). **[Apache Flink](https://flink.apache.org/)** ✅ (true-streaming, event-time, watermarks, windowing — tumbling/sliding/session, stateful functions). **[Materialize](https://materialize.com/)** / **[RisingWave](https://risingwave.com/)** (streaming SQL).
  * **CAP, Consensus & Consistency:** CAP theorem, PACELC, consensus (Paxos, Raft), eventual consistency, **CRDTs** for collaborative systems, idempotency, exactly-once vs at-least-once vs at-most-once.
  * **[MIT Mining Massive Datasets / Stanford CS246]**: MapReduce algorithms (word count, inverted index, joins), **LSH** (MinHash, random projections), PageRank as eigenvector of stochastic matrix, recommendation systems at scale, frequent itemsets (A-Priori, PCY, Multistage), streaming algorithms (reservoir sampling, Bloom, Count-Min Sketch, HyperLogLog), AdWords / online bipartite matching.

* **2026 Resources:**
  * **Primary Course Link:** [Stanford CS246 2025 lectures (Leskovec)](https://web.stanford.edu/class/cs246/) · [DataExpert.io Free Data Engineer Bootcamp (2025, Zach Wilson)](https://www.dataexpert.io/free-data-engineer-bootcamp) ✅ · [Databricks Spark path](https://www.databricks.com/learn/training/home).
  * **Community handbook:** [DataExpert-io / data-engineer-handbook (free, curated)](https://github.com/DataExpert-io/data-engineer-handbook) ✅ — the 2026 community-maintained DE roadmap.
  * **Required Reading:**
    * Kleppmann — *Designing Data-Intensive Applications* — chapters 6–12 for distributed systems, replication, partitioning, consistency.
    * Reis & Housley — [*Fundamentals of Data Engineering*](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/) ✅ — the full data-engineering lifecycle.
    * *Mining of Massive Datasets* (3e, [free online](http://www.mmds.org/)) — Leskovec, Rajaraman, Ullman — chapters 2–7.
    * [*Streaming Systems*](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) — Akidau, Chernyak, Lax (O'Reilly 2018).
  * **Blogs / Newsletters:** [Joe Reis Substack](https://joereis.substack.com/) ✅, [Kimball Group Tips](https://www.kimballgroup.com/) ✅, [High-Scalability](http://highscalability.com/).
  * **Practical Implementation:** **Apache Spark 3.5+** via **PySpark**, **Apache Iceberg** or **Delta Lake** on Parquet, **Apache Airflow 2.x / 3.0-preview**, **Apache Kafka 3.8+** (local via `kraft` mode), **DuckDB** as your single-node Spark stand-in for learning.

* **📋 Mandatory mini-projects:**
  1. **Build a mini lakehouse** on DuckDB + Parquet + Iceberg on your laptop; write `MERGE INTO` upserts; inspect snapshots and time-travel.
  2. **Airflow DAG** that ingests an open API (e.g., NYC Taxi) → stores Parquet on S3/minio → transforms via dbt → serves to a Streamlit dashboard.
  3. **Kafka + Flink** streaming word-count over a simulated tweet stream; exercise watermarks and late data.
  4. **Spark vs Polars vs DuckDB benchmark** on a 10-GB Parquet dataset — measure wall-clock, peak RAM, and lines-of-code.

---

# 🟧 CLASSICAL MACHINE LEARNING STRATUM (Modules 9–12)

> This stratum is the intersection of every university's "first ML course" — MIT 6.390, Harvard CS 1810, Cambridge MLRD/MLBI, IITM BSCS2004/2007/2008.

---

<a id="module-9"></a>
## Module 9: Supervised Learning — Regression Family

* **The Tutor's "Why":** Linear regression is the universal first ML algorithm because it teaches you optimisation, loss functions, regularisation, and statistical inference all at once. The **Gauss-Markov theorem** appears in every single one of our four universities.

* **Strict Prerequisites:** Modules 3 (projections, SVD), 5 (Normal/Student-t), 6 (hypothesis tests for coefficients).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 1 (Spring 2026): "Intro to ML and Linear Regression"]**: Framing ML problems (problem class, assumptions, evaluation), baselines, **generalisation (train vs test)**, the ERM principle.
  * **[MIT 6.390 · Lec 2: "Regression & Regularization"]**: Ordinary Least Squares (OLS), closed-form normal equations β̂ = (XᵀX)⁻¹Xᵀy, geometric interpretation as projection onto column space of X, **Ridge Regression** (L2 regularisation, closed form, ties to Tikhonov regularisation), **Lasso** (L1 regularisation, sparsity, coordinate descent solver), **Elastic Net**.
  * **[MIT 6.390 · Lec 3: "Gradient Descent"]**: Batch GD, SGD, mini-batch SGD, step-size selection, momentum, Nesterov accelerated gradient, convergence analysis for convex quadratic functions.
  * **[Harvard CS109A · Lec 3 "kNN and Linear Regression"]**: **k-Nearest Neighbours regression** (no training, lazy learning, curse of dimensionality), simple linear regression derivation.
  * **[Harvard CS109A · Lec 4 "Multi-linear and Polynomial Regression"]**: Multiple predictors, design matrix, interaction terms, basis expansions (polynomial, piecewise constant, cubic splines, natural cubic splines, smoothing splines).
  * **[Harvard CS109A · Lec 5 "Model Selection and Cross Validation"]**: Validation set, **K-fold cross-validation** (standard, stratified, LOOCV, time-series CV with `TimeSeriesSplit`), **information criteria** (AIC, BIC, Mallow's Cp, adjusted R²), **bias-variance decomposition** (formal proof).
  * **[Harvard CS109A · Lec 6 "Regularization: Ridge and Lasso"]**: Coefficient paths, hyperparameter search (grid, random, Bayesian optimisation with Optuna), early stopping as implicit regularisation.
  * **[Harvard CS109A · Advanced Section 4 "GLMs"]**: **Generalised Linear Models** — exponential family (canonical form, natural parameter, log-partition function, dispersion), link functions (identity, log, logit, probit, complementary log-log), IRLS algorithm (covered in Cambridge ML&BI).
  * **[IITM BSCS2008 Week 3-4]**: Linear regression in scikit-learn; **gradient descent — batch vs stochastic**; polynomial regression pipeline; regularised linear models.
  * **[Cambridge Data Science · "Feature spaces"]**: Linear models as projection onto span of features; design of features.
  * **[Cambridge ML & Bayesian Inference · "Gaussian processes"]** (2 lectures): **Regression via Gaussian processes**, kernel functions (squared exponential, Matérn, periodic), marginal likelihood for hyperparameter learning, **preview of non-parametric Bayesian regression**.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 Spring 2026](https://introml.mit.edu/spring26/lectures/lec01) · [Harvard CS109A 2021 Lec 3-6](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html).
  * **Required Reading (Latest 2026 Editions):**
    * _An Introduction to Statistical Learning with Python_ (ISLP) — Chapters 3, 5, 6.
    * _The Elements of Statistical Learning_ (ESL, 2nd Ed corrected 12th printing) — Chapters 3, 5.
    * _Pattern Recognition and Machine Learning_ (Bishop, 2006) — Chapter 3.
  * **Practical Implementation:** **scikit-learn 1.5+** (`LinearRegression`, `Ridge`, `Lasso`, `ElasticNet`, `KNeighborsRegressor`, `GaussianProcessRegressor`), **statsmodels** for inferential output, **`torch.optim.SGD` / `torch.optim.AdamW`** once you graduate to M15.

* **📦 Module Project (mandatory) — regression decision service:** Build a leakage-safe baseline-to-regularised pipeline, report uncertainty and subgroup errors, and serve one prediction endpoint. **Definition of done:** data/model/API tests, `README`, and results memo. **Production stretch:** Dockerise it and track experiments in MLflow or W&B.

---

<a id="module-10"></a>
## Module 10: Supervised Learning — Classification & Kernel Methods

* **The Tutor's "Why":** Classification is supervised learning in its most deployed form — spam filters, credit scoring, disease diagnosis. Support Vector Machines are mandatory at every university because their **dual formulation + kernel trick** is the purest expression of convex optimisation meeting functional analysis.

* **Strict Prerequisites:** Module 9, plus Lagrange multipliers (M2) and quadratic forms (M3).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 4 (S26): "Logistic Regression"]**: Sigmoid function σ(z) = 1/(1+e⁻ᶻ), log-odds/logit, **cross-entropy loss** (NLL of Bernoulli), gradient (no closed form), decision boundary (linear), multiclass softmax with categorical cross-entropy, one-vs-rest vs multinomial, class imbalance (oversampling, undersampling, SMOTE, class weights, focal loss).
  * **[MIT 6.86x · Unit 1 Lec 2-4]**: **Perceptron algorithm** (Rosenblatt 1958) — update rule, mistake bound (Novikoff's theorem, proof), linear separability, **Hinge loss and margin boundaries**, regularisation.
  * **[MIT 6.86x · Unit 2 Lec 6 "Nonlinear Classification"]**: Feature transformations, **kernel trick** motivation.
  * **[Harvard CS109A · Lec 14-15 "Logistic Regression 1 & 2"]**: MLE estimation, Newton-Raphson / IRLS, Wald CIs for odds ratios, ROC curves, AUC, precision/recall/F1/F2, confusion matrix, calibration (Platt scaling, isotonic regression), threshold selection.
  * **[Harvard CS 1810 (S26)]**: **Support Vector Machines (SVMs)** — maximum-margin hyperplane derivation, hard-margin primal problem, soft-margin with slack variables ξᵢ, **Lagrangian dual formulation**, KKT conditions, support vectors, **kernel trick** (Mercer's theorem), standard kernels (linear, polynomial, RBF/Gaussian, sigmoid), kernel construction rules, string kernels, graph kernels.
  * **[Cambridge ML & Bayesian Inference · Lec "Linear classifiers I" (2 lectures)]**: Supervised learning via **error minimisation**, **Iterative Reweighted Least Squares (IRLS)** with full derivation, **maximum margin classifier** geometric derivation.
  * **[Cambridge ML & Bayesian Inference · Lec "Support vector machines (SVMs)" (2 lectures)]**: The kernel trick formalised, problem formulation as QP, **constrained optimisation and the dual problem**, SVM training algorithm (SMO — Sequential Minimal Optimisation), ν-SVM, one-class SVM for anomaly detection.
  * **[Cambridge ML & Bayesian Inference · Lec "How to classify optimally" (2 lectures)]**: Treating learning probabilistically — **Bayesian decision theory**, **Bayes-optimal classifier**, likelihood functions and priors, Bayes' theorem applied to supervised learning, **Maximum Likelihood vs Maximum a Posteriori hypotheses** (with proof of equivalence in flat-prior case), reinterpretation of backprop as MLE with squared-error or cross-entropy loss.
  * **[Cambridge ML & Real-World Data · Topic 1 "Statistical Classification" (7 sessions)]**: **Naive Bayes** parameter estimation with Laplace smoothing, statistical laws of language (Zipf's, Heaps'), **statistical tests for classification tasks** (McNemar's test for paired classifier comparison), **cross-validation and test sets**, uncertainty and human agreement (Cohen's κ, Fleiss' κ).
  * **[IITM BSCS2008 · Week 5-8]**: Logistic regression in scikit-learn; binary vs multiclass classification via one-vs-rest and softmax; **SVMs** with scikit-learn (`SVC`, `LinearSVC`); kernel selection in practice.
  * **[MIT 6.86x · Unit 1 Lec 4 "Linear Classification and Generalization"]**: VC dimension informal, PAC learning introduction.
  * **[Harvard CS 1810]**: **Linear Discriminant Analysis (LDA)** — generative classifier, equal class covariance assumption, **Quadratic Discriminant Analysis (QDA)**, Gaussian Naive Bayes as diagonal-covariance QDA.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 S26 Lec 4](https://introml.mit.edu/spring26/lectures/lec04) · [Cambridge ML&BI](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/).
  * **Required Reading (Latest 2026 Editions):**
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 4, 6, 7.
    * ISLP — Chapters 4, 9.
    * _Learning with Kernels_ — Schölkopf & Smola — deep dive on SVMs.
  * **Practical Implementation:** **scikit-learn** (`LogisticRegression`, `SVC`, `LinearSVC`, `GaussianNB`, `MultinomialNB`, `LinearDiscriminantAnalysis`, `QuadraticDiscriminantAnalysis`); **`libsvm`** directly for research; **`cvxpy`** to hand-code the SVM dual QP for didactic clarity.

* **🎯 Calibration & Reliability:** A classifier that outputs `P(y=1 | x) = 0.9` but is right only 70% of the time is *mis-calibrated* — disastrous for medical, financial, and risk-scoring applications.
  * **Calibration methods:** [**Platt scaling**](https://en.wikipedia.org/wiki/Platt_scaling) (logistic calibration on held-out scores), **isotonic regression** (non-parametric, monotone step-function, better for ≥ 1000 calibration samples), **temperature scaling** (single-parameter scalar on logits; the standard for modern neural networks — Guo et al. ICML 2017), **Beta calibration**, **Dirichlet calibration** (multi-class), **histogram binning**.
  * **Metrics:** **Brier score**, **Expected Calibration Error (ECE)**, **Maximum Calibration Error (MCE)**, **reliability diagrams** (calibration curves), **log-loss** decomposition into refinement + calibration.
  * **Practical:** [`sklearn.calibration.CalibratedClassifierCV`](https://scikit-learn.org/stable/modules/calibration.html), [`sklearn.calibration.calibration_curve`](https://scikit-learn.org/stable/modules/generated/sklearn.calibration.calibration_curve.html), [`netcal`](https://github.com/EFS-OpenSource/calibration-framework) for DL calibration.
  * **Why it matters for 2026 interviews:** every senior-DS interview asks about calibration before asking about model choice.

* **📦 Module Project (mandatory) — churn decision dashboard:** Implement logistic regression from scratch with NumPy (`__init__` → `sigmoid` → `fit` → `predict`), compare it with scikit-learn, calibrate probabilities, and document a threshold policy. **Definition of done:** gradient/parity/failure tests, `README`, and results memo. **Production stretch:** deploy the dashboard with CI and prediction logging.

---

<a id="module-11"></a>
## Module 11: Unsupervised Learning, Dimensionality Reduction & Mixture Models

* **The Tutor's "Why":** The universe is overwhelmingly unlabelled. Every one of our four universities treats PCA as an eigenvalue problem, K-means as Lloyd's algorithm, and mixture models as the EM-algorithm's canonical application. Harvard CS109B's **very first lecture** is clustering.

* **Strict Prerequisites:** Module 3 (SVD, eigendecomposition), Module 5 (multivariate Gaussian), Module 9 (MLE).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 10 "Principal Component Analysis"]**: **PCA** derivation three ways — variance maximisation, reconstruction error minimisation, and **SVD of the centred data matrix**; eigenvalue scree plot, Kaiser criterion, parallel analysis; **Advanced Section 3: "Math Foundations of PCA"** — formal proof via Lagrange multipliers; kernel PCA; sparse PCA; probabilistic PCA.
  * **[Harvard CS109B · Lec 1-2 "Clustering 1 & 2"]**: **K-means algorithm** (Lloyd's iteration), random initialisation and **K-means++**, within-cluster sum of squares (WCSS), elbow method, silhouette coefficient, gap statistic, **Hierarchical clustering** (agglomerative — single/complete/average/Ward linkage; divisive), dendrograms, cophenetic correlation coefficient, **DBSCAN** (eps, minPts, core vs border vs noise), OPTICS, HDBSCAN (2026 go-to), Mean-Shift, Spectral clustering (graph Laplacian eigenvectors).
  * **[Harvard CS109B · Advanced Section 1 "Gaussian Mixture Models"]**: **GMM** as probabilistic clustering, responsibilities γₙₖ, **EM algorithm** for GMMs — E-step computes responsibilities, M-step updates μₖ, Σₖ, πₖ; convergence proof via Jensen's inequality; choosing K via BIC; comparison to K-means (K-means as degenerate GMM).
  * **[Cambridge ML & Bayesian Inference · "Unsupervised learning I"]**: **The k-means algorithm** derivation, **clustering as a maximum likelihood problem** (hard vs soft assignments).
  * **[Cambridge ML & Bayesian Inference · "Unsupervised learning II"]**: **The EM algorithm** — general form (E-step = variational lower bound, M-step = maximise over parameters), application to clustering, application to missing-data problems, **connection to variational inference** (preview of M13).
  * **[MIT 6.86x · Unit 4 Lec 13-16]**: Clustering 1 & 2; Generative models; **Mixture Models and EM algorithm**; Project 4 — Collaborative Filtering via Gaussian Mixtures (**matrix factorisation perspective**).
  * **[MIT 6.390 · Lec 8 (S26): "Representation Learning"]**: Modern view of unsupervised learning — **autoencoders as non-linear PCA**, bottleneck layer, tied weights, denoising autoencoders, sparse autoencoders.
  * **[MIT 6.790 · Part II "Unsupervised Learning"]**: Dimensionality reduction (PCA, Kernel PCA, **ISOMAP**, **Locally Linear Embedding**, **t-SNE** with perplexity tuning, **UMAP** with `n_neighbors`/`min_dist`), matrix estimation (low-rank matrix completion — Netflix prize), feature extraction from unstructured text (topic models — LDA).
  * **[IITM BSCS2008 · Week 12]**: Unsupervised learning in scikit-learn.
  * **[MIT 6.7960 · Week 7 "Representation learning — similarity-based"]**: **Metric learning**, contrastive learning (SimCLR, MoCo, CLIP training objective), InfoNCE loss, alignment and uniformity criteria.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109B 2022 Lec 1-2](https://harvard-iacs.github.io/2022-CS109B/) · [MIT 6.86x Unit 4](https://www.edx.org/learn/machine-learning/massachusetts-institute-of-technology-machine-learning-with-python-from-linear-models-to-deep-learning).
  * **Required Reading (Latest 2026 Editions):**
    * ESL — Chapter 14.
    * PRML Bishop — Chapters 9, 12.
    * _Probabilistic Machine Learning: An Introduction_ (Murphy, MIT Press 2022) — chapters 20-21.
  * **Practical Implementation:** **scikit-learn** (`KMeans`, `DBSCAN`, `AgglomerativeClustering`, `GaussianMixture`, `PCA`, `KernelPCA`, `TruncatedSVD`); **`hdbscan`**, **`umap-learn`**, **`openTSNE`**; **`pymc`** for Bayesian GMMs.

* **📦 Module Project (mandatory) — customer segmentation study:** Implement K-Means from scratch with NumPy, compare against scikit-learn and density-based clustering, and test stability across seeds. **Definition of done:** convergence/parity tests, `README`, and results memo. **Production stretch:** track runs and publish a monitored segmentation dashboard.

---

<a id="module-12"></a>
## Module 12: Ensemble Methods, Tree-Based Learning & Boosting

* **The Tutor's "Why":** On tabular data (still the majority of enterprise data in 2026), **gradient-boosted trees (XGBoost/LightGBM/CatBoost) beat deep learning** the overwhelming majority of the time. Harvard CS109A dedicates **four full lectures** to trees/bagging/RF/boosting. You must master this before assuming neural networks are always better.

* **Strict Prerequisites:** Modules 9-10 (have solved classification and regression).

* **Exhaustive Topic List:**
  * **[Harvard CS109A · Lec 16 "Decision Tree"]**: CART algorithm (Breiman 1984); splitting criteria — **Gini impurity**, **entropy / information gain**, variance reduction for regression; tree growth; pre-pruning (max_depth, min_samples_split) vs post-pruning (cost-complexity pruning α-path); handling of categorical variables; missing-value handling (surrogate splits).
  * **[Harvard CS109A · Lec 17 "Bagging"]**: Bootstrap aggregation; variance reduction mechanism; out-of-bag (OOB) error estimate as free cross-validation.
  * **[Harvard CS109A · Lec 18 "Random Forest"]**: Feature subsampling (√p for classification, p/3 for regression), **variable importance measures** (Gini importance, permutation importance, SHAP values — previewed), extremely randomised trees (ExtraTrees).
  * **[Harvard CS109A · Lec 19 "Boosting"]**: **AdaBoost** (weighted training, exponential loss derivation, Friedman-Hastie-Tibshirani statistical view), **Gradient Boosting Machines** (functional gradient descent, learning rate shrinkage, stochastic gradient boosting), **XGBoost** (regularised objective, second-order Taylor expansion of loss, handling missing values, sparse-aware split finding), **LightGBM** (histogram binning, GOSS — Gradient-based One-Side Sampling, EFB — Exclusive Feature Bundling, leaf-wise growth), **CatBoost** (ordered boosting, symmetric trees, native categorical handling).
  * **[Harvard CS109A · Lec 20 "Model Interpretability"]**: **SHAP** (Shapley values from coalitional game theory, TreeSHAP efficient computation), **LIME** (local surrogate models), **Partial Dependence Plots**, **ICE plots**, permutation-based feature importance, **counterfactual explanations**.
  * **[Harvard CS109A · Advanced Section 5 "Stacking & Mixture of Experts"]**: **Stacking** (level-0 base learners + level-1 meta-learner), **blending**, **Mixture of Experts** architecture (gating network + expert networks — preview of modern MoE transformers in M18).
  * **[IITM BSCS2008 · Week 9-10]**: Decision Trees, Ensemble Learning, and Random Forests (two full weeks).
  * **[MIT 6.86x]**: Classification and regression trees covered in homework form.
  * **[Harvard CS 1810]**: "Ensemble methods and boosting" as a named topic in the 2026 syllabus.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109A Lec 16-20](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html).
  * **Required Reading (Latest 2026 Editions):**
    * ISLP — Chapter 8.
    * ESL — Chapter 10 (boosting), 15 (random forests).
    * XGBoost paper (Chen & Guestrin 2016) — mandatory.
    * _Interpretable Machine Learning_ — Christoph Molnar — [free online, 2024 edition](https://christophm.github.io/interpretable-ml-book/).
  * **Practical Implementation:** **scikit-learn** (`DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `HistGradientBoostingClassifier` — now default, C++-backed), **XGBoost 2.x**, **LightGBM 4.x**, **CatBoost 1.2+**, **`shap` 0.46+**, **`interpret` (Microsoft InterpretML)**, **`dalex`**.

* **📦 Module Project (mandatory) — tree benchmark:** Implement a small CART classifier from scratch, then compare it with random forest and gradient boosting on tabular data with calibration and explainability. **Definition of done:** split/prediction/parity tests, `README`, and results memo. **Production stretch:** package the winner behind a Dockerised API with CI.

---

# 🟦 PROBABILISTIC & BAYESIAN STRATUM (Modules 13–14)

---

<a id="module-13"></a>
## Module 13: Bayesian Inference, Graphical Models & MCMC

* **The Tutor's "Why":** Harvard CS109B allocates **weeks 2-4 (five consecutive Bayes lectures)** to this; MIT 6.790 dedicates Part III entirely to it; Cambridge's ML & Bayesian Inference is named after it; Cambridge MLMI Module 1 states it as a foundational objective. Ignore this module and you will never understand uncertainty quantification, variational autoencoders, or modern Bayesian neural networks.

* **Strict Prerequisites:** Module 5 (conjugate priors, Beta, Gamma, Dirichlet, Multivariate Normal), Module 11 (EM algorithm).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 3 "Bayes 1"]**: **Philosophical basis of Bayesianism** — subjective probability, Cox's theorem (probability as extension of logic), Dutch book argument. Prior × Likelihood ∝ Posterior. Conjugate prior families (Beta-Binomial, Gamma-Poisson, Normal-Normal, Dirichlet-Multinomial, Normal-Inverse-Gamma, Normal-Inverse-Wishart).
  * **[Harvard CS109B · Lec 4 "Bayes 2"]**: **Posterior predictive distribution**, credible intervals vs confidence intervals (conceptual distinction), marginal likelihood (evidence), Bayes factors for model comparison.
  * **[Harvard CS109B · Lec 5 "Bayes 3"]**: **Hierarchical (multi-level) Bayesian models** — partial pooling, shrinkage, James-Stein estimator, empirical Bayes, Gibbs sampling introduction.
  * **[Harvard CS109B · Lec 6 "Bayes 4"]**: **Markov Chain Monte Carlo (MCMC)** — detailed balance condition, **Metropolis-Hastings algorithm** with proposal distributions and acceptance probability, **Gibbs sampling** (when conditionals are tractable), Hamiltonian Monte Carlo (HMC) preview.
  * **[Harvard CS109B · Lec 7 "Bayes 5"]**: **Variational Inference** — ELBO (Evidence Lower Bound) derivation, mean-field approximation, coordinate ascent VI, **stochastic VI**, normalising flows preview, **reparameterisation trick** (preview of VAEs in M16).
  * **[Harvard CS109B · Advanced Section 2 "Particle Filters / Sequential Monte Carlo"]**: **Sequential Monte Carlo** — bootstrap filter, importance sampling, resampling (systematic, residual, stratified), particle degeneracy, effective sample size, auxiliary particle filter.
  * **[Cambridge ML & Bayesian Inference · Lec "Bayesian networks I" (2 lectures)]**: **Directed graphical models (Bayesian networks)** — representing uncertain knowledge as DAGs, joint distribution factorisation, **conditional independence** (d-separation, Markov blanket), **exact inference** (variable elimination, junction tree algorithm / message passing, belief propagation for trees).
  * **[Cambridge ML & Bayesian Inference · Lec "Bayesian networks II"]**: **Markov Random Fields (undirected graphical models)** — Gibbs distributions, potential functions, Hammersley-Clifford theorem, Ising model, **approximate inference**, **Markov chain Monte Carlo methods** (full MH + Gibbs treatment).
  * **[Cambridge ML & Bayesian Inference · Lec "Linear classifiers II"]**: **The Bayesian approach to neural networks** — Laplace approximation (Gaussian at MAP), Bayesian backpropagation (MacKay), MC dropout as approximate Bayesian inference.
  * **[MIT 6.790 · Part III "Probabilistic Modeling"]**: Incorporating prior knowledge, sampling from complex distributions, Bayes rule as basis of all inference, selecting priors (Gaussian → ridge; Laplace → lasso; Dirichlet-process for non-parametric Bayes), **Gibbs sampling derivation**, **Metropolis-Hastings with full proof of detailed balance**.
  * **[MIT 6.790]**: MCMC listed as "one of the top 10 algorithms of all time" alongside quicksort and FFT.
  * **[Cambridge MLMI Module 1]**: **Maximum-likelihood vs Bayesian inference** — strengths and weaknesses of both; **belief propagation** algorithm.
  * **[Harvard CS 1810 (S26)]**: "Graphical models", "hidden Markov models" (→ M14), "inference methods" as syllabus topics.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard CS109B 2022 schedule](https://harvard-iacs.github.io/2022-CS109B/) (Bayes lectures 3-7) · [Cambridge ML&BI 2025-26](https://www.cl.cam.ac.uk/teaching/2526/MLBayInfer/) · [MIT 6.790 Part III](https://gradml.mit.edu/intro/).
  * **Required Reading (Latest 2026 Editions):**
    * _Probabilistic Machine Learning: Advanced Topics_ (Kevin Murphy, **MIT Press 2023**) — Chapters 1-12 (most current Bayesian treatment).
    * _Bayesian Data Analysis_ (**3rd Edition**) — Gelman, Carlin, Stern, Dunson, Vehtari, Rubin (BDA3).
    * _Pattern Recognition and Machine Learning_ — Bishop — Chapters 8 (graphical models), 10 (VI), 11 (MCMC).
    * _Bayesian Reasoning and Machine Learning_ — David Barber — [free PDF](http://www.cs.ucl.ac.uk/staff/D.Barber/brml/) (explicitly listed in Cambridge ML&BI reading list).
  * **Practical Implementation:** **PyMC 5.x** (with PyTensor backend), **NumPyro 0.15+** (JAX-native, 10-100× faster for complex models, standard in 2026 research), **Stan** via `cmdstanpy`, **TensorFlow Probability 0.24+**, **`arviz`** for posterior diagnostics (R̂, ESS, trace plots, posterior predictive checks).

* **📦 Module Project (mandatory) — Bayesian decision package:** Fit a hierarchical model, run prior/posterior predictive checks and convergence diagnostics, then express a decision under uncertainty. **Definition of done:** simulation/recovery tests, `README`, and results memo. **Production stretch:** track posterior artifacts and deploy a reproducible report pipeline.

---

<a id="module-14"></a>
## Module 14: Sequence Modelling — HMMs, Kalman Filters & Time Series

* **The Tutor's "Why":** Time is the most important axis in the real world. Cambridge ML & Real-World Data dedicates **Topic 2 (4 sessions) entirely** to HMMs with a biological application. MIT MicroMasters C4 is a whole course on time series with interventions. The state-space model framework unifies HMMs, Kalman filters, and particle filters.

* **Strict Prerequisites:** Module 5 (Markov chains — Stat 110 Lec 31-33), Module 13 (message passing).

* **Exhaustive Topic List:**
  * **[Cambridge ML & Real-World Data · Topic 2 "Sequence Analysis" (4 sessions)]**: **Hidden Markov Models (HMM)** — model definition (hidden state chain + observation emissions), assumptions (Markov property on hidden chain, observation independence given state), the three canonical problems (Rabiner 1989):
    1. **Evaluation** — P(observations | model) via **Forward algorithm**.
    2. **Decoding** — most likely hidden sequence via **Viterbi algorithm** (with full dynamic-programming derivation).
    3. **Learning** — parameter estimation via **Baum-Welch / Forward-Backward** (EM for HMMs).
    * Application: **predicting protein interactions with a cell membrane** (Cambridge's specific biological application).
  * **[Harvard CS 1810 (S26)]**: **Hidden Markov Models** as a named 2026 syllabus topic.
  * **[MIT 6.431x]**: Bernoulli process, Poisson process, **hidden random processes** (preview of state-space models).
  * **[Cambridge MLMI 1]**: **Kalman filter** implementation — state-space model for linear Gaussian systems, prediction step and update step, Rauch-Tung-Striebel smoother, **extended Kalman filter (EKF)** for nonlinear systems, **unscented Kalman filter (UKF)**, connection to Bayesian belief update.
  * **[MIT MicroMasters 14.310x / "Data Analysis: Learning Time Series with Interventions"]**: Time series basics — trend, seasonality, cyclicity, stationarity (strong vs weak/covariance stationarity), ACF/PACF, white noise tests (Ljung-Box); ARMA models; **ARIMA** and **SARIMA** (Box-Jenkins methodology); Vector Autoregression (VAR); Granger causality; cointegration and Engle-Granger two-step; **ARCH/GARCH** for volatility; state-space formulation; Kalman filter as linear-Gaussian HMM; structural time-series models (Harvey BSM); **prophet** (Facebook's decomposable model); **DeepAR**, **Temporal Fusion Transformers** (modern 2026 approach); **intervention analysis** (difference-in-differences, interrupted time series, synthetic control); regression discontinuity; instrumental variables for causal inference.
  * **[Harvard CS109B · Lec 17 "Recurrent Neural Networks"]**: **RNN for sequence modelling** (connects to M15).
  * **[Harvard CS109B · Lec 18 "NLP 1 — GRUs / LSTMs"]**: **Long Short-Term Memory (LSTM)** — gate equations (input, forget, output gates), cell state, vanishing gradient solution; **Gated Recurrent Unit (GRU)** — update and reset gates.

* **2026 Resources:**
  * **Primary Course Link:** [Cambridge ML & Real-World Data](https://www.cl.cam.ac.uk/teaching/2324/MLRD/) · [MITx 14.310x](https://micromasters.mit.edu/ds/).
  * **Required Reading (Latest 2026 Editions):**
    * _Forecasting: Principles and Practice_ (**3rd Edition**) — Rob Hyndman — [free online](https://otexts.com/fpp3/).
    * _Time Series Analysis_ — James Hamilton — classical econometric reference.
    * Rabiner, "A Tutorial on Hidden Markov Models" (IEEE 1989) — mandatory historical reading.
    * Bishop PRML — Chapter 13 (sequential data).
  * **Practical Implementation:** **`statsmodels.tsa`** (ARIMA, SARIMAX, VAR, state-space), **`pmdarima`** (auto-ARIMA), **`prophet` 1.1+**, **`hmmlearn`**, **`pykalman`**, **`filterpy`** for Kalman variants, **`darts`** (Unit8's unified TS library — 2026 favourite), **`sktime` 0.30+**, **`neuralforecast`** (Nixtla) for modern deep TS.

* **📦 Module Project (mandatory) — forecast dashboard:** Compare naïve, statistical, and learned forecasts using rolling-origin validation; quantify interval coverage and failure during regime change. **Definition of done:** leakage/metric tests, `README`, and results memo. **Production stretch:** schedule retraining and monitor forecast drift.

---

# 🟪 DEEP LEARNING STRATUM (Modules 15–17)

---

<a id="module-15"></a>
## Module 15: Deep Learning Foundations — MLPs, CNNs, Backprop

* **The Tutor's "Why":** The deep-learning revolution (2012-present) defines modern AI. Harvard CS109B allocates **four full lectures (8-11) to neural network fundamentals**; MIT 6.3900 Spring 2026 spends **three lectures (5, 6, 7) on NNs and CNNs**; MIT 6.7960 is an entire course. Master the mathematics before touching a GPU.

* **Strict Prerequisites:** Module 2 (chain rule), Module 3 (matrix calculus), Module 9 (SGD), Module 10 (logistic regression, cross-entropy loss).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 8 "Neural Networks 1 (MLP)"]**: Biological motivation vs artificial neuron (McCulloch-Pitts, perceptron), **Multi-Layer Perceptron (MLP)** architecture — affine transformation + activation function; **universal approximation theorem** (Cybenko 1989, Hornik 1991, with proof sketch).
  * **[Harvard CS109B · Lec 9 "NN 2 — Gradient Descent, SGD, BackProp"]**: **Backpropagation algorithm** — full derivation via chain rule as dynamic programming over the computation graph; vanishing/exploding gradients; **Xavier/Glorot initialisation**, **He initialisation** (theoretical justification for each).
  * **[Harvard CS109B · Lec 10 "NN 3 (Optimizers)"]**: **Momentum**, **Nesterov momentum**, **AdaGrad**, **RMSProp**, **Adam**, **AdamW** (decoupled weight decay — 2017 fix), **LAMB** (for large-batch), **Lion** (2023, Chesterton), **Sophia** (2023), learning-rate schedules (step decay, exponential, cosine annealing, warmup, one-cycle), gradient clipping.
  * **[Harvard CS109B · Lec 11 "NN 4 (Regularization)"]**: **L1/L2 weight decay**, **Dropout** (Hinton 2014 — inverted dropout, concrete dropout), **Batch Normalisation** (Ioffe-Szegedy 2015 — full derivation, internal covariate shift debate, post-hoc explanations), **Layer Normalisation**, **Group Normalisation**, **Instance Normalisation**, **RMSNorm** (2026 standard in LLMs), **early stopping**, **data augmentation**, **label smoothing**, **mixup**, **cutmix**.
  * **[Harvard CS109B · Lec 12 "CNNs 1 (Basics)"]**: **Convolutional Neural Networks** — convolution operation (discrete 2D), **kernels as learnable filters**, stride, padding (valid, same, full), pooling (max, average, global), translation equivariance vs invariance; classic architectures: **LeNet-5**, **AlexNet**, **VGG-16/19**, **GoogLeNet/Inception** (1×1 convolutions for dimensionality reduction).
  * **[Harvard CS109B · Lec 13 "CNNs 2 (Regularization)"]**: Data augmentation for vision, dropout in CNNs, batch-norm placement debate.
  * **[Harvard CS109B · Lec 14 "CNNs 3 (Receptive Field)"]**: **Effective receptive field** calculation, dilated/atrous convolutions, **ResNet** (residual connections — identity mapping, full derivation of gradient flow improvement), **DenseNet**, **SqueezeNet**, **MobileNet** (depthwise-separable convolution), **EfficientNet** (compound scaling), **ConvNeXt** (2022 — CNN catches up to ViT).
  * **[Harvard CS109B · Lec 15 "CNNs 4 (Saliency Maps)"]**: Gradient-based saliency, **Grad-CAM** (Selvaraju 2017), integrated gradients, **SmoothGrad**, adversarial examples (FGSM, PGD, Carlini-Wagner).
  * **[Harvard CS109B · Advanced Section 3 "Solvers"]**: Second-order methods, L-BFGS, natural gradient, K-FAC.
  * **[Harvard CS109B · Advanced Section 4 "Segmentation"]**: **Semantic segmentation** (FCN, U-Net, DeepLab); **instance segmentation** (Mask R-CNN); **panoptic segmentation**.
  * **[Harvard CS109B · Advanced Section 5 "SOTA & Transfer Learning"]**: ImageNet pretraining, **fine-tuning** vs **linear probing** vs **LoRA** (→ M18), feature extraction.
  * **[Harvard CS109B · Advanced Section 6 "Autoencoders"]**: Vanilla AEs, denoising AEs, contractive AEs (Jacobian penalty), sparse AEs (KL penalty on activations).
  * **[MIT 6.390 · Lec 5-6-7 (Spring 2026)]**: "Features & Neural Networks I", "Neural Networks II", "Convolutional Neural Networks" — with extensive labs.
  * **[MIT 6.7960 · Fall 2025, Week 1-3 (Beery · He · Khattab)]**: Course overview (Beery); **How to train a neural net** (Beery — SGD, backprop, autodiff, differentiable programming); **Approximation theory** (Khattab — universal approximation, **Barron's theorem**, depth separation); **Architectures: Grids** (Beery — CNNs in depth); **Architectures: Memory and Sequence Modeling** (He — RNNs, LSTMs, sequence models); **PyTorch Tutorial** sessions with Jamie Meindl and Sharut Gupta. Reading: *Foundations of Computer Vision* chapters on neural nets, gradient descent, backprop, CNNs (all [visionbook.mit.edu](https://visionbook.mit.edu/)).
  * **[MIT 6.7960 · Fall 2025, Week 4]**: **Architectures: Transformers** (Beery — tokens + attention + positional codes; Transformers unify MLPs, GNNs, CNNs); **Generalization Theory** (Khattab — PAC, overparameterisation, **double descent**, inadequacy of VC dimension, inductive biases; readings include arXiv 1611.03530, 2503.02113, 2310.00865).
  * **[IITM BSCS3002 — Deep Learning]**: IITM's dedicated Deep Learning course covers the above plus practical engineering on **PyTorch**.
  * **[IITM BSCS2008 · Week 11]**: Neural networks in scikit-learn (MLP introduction).
  * **[Harvard CS 1810]**: Neural networks as a syllabus topic.
  * **[MIT 6.S191 bootcamp]**: Condensed practical treatment.

* **2026 Resources:**
  * **Primary Course Link:** [**MIT 6.7960 Fall 2025 live schedule**](https://deeplearning6-7960.github.io/) (15 weeks · Beery · He · Khattab) · [MIT 6.390 Spring 2026 calendar](https://introml.mit.edu/spring26/calendar) · [**MIT 6.S191 (2026 edition, Amini)**](https://introtodeeplearning.com/) · [Harvard CS109B 2022 (latest public)](https://harvard-iacs.github.io/2022-CS109B/).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **_Deep Learning: Foundations and Concepts_** — Bishop & Bishop (**Springer 2024**, free online [bishopbook.com](https://bishopbook.com/)) — **primary text** for this module.
    * _Understanding Deep Learning_ — Simon Prince (MIT Press 2024; free online [udlbook.github.io](https://udlbook.github.io/udlbook/)) — chapters 1‑12.
    * _Dive into Deep Learning_ — Zhang, Lipton, Li, Smola — [d2l.ai](https://d2l.ai/) — PyTorch + JAX parallel implementations, continuously updated.
    * _Foundations of Computer Vision_ — Torralba, Isola, Freeman (**MIT Press 2024**, free online at [visionbook.mit.edu](https://visionbook.mit.edu/)) — the official MIT 6.7960 textbook.
    * *Hands‑On Machine Learning with Scikit‑Learn and PyTorch* — Géron (O'Reilly Oct‑Dec 2025).
    * _Deep Learning_ — Goodfellow, Bengio, Courville (2016, still relevant as historical reference).
  * **Practical Implementation:** **PyTorch 2.11.0** (`torch.compile`, FSDP2, CUDA 13, `torch.func.grad`, `torch.distributed.tensor`), **JAX 0.10.0** with **Flax 0.10+** / **NNX** / **Equinox** for functional DL, **Hugging Face Accelerate** for distributed training, **Weights & Biases** or **MLflow 3.11+** for experiment tracking, **Lightning 2.4+** for training‑loop abstraction.

* **🚀 Deep Learning Systems — Training at Scale:** Modern DL is as much a *systems* discipline as an algorithms discipline. Stanford CS336 dedicates weeks to it.
  * **JAX alongside PyTorch:** [JAX docs](https://docs.jax.dev/) ✅, [Flax NNX](https://flax.readthedocs.io/) ✅ — mainstream at Google, DeepMind, Anthropic. Learn `jit`, `vmap`, `pmap`, `scan`, `shard_map`, `jax.Array` with sharding, and the [tour of JAX tutorials](https://docs.jax.dev/en/latest/tutorials.html).
  * **Mixed-Precision Training:** `torch.amp`, `bfloat16` vs `fp16` vs `fp8` (H100/B200), loss-scaling, stochastic rounding; **why bf16 is the 2026 default** (no loss-scaling needed, wider dynamic range).
  * **Gradient Checkpointing:** Trade compute for memory; `torch.utils.checkpoint`, `jax.checkpoint` — required for any model that doesn't fit in GPU RAM.
  * **Fully-Sharded Data Parallel (FSDP / FSDP2):** [PyTorch FSDP API docs](https://docs.pytorch.org/docs/stable/fsdp.html) ✅ + [Getting-Started-with-FSDP2 tutorial](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) ✅. Shard parameters, gradients, and optimiser states across GPUs — the 2026 default for any model > 7B.
  * **Distributed primitives:** DDP, FSDP/FSDP2, Tensor-Parallel (Megatron-style), Pipeline-Parallel (GPipe, PipeDream), **3D parallelism** (DP × TP × PP), ZeRO-1/2/3 (DeepSpeed).
  * **Throughput engineering:** [Triton](https://github.com/triton-lang/triton) ✅ kernels, **FlashAttention-2 / 3** (Tri Dao), **PagedAttention** (vLLM), activation recomputation strategies, `torch.compile` with `fullgraph=True`.
  * **Reading:** [*How to Scale Your Model* (Google JAX scaling book, 2024)](https://jax-ml.github.io/scaling-book/) ✅, [PyTorch DTensor docs](https://pytorch.org/docs/stable/distributed.tensor.html), Stanford CS336 Lectures 5-7 (scaling, parallelism, systems).

* **📦 Module Project (mandatory) — vision training system:** Train a small CNN with reproducible data/versioned configs, baseline it, run ablations, and analyse errors and calibration. **Definition of done:** data/model smoke tests, `README`, and results memo. **Production stretch:** containerise training, enable CI, and track runs.

---

<a id="module-16"></a>
## Module 16: Representation Learning, Transformers & Generative Models

* **The Tutor's "Why":** The Transformer (Vaswani et al. 2017, *Attention is All You Need*) is **the** defining architecture of 2026. MIT 6.390 Spring 2026 dedicates Lecture 9 entirely to it. Every frontier lab, from OpenAI to DeepMind to Anthropic, builds on transformers + diffusion. This module is the ticket to research-grade work.

* **Strict Prerequisites:** Module 15 (backprop, CNNs, RNNs, attention preview).

* **Exhaustive Topic List:**
  * **[Harvard CS109B · Lec 16 "Intro to Language Models"]**: n-gram language models, perplexity, statistical LM vs neural LM.
  * **[Harvard CS109B · Lec 17 "Recurrent Neural Networks"]**: RNN forward/backward through time, bidirectional RNNs.
  * **[Harvard CS109B · Lec 18 "NLP 1 (GRUs/LSTMs)"]**: LSTM full derivation, GRU comparison, vanishing-gradient resolution.
  * **[Harvard CS109B · Lec 19 "NLP 2 (ELMo)"]**: Contextual word embeddings, character-level convolutions, bidirectional LM.
  * **[Harvard CS109B · Advanced Section 7 "Word2Vec"]**: **Skip-gram**, **CBOW**, negative sampling, hierarchical softmax, GloVe (global co-occurrence), FastText (subword embeddings).
  * **[Harvard CS109B · Lec 20 "NLP 3 (Seq2Seq & Attention)"]**: **Encoder-decoder architecture**, **Bahdanau attention** (additive), **Luong attention** (multiplicative), content-based vs location-based attention.
  * **[Harvard CS109B · Lec 21 "NLP 4 (Transformers)"]**: **The Transformer** — Vaswani et al. 2017 in full. Scaled dot-product attention (Q, K, V), **multi-head attention**, **positional encoding** (sinusoidal, learned, rotary RoPE, ALiBi, YaRN), encoder stack, decoder stack with masked self-attention, layer norm placement (pre-LN vs post-LN — 2020 pre-LN victory), feed-forward network (GELU → SwiGLU), residual connections.
  * **[Harvard CS109B · Advanced Section 8 "BERT"]**: **BERT** (bidirectional encoder, masked language modelling, next-sentence prediction), **RoBERTa**, **ALBERT**, **DistilBERT**, **ELECTRA** (replaced token detection), **DeBERTa** (disentangled attention).
  * **[MIT 6.390 · Lec 9 (Spring 2026) "Transformers"]**: Dedicated lecture on transformer architecture.
  * **[MIT 6.7960 · Fall 2025 Week 4 "Architectures: Transformers" (Beery)]**: Three key ideas — **tokens, attention, positional codes**; Transformers as unified framework (subsuming MLPs, GNNs, CNNs); reading = *visionbook.mit.edu/transformers*.
  * **[MIT 6.7960 · Fall 2025 Weeks 5‑7 "Representation Learning" (He, Khattab)]**: **Reconstruction‑based** (autoencoders, VQ-VAE, MAE — Masked Autoencoders); **Similarity‑based / Neural Information Retrieval** — information retrieval, contrastive learning (InfoNCE, hard negatives, KL distillation), sub‑linear search & scaling trade‑offs (cross‑encoders, bi‑encoders, **late interaction / ColBERT**); **Representation Learning and Information Theory** — NN‑GP correspondence, NTK — Neural Tangent Kernel.
  * **[MIT 6.7960 · Fall 2025 Weeks 6‑9 "Foundation Models" (Khattab, He)]**: **Pre‑training** (causal LM loss, SmolLM3, OLMo 2, Marin 8B); **Scaling laws** (Kaplan 2020 + Chinchilla 2022 + Emergent Abilities debate: are emergent abilities a mirage?); **Generative models: basics → VAE & GAN → Diffusion & Flows** (Kaiming He); **Post‑training** (instruction tuning, DPO, GRPO).
  * **[Harvard CS109B · Lec 22-23 "GANs 1 & 2"]**: **Generative Adversarial Networks** — minimax game formulation (Goodfellow 2014), optimal discriminator proof, **mode collapse**, **Wasserstein GAN** (earth-mover distance, Kantorovich-Rubinstein duality), **WGAN-GP** (gradient penalty), **DCGAN**, **Progressive GAN**, **StyleGAN 2/3**, **BigGAN**, **Conditional GAN**, **Pix2Pix**, **CycleGAN** (unpaired translation).
  * **[Harvard CS109B · Advanced Section 9 "More GANs"]**: Evaluation metrics (IS, FID, KID, precision-recall), tricks (spectral normalisation, self-attention GAN — SAGAN).
  * **[MIT 6.7960 · Week 8-9 "Generative models"]**:
    * **Basics** — density models, energy-based models, Langevin samplers, **autoregressive models** (PixelRNN, PixelCNN, MADE, WaveNet), GANs.
    * **Representation-meets-generation** — **VAEs** (Kingma 2013) with full ELBO derivation, **reparameterisation trick** (ε ~ 𝒩(0,I); z = μ + σε), β-VAE for disentanglement, VQ-VAE, NVAE.
    * **Conditional models** — cGAN, cVAE, conditional diffusion, paired image-to-image (Pix2Pix), text-to-image (DALL-E, Imagen, Stable Diffusion, Midjourney), image-to-text (captioning).
  * **[MIT 6.7960]**: **Diffusion Models (DDPM)** — forward noising process, reverse denoising process, **score-matching formulation** (Song & Ermon), **variational diffusion** (Ho et al. 2020), classifier-free guidance, **latent diffusion** (Stable Diffusion), **DPM-Solver / DPM-Solver++** (2022 ODE samplers), **Flow Matching** (2023), **Rectified Flow** (2024 — the 2026 SOTA for image/video gen).
  * **[MIT 6.7960 · Week 10-11 "Generalization (OOD) & Transfer Learning"]**: **Adversarial robustness** (FGSM, PGD attacks, certified defences), **distribution shift** (covariate shift, label shift, concept drift), **domain adaptation** (DANN, CORAL, MMD), **foundation models** — fine-tuning, **linear probing**, **knowledge distillation**, **prompting**, **parameter-efficient fine-tuning** (PEFT: adapters, LoRA, QLoRA, IA³, prompt tuning, prefix tuning).
  * **[MIT 6.7960 · Week 11 "Scaling Laws"]**: **Kaplan scaling laws** (2020), **Chinchilla scaling laws** (Hoffmann 2022 — compute-optimal N*D allocation), power-law behaviour, breaking power laws via data pruning, critical batch size.
  * **[IITM BSCS3005 — Computer Vision]**: Image classification, object detection (YOLO v8-v10, DETR), segmentation, video understanding, 3D vision, **NeRF** (Neural Radiance Fields), **3D Gaussian Splatting** (2023 SOTA — 2026 standard for 3D scenes).
  * **[IITM BSCS3004 — LLMs]**: Dedicated course on language modelling (see M18).

* **2026 Resources:**
  * **Primary Course Link:** [**MIT 6.7960 Fall 2025 full schedule**](https://deeplearning6-7960.github.io/) (weeks 4‑11) · [**Stanford CS336 Spring 2026 Lec 3–4**](https://cs336.stanford.edu/) (architectures + MoE) · [Harvard CS109B 2022 Lec 16‑23](https://harvard-iacs.github.io/2022-CS109B/) · [MIT 6.390 S26 Lec 9](https://introml.mit.edu/spring26/lectures/lec09).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **Bishop & Bishop — *Deep Learning: Foundations and Concepts*** (Springer 2024, free at [bishopbook.com](https://bishopbook.com/)) — chapters on attention and transformers.
    * _Understanding Deep Learning_ — Prince — Chapters 12‑18 (transformers, GANs, VAEs, diffusion).
    * **_Hands‑On Large Language Models_** — Alammar & Grootendorst (O'Reilly, Sep 2024, 428 pp.) — [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models).
    * Vaswani et al. 2017 ("Attention is All You Need") — **mandatory primary‑source reading**.
    * Ho, Jain, Abbeel 2020 ("DDPM") — for diffusion.
    * Lipman et al. 2023 ("Flow Matching") & Liu et al. 2022 ("Rectified Flow") — 2026 generative SOTA.
    * Radford et al. 2021 ("CLIP") — multi‑modal foundation.
    * _The Little Book of Deep Learning_ — François Fleuret — concise reference.
  * **Practical Implementation:** **Hugging Face Transformers v5.0 / v4.57 LTS**, **Diffusers 0.30+** (image/video), **PEFT 0.14+** (LoRA/QLoRA/DoRA), **xformers** / **FlashAttention‑3**, **bitsandbytes** (4/8‑bit), **`torch.compile`** + **`torch.fullgraph`** (2× speedups), **Triton 3.x** for custom kernels (Stanford CS336 Lec 6).

* **📦 Module Project (mandatory) — pretrained sentiment service:** Fine-tune or linearly probe a transformer, compare against a classical baseline, and report robustness, latency, and model-card limitations. **Definition of done:** preprocessing/inference tests, `README`, and results memo. **Production stretch:** deploy a monitored API with Docker and CI.

---

<a id="module-17"></a>
## Module 17: Reinforcement Learning & Decision Making

* **The Tutor's "Why":** RL drives robotics, game AI, and — most importantly in 2026 — the RLHF alignment of LLMs. MIT 6.390 Spring 2026 Lec 10-11 covers MDPs and RL. IITM runs a dedicated BSCS3003 course. Harvard CS 1810 (2026) lists reinforcement learning as a named syllabus topic.

* **Strict Prerequisites:** Module 5 (Markov chains, expectation), Module 15 (can train a deep network).

* **Exhaustive Topic List:**
  * **[MIT 6.390 · Lec 10 (Spring 2026) "Markov Decision Processes"]**: **MDP formulation** — (S, A, P, R, γ), episodic vs continuing tasks, **Bellman equations** (value iteration, policy iteration), **optimality** (Bellman optimality operator, contraction mapping theorem proof), dynamic programming for MDPs.
  * **[MIT 6.390 · Lec 11 (Spring 2026) "Reinforcement Learning"]**: **Model-free RL** — **Monte Carlo methods** (first-visit, every-visit), **Temporal Difference (TD)** learning, **TD(0)**, TD(λ), SARSA, **Q-learning** (off-policy TD control), **Deep Q-Networks (DQN)** (Mnih et al. 2015 — experience replay, target network, Atari), Double DQN, Dueling DQN, Rainbow DQN.
  * **[MIT 6.790 · Part IV "Decision Making"]**: Optimising under model uncertainty; **explore-vs-exploit tradeoff**; **credit assignment problem**; two key timescales (state dynamics vs information dynamics) → framework table distinguishing optimisation, MDPs, RL.
  * **[MIT 6.86x · Unit 5 Lec 17-19]**: **Reinforcement Learning 1 & 2**; Applications to **Natural Language Processing** (dialogue systems as RL, text summarisation as RL).
  * **[IITM BSCS3003 — Reinforcement Learning]**: Dedicated 12-week course covering:
    * Multi-armed bandits (ε-greedy, UCB, Thompson sampling, contextual bandits — LinUCB, Neural contextual bandits).
    * Policy gradient methods — **REINFORCE** (Williams 1992, log-likelihood trick derivation), **Actor-Critic** (A2C, A3C), **Advantage function**, **GAE** (Generalised Advantage Estimation).
    * **Trust Region methods** — TRPO (Schulman 2015), **PPO** (Schulman 2017 — clipped objective, the RLHF workhorse), **TRPO vs PPO vs ACKTR**.
    * **Deterministic Policy Gradient** (DPG), **DDPG**, **TD3**, **SAC** (Soft Actor-Critic, max-entropy RL).
    * **Model-based RL** — Dyna-Q, **MuZero**, **DreamerV3** (2024), **World models**.
    * **Inverse RL** (IRL), **Imitation Learning** (Behavioural Cloning, DAgger), **GAIL** (Generative Adversarial Imitation Learning).
    * **Offline RL** — BCQ, CQL, IQL, decision transformer.
    * **Hierarchical RL** — options framework, feudal networks, HIRO.
    * **Multi-agent RL** — self-play, fictitious play, MADDPG, AlphaZero, counterfactual regret minimisation.
  * **[MIT 6.7960 · Week 15 "Efficient Policy Optimization Techniques for LLMs"]**: **RLHF challenges**, simplifying RL policy optimisation to **relative reward regression** (DPO — Direct Preference Optimisation, Rafailov 2023), **IPO**, **KTO**, **ORPO**, multi-turn RLHF extensions.

* **2026 Resources:**
  * **Primary Course Link:** [MIT 6.390 Spring 2026 Lec 10-11](https://introml.mit.edu/spring26/) · [David Silver DeepMind RL Course (YouTube, still canonical)](https://www.youtube.com/watch?v=2pWv7GOvuf0) · **[IITM BSCS3003 Reinforcement Learning](https://study.iitm.ac.in/ds/course_pages/BSCS3003.html)**.
  * **Required Reading (Latest 2026 Editions):**
    * _Reinforcement Learning: An Introduction_ (**2nd Edition, 2018, 2024 reprint**) — Sutton & Barto — [free PDF](http://incompleteideas.net/book/the-book-2nd.html) — **the canonical text**.
    * _Algorithms for Decision Making_ — Kochenderfer, Wheeler, Wray (MIT Press 2022) — [free online](https://algorithmsbook.com/).
    * _Foundations of Deep Reinforcement Learning_ — Graesser & Keng — for practitioners.
  * **Practical Implementation:** **Gymnasium** (successor to OpenAI Gym), **Stable-Baselines3 2.x**, **CleanRL** (single-file implementations — best for learning), **RLlib** (Ray, for distributed), **PettingZoo** (multi-agent), **trl** (Hugging Face — for RLHF), **DeepMind Acme**, **PufferLib** (2025, unified wrapper).

* **📦 Module Project (mandatory) — reproducible control agent:** Train and evaluate a compact RL agent over multiple seeds; compare against a random policy and report learning stability. **Definition of done:** environment/policy tests, `README`, and results memo. **Production stretch:** track experiments and publish an evaluation dashboard.

---

# 🔴 FRONTIER & PRODUCTION STRATUM — Modules 18, 21–26

---

<a id="module-18"></a>
## Module 18: Large Language Models, RLHF & Alignment

* **The Tutor's "Why":** This is the defining technology of 2026. IITM has a **dedicated course BSCS3004 on LLMs**; MIT 6.7960 Week 12 and 15 cover LLMs and RLHF explicitly; Harvard's AC215 covers MLOps for models. If you cannot build, fine-tune, and deploy an LLM in 2026, you are not employable as a senior data scientist.

* **Strict Prerequisites:** Modules 16 (transformers), 17 (PPO, DPO).

* **Exhaustive Topic List:**
  * **[IITM BSCS3004 — LLMs]**: Full dedicated course covering:
    * **Tokenisation** — BPE (Byte Pair Encoding), WordPiece, SentencePiece, Unigram LM, **tiktoken** (OpenAI), SuperBPE (2024).
    * **Pre-training** — causal LM, masked LM, prefix LM, next-token-prediction loss at scale.
    * **Architectures** — GPT family (GPT-2, GPT-3, GPT-4, GPT-4o, **GPT-5** 2025), Llama (1/2/3/4), Mistral, Gemma, Qwen, DeepSeek (R1 reasoning model 2025), Claude (Sonnet 4, Opus 4).
    * **Context-length extensions** — RoPE scaling, YaRN, Position Interpolation, LongRope, ring attention, infinite attention.
    * **Efficient attention** — FlashAttention v1/v2/v3, PagedAttention (vLLM), sliding-window, Mixture-of-Experts (MoE — Mixtral, DeepSeek-V3), State-Space Models (Mamba, Mamba-2, Jamba hybrid), linear attention (RWKV, Retentive Networks).
  * **[MIT 6.7960 Week 12 (2024) "Large Language Models" — Jacob Andreas guest lecture]**: **LLM basics**, **prompting**, **In-Context Learning** (zero-shot, few-shot, chain-of-thought — Wei 2022, tree-of-thought, graph-of-thought), **Chain-of-Thought reasoning** ("Let's think step by step", Kojima 2022), **Instruction tuning** (FLAN, T0, InstructGPT), **Self-Consistency**, **Self-Refine**, **Reflexion**.
  * **[MIT 6.7960 Week 15 / RLHF]**: **RLHF pipeline** — SFT → Reward Modelling → PPO; **Reward hacking** and mitigations; **DPO** (Direct Preference Optimisation, Rafailov 2023 — eliminates reward model); **IPO, KTO, ORPO, SimPO, GRPO** (2025); **Constitutional AI** (Anthropic); **RLAIF** (AI feedback); **multi-turn RLHF**.
  * **[MIT 6.3900 / 6.390 Lec_future]**: Frontier topics.
  * **PEFT — parameter-efficient fine-tuning**: **LoRA** (Hu 2021 — low-rank adaptation), **QLoRA** (Dettmers 2023 — 4-bit quantised), **DoRA** (Weight-Decomposed LoRA, 2024), **AdaLoRA**, **IA³**, **prompt tuning**, **prefix tuning**, **P-tuning v2**, **spectrum fine-tuning**.
  * **Quantisation & compression**: Post-training quantisation (PTQ — GPTQ, AWQ, **SmoothQuant**, **SqueezeLLM**), Quantisation-Aware Training (QAT), 1-bit LLMs (BitNet b1.58), pruning (magnitude, structured, Wanda, SparseGPT), knowledge distillation (TinyBERT, DistilLlama).
  * **Retrieval-Augmented Generation (RAG)**: Dense retrievers (DPR, ColBERT v2, BGE, E5, **Voyage-3** 2025), hybrid search (BM25 + dense), vector databases (**pgvector**, **Qdrant**, **Weaviate**, **Milvus**, **LanceDB** 2026), **GraphRAG** (Microsoft 2024), **Agentic RAG**, reranking (Cohere Rerank 3, **Jina Reranker v2**), **HyDE** (Hypothetical Document Embeddings).
  * **Agentic systems**: Tool use / function calling, **ReAct** (Reasoning + Acting), **MCP (Model Context Protocol)** — Anthropic 2024/2025 standard, multi-agent frameworks (**AutoGen** 0.4+, **CrewAI**, **LangGraph**, **OpenAI Swarm/Agents SDK** 2025, **Claude Code**).
  * **Alignment & Safety**: Red-teaming, jailbreaks (AutoDAN, GCG — Universal Transferable Suffixes), **mechanistic interpretability** (Anthropic, Transformer Circuits — induction heads, circuits, **Sparse Autoencoders** for superposition 2024), **activation steering**, **Representation Engineering** (RepE), scalable oversight (debate, recursive reward modelling, weak-to-strong generalisation).
  * **Evaluation**: MMLU, MMLU-Pro, GPQA, MATH, HumanEval, SWE-Bench, ARC-AGI (François Chollet), BIG-Bench Hard, Long-context (RULER, LongBench), **LMSys Arena** (ELO ratings), **Chatbot Arena Hard**, **LiveCodeBench**, **Aider Leaderboard**.
  * **Multi-modality**: Vision-Language Models (LLaVA, GPT-4V, Claude 3.5 Sonnet Vision, **Molmo** 2024, **Pixtral**), audio (Whisper v3, Voice-Mode, **Moshi**), video (Sora, Veo 2, **Runway Gen-3**, **Kling 2.0**).

* **2026 Resources:**
  * **Primary Course Link:** [**Stanford CS336 Spring 2026 “Language Modeling from Scratch”**](https://cs336.stanford.edu/) (Hashimoto · Liang, LIVE 30 Mar 2026 — 17 lectures + 5 assignments covering tokenizer → Transformer → Triton FlashAttention → parallelism → data pipelines → SFT → RLHF/DPO → RLVR) · [CS336 Spring 2025 archive](https://cs336.stanford.edu/spring2025/) + [YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_) · [IITM BSCS3004](https://onlinedegree.iitm.ac.in/) · [Princeton COS 597G](https://www.cs.princeton.edu/courses/archive/fall22/cos597G/) · [**MIT 6.7960 Fall 2025 Week 8‑9, 11–13**](https://deeplearning6-7960.github.io/) (Foundation Model pre‑/post‑training, scaling laws, inference‑time algorithms) · [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/) (free, certified) · [Hugging Face Smol Training Playbook](https://huggingface.co/spaces/HuggingFaceTB/smol-training-playbook) (200+ pages of real training secrets, Oct 2025).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * **_Build a Large Language Model (From Scratch)_** — Sebastian Raschka (Manning 2024) — **do this alongside CS336 Assignment 1**.
    * **_Hands‑On Large Language Models_** — Alammar & Grootendorst (O'Reilly Sep 2024, 428 pp., [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)).
    * **_AI Engineering_** — Chip Huyen (O'Reilly Jan 2025) — the practical engineer's view.
    * **_Speech and Language Processing_ (3rd Edition draft — continually updated through 2026)** — Jurafsky & Martin — [free online](https://web.stanford.edu/~jurafsky/slp3/) (chapters 9‑11 for LLMs, chapter 14 for dialogue).
    * **_Transformers v5_ release notes** — Hugging Face blog ([huggingface.co/blog/transformers-v5](https://huggingface.co/blog/transformers-v5), Dec 2025).
    * **_MCP Specification — 2025‑06‑18 + Nov 2025 anniversary release_** — [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification/2025-06-18).
    * Anthropic Transformer Circuits thread ([transformer-circuits.pub](https://transformer-circuits.pub/)) — mandatory for interpretability.
    * "A Survey of LLMs" (Zhao et al., 2023, updated 2025) — arXiv comprehensive survey.
  * **Practical Implementation:** **Hugging Face `transformers` v5.6+** (April 2026 PyPI), **`datasets` 3.x**, **`accelerate` 1.x**, **`peft` 0.19+** (LoRA/QLoRA/DoRA), **`trl` 1.2+** (SFT, DPO, GRPO, ORPO, KTO, SimPO), **`bitsandbytes` 0.44+**, **`vLLM` 0.19+** (production inference with continuous batching, paged attention, prefix caching), **`SGLang`** (2026 fastest), **`llama.cpp`** + GGUF (CPU inference), **Ollama** / **LM Studio** (local deployment), **LangGraph 1.1+** / **LlamaIndex 0.11+** / **DSPy 3.2+** (2026 prompting frameworks), **`smolagents` 1.24+** + **MCP SDK (Python/TypeScript)** (Anthropic's Nov 2025 standard — used by Claude Desktop, Cursor, VS Code, Zed), **Unsloth** (efficient fine‑tuning, 2× faster), **Marin** / **OLMo 2** / **SmolLM3** open training recipes.

* **🎯 Fine-Tuning Playbook:** Learn the operational trade-offs behind each parameter-efficient fine-tuning method.
  * **When to full-fine-tune vs LoRA vs QLoRA vs DoRA:** cost curves (VRAM, $, wall-clock), quality trade-offs; **LoRA** works for 90% of alignment tasks; **QLoRA** enables 65B on a single 48GB GPU; **DoRA** (Weight-Decomposed LoRA, 2024) closes the full-FT quality gap at LoRA cost.
  * **Frameworks:**
    * [**Unsloth**](https://github.com/unslothai/unsloth) ✅ — 2× faster, 60% less VRAM; drop-in for HF Trainer.
    * [**Axolotl**](https://github.com/axolotl-ai-cloud/axolotl) ✅ — YAML-configured, handles data-prep/packing/sequence-parallel out of the box; the community standard for reproducible open-source fine-tunes.
    * [**TRL**](https://github.com/huggingface/trl) ✅ 1.2+ — SFTTrainer, DPOTrainer, GRPOTrainer, RewardTrainer, ORPOTrainer.
    * [**PEFT**](https://github.com/huggingface/peft) ✅ 0.19+ — LoRA/QLoRA/DoRA/IA³/Prompt Tuning/Prefix Tuning APIs.
  * **Prompt Compilation & DSPy:** [**DSPy**](https://github.com/stanfordnlp/dspy) ✅ 3.2+ — programs-not-prompts, compile signatures with optimisers (BootstrapFewShotWithRandomSearch, MIPROv2, COPRO); [**TextGrad**](https://github.com/zou-group/textgrad) ✅ — differentiate through LLM calls with natural-language gradients.
  * **Inference Optimisation:** [**vLLM 0.19+**](https://docs.vllm.ai/) ✅ (continuous batching, PagedAttention, prefix caching, speculative decoding), [**SGLang**](https://github.com/sgl-project/sglang) ✅ (fastest for structured output and constrained decoding), [**TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) ✅, **speculative decoding** (Medusa, EAGLE, self-speculation), **KV-cache tricks** (prefix caching, chunked prefill, multi-query/grouped-query attention).
  * **Lifecycle Evals (must-know frameworks):**
    * [**promptfoo**](https://github.com/promptfoo/promptfoo) ✅ — declarative YAML evals + CI integration.
    * [**DeepEval**](https://github.com/confident-ai/deepeval) ✅ — pytest-like LLM evals with G-Eval, faithfulness, hallucination metrics.
    * [**Ragas**](https://github.com/explodinggradients/ragas) ✅ — the de-facto RAG evaluation framework.
    * [**OpenAI Evals**](https://github.com/openai/evals) ✅ — Python + YAML spec, works with any endpoint.
    * [**lm-evaluation-harness (EleutherAI)**](https://github.com/EleutherAI/lm-evaluation-harness) ✅ — the canonical open-source harness (MMLU, GSM8K, HellaSwag, BBH, TruthfulQA, HumanEval).
    * [**HF Open LLM Leaderboard**](https://huggingface.co/open-llm-leaderboard) ✅ — the public scoreboard.

* **📦 Module Project (mandatory) — adaptation benchmark:** Compare zero/few-shot prompting with one PEFT method on a bounded task; evaluate quality, cost, latency, safety failures, and reproducibility. **Definition of done:** prompt/data/inference tests, `README`, and results memo. **Production stretch:** containerise evaluation and gate regressions in CI.

---

<a id="module-21"></a>
## Module 21: RAG, Vector DBs & Retrieval Systems

* **The Tutor's "Why":** RAG is the single most-deployed LLM pattern in production (Oct 2025: >70% of enterprise LLM deployments per Menlo Ventures state-of-AI report). Getting chunking + retrieval + reranking right is often the difference between a demo and a product.

* **Strict Prerequisites:** Module 18 (LLMs, tokenisation), Module 11 (embeddings, cosine similarity, PCA/SVD for retrieval concepts), Module 8a (SQL — for metadata filtering and hybrid search).

* **Zero-shot vs RAG vs fine-tuning decision gate:**
  1. Start with **zero/few-shot prompting** when the model already has the knowledge and the problem is instruction, format, or reasoning quality. It is the cheapest baseline and must be evaluated first.
  2. Choose **RAG** when answers must use private, changing, attributable, or access-controlled knowledge. Measure retrieval separately from generation; citations do not prove faithfulness.
  3. Choose **fine-tuning/PEFT** when repeated examples are needed to change behaviour, style, tool selection, output structure, or domain task performance—not merely to inject facts. Keep an untouched evaluation set.
  4. Combine them only when ablations show independent value. Compare quality, latency, cost, security, maintenance, and rollback; do not select a stack because it is fashionable.

* **Exhaustive Topic List:**
  * **Chunking strategies:** fixed-size, **recursive character splitters**, **semantic chunking** (embedding-based), **sentence-window retrieval**, **parent-document retrieval**, **auto-merging retrieval** (LlamaIndex), **late chunking** (Jina 2024 — embed whole doc, chunk embeddings post-hoc), **contextual retrieval** (Anthropic 2024 — LLM prepends context to each chunk before embedding).
  * **Embeddings:** **OpenAI text-embedding-3-large/small**, **Voyage-3-large** (2025 leader on MTEB), **BGE-M3** (BAAI, multilingual + multi-granularity), **Jina v3**, **Nomic Embed v2**, **Cohere Embed v4**, **NV-Embed** (NVIDIA). Learn **MTEB benchmark** (Massive Text Embedding Benchmark).
  * **Hybrid search:** **BM25** + dense (reciprocal rank fusion, RRF), **SPLADE** (sparse neural retrieval), **ColBERT v2 / ColPali** (late interaction — [ColBERT repo](https://github.com/stanford-futuredata/ColBERT) ✅).
  * **Rerankers:** **Cohere Rerank 3**, **BGE-Reranker v2**, **Jina Reranker v2**, **Voyage Rerank**, **Answer.ai RankZephyr / RankGPT**.
  * **Vector databases:** [**pgvector**](https://github.com/pgvector/pgvector) ✅ (Postgres extension, 2026 default for mixed workloads), [**Qdrant**](https://qdrant.tech/) ✅, [**Weaviate**](https://weaviate.io/) ✅, [**Milvus**](https://milvus.io/) ✅, [**LanceDB**](https://lancedb.com/) ✅ (embedded, Lance format), **Chroma**, **FAISS** (Meta, library — not a DB).
  * **Indexing & ANN algorithms:** **HNSW** (Hierarchical Navigable Small World), **IVF** (Inverted File with quantisation — IVF-PQ, IVF-SQ), **DiskANN**, **ScaNN** (Google), trade-offs (build time vs query latency vs recall@k).
  * **RAG patterns:** naive RAG, **Advanced RAG** (pre-retrieval query rewriting, HyDE, query decomposition, multi-query, step-back prompting), **GraphRAG** (Microsoft 2024 — community summaries, entity graphs), **Agentic RAG** (router + multi-tool), **Corrective RAG (CRAG)**, **Self-RAG**, **FLARE**.
  * **Evaluation pipeline:** version a labelled query set; separate retrieval metrics (**nDCG@k, MRR, recall@k**) from generation metrics (**faithfulness, answer relevance, context precision/recall**); add abstention and citation checks; run prompt/RAG regression tests in CI; track latency and cost by slice. **Needle-in-a-Haystack** is a diagnostic, not a product-quality substitute.
  * **Prompt-injection security:** treat retrieved text as untrusted data; test direct and indirect injection, poisoned documents, data exfiltration, malicious links, and instruction collisions. Enforce source ACLs before retrieval, delimit data from instructions, minimise tool privileges, validate outputs, and include adversarial cases in every release gate.

* **2026 Resources:**
  * **Primary Course Link:** [**Pinecone Learning Center**](https://www.pinecone.io/learn/) ✅ (comprehensive free RAG/vector primer) · [**LlamaIndex docs**](https://docs.llamaindex.ai/) ✅ (practical cookbook-driven) · [**LangChain RAG tutorial**](https://python.langchain.com/docs/tutorials/rag/) · [DeepLearning.AI short courses — "Advanced Retrieval for AI" & "Building and Evaluating Advanced RAG"](https://www.deeplearning.ai/).
  * **Required Reading:**
    * Lewis et al. 2020 ("Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks") — the original RAG paper.
    * Anthropic (Sep 2024) "Introducing Contextual Retrieval" — the 2024 enterprise-grade baseline.
    * Microsoft GraphRAG paper (2024).
    * [BGE / FlagEmbedding docs](https://github.com/FlagOpen/FlagEmbedding) — embeddings best practices.
  * **Practical Implementation:** **LlamaIndex 0.11+**, **LangChain 0.3+**, **Haystack 2.x** (deepset), **DSPy 3.2+** (retrieval modules), **pgvector + Postgres 17**, **Qdrant-client 1.17+**, **Ragas**.

* **📋 Mandatory mini-projects:**
  1. **Build a RAG over your own PDFs** — chunking → pgvector → BGE reranker → answer-with-citations; measure Ragas faithfulness & context precision.
  2. **Hybrid search A/B** — BM25-only vs dense-only vs hybrid-with-RRF; measure nDCG@10 on a labelled query set.
  3. **GraphRAG on a technical corpus** — run Microsoft GraphRAG, inspect community summaries, compare against vanilla RAG on multi-hop questions.

---

<a id="module-22"></a>
## Module 22: Agentic AI — LangGraph, CrewAI, MCP & A2A

* **The Tutor's "Why":** 2025 was the "year of the agent" and 2026 is the year of *reliable* agents. Every 2026 senior AI-engineer interview covers LangGraph + MCP + SWE-bench. HuggingFace launched a certified free [Agents Course](https://huggingface.co/learn/agents-course/) specifically to teach this. Closes Gap #4 of the benchmark PDF.

* **Strict Prerequisites:** Module 18 (LLMs, tool-use, function calling), Module 21 (retrieval).

* **Exhaustive Topic List:**
  * **Agent architectures:** ReAct (Reasoning + Acting), **Reflexion** (self-reflection), **Plan-and-Solve**, **Chain-of-Thought with tools**, **Tree-of-Thoughts**, **Graph-of-Thoughts**, **LATS** (Language Agent Tree Search).
  * **Frameworks (open-source):**
    * [**LangGraph**](https://www.langchain.com/langgraph) ✅ 1.1+ — stateful, cyclic, multi-agent graphs; the 2026 production default.
    * [**CrewAI**](https://docs.crewai.com/) ✅ **1.15.5** ([PyPI JSON verified 2026-07-26](https://pypi.org/pypi/crewai/json)) — role-based multi-agent orchestration; use only when multiple explicit roles improve an evaluated workflow.
    * [**smolagents**](https://github.com/huggingface/smolagents) ✅ 1.24+ (Hugging Face) — code-agents that write Python to act; ~1000 LOC.
    * **AutoGen** 0.4+ (Microsoft), **OpenAI Agents SDK** (formerly Swarm, 2025), **Anthropic Claude Agent SDK** (2025).
  * **Model Context Protocol (MCP)** — Anthropic-led open standard (Nov 2024) for LLMs to access tools, resources, and prompts across applications.
    * Base spec: [modelcontextprotocol.io](https://modelcontextprotocol.io/) ✅
    * Spec revisions: [**2025-06-18 spec**](https://modelcontextprotocol.io/specification/2025-06-18) ✅ (structured tool output, resource-based OAuth), **Nov 2025 anniversary release** (code-execution-with-MCP pattern).
    * Implementations: `@modelcontextprotocol/sdk` (Python + TypeScript), [**mcp-servers**](https://github.com/modelcontextprotocol/servers) reference implementations (Filesystem, GitHub, Postgres, Slack, Browser, Google Drive, Sentry). Used in production by Claude Desktop, Cursor, VS Code, Zed, Replit, Sourcegraph Cody, Windsurf.
  * **Agent-to-Agent (A2A) Protocol** — Google's Apr 2025 open standard for cross-platform agent interop (complements MCP: MCP = tool-layer, A2A = agent-layer).
  * **Tooling & Sandboxing:** [**E2B**](https://e2b.dev/) ✅ (cloud sandboxes for code-execution agents), [**Daytona**](https://www.daytona.io/) ✅, [**Modal**](https://modal.com/) ✅ (serverless GPU sandboxes).
  * **Evaluation benchmarks:**
    * [**GAIA**](https://huggingface.co/gaia-benchmark) ✅ — Meta/HF general AI-assistant benchmark (3 levels).
    * [**SWE-bench**](https://www.swebench.com/) ✅ — resolve real GitHub issues; SWE-bench Verified (2024), SWE-bench Multimodal (2025).
    * **τ-bench** (tau-bench, Sierra 2024) — tool-use in realistic customer-service scenarios.
    * **WebArena**, **VisualWebArena** — browser-based agent eval.
    * **BrowseComp** (OpenAI 2025) — hard web-research eval.
  * **Patterns from Anthropic's ["Building Effective Agents"](https://www.anthropic.com/research/building-effective-agents) ✅ (Dec 2024):** workflows (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer) vs true agents (loops with tools). **"Start with prompts, graduate to workflows, only use full agents when you need them."**
  * **Agent security and eval pipeline:** define task-level success, tool-call validity, side-effect budgets, latency/cost, and human-escalation rates; replay a versioned scenario suite in CI. Test direct/indirect prompt injection, confused-deputy attacks, tool-output poisoning, secret/PII exfiltration, excessive agency, and unsafe retries. Use allowlisted tools, least privilege, typed schemas, approval gates for irreversible actions, sandboxing, audit logs, and kill switches.

* **2026 Resources:**
  * **Primary Course (free, certified):** [**Hugging Face AI Agents Course**](https://huggingface.co/learn/agents-course/) ✅ — free, certified, uses smolagents + LangGraph + LlamaIndex; covers MCP integration.
  * **Berkeley LLM Agents MOOC:** [**llmagents-learning.org**](https://llmagents-learning.org/) ✅ (Fall 2024, Advanced Spring 2025) — with speakers including Denny Zhou, Graham Neubig, Jason Weston.
  * **Primary articles:**
    * [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) ✅
    * [OpenAI Cookbook — Agents](https://cookbook.openai.com/topic/agents)
    * [LangChain — "In the Loop" agent series](https://blog.langchain.dev/)
  * **Practical Implementation:** **LangGraph 1.1+**, **CrewAI**, **smolagents 1.24+**, **MCP Python SDK** (`pip install mcp`), **E2B / Modal / Daytona** for sandboxing, **Arize Phoenix / LangSmith / W&B Weave** for tracing (cross-ref to M24).

* **📋 Mandatory mini-projects:**
  1. **Build an MCP server** that exposes a small SQL database; connect it to Claude Desktop or Cursor and run ~10 queries.
  2. **LangGraph multi-agent** researcher that does planning → parallel web-search → synthesis → citation-checking; trace with LangSmith.
  3. **SWE-bench-Lite subset:** run a minimal agent on 5 SWE-bench instances and measure pass@1 vs pass@10.

---

<a id="module-23"></a>
## Module 23: AI Safety, Alignment, Interpretability, Evals & Policy

* **The Tutor's "Why":** No serious 2026 AI/ML role is hired without alignment and safety literacy. MIT AI Safety Forum + Berkeley MIDS + [AISF Alignment Fundamentals](https://aisafetyfundamentals.com/alignment/) ✅ all cover this. Closes Gaps #6, #12, and #13 of the benchmark PDF.

* **Strict Prerequisites:** Module 18 (LLMs, RLHF), Module 22 (agents).

* **Exhaustive Topic List:**
  * **Alignment problem framing:** outer vs inner alignment, specification gaming, reward hacking (Krakovna et al. 2020 taxonomy), mesa-optimisation, goal misgeneralisation (Langosco et al. 2022), deceptive alignment, sycophancy (Sharma et al. Anthropic 2024).
  * **RLHF pathologies & mitigations:** reward-model overoptimisation (Gao et al. 2023 scaling laws for reward hacking), length bias, sycophancy, mode collapse; **Constitutional AI** (Bai 2022), **RLAIF**, **weak-to-strong generalisation** (OpenAI 2023), **scalable oversight** (debate — Irving 2018, recursive reward modelling — Leike 2018, prover-verifier games).
  * **Mechanistic Interpretability:** [**Transformer Circuits thread**](https://transformer-circuits.pub/) ✅ (Anthropic). Core concepts: **features, circuits, motifs**, **induction heads** (Olsson et al. 2022), **superposition** (many features in few neurons), **polysemanticity**, **Sparse Autoencoders (SAEs)** as the 2024-2026 workhorse for recovering monosemantic features — see [**Scaling Monosemanticity** (Templeton et al. 2024)](https://transformer-circuits.pub/2024/scaling-monosemanticity/) ✅ and [**Golden Gate Claude**](https://www.anthropic.com/news/golden-gate-claude) ✅. Extensions: **Crosscoders**, **Transcoders**, **attribution patching**, **path patching**, **activation patching**.
  * **Activation/Representation Engineering:** RepE (Zou et al. 2023), steering vectors, contrastive activation addition (CAA), honesty probes.
  * **Eval harnesses (beyond basic LLM evals):**
    * [**OpenAI evals**](https://github.com/openai/evals) ✅
    * [**lm-evaluation-harness** (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness) ✅
    * [**Inspect** (UK AISI)](https://inspect.ai-safety-institute.org.uk/) — dedicated safety-eval framework.
    * [**HF Open LLM Leaderboard**](https://huggingface.co/open-llm-leaderboard) ✅
    * [**METR evals**](https://metr.org/) — task-duration-based capability evals.
    * Dangerous-capability evals: cyber (Cybench), CBRN, persuasion, agentic autonomy.
  * **Jailbreaks & red-teaming:** GCG (Universal adversarial suffixes, Zou 2023), AutoDAN, PAIR, Crescendo, many-shot jailbreaking (Anthropic 2024), prompt-injection at tool layer.
  * **AI Safety Policy & Regulation (2026):**
    * [**EU AI Act**](https://artificialintelligenceact.eu/) ✅ (fully in force 2 Aug 2026 for GPAI, risk categories, transparency, copyright, datasheets).
    * [**NIST AI RMF 1.0 + GenAI Profile**](https://www.nist.gov/itl/ai-risk-management-framework) ✅ (Jul 2024).
    * [**AI.gov**](https://ai.gov/) ✅ (US federal portal), US Executive Orders 2023/2025, UK AISI, Singapore AI Verify.
    * **ISO/IEC 42001:2023** (AI management system), **ISO 23894** (AI risk), **ISO 42005** (AI impact assessment).
    * **Model cards** (Mitchell et al. 2019), **datasheets for datasets** (Gebru et al. 2021), **system cards** (OpenAI/Anthropic style), **responsible scaling policies** (Anthropic RSP v2.1, OpenAI Preparedness Framework, Google DeepMind Frontier Safety Framework).
  * **Ethics foundations:** dual-use research, **differential privacy** (re-iterated from M24), fairness (DP/EO/Calibration trade-offs, impossibility result — Chouldechova 2017), FAT/FAccT community.

* **2026 Resources:**
  * **Primary Course (free):** [**AI Safety Fundamentals — Alignment Track**](https://aisafetyfundamentals.com/alignment/) ✅ (Bluedot Impact, 12-week curriculum, free facilitated cohorts 3×/year).
  * **Supplementary:** [AISF Governance Track](https://aisafetyfundamentals.com/governance/), [ARENA ML alignment curriculum](https://www.arena.education/), [Neel Nanda — MI study guide](https://www.neelnanda.io/mechanistic-interpretability/getting-started), [**EleutherAI Cookbook**](https://github.com/EleutherAI/cookbook) ✅.
  * **Required Reading:**
    * Amodei et al. 2016 "Concrete Problems in AI Safety" — the canonical problem enumeration.
    * Olah et al. — [Transformer Circuits thread](https://transformer-circuits.pub/) ✅.
    * Hubinger et al. 2019 "Risks from Learned Optimization" (mesa-optimisation).
    * Russell — *Human Compatible* (2019).
    * Christian — *The Alignment Problem* (2020).
    * [Anthropic "Core Views on AI Safety"](https://www.anthropic.com/news/core-views-on-ai-safety) (2023).
  * **Practical Implementation:** **TransformerLens** (Neel Nanda) for mech-interp, **SAELens** for Sparse Autoencoders, **`garak`** (red-teaming LLM scanner), **`pyrit`** (Microsoft AI red-team toolkit), **inspect-ai** (UK AISI evals), **promptfoo / DeepEval** (cross-ref M18).

* **📋 Mandatory mini-projects:**
  1. **Reproduce an induction head** on a 2-layer attention-only toy transformer (from the Transformer Circuits thread).
  2. **Train an SAE** on GPT-2 small activations at one layer; find and label 5 monosemantic features.
  3. **Red-team an open model** using `garak` or hand-crafted GCG suffixes; write a 2-page eval report with model card.
  4. **Draft an EU-AI-Act-compliant model card** for a hypothetical general-purpose AI model.

---

<a id="module-24"></a>
## Module 24: MLOps + LLMOps + AgentOps



* **The Tutor's "Why":** A Jupyter notebook is not a product. The 2026 data scientist must understand the entire lifecycle across three operational tiers: **(1) MLOps** for classical models, **(2) LLMOps** for prompt- and model-driven systems, and **(3) AgentOps** for the new class of stateful, tool-using agents from M22. Harvard's AC215 (new 2024) covers the first tier in depth; the other two are 2024-2026 standards, not yet in any university course.

* **Strict Prerequisites:** Any model from Modules 9-18.

* **Exhaustive Topic List:**
  * **[Harvard AC215 "Advanced Practical Data Science"]**: Containers (Docker, Docker Compose), container orchestration (Kubernetes, KubeFlow, Ray), **data pipelines** (Apache Airflow, Dagster 1.x, Prefect 3.x), **model registries**, **feature stores** (Feast, Tecton), API serving (FastAPI, BentoML, Ray Serve, Modal, Replicate), **A/B testing** (multi-armed bandit deployment, shadow deployment, canary, blue-green), **model monitoring** (data drift — KS test, PSI, JS divergence; concept drift; prediction drift), **observability** (OpenTelemetry, Weights & Biases, Arize, WhyLabs, Evidently).
  * **[IITM BSCS2003 — Modern Application Development I]**: Flask, Vue.js, REST APIs, OAuth, JWT, WebSockets, deployment to Heroku/Vercel/Fly.io.
  * **[IITM BSSE2001/BSSE2002 — Software Engineering & Testing]**: SDLC, agile, scrum, unit/integration/system testing, TDD, BDD, code review, pair programming, version control workflows (git-flow, trunk-based, GitHub Flow), CI/CD (GitHub Actions, GitLab CI, Jenkins).
  * **Experiment tracking & reproducibility**: Weights & Biases, MLflow 2.x, Neptune.ai, DVC (Data Version Control), Hydra for config, Pydantic 2.x for validation.
  * **GPU clusters & distributed training** (see **Stanford CS336 Lec 7–8 “Parallelism”**): Data parallelism (PyTorch DDP, **FSDP2**), tensor parallelism (Megatron‑LM), pipeline parallelism (GPipe, PipeDream), **3D parallelism**, ZeRO (DeepSpeed 1/2/3), **context parallelism** (Ring Attention), communication primitives (AllReduce, NCCL), gradient checkpointing, gradient accumulation, mixed precision (fp16, bf16, **fp8** — H100/H200/B200), **NVIDIA Blackwell (B200)** training (since PyTorch 2.7, April 2025).
  * **Inference optimisation**: TensorRT-LLM, vLLM continuous batching, speculative decoding, **prefix caching**, **chunked prefill**, INT8/INT4 quantisation at inference, KV-cache management.
  * **Responsible AI & governance**:
    * **Fairness metrics** — demographic parity, equalised odds, equal opportunity, calibration within groups; Aequitas, Fairlearn, AIF360.
    * **Explainability** — SHAP, LIME, Captum (for PyTorch), TCAV, counterfactuals (DiCE).
    * **Privacy** — **Differential Privacy** (Dwork 2006 formal definition, ε-δ-DP, Laplace and Gaussian mechanisms, composition theorems, moments accountant, DP-SGD — Abadi 2016), **Federated Learning** (FedAvg, FedProx, personalised FL), **Secure Multi-Party Computation** (SMPC), **Homomorphic Encryption** preview.
    * **Security** — adversarial attacks (M15), **prompt injection**, **data poisoning**, **model stealing / extraction**, **membership inference attacks**.
    * **Regulation (2026)** — **EU AI Act** (fully in force 2 Aug 2026 for GPAI obligations; risk categories, transparency duties, copyright and datasheet requirements), GDPR Art 22 (right to explanation), **ISO/IEC 42001:2023** (AI management), **NIST AI Risk Management Framework 1.0 + GenAI Profile (Jul 2024)**, **UK AI Safety Institute / AISI Inspect** evaluation framework, **US Executive Order on AI** (Biden 2023; Trump admin 2025 rollback + new E.O. on AI competitiveness).
  * **Agents and tool/data plumbing (2026)** — **Model Context Protocol (MCP)** — Anthropic‑led open standard for LLM↔tool/data servers; **2025‑06‑18 spec revision** + **Nov 2025 anniversary release** add structured tool output, resource‑based OAuth auth, code‑execution‑with‑MCP design pattern. Used in production by Claude Desktop, Cursor, VS Code, Zed, Replit, Sourcegraph Cody. Core ecosystem: **`@modelcontextprotocol/sdk`** (Python + TypeScript), `mcp-servers/*` (reference implementations for Filesystem, GitHub, Postgres, Slack, Browser).
  * **[Harvard CS109A · Lec 13 "Ethics"]**: Formal ethics module — fairness, accountability, transparency (FAT/FAccT), **dual-use research**, embedded ethics (Harvard Embedded EthiCS).
  * **[Harvard CS 1810 "Philosophy"]**: "With great power comes great responsibility" — mandatory embedded-ethics lecture.

* **2026 Resources:**
  * **Primary Course Link:** [Harvard AC215 2024](https://harvard-iacs.github.io/2024-AC215/) · [Made With ML](https://madewithml.com/) · [Full Stack Deep Learning](https://fullstackdeeplearning.com/) · [**Hugging Face Agents Course**](https://huggingface.co/learn/agents-course/) (MCP + smolagents, free) · [**MCP docs**](https://modelcontextprotocol.io/) (Nov 2025 spec).
  * **Required Reading (Latest 2026 Editions — verified April 2026):**
    * _Designing Machine Learning Systems_ — Chip Huyen (O'Reilly 2022, still canonical).
    * **_AI Engineering_** — Chip Huyen (O'Reilly **Jan 2025**) — the 2026 successor.
    * _Machine Learning Engineering_ — Andriy Burkov.
    * _Algorithms of Oppression_ — Safiya Umoja Noble.
    * _Weapons of Math Destruction_ — Cathy O'Neil.
    * **EU AI Act consolidated text** (Regulation (EU) 2024/1689) — Annexes III–IV for high‑risk systems.
    * **NIST AI RMF 1.0 + GenAI Profile** ([nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)).
  * **Practical Implementation (MLOps tier):** **Docker 27+** / **Podman 5+**, **Kubernetes 1.32+**, **Terraform 1.9+**, **Pulumi** (modern alternative), **AWS/GCP/Azure SDKs**, **Ray 2.x** (Ray Tune, Ray Serve, Ray Data, RLlib), **vLLM**, **SGLang**, **BentoML**, **SkyPilot** (multi‑cloud), **Modal** (serverless GPU, $30/mo free tier, Stanford CS336 sponsor), **RunPod** / **Lambda** / **Nebius** (B200 access from ~$5/h), **Fairlearn 0.11+**, **AIF360**, **Opacus** (DP for PyTorch), **Flower** (federated learning), **MCP SDK** (Python + TypeScript, `pip install mcp`), **LangFuse** / **Arize Phoenix** (LLM observability), **Weights & Biases Weave** (LLM tracing), **Evidently 0.4+** (drift monitoring).

* **🤖 LLMOps Tier:** Operational practices specific to prompt-driven and LLM-driven systems.
  * **Prompt versioning & CI:** [**Langfuse**](https://langfuse.com/) ✅ (open-source, self-hostable), [**PromptLayer**](https://promptlayer.com/) ✅, [**Helicone**](https://www.helicone.ai/) ✅ (gateway + observability).
  * **Token & cost monitoring:** per-user, per-feature, per-model budgeting; rate-limit backpressure; fallback routing (GPT-4 → Claude → Llama 3); **LiteLLM** proxy, **OpenRouter**, **Portkey**.
  * **Guardrails:** [**NeMo Guardrails** (NVIDIA)](https://github.com/NVIDIA/NeMo-Guardrails) ✅, [**Guardrails AI**](https://www.guardrailsai.com/) ✅, [**Llama Guard / PurpleLlama**](https://github.com/meta-llama/PurpleLlama) ✅ (Meta), **Rebuff** (prompt-injection detection), **Lakera Guard**.
  * **LLM observability & tracing:** [**OpenTelemetry GenAI semantic conventions**](https://opentelemetry.io/docs/specs/semconv/gen-ai/) ✅ (the 2025-2026 standard), **Langfuse traces**, **Honeycomb for AI**, cost & latency dashboards.
  * **Evals in production:** reuse **promptfoo**, **DeepEval**, **Ragas** (M18); **A/B test prompts** as you would models.

* **Minimum Production Bar for Portfolio Projects (mandatory):**
  - **Repository, quality, and reproducibility:** typed `src/` package instead of a loose notebook; pinned environment; formatter/linter/type check; pytest unit and integration tests; deterministic seeds where meaningful; documented data/model/prompt versions.
  - **Delivery:** Dockerfile with non-root runtime and health check; CI runs quality checks, tests, and eval regressions; one real deployment target; secrets are externalised; rollback procedure is rehearsed.
  - **Evidence:** MLflow or W&B for model experiments, or versioned prompt/eval artifacts for LLM systems; architecture diagram; model/system card; README with setup, eval set, results, latency/cost, limitations, and failure cases.
  - **Operations:** structured logs and traces, request/correlation IDs, service-level indicator and target, dashboards/alerts, data/model/prompt drift checks, dependency/security scanning, and a short incident/runbook document.
  - **LLM/agent additions:** prompt-injection tests, source/tool access controls, offline eval gate, production sampling, human escalation, token/cost budgets, sandboxing for code or tools, and a kill switch.

* **🤖 AgentOps Tier:** Operational practices for stateful, tool-using agents (from M22).
  * **Agent tracing & debugging:** [**LangSmith**](https://www.langchain.com/langsmith) ✅, [**Arize Phoenix**](https://github.com/Arize-ai/phoenix) ✅ (open-source OTel-native), [**W&B Weave**](https://wandb.ai/site/weave) ✅, **Helicone Agents**, **Comet Opik**.
  * **Agent eval harnesses (production):** [**GAIA**](https://huggingface.co/gaia-benchmark) ✅, [**SWE-bench**](https://www.swebench.com/) ✅, **τ-bench**, **WebArena** — run these as regression tests.
  * **Sandboxing & isolation:** [**E2B**](https://e2b.dev/) ✅, [**Daytona**](https://www.daytona.io/) ✅, [**Modal**](https://modal.com/) ✅, Firecracker microVMs, gVisor.
  * **Key primary anchors for all three tiers:** [**Full Stack Deep Learning**](https://fullstackdeeplearning.com/) ✅, [**Made With ML** (Goku Mohandas)](https://madewithml.com/) ✅, [**Chip Huyen — *AI Engineering***](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) ✅.

* **📦 Module Project (mandatory) — productionise a prior module:** Choose one model, RAG, or agent project and take it through repository structure, typed code, tests, Docker, CI, tracking/tracing, monitoring, deployment, and rollback documentation. **Definition of done:** every Minimum Production Bar check below passes; the `README` includes architecture, evals, latency/cost, limitations, and a results memo. **Production stretch:** add a load test and operational SLO dashboard.

---

<a id="module-25"></a>
## Module 25: Product DS, Business, Communication & Storytelling

* **The Tutor's "Why":** A senior data scientist must be able to (a) frame a business problem as a measurable DS problem, (b) communicate results to non-technical stakeholders, and (c) drive decisions. Most theory-heavy curricula ignore this; CMU's MSPPM-DA and UMich MADS programs dedicate entire courses to it. Every Meta / Airbnb / Uber / Spotify DS interview has a "product case" loop.

* **Strict Prerequisites:** Module 6½ (A/B testing literacy), any modelling module.

* **Exhaustive Topic List:**
  * **Decision Intelligence framework:** Cassie Kozyrkov's five stages — frame the decision → explore the data → form hypothesis → build the model → make the decision; **cost of being wrong** analysis before modelling.
  * **Metric design:** north-star metrics, input vs output metrics, guardrail metrics, leading vs lagging indicators, **proxy metrics** (and their failures — Campbell's / Goodhart's laws), **OEC** (Overall Evaluation Criterion, Kohavi), product ↔ platform metric trees.
  * **Stakeholder communication:** executive summaries (1-page, BLUF — Bottom Line Up Front), **pyramid principle** (Minto), narrative structuring (situation → complication → question → answer), **SCQA** framework.
  * **Data storytelling & visualisation (cross-ref M7):** Cole Nussbaumer Knaflic's *Storytelling with Data*, [**Ben Shneiderman's "Overview, Zoom & Filter, Details-on-Demand"**](https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf) framework, Edward Tufte's data-ink ratio.
  * **Business framing:** CRISP-DM revisited for 2026, **problem decomposition trees**, **assumption stacks**, **back-of-envelope sizing** (Fermi estimation), TAM/SAM/SOM, unit economics.
  * **Product-DS interview loops:** Meta product-analytics loop, Airbnb "diagnose a drop" question class, case frameworks for growth / engagement / retention / monetisation, A/B-test design under interviews (cross-ref M6½).
  * **Experimentation culture & governance:** experiment review processes, **trustworthy experimentation** (Kohavi's 12 pitfalls), **HiPPO** (Highest-Paid Person's Opinion) management, pre-registration of analysis plans.
  * **Communication artefacts:** **one-pagers**, **tech-spec docs**, **model cards** (cross-ref M23), **PR/FAQ** (Amazon working-backwards), post-launch readouts.
  * **Ethics in product decisions:** dark patterns, informed consent, opt-out vs opt-in, **digital wellbeing** metrics.

* **2026 Resources:**
  * **Primary Anchors (free):**
    * [**Cassie Kozyrkov — Decision Intelligence / Making Better Decisions with AI**](https://www.decisionintelligence.co/) ✅ + her [LinkedIn Learning course](https://www.linkedin.com/learning/instructors/cassie-kozyrkov) ✅ (free via many library programs).
    * **Ron Kohavi** — [exp-platform.com](https://exp-platform.com/) ✅ (industrial A/B testing, shared with M6½).
    * **Erika Hall** — *Just Enough Research* (free chapter; full book Rosenfeld Media 2019).
  * **University programs that teach this rigorously:**
    * [**CMU MSPPM-DA (Heinz College — Master of Science in Public Policy & Management: Data Analytics)**](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) ✅ — policy-DS communication focus.
    * [**UMich School of Information — Master of Applied Data Science (MADS)**](https://www.si.umich.edu/programs/master-applied-data-science) ⚠️ bot-gated for curl but reader-accessible; explicitly teaches storytelling, communication, and stakeholder management in dedicated courses.
    * **Berkeley MIDS W271** (statistical methods for discrete response) + **W241** (experiments) for the methodological side.
  * **Required Reading:**
    * Cole Nussbaumer Knaflic — *Storytelling with Data* (Wiley 2015; *Let's Practice!* 2019).
    * Kohavi, Tang, Xu — [*Trustworthy Online Controlled Experiments*](https://doi.org/10.1017/9781108653985) ✅ (Cambridge 2020) — shared with M6½.
    * Barbara Minto — *The Pyramid Principle*.
    * Edward Tufte — *The Visual Display of Quantitative Information* (2e, 2001).
    * Cathy O'Neil — *Weapons of Math Destruction* (for the ethics layer).
  * **Blogs & newsletters:** [**Decision Intelligence / Decision.AI**](https://decision.ai/), Cassie Kozyrkov's Medium (archive), Amplitude / Mixpanel analytics blogs, [**Locally Optimistic** (analytics engineering community)](https://locallyoptimistic.com/).

* **📋 Mandatory mini-projects:**
  1. **One-page product memo:** Given a ∆-metric scenario (e.g., 7-day retention drops 3 pp), write a one-page memo — framing, root-cause hypotheses, proposed experiments, expected ROI.
  2. **Metric tree exercise:** For a product of your choice (marketplace, social, SaaS, media), construct a 3-level metric tree from north-star to input-level; identify guardrails.
  3. **Stakeholder readout:** Take any modelling project (your own or a Kaggle one); produce a 10-minute executive readout video + 3-page brief targeted at a non-technical VP.

---

<a id="module-26"></a>
## Module 26: Capstone — Research, Systems & Applied Tracks



* **The Tutor's "Why":** Every one of our four reference universities requires a substantial capstone. IITM requires a capstone project; Harvard CS109B culminates in a final project showcase; MIT 6.7960's grade is 35% final project; Cambridge MLMI runs a **4-month research dissertation** from end of Lent Term; Berkeley MIDS runs a client-sponsored capstone. This is the module where you convert a portfolio into a career. **v2026.2 introduces three tracks** so that research-leaning, systems-leaning, and applied-leaning students all have a rubric that matches their intended next step.

* **🎯 Three-Track Capstone Rubric (NEW v2026.2):**

  **Track 1 — Research** *(submit to a workshop; appropriate for PhD-bound / research-engineer roles).*
  - **Goal:** Produce a short paper (4–8 pages) worthy of an arXiv preprint + a NeurIPS / ICML / ICLR workshop submission.
  - **Rubric (100 pts):** Novelty (25) · Rigor — proofs, ablations, baselines (25) · Reproducibility — public repo + seeds + environment (25) · Clarity — writing quality & figures (25).
  - **Cross-reference:** Cambridge MLMI dissertation + MIT 6.7960 final-project blog post (Distill-quality).

  **Track 2 — Systems** *(deploy a production system with SLOs; appropriate for ML-engineer / AI-engineer roles).*
  - **Goal:** A publicly deployed LLM- or ML-driven system with measurable SLOs and an ops runbook.
  - **Rubric (100 pts):** Architecture diagram + tech spec (25) · Evals — promptfoo/Ragas/lm-eval (25) · Latency + cost SLOs met (p50/p95/p99, $/request) (25) · Ops runbook — on-call, rollback, monitoring dashboards (25).
  - **Cross-reference:** Stanford CS336 Assignment 5 (scaling + systems) + Chip Huyen's *AI Engineering* Ch 9–10.

  **Track 3 — Applied** *(real business / sponsored problem with causal evaluation; appropriate for product-DS / senior-DS roles).*
  - **Goal:** Address a real stakeholder's problem with a defensible causal estimate of impact.
  - **Rubric (100 pts):** Problem framing — business → DS translation (25) · Causal validity — identification strategy, sensitivity (25) · Stakeholder communication — one-pager + exec readout (25) · Measured impact — A/B test or quasi-experiment results (25).
  - **Cross-reference:** Berkeley MIDS capstone + CMU MSPPM-DA + IITM BSMS2001P Business Data Management Project.

* **Strict Prerequisites:** All previous modules, or sufficient depth in a chosen specialisation.

* **Exhaustive Topic List:**
  * **[Cambridge MLMI Research Project]**: Substantial research project from end of Lent Term through end of course, leading to **dissertation and poster presentation**. Must be in chosen track area.
  * **[Cambridge MLMI 2022-23 example projects]**: "Disease Subtyping and Biomarker Discovery using High-Dimensional Bayesian Mixture Models with Feature Selection", "Diffusion Models for Peptide Bonding" — demonstrates expected scope.
  * **[MIT 6.7960 Final Project]**: Research blog post format — background, investigation, results, with plots/animations/interactive graphics. Distill-pub standard.
  * **[Harvard CS109A/B Final Project]**: Final Project Showcase with peer evaluations.
  * **[IITM BS Project / MSMS2001P Business Data Management Project]**: Real-world applied project with business stakeholder.
  * **The Capstone Framework (synthesised)**:
    1. **Problem identification** — Novel contribution or improved benchmark. Connect to one of: climate/energy, medicine/bio, education, robotics, finance, public-interest tech.
    2. **Literature review** — Use **Semantic Scholar** + **Connected Papers** + **Elicit** + **OpenReview** for systematic search; maintain **Zotero 7** library.
    3. **Reproducibility package** — Repo with `README.md`, `pyproject.toml` (using `uv`), `data/` (with DVC or HuggingFace datasets), `notebooks/`, `src/` with typed Python, `tests/`, `Dockerfile`, GitHub Actions CI, arXiv paper (LaTeX `acmart` or `NeurIPS`), model card, datasheet for datasets (Gebru et al. 2018).
    4. **Writing** — Follow ICML/NeurIPS/ICLR/JMLR style; include reproducibility checklist; publish blog post on Distill-style platform.
    5. **Dissemination** — Release to arXiv, submit to workshop/conference, present poster, tweet-summary, **HuggingFace model/dataset release**.
  * **Suggested 2026-relevant capstone directions**:
    * Fine-tune a small LLM (<7B) on a domain corpus with **DPO/GRPO**; benchmark vs base.
    * Train a **diffusion model** or **flow-matching** generator on a novel domain.
    * Build an **agentic system** using MCP + an open-source model; evaluate on a task suite.
    * **Mechanistic interpretability** — find circuits in a small transformer using Sparse Autoencoders.
    * **Bayesian deep learning** — variational BNN / Laplace approximation on a scientific dataset.
    * Climate/energy ML — solar forecasting, grid optimisation, satellite-image analysis.
    * Medical ML — with proper IRB/data-use agreement; e.g., MIMIC-IV, UK Biobank.

* **2026 Resources:**
  * **Primary Course Link:** [Cambridge MLMI course structure](https://www.mlmi.eng.cam.ac.uk/about-programme/course-structure) · [MLMI past projects](https://www.mlmi.eng.cam.ac.uk/course-highlights/2022-2023-course-highlights).
  * **Required Reading (Latest 2026 Editions):**
    * _The Craft of Research_ (4th Ed) — Booth, Colomb, Williams.
    * _How to Write a Lot_ — Paul Silvia.
    * _Writing Science_ — Joshua Schimel.
    * ML Reproducibility Checklist — NeurIPS 2019+.
  * **Practical Implementation:** **Zotero 7** + **Better BibTeX**, **Obsidian** or **LogSeq** for research notes, **Typst** or **LaTeX Overleaf** for writing, **Jupyter Book** for interactive docs, **HuggingFace Spaces** for demo deployment, **ArXiv** for preprints, **OpenReview** for submissions.

---

<a id="career-operations"></a>
# Career Operations

Technical study is necessary but not sufficient. Treat the job search as an observable system: take action, collect feedback, adjust the smallest skill gap, and repeat. This operating model is supported by the career-transition evidence in [this practitioner interview](https://www.youtube.com/watch?v=FeQZmQMffzc) and by the live-role sample below.

## The operating doctrine

1. **Use an internal locus of control.** You cannot control hiring cycles, geography, credentials, or a recruiter's response. You can control weekly shipped evidence, applications, outreach, interview practice, and follow-up.
2. **Apply at roughly 70% match.** A job description is a wish list, not an exam specification. Apply when you can prove most core outcomes and can name a credible plan for the rest; do not fabricate experience.
3. **Run targeted cold outreach.** Each week, send 5–10 short notes to practitioners, hiring managers, alumni, maintainers, or local organisations. Ask one specific question, refer to their work, and link one relevant artifact—not a generic request for a referral.
4. **Treat interviews as skill-gap data.** After every screen or loop, record the question class, your confidence, missing evidence, and one remediation task mapped to a module. Rejection is a data point, not an identity verdict.
5. **Build for real people.** Source capstones from a nonprofit, small business, research group, open-source maintainer, civic organisation, or professional community. Agree on a narrow outcome, privacy constraints, and a handoff date.
6. **Create community accountability.** Use a weekly demo group, study cohort, meetup, open-source community, or public build log. Report what shipped, what failed, and next week's smallest deliverable.

> **Timeline reconciliation:** the M1 estimate of **9–12 months** means Python fluency plus enough portfolio evidence to begin competing for entry-level work. A full career transition commonly takes **18–36 months** because it also includes domain knowledge, production depth, interviewing, networking, market timing, and repeated application cycles. Start applying when the 70% bar and portfolio evidence are present; continue the academic path while searching. Neither estimate is a guarantee.

## 2026 role checklist mapped to this roadmap

| Target role | Evidence employers repeatedly requested | Roadmap proof points |
|---|---|---|
| **AI Engineer (Applications)** | Python software engineering; foundation-model APIs; prompting; RAG/vector search; agents/tool calling; eval harnesses; prompt-injection/PII defenses; tracing; Docker/CI/deployment | M1, M7, M8a, M18, M21–M24; ship the cited RAG assistant, an agent eval suite, and the M24 production bar |
| **ML Engineer** | Python; scikit-learn/PyTorch/TensorFlow; end-to-end model ownership; evaluation/experimentation; serving/versioning; CI/CD; Docker/Kubernetes/cloud; observability | M1–M12, M15–M17, M24, M26 Systems; ship a calibrated model API with tracked experiments, SLOs, and rollback |
| **Data Scientist** | SQL; statistics; experimentation and causal inference; Python or R; product metrics; stakeholder communication; reproducible analysis | M5–M10, M12–M14, M25, M26 Applied; ship an experiment or quasi-experiment with a decision memo and executive readout |
| **Data Engineer** | Python and SQL; data modelling; Spark/Flink; Kafka; Airflow/dbt/Prefect; cloud warehouse/lakehouse; CI/CD; quality, governance, and observability | M1, M4, M7, M8a–M8b, M24, M26 Systems; ship a tested batch/streaming platform with lineage, alerts, and runbook |

Use this as a **portfolio checklist, not keyword stuffing**. For each claimed skill, keep a public artifact, test, benchmark, design note, or stakeholder outcome that demonstrates it.

## Live job-posting evidence sample

The checklist above was synthesised from these **12 postings, live-checked on 2026-08-01**. Postings expire, so the audit records the check date and requirements rather than treating any one vacancy as permanent truth.

| Role family | Live postings reviewed | Repeated signal |
|---|---|---|
| AI Engineer | [Healx — Agentic AI Engineer](https://jobs.lever.co/healx/c1dc1b43-066f-427f-a299-0a0b0dc4748f) · [Infinite PL — AI Engineer](https://jobs.lever.co/infinitepl/3ce62a59-7e6c-45d2-a6c0-44a2893dbce1) · [Kobie — AI Engineer](https://jobs.lever.co/kobie/d14582bd-64a2-439e-a7e3-a50ce7270a3d) | LLM APIs, RAG, agents, evals, security, tracing, and production Python |
| ML Engineer | [Bumble — Machine Learning Engineer](https://jobs.lever.co/bumbleinc/51d32f4a-e482-486d-aeab-62924c7c92d7) · [Spear AI — Machine Learning Engineer](https://jobs.lever.co/spear-ai/e8994579-014e-4a11-a407-d50b843aac52) · [PayU — Machine Learning Engineer](https://jobs.lever.co/payugpo/49975338-7270-422e-a3c1-e2375394cef4) | Model ownership, ML frameworks, CI/CD, containers/cloud, serving, evaluation, and observability |
| Data Scientist | [HighLevel — Staff Data Scientist, Experimentation & Causal Inference](https://jobs.lever.co/gohighlevel/0129e5bc-74e4-4f7c-9983-891da20542e8) · [Foodsmart — Staff Data Scientist, Growth Analytics](https://jobs.lever.co/foodsmart/c711b611-ac13-4167-8b60-5c0adb32af26) · [Airalo — Marketing Analytics Lead](https://jobs.lever.co/airalo/7b05ec00-a5a6-4597-ac35-4f6baa64ea92) | SQL, experiments/causal methods, product metrics, Python/R, and stakeholder decisions |
| Data Engineer | [RAVL — Data Engineer](https://jobs.lever.co/ravl_io/9e942ef6-d1c4-4404-84b7-de6cd6c94b21) · [Breakwater Technology — Senior Data Engineer](https://jobs.lever.co/BreakwaterTech/45372c18-b24d-4a36-b05a-06e616b08450) · [SteerBridge — Data Engineer II](https://jobs.lever.co/steerbridge/084800cd-1bae-4b31-b653-da05c521b2d6) | Python/SQL, orchestration, distributed processing, warehouses/lakehouses, quality, and operational ownership |

---

<a id="books"></a>
# 📖 Core Textbook Reading List

<a id="practitioner-shelf"></a>
## Practitioner Shelf

These application-first books **supplement rather than replace** the academic list below. Every print/ebook purchase is optional; use free course material, library access, sample chapters, or the author's public material when cost is a barrier.

| Practitioner title | Verified edition / availability | Best module and track mapping |
|---|---|---|
| [*Automate the Boring Stuff with Python*](https://nostarch.com/automate-boring-stuff-python-3rd-edition) — Al Sweigart | **3rd ed. (2025)**; print ISBN **978-1-7185-0340-3**; optional paid print/ebook, with a [free online edition](https://automatetheboringstuff.com/) | M1; every practitioner track, especially first useful automations |
| [*Software Engineering for Data Scientists*](https://www.oreilly.com/library/view/software-engineering-for/9781098136192/) — Catherine Nelson | **1st ed. (O'Reilly, 2024)**; print ISBN **978-1-098-13620-8**; optional paid/library title; ⚠️ publisher page is bot-gated to automated checks | M1, M7, M24; Data Scientist, ML Engineer, and AI Engineer production habits |
| *The Manga Guide to* [*Statistics*](https://nostarch.com/releases/manga_statistics.html), [*Linear Algebra*](https://nostarch.com/linearalgebra), and [*Calculus*](https://nostarch.com/releases/manga_calculus.html) | English editions in print; ISBNs **978-1-59327-189-3**, **978-1-59327-413-9**, and **978-1-59327-194-7**; all optional paid books | M5, M3, M2; Practitioner Fast Lane intuition pass before the proof track |
| [*The StatQuest Illustrated Guide to Machine Learning* and *The StatQuest Illustrated Guide to Neural Networks and AI*](https://statquest.org/statquest-store/) — Josh Starmer | ML guide **2022**, ISBN **979-8986924007**; NN/AI guide **2025**, ISBN **979-8303440616**; optional paid print books; free StatQuest videos remain the no-cost route | M9–M12 and M15–M18; applied ML and AI Engineer intuition/reference |
| [*Build a Large Language Model (From Scratch)*](https://www.manning.com/books/build-a-large-language-model-from-scratch) — Sebastian Raschka | **Manning, 2024**; ISBN **978-1-63343-716-6**; optional paid print/ebook with publisher sample/code access | M16, M18; model-depth AI Engineer and ML Engineer |
| [*AI Engineering: Building Applications with Foundation Models*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) — Chip Huyen | **1st ed. (O'Reilly, 2025)**; print ISBN **978-1-098-16630-4**; optional paid/library title; ⚠️ publisher page is bot-gated to automated checks | M18, M21–M24; primary shelf text for AI Engineer (Applications) |
| [*Generative AI System Design Interview*](https://bytebytego.com/courses/genai-system-design-interview) — Ali Aminian and Hao Sheng | **ByteByteGo, 2024**; ISBN **978-1-73604-914-3**; optional paid book/course | M21–M24 and Career Operations; AI/ML systems design and interview synthesis |

> **How to use the shelf:** choose at most one application-first book alongside one module's primary academic text. The practitioner book optimises for momentum and patterns; the academic book supplies derivations, assumptions, and research depth.

> **Tier 1 (own a copy)**. These are the books you should have on your shelf, marked-up, for the rest of your career.

| # | Title | Authors | Edition / Year | Primary Modules | Free PDF? |
|---|---|---|---|---|---|
| 1 | _Introduction to Probability_ | Blitzstein & Hwang | 2nd Ed. (2019; 2024 reprint) | M5 | ✅ [stat110](https://projects.iq.harvard.edu/stat110/home) |
| 2 | _Mathematics for Machine Learning_ | Deisenroth, Faisal, Ong | 2020 (2024 reprint) | M2, M3, M5 | ✅ [mml-book.com](https://mml-book.com/) |
| 3 | _An Introduction to Statistical Learning with Python_ (ISLP) | James, Witten, Hastie, Tibshirani, Taylor | 1st Ed. (2023, 2025 reprint) | M6, M9-M12 | ✅ [statlearning.com](https://www.statlearning.com/) |
| 4 | _Elements of Statistical Learning_ (ESL) | Hastie, Tibshirani, Friedman | 2nd Ed., 12th printing | M9-M12 | ✅ [hastie.su.domains](https://hastie.su.domains/ElemStatLearn/) |
| 5 | **_Deep Learning: Foundations and Concepts_** (NEW — primary DL text) | Christopher M. Bishop & Hugh Bishop | **Springer 2024**, 1st Ed., 607 pp., ISBN 978‑3‑031‑45467‑7 | M15‑M16 | ✅ [bishopbook.com](https://bishopbook.com/) |
| 6 | _Probabilistic Machine Learning: An Introduction_ (PML1) | Kevin P. Murphy | MIT Press 2022 | M11-M16 | ✅ [probml.github.io](https://probml.github.io/pml-book/book1.html) |
| 7 | _Probabilistic Machine Learning: Advanced Topics_ (PML2) | Kevin P. Murphy | MIT Press 2023 | M13-M17 | ✅ [probml.github.io](https://probml.github.io/pml-book/book2.html) |
| 8 | _Understanding Deep Learning_ | Simon Prince | MIT Press 2024 | M15-M16 | ✅ [udlbook.github.io](https://udlbook.github.io/udlbook/) |
| 9 | _Dive into Deep Learning_ | Zhang, Lipton, Li, Smola | 2024, continuously updated | M15-M16 | ✅ [d2l.ai](https://d2l.ai/) |
| 10 | _Reinforcement Learning: An Introduction_ | Sutton & Barto | 2nd Ed. 2018 (2024 reprint) | M17 | ✅ [incompleteideas.net](http://incompleteideas.net/book/the-book-2nd.html) |
| 11 | _Bayesian Data Analysis_ (BDA3) | Gelman et al. | 3rd Ed. 2013 (2024 reprint) | M6, M13 | ✅ [stat.columbia.edu](http://www.stat.columbia.edu/~gelman/book/) |
| 12 | _Introduction to Algorithms_ (CLRS) | Cormen, Leiserson, Rivest, Stein | 4th Ed. 2022 | M4 | — |
| 13 | _Introduction to Linear Algebra_ | Gilbert Strang | 6th Ed. 2023 | M3 | — |
| 14 | _Designing Data-Intensive Applications_ | Martin Kleppmann | 1st Ed. 2017 (2nd Ed. coming 2026) | M8, M19 | — |
| 15 | **_Speech and Language Processing_ (3rd Ed. draft, continually updated)** | Jurafsky & Martin | Draft 2024–2026 | M16, M18 | ✅ [stanford.edu/~jurafsky/slp3/](https://web.stanford.edu/~jurafsky/slp3/) |
| 16 | _Foundations of Computer Vision_ | Torralba, Isola, Freeman | **MIT Press 2024** | M15-M16 | ✅ [visionbook.mit.edu](https://visionbook.mit.edu/) |
| 17 | _Designing Machine Learning Systems_ | Chip Huyen | O'Reilly 2022 (2024 reprint) | M19 | — |
| 18 | _Build a Large Language Model (From Scratch)_ | Sebastian Raschka | Manning **2024** | M18 | Partial GitHub mirror |
| 19 | _Python for Data Analysis_ | Wes McKinney | 3rd Ed. 2022 | M7 | ✅ [wesmckinney.com](https://wesmckinney.com/book/) |
| 20 | _Fluent Python_ | Luciano Ramalho | 2nd Ed. 2022 (3rd Ed. in progress) | M1 | — |
| **21** | **_Hands‑On Machine Learning with Scikit‑Learn and PyTorch_** (NEW, **replaces TF edition**) | Aurélien Géron | **O'Reilly, Oct–Dec 2025**, 878 pp. | M9‑M17 | GitHub: [ageron/handson-mlp](https://github.com/ageron/handson-mlp) |
| **22** | **_Hands‑On Large Language Models_** (NEW) | Jay Alammar & Maarten Grootendorst | **O'Reilly, Sep 2024**, 428 pp. | M18 | [HandsOnLLM repo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) |
| **23** | **_AI Engineering_** (NEW) | Chip Huyen | O'Reilly Jan 2025 | M18‑M19 | — |
| **24** | **_Pattern Recognition and Machine Learning_** (PRML — moved to Tier 1‑reference) | Christopher Bishop | 2006 (still in print) | M9‑M17 | — |
| **25** | **_Linear Algebra Done Right_ — 4th Edition (the abstract / proof‑track linear algebra)** | Sheldon Axler | **Springer 2024**, 400 pp., ISBN 978‑3‑031‑41025‑3 | M3 | ✅ [linear.axler.net](https://linear.axler.net/) |
| **26** | **_Introduction to Probability for Data Science_ — bridges Stat 110 to Python code** | Stanley H. Chan | Michigan Publishing **2021/2023**, 700+ pp. | M5 | ✅ [probability4datascience.com](https://probability4datascience.com/) |
| **27** | **_Convex Optimization_** (paired with Stanford EE364A) | Stephen Boyd & Lieven Vandenberghe | Cambridge 2004, **6th printing 2023** | M2, M9‑M11 | ✅ [stanford.edu/~boyd/cvxbook/](https://stanford.edu/~boyd/cvxbook/) |
| **28** | **_Information Theory, Inference, and Learning Algorithms_** | David J. C. MacKay | Cambridge **2003** (the gold-standard intro to entropy/MI) | M5, M16, M18 | ✅ [inference.org.uk/itila](https://archive.org/details/MackayInformationTheoryFreeEbookReleasedByAuthor) |
| **29** | **_High-Dimensional Probability_ — concentration inequalities for ML/statistics** | Roman Vershynin | Cambridge **2018** (free draft online) | M5, M9, M15 | ✅ [vershyn HDP draft](https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.html) |
| **30** | **_Book of Proof_ — proof-writing for first-year university** | Richard Hammack | **3rd Edition, 2018** (CC-BY) | **M0b** | ✅ [richardhammack.github.io/BookOfProof](https://richardhammack.github.io/BookOfProof/) |
| **31** | **_How to Prove It: A Structured Approach_ + *With Lean* (browser-interactive)** | Daniel J. Velleman | Cambridge **3e, 2019** + Lean companion **2024** | **M0b** | Lean: ✅ [djvelleman.github.io/HTPIwL](https://djvelleman.github.io/HTPIwL/) |
| **32** | **_Mathematics for Computer Science_ (MIT 6.042J textbook)** | Lehman, Leighton, Meyer | **2015 final, still current**, MIT Press | **M0b**, M4 | ✅ [OCW PDF](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/) |
| **33** | **_Numerical Linear Algebra_** | Lloyd N. Trefethen & David Bau III | SIAM **1997**, 25th-anniversary printing 2022 | M3, M24 | — |
| **34** | **_Trustworthy Online Controlled Experiments_** (industrial A/B-testing bible) | Ron Kohavi, Diane Tang, Ya Xu | Cambridge **2020** | **M6½**, M25 | — |
| **35** | **_Fundamentals of Data Engineering_** (Gap #2 anchor) | Joe Reis & Matt Housley | O'Reilly **2022** | **M8a, M8b** | — |
| **36** | **_Causal Inference: What If_** (free) | Miguel A. Hernán & James M. Robins | Continuously updated, **2024 revision** | **M6½** | ✅ [Harvard / Hernan What If PDF](https://www.hsph.harvard.edu/miguel-hernan/wp-content/uploads/sites/1268/2024/01/hernanrobins_WhatIf_2jan24.pdf) |
| **37** | **_Causal Inference in Statistics: A Primer_** | Judea Pearl, Madelyn Glymour, Nicholas P. Jewell | Wiley **2016** | **M6½** | — |
| **38** | **_Storytelling with Data_** (+ *Let's Practice!*) | Cole Nussbaumer Knaflic | Wiley 2015 / 2019 | **M25** | — |

> **Tier 2 (reference)**: _All of Statistics_ (Wasserman), _Statistical Inference_ (Casella & Berger), _Bayesian Reasoning and Machine Learning_ (Barber), _Machine Learning: A Probabilistic Perspective_ (Murphy 2012), _Deep Learning_ (Goodfellow/Bengio/Courville 2016), _Algorithms for Decision Making_ (Kochenderfer), _Interpretable Machine Learning_ (Molnar), _Forecasting: Principles and Practice_ (Hyndman 3rd Ed. 2021), _Mining of Massive Datasets_ (Leskovec 3rd Ed. 2020, free at [mmds.org](http://www.mmds.org/)), _The Elements of Statistical Learning_ (ESL — still canonical), **_Active Calculus_** (Boelkins, free 2024), **_Linear Algebra and Learning from Data_** (Strang 2019/25 reprint), **_The Matrix Cookbook_** (Petersen-Pedersen 2024), **_Probability with Martingales_** (Williams 1991, PhD-track), **_Measure, Integral and Probability_** (Capinski-Kopp 2e 2014, PhD-track), **_Tao Analysis I & II_** (Hindustan Book Agency, 4e 2022, real-analysis bridge for PhD-track).

---

<a id="toolchain"></a>
# 🛠️ Production Toolchain

A practical stack mapped to the curriculum. Version numbers below are a dated reference snapshot, not permanent recommendations; check the linked project before installing.

> **Minimum Production Bar:** every serious portfolio repository uses typed package code, automated tests, a reproducible/pinned environment, Docker, CI, experiment or prompt/eval tracking, structured logging/tracing, monitoring with at least one SLI/SLO, a real deployment target, security/eval release gates, and a README containing architecture, results, cost/latency, limitations, and rollback. See [M24](#module-24) for the complete checklist.

| Category | Tool | **Reference snapshot** | Why it matters |
|---|---|---|---|
| **Python runtime** | CPython | **3.13+** (3.14 RC compatible) | Free‑threaded build (PEP 703) in experimental; per‑interpreter GIL for parallel ML workloads |
| **Package manager** | `uv` | **0.11.7** (Apr 2026) | 10‑100× faster than pip/poetry; now the de‑facto standard; replaces `pipenv`/`poetry`/`virtualenv` |
| **Env manager** | `pixi` or `conda` / `mamba` | latest | For non‑Python system deps (CUDA 13, MKL, mamba = fast conda) |
| **IDE** | VS Code + Cursor / Zed | latest | Cursor = AI‑native forks; Zed = Rust‑fast, multiplayer |
| **Notebooks** | Jupyter Lab / `marimo` | Lab 4.x / marimo 0.10+ | marimo = reactive + reproducible notebooks (2026 favourite) |
| **Formatter / Linter** | `ruff` | **0.7+** | One Rust binary replaces Black, isort, flake8, pylint, pyupgrade, autoflake, pydocstyle |
| **Type checker** | `pyright` (or `mypy`) | 1.1.400+ | Gradual typing essential; `pyright` is the 2026 default |
| **DataFrames** | **Polars** + **DuckDB** | **1.40.1 / 1.5.2** | Polars streaming engine 3‑7× faster than in‑memory; DuckDB 1.5 for single-node OLAP |
| **Data validation** | **Pandera** / **Great Expectations** | latest | Schema + quality contracts for pipelines (M7, M8a/b, M24) |
| **Numerical core** | NumPy | **2.2+** | New dtypes (StringDType, variable‑precision); 50% smaller wheel |
| **Classical ML** | scikit-learn | **1.8.0** (Dec 2025) | Native Polars support; `set_output("polars")` on every transformer |
| **Boosting** | XGBoost / LightGBM / CatBoost | 2.x / 4.x / 1.2+ | Still dominant on tabular; XGBoost 2 has GPU hist + vector leaf |
| **Causal Inference** | **DoWhy** / **EconML** / **CausalML** | latest | End-to-end causal workflow (M6½); DoWhy = identify→estimate→refute |
| **Deep Learning** | **PyTorch** | **2.11.0** (23 Mar 2026) | `torch.compile` + FSDP2 + CUDA 13 + Blackwell (B200); TorchTitan for large‑scale |
| **Alt DL** | **JAX** + Flax / Equinox / NNX | **0.10.0** (16 Apr 2026) | TPU‑first; PT/JAX bridge via PyTorch/XLA 2.7; `jax.jit()` decorator‑factory pattern |
| **Bayesian** | NumPyro / PyMC / blackjax | **0.20.1 / 5.28.4 / latest** | JAX‑backed; PyMC 5 uses PyTensor backend |
| **Transformers** | **Hugging Face Transformers** | **v5.6.2** (Apr 2026) | v5 = simplified model definitions; v4.57 LTS = final v4 branch. Works with PyTorch 2.4+. |
| **LLM fine‑tuning** | `trl` + `peft` + **Unsloth** + Axolotl | **TRL 1.2.0 · PEFT 0.19.1** | SFT / DPO / **GRPO** / **RLVR** / KTO / IPO / ORPO / SimPO — one surface |
| **LLM inference** | **vLLM** / **SGLang** / TensorRT-LLM | **0.19.1** / latest | Continuous batching, paged‑attention, prefix caching, **FlashAttention‑3**, speculative decoding |
| **LLM evals** | **promptfoo** / **DeepEval** / **Ragas** / **lm-eval-harness** | latest | M18 fine-tuning playbook + M24 LLMOps |
| **Agents & Tools** | `smolagents` / **LangGraph** / LlamaIndex / CrewAI | **smolagents 1.24.0 · LangGraph 1.1.9 · CrewAI 1.15.5** | **MCP‑native** since v1.0; CrewAI version verified via [PyPI JSON](https://pypi.org/pypi/crewai/json) on 2026-07-26 |
| **MCP** | Anthropic MCP SDK (Py / TS) | 2025‑06‑18 spec + Nov 2025 anniversary | Standard for LLM↔tool/data interoperability |
| **Agent sandboxing** | E2B / Daytona / Modal | latest | Isolated code-execution for agents (M22, M24 AgentOps) |
| **Prompting** | **DSPy** | **3.2.0** (Apr 2026) | Programmatic prompting; optimiser‑driven; 2026 research favourite |
| **Vector DB** | **pgvector** / **Qdrant** / Weaviate / Milvus / LanceDB | **Qdrant-client 1.17.1** | pgvector = Postgres‑native; Qdrant = Rust; LanceDB = arrow‑first |
| **RAG orchestration** | **LlamaIndex** / **LangChain** / Haystack | latest | M21 toolchain; cookbook-driven |
| **MLOps** | **Ray** / **MLflow** / **W&B** | 2.x / **3.11.1** / latest | Ray for scaling / RLlib; MLflow 3 tracking; W&B for research |
| **LLMOps** | **Langfuse** / Helicone / PromptLayer | latest | Prompt versioning + observability (M24 tier) |
| **AgentOps** | **LangSmith** / **Arize Phoenix** / W&B Weave | latest | Agent tracing + replay (M24 tier) |
| **Guardrails** | NeMo Guardrails / Guardrails AI / Llama Guard | latest | Input/output filtering + jailbreak defence (M23, M24) |
| **Interpretability** | **TransformerLens** / SAELens | latest | Mech-interp + sparse autoencoders (M23) |
| **Data Engineering** | **dbt-core** / Airflow / Dagster / Prefect / Kafka / Spark / Flink | **dbt 1.11.8** | M8a/b stack |
| **Containers** | Docker / Podman | 27+ / 5+ | Multi‑arch, rootless, SBOM |
| **Orchestration** | Kubernetes / **Dagster** / Prefect | 1.32+ / 1.x / 3.x | Dagster > Airflow for ML pipelines (asset‑centric) |
| **Serving / demos** | **FastAPI** + BentoML / **Modal** / **Streamlit** | **Streamlit 1.60.0** | APIs for services; Streamlit for portfolio UIs ([PyPI JSON verified 2026-07-26](https://pypi.org/pypi/streamlit/json)), not a substitute for tested service boundaries |
| **Experiment config** | **Hydra** + **Pydantic** | 1.3+ / 2.10+ | Pydantic 2 is 20× faster than v1 |
| **Reproducibility** | DVC + Git LFS | 3.x / latest | Version control for data + models |
| **Writing** | Typst or LaTeX + Zotero 7 | latest | Typst = modern LaTeX alternative, compiles in ms |
| **GPU compute (self‑study)** | Modal · RunPod · Lambda · Nebius · Together | March 2026 prices | B200: Modal $6.25/h · RunPod $4.99/h · Lambda $6.69/h (Stanford CS336 sponsor list) |

---

<a id="progress-tracker"></a>
# ✅ Progress Tracker

> Fork this repo, copy this section, and replace `[ ]` with `[x]` as you complete each sub-module.

### 🚀 Practitioner Fast Lane
- [ ] Chose the 6–9 month practitioner route or documented why I am following the full academic path
- [ ] Completed the M1 four-phase Python plan and shipped the weather CLI/API project
- [ ] Completed intuition-first passes in M0/M2/M3/M5 and recorded which proofs/derivations remain deferred
- [ ] Built NumPy logistic regression, K-Means, and decision tree implementations with parity tests
- [ ] Shipped prompting/RAG/agent/eval work with prompt-injection tests
- [ ] Met the M24 Minimum Production Bar on one deployed project

### 📦 Project completion bar (repeat for every M1–M25 module)
- [ ] Automated tests include the critical path and a failure case
- [ ] `README` documents setup, architecture, usage, results, and limitations
- [ ] Short results memo records evidence, errors, and next steps
- [ ] Added at least one production stretch: Docker, CI, tracking, monitoring, or deployment

### 🩺 Math-Foundations Diagnostic
- [ ] Took the **15-question diagnostic** and recorded my score per strand
- [ ] Decided whether to do **Module 0** (mandatory if any strand < 70%)

### 🟩 Foundation Stratum
- [ ] **Module 0a**: Pre-Calculus & Trigonometry (Khan Academy / MIT 18.01A)
- [ ] **Module 0b**: Logic, Proof & Discrete-Math Primer (Hammack + Velleman + MIT 6.042J; optional: Lean 4 first proof)
- [ ] **Module 1**: Programming Foundations (CS50P + MIT 6.0001/6.0002)
- [ ] **Module 2**: Calculus + Matrix Calculus + Convex Optimisation (MITx 18.01.1/2/3x + 18.02 + **MIT 18.S096/063 Matrix Calc** + **Stanford EE364A Boyd**)
- [ ] **Module 3**: Linear Algebra — Computational + Abstract + Applications (MIT 18.06 + 3Blue1Brown + **Axler 4e 2024** + Townsend 2024 + Trefethen/Bau)
- [ ] **Module 4**: DSA (MIT 6.006 + GaTech series)
- [ ] **Module 5**: Probability + Concentration + Information Theory + Measure Bridge (Stat 110 + MITx 6.431x + **Stanley Chan 2021** + **MacKay 2003** + **Vershynin 2018**)

### 🟨 Core Statistics Stratum
- [ ] **Module 6**: Inference (MITx 18.6501x + STAT 111)
- [ ] **Module 6½**: Causal Inference & Experimentation (Brady Neal + MIT 14.387 + Kohavi + DoWhy)
- [ ] **Module 7**: EDA & Viz (CS109A Lec 1-2, 9, 12-13 + Polars/DuckDB modernisation)
- [ ] **Module 8a**: Databases, SQL & Warehouses (IITM BSCS2001 + Kimball + dbt Learn)
- [ ] **Module 8b**: Distributed Data & Streaming (Stanford CS246 + DataExpert.io + Reis & Housley + Spark + Kafka + Airflow + Iceberg)

### 🟧 Classical ML Stratum
- [ ] **Module 9**: Regression (MIT 6.390 Lec 1-3, CS109A Lec 3-6)
- [ ] **Module 10**: Classification & SVMs + Calibration (MIT 6.390 Lec 4, CS109A Lec 14-15, CS 1810, Cambridge ML&BI + Platt/Isotonic/Temperature scaling)
- [ ] **Module 11**: Unsupervised (CS109A Lec 10, CS109B Lec 1-2, MIT 6.86x Unit 4)
- [ ] **Module 12**: Ensembles (CS109A Lec 16-20)

### 🟦 Probabilistic Stratum
- [ ] **Module 13**: Bayes + MCMC (CS109B Lec 3-7, Cambridge ML&BI, MIT 6.790 Part III; PyMC 5.28 + NumPyro 0.20)
- [ ] **Module 14**: HMMs & Time Series + Foundation Models (Cambridge MLRD Topic 2, MITx 14.310x; + Prophet/TimeGPT/Chronos/Lag-Llama)

### 🟪 Deep Learning Stratum
- [ ] **Module 15**: DL Foundations + JAX/FSDP/Mixed-Precision (CS109B Lec 8–15, MIT 6.390 Lec 5–7, **MIT 6.7960 Fall 2025 W1–4**, **MIT 6.S191 2026**, **Google Scaling Book**)
- [ ] **Module 16**: Transformers + ViT + Diffusion + SSMs + MoE (CS109B Lec 16–23, **MIT 6.7960 Fall 2025 W4‑11**, MIT 6.390 Lec 9, **Stanford CS336 Lec 3–4, 6**; DINOv2/SAM 2/LLaVA/Mamba)
- [ ] **Module 17**: RL + Modern LLM RL (MIT 6.390 Lec 10–11, IITM BSCS3003, **Stanford CS336 Lec 15–17 RLVR**, CleanRL, Berkeley CS285, Spinning Up)

### 🔴 Frontier / Production Stratum
- [ ] **Module 18**: LLMs & Fine-Tuning Playbook (**Stanford CS336 Spring 2026**, IITM BSCS3004, MIT 6.7960 W8–13, **HF Agents Course**, **MCP Nov 2025 spec**, Unsloth/Axolotl/TRL/PEFT/DSPy/vLLM/SGLang)
- [ ] **Module 21**: RAG + Vector DBs (Pinecone Learn + LlamaIndex + pgvector + Qdrant + Ragas)
- [ ] **Module 22**: Agentic AI — LangGraph/CrewAI/MCP/A2A (HF Agents Course + Berkeley LLM Agents + Anthropic Building Effective Agents + GAIA + SWE-bench)
- [ ] **Module 23**: AI Safety + Interpretability + Evals + Policy (AISF Alignment Fundamentals + Transformer Circuits + EU AI Act + NIST AI RMF + inspect-ai)
- [ ] **Module 24**: MLOps + LLMOps + AgentOps (Harvard AC215, Chip Huyen AI Engineering, FSDL, Made With ML, Langfuse/LangSmith/Phoenix/Weave)
- [ ] **Module 25**: Product DS · Communication · Decision Intelligence (Kozyrkov + Kohavi Trustworthy Experiments + Storytelling with Data + CMU MSPPM-DA / UMich MADS)

### 🏆 Capstone Stratum
- [ ] **Module 26**: Capstone Project — Choose **1 of 3 tracks**: Research / Systems / Applied (arXiv preprint + HF release + MCP‑compliant tool/agent OR production system with SLOs OR stakeholder-sponsored applied project with causal evaluation)

### Career Operations
- [ ] Selected one target role and mapped every claimed skill to public evidence
- [ ] Began applying at roughly 70% match without overstating experience
- [ ] Run weekly targeted outreach and community accountability
- [ ] Log interview questions as module-mapped skill-gap data
- [ ] Scoped at least one project for a real person or organisation
- [ ] Reconciled the 9–12 month job-readiness milestone with an 18–36 month transition plan

---

<a id="acknowledgements"></a>
# 🙏 Acknowledgements & Attribution

This curriculum synthesises publicly-available syllabi from:

* **IIT Madras** — [study.iitm.ac.in/ds](https://study.iitm.ac.in/ds/) (BS in Data Science and Applications, 2025–26).
* **Harvard University** — [Harvard CS109A](https://harvard-iacs.github.io/2021-CS109A/pages/schedule.html) and [CS109B](https://harvard-iacs.github.io/2022-CS109B/), [stat110.hsites.harvard.edu](https://stat110.hsites.harvard.edu/) (STAT 110), [harvard-ml-courses.github.io/cs181-web/](https://harvard-ml-courses.github.io/cs181-web/) (CS 1810, Spring 2026), [cs50.harvard.edu/python](https://cs50.harvard.edu/python/) (CS50P).
* **Massachusetts Institute of Technology** — [introml.mit.edu/spring26](https://introml.mit.edu/spring26) (6.390), [gradml.mit.edu](https://gradml.mit.edu/) (6.790), [**deeplearning6-7960.github.io**](https://deeplearning6-7960.github.io/) (6.7960 Fall 2025), [introtodeeplearning.com](https://introtodeeplearning.com/) (6.S191 2026), [micromasters.mit.edu/ds](https://micromasters.mit.edu/ds/) (Statistics & Data Science MicroMasters), [visionbook.mit.edu](https://visionbook.mit.edu/) (Foundations of Computer Vision 2024), [ocw.mit.edu](https://ocw.mit.edu/) (18.01/18.02/18.06/6.0001/6.0002/6.006), [ocw.mit.edu/14-387](https://ocw.mit.edu/courses/14-387-applied-econometrics-mostly-harmless-big-data-fall-2014/) (14.387 Applied Econometrics).
* **University of Cambridge** — [cl.cam.ac.uk/teaching/2526](https://www.cl.cam.ac.uk/teaching/) (Part IA/IB/II), [mlmi.eng.cam.ac.uk](https://www.mlmi.eng.cam.ac.uk/) (MPhil MLMI 2026 entry).
* **Stanford University** — [cs336.stanford.edu](https://cs336.stanford.edu/) (Language Modeling from Scratch, Spring 2026) · [cs246.stanford.edu](https://web.stanford.edu/class/cs246/) (Mining Massive Datasets) · [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/) (SLP 3rd ed. draft) · [web.stanford.edu/class/ee364a](https://web.stanford.edu/class/ee364a/) (Convex Optimization).
* **UC Berkeley** — [ischool.berkeley.edu/courses/datasci/241](https://www.ischool.berkeley.edu/courses/datasci/241) (MIDS Causal Inference — anchor for M6½) · [rail.eecs.berkeley.edu/deeprlcourse](https://rail.eecs.berkeley.edu/deeprlcourse/) (CS285 Deep RL) · [llmagents-learning.org](https://llmagents-learning.org/) (LLM Agents MOOC — anchor for M22).
* **CMU / UMich (Product-DS anchors)** — [heinz.cmu.edu](https://www.heinz.cmu.edu/programs/public-policy-management-master/data-analytics) (MSPPM-DA) · [si.umich.edu](https://www.si.umich.edu/programs/master-applied-data-science) (MADS).
* **Hugging Face** — [huggingface.co/learn](https://huggingface.co/learn) (Agents Course, Smol Course, Smol Training Playbook).
* **Microsoft** — [Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners) and [ML for Beginners](https://github.com/microsoft/ML-For-Beginners), used as project-based companion curricula with quizzes, assignments, and guided lesson navigation.
* **Anthropic / MCP Consortium** — [modelcontextprotocol.io](https://modelcontextprotocol.io/) (Nov 2025 spec) · [transformer-circuits.pub](https://transformer-circuits.pub/) (mechanistic interpretability research).

All university material remains © their respective institutions; this repository only cites and organises publicly‑disclosed syllabi.

---

<div align="center">

**Learn the foundations. Build the systems. Show the work.**

Maintained as a free-first curriculum · [CC BY-SA 4.0](LICENSE.md) · Corrections and resource updates are welcome

</div>
