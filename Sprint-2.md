# Sprint 2 – Production Hardening & Authentication

**Sprint Duration:** 2 Weeks · **May 6 – May 20 2025**
**Velocity Capacity:** 5 dev‑hrs/week/person × 2 weeks × 7 members = **70 hrs**

| Role                    | Team Member              | Allocation (hrs) |
| ----------------------- | ------------------------ | ---------------- |
| Lead Dev / PM           | **Alex**                 |  10              |
| Full‑stack Dev          | Denisa‑Iulia V. @dv11079 |  10              |
| Full‑stack Dev          | Fares E. @fe18597        |  10              |
| Full‑stack Dev          | Huraira A. @ha06705      |  10              |
| Full‑stack Dev          | Kazi R. @kr09619         |  10              |
| Backend + ML Specialist | Lev M. @lm21363          |  10              |
| Backend + ML Specialist | Sameer K. @sk20179       |  10              |

---

## 1 · Sprint Goal

> **Deliver a production‑ready release candidate (RC‑1) that adds secure user authentication, completes all unfinished MVP epics, and hardens the stack for scalability, maintainability, and performance.**
> RC‑1 must deploy with **one** `docker compose up --build -d` on Ubuntu 24.04, pass CI/CD, and satisfy acceptance criteria from the Project Charter.

---

## 2 · Key Objectives

1. **Integrate Authentication & Account Management**
   Implement email‑based sign‑up/login with Supabase GoTrue; expose typed auth hooks in the frontend and protect admin endpoints.
2. **Finish Incomplete Sprint‑1 Epics**
   Ship the Survival Calculator UI, Prediction API, Model Inference & Training endpoints, and CI/CD pipeline (Docker push).
3. **Observability & Performance**
   Add structured logging, Prometheus metrics, health‑check dashboards, and verify model inference latency < 150 ms (p95).
4. **E2E Testing & QA Hardening**
   Achieve ≥ 80 % unit‑/integration‑coverage and green nightly Playwright suite.
5. **Documentation & Release Assets**
   Freeze the architecture docs, update READMEs, and prepare release notes & demo script for Sprint Review.

---

## 3 · Epics & Task Break‑down

### Epic A · CI/CD, Container Registry & GitLab

| ID     | Title                                 | Owner(s) | Est hrs | Acceptance Criteria                                                                       |
| ------ | ------------------------------------- | ----- | ------- | ----------------------------------------------------------------------------------------- |
| **A2** | feat/ci‑cd‑prod‑build (🎯 carry‑over) | Lev   |  6      | Build & push frontend/backend/model images; pipeline blocks on health‑tests; tags `rc‑1`. |
| A3     | chore/auto‑semantic‑versioning        | Lev   |  3      | Conventional‑commits drive version tag; changelog.md auto‑generated.                      |

### Epic B · Frontend (UI / UX)

| ID     | Title                                       | Owner(s)      | Est hrs | Acceptance Criteria                                                                 |
| ------ | ------------------------------------------- | ------------- | ------- | ----------------------------------------------------------------------------------- |
| **B2** | **feat/survival‑calculator‑ui** (🎯 carry‑over) | Fares, Huraira | 10      | All 8 passenger fields with validation; realtime fetch `/predict`; results shown in card; reset btn; responsive mobile layout. |
| B3     | feat/signin-up                        | Kazi          |  5      | Sign‑up/login lazy components; email magic link; passwordless login; error handling. |
| B5     | feat/auth‑hooks & protected‑routes          | Kazi          |  8      | React context using Supabase JS SDK; `/admin` requires login; session persisted via localStorage.                 |
| B6     | feat/toast‑notifications                    | Denisa        |  3      | Success/error toast component wired to API calls.                                   |

### Epic C · Backend (API)

| ID     | Title                                   | Owner(s)       | Est hrs | Acceptance Criteria                                                                                       |
| ------ | --------------------------------------- | -------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| **C2** | **feat/backend‑prediction** (🎯 carry‑over) | Denisa, Huraira |  8      | `POST /predict/` validates Pydantic; proxies to model service; returns probability; ≥ 95 % unit coverage. |
| C4     | feat/auth‑middleware                    | Huraira        |  5      | JWT from Supabase; admin scope enforcement on `/models/*`.                                                |
| C5     | perf/sql‑alchemy‑pool‑tuning            | Lev            |  3      | Async pool ≥ 20; compatible with pgBouncer.                                                               |

### Epic D · Model Service

| ID     | Title                                     | Owner(s)  | Est hrs | Acceptance Criteria                                                        |
| ------ | ----------------------------------------- | ------ | ------- | -------------------------------------------------------------------------- |
| **D1** | **feat/model‑service‑inference** (🎯 carry‑over) | Sameer |  6      | Load RF model once; `/inference` returns float prob p95 < 150 ms (local).  |
| **D2** | **feat/model‑service‑training** (🎯 carry‑over)  | Sameer |  7      | Async background training; persist `.pkl`; accuracy ≥ 0.79; emits progress logs. |
| D3     | chore/model‑registry‑schema               | Lev    |  4      | Alembic migration for `model` & `feature` tables finalized; add FK indexes.                 |

### Epic E · Auth & DB

| ID     | Title                                        | Owner(s) | Est hrs | Acceptance Criteria                                                             |
| ------ | -------------------------------------------- | ----- | ------- | ------------------------------------------------------------------------------- |
| **E1** | **feat/supabase‑setup‑complete** (🎯 carry‑over) | Lev   |  5      | Supabase runs in compose; password env‑validated; email magic‑link disabled; `users` table audited. |
| E2     | feat/db‑seed‑scripts                         | Lev   |  2      | On first boot, seed admin user & features via `/docker-entrypoint-initdb.d`.    |

### Epic F · QA, Testing & Docs

| ID | Title                     | Owner(s)     | Est hrs | Acceptance Criteria                                                                   |
| -- | ------------------------- | --------- | ------- | ------------------------------------------------------------------------------------- |
| F1 | test/unit‑integration‑e2e | Alex, All | 10      | Frontend RTL, backend pytest, model pytest; PlaywrightE2E for happy‑path; coverage ≥ 80 %.   |
| F2 | docs/finalize‑rc‑1        | Alex      |  4      | READMEs & `docs/` updated; architecture diagram refreshed; sprint review deck skeleton ready. |

**Total estimated hrs:** **70** (within sprint capacity)

---

## 4 · Definition of Done (Sprint 2)

* RC‑1 builds & deploys with **zero manual configuration** on Ubuntu 24.04.
* Email sign‑up/login works; `/admin` requires authentication.
* Survival Calculator delivers predictions < 150 ms p95 (localhost).
* Admin console lists, trains, deletes models via secured API.
* CI/CD pushes signed images to GitLab registry; nightly E2E green.
* Coverage ≥ 80 %; docs & diagrams match implementation.
* All epics above closed in GitLab with peer‑review & green pipeline.

---

## 5 · Workflow & Ceremonies

* **Stand‑ups:** Tue & Fri 16:00 CET · 15-30 min.
* **Backlog Grooming:** Wed 17:00 CET.
* **Sprint Review + Retro:** Tue May 20 16:00 CET.

Merge requests require:

* 1 ✔️ peer review · CI green · Issue reference · Conventional commit message.

---

## 6 · Risks & Mitigations

| Risk                         | Likelihood | Impact | Mitigation                                                            |
| ---------------------------- | ---------- | ------ | --------------------------------------------------------------------- |
| Supabase auth config delays  | M          | H      | Lev to spike early; fallback to JWT mock if blocked.                  |
| Model training time > 10 min | M          | M      | Run training async in background; return progress; add timeout guard. |
| Pipeline registry quota      | L          | M      | Retain only last 3 image tags; nightly cleanup job.                   |

---

## 7 · Sprint Review Checklist

* [ ] RC‑1 live demo: sign‑up → predict → admin train/delete model.
* [ ] Performance report: inference latency, DB connection pool stats.
* [ ] CI/CD dashboard: build, test, deploy stages all green.
* [ ] Documentation walk‑through.

---

*Prepared by **team/random\_iceberg** · updated May 6 2025*
