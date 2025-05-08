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

> **Deliver a production‑ready release candidate (RC‑1) that implements backend‑driven user authentication (signup/login), completes all unfinished MVP epics (including the now‑finished Survival Calculator), and hardens the stack for observability, performance, and maintainability.**  
> RC‑1 must deploy with **one** `docker compose up --build -d` on Ubuntu 24.04, pass CI/CD, and satisfy acceptance criteria from the Project Charter.

---

## 2 · Key Objectives

1. **Backend‑Native Authentication & Account Management**  
   Replace Supabase container with FastAPI‑based signup/login endpoints using JWT; secure `/admin` and user‑scoped routes.
2. **Finalize Remaining Sprint 1 Epics**  
   Ensure Survival Calculator UI (now done), Prediction API, Model Inference & Training endpoints, and CI/CD image push are all production‑grade.
3. **Observability & Performance**  
   Add structured logging, Prometheus metrics, health‑check dashboards; verify model inference p95 < 150 ms.
4. **E2E Testing & QA Hardening**  
   Achieve ≥ 80 % unit‑/integration‑coverage and green nightly Playwright suite.
5. **Documentation & Release Assets**  
   Freeze architecture docs, update all READMEs, and prepare release notes & demo script for Sprint Review.

---

## 3 · Epics & Task Break‑down

### Epic A · CI/CD, Container Registry & GitLab

| ID     | Title                                 | Owner(s) | Est hrs | Acceptance Criteria                                                                       |
| ------ | ------------------------------------- | -------- | ------- | ----------------------------------------------------------------------------------------- |
| **A2** | feat/ci‑cd‑prod‑build (🎯 carry‑over) | Lev      |  6      | Build & push frontend/backend/model images; pipeline blocks on health‑tests; tags `rc‑1`. |
| A3     | chore/auto‑semantic‑versioning        | Lev      |  3      | Conventional‑commits drive version tag; changelog.md auto‑generated.                      |

### Epic B · Frontend (UI / UX)

| ID     | Title                                       | Owner(s)      | Est hrs | Acceptance Criteria                                                                 |
| ------ | ------------------------------------------- | ------------- | ------- | ----------------------------------------------------------------------------------- |
| **B2** | feat/survival‑calculator‑ui (🎯 done)       | Fares, Huraira | 0       | _Completed in Sprint 1._                                                           |
| B4     | feat/signin-up                              | Kazi          |  5      | Signup/login components; form validations; API integration to backend endpoints.    |
| B5     | feat/auth‑hooks & protected‑routes          | Kazi          |  8      | React context + custom hooks for JWT; `/admin` route guarded; session persisted.    |
| B6     | feat/toast‑notifications                    | Kazi          |  3      | Reusable toast component; wired to all success/error responses.                     |

### Epic C · Backend (API)

| ID     | Title                                   | Owner(s)        | Est hrs | Acceptance Criteria                                                                                       |
| ------ | --------------------------------------- | --------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| **C2** | feat/backend‑prediction (🎯 carry‑over) | Denisa, Huraira |  8      | _Completed in Sprint 1._     |
| C4     | feat/auth‑middleware                    | Huraira         |  5      | Extract & verify JWT; enforce `admin` role on `/models/*` and other protected routes.                    |

### Epic D · Model Service

| ID     | Title                                     | Owner(s)  | Est hrs | Acceptance Criteria                                                        |
| ------ | ----------------------------------------- | --------- | ------- | -------------------------------------------------------------------------- |
| **D1** | feat/model‑service‑inference (🎯 carry‑over) | Sameer    |  6      | Load RF model once; `/inference` returns float prob p95 < 150 ms (local).  |
| **D2** | feat/model‑service‑training (🎯 carry‑over)  | Sameer    |  7      | Async background training; persist `.pkl`; accuracy ≥ 0.79; emits progress logs. |
| D3     | chore/model‑registry‑schema               | Lev       |  4      | Alembic migration for `model` & `feature` tables finalized; add FK indexes. |

### Epic E · Backend Authentication & User Schema

| ID     | Title                                        | Owner(s) | Est hrs | Acceptance Criteria                                                             |
| ------ | -------------------------------------------- | -------- | ------- | ------------------------------------------------------------------------------- |
| **E1** | feat/backend‑auth‑implementation             | Kazi     |  8      | FastAPI endpoints for `POST /signup` and `POST /login`; issue JWT; store users in DB. |
| E2     | feat/db‑user‑schema & seed                   | Lev      |  2      | Add `users` table via Alembic; seed admin account in init script.               |

### Epic F · QA, Testing & Docs

| ID | Title                     | Owner(s)     | Est hrs | Acceptance Criteria                                                                   |
| -- | ------------------------- | ------------ | ------- | ------------------------------------------------------------------------------------- |
| F1 | test/unit‑integration‑e2e | Alex, All    | 10      | Frontend RTL, backend pytest, model pytest; Playwright E2E for core flows; coverage ≥ 80 %. |
| F2 | docs/finalize‑rc‑1        | Alex         |  4      | All READMEs & `docs/` updated; architecture diagrams refreshed; sprint review deck ready. |

**Total estimated hrs:** **70** (within sprint capacity)

---

## 4 · Definition of Done (Sprint 2)

* RC‑1 builds & deploys with **zero manual configuration** on Ubuntu 24.04.  
* FastAPI‐driven signup/login work; `/admin` and protected routes require valid JWT.  
* Survival Calculator remains < 150 ms p95 (local).  
* Admin console lists, trains, deletes models via secured API.  
* CI/CD pushes signed images to GitLab registry; nightly E2E green.  
* Coverage ≥ 80 %; docs & diagrams match implementation.  
* All epics closed in GitLab with peer review & green pipeline.

---

## 5 · Workflow & Ceremonies

* **Stand‑ups:** Tue & Fri 16:00 CET · 15–30 min.  
* **Backlog Grooming:** Wed 17:00 CET.  
* **Sprint Review + Retro:** Tue May 20 16:00 CET.

Merge requests require:

* 1 ✔️ peer review · CI green · Issue reference · Conventional commit message.

---

## 6 · Risks & Mitigations

| Risk                         | Likelihood | Impact | Mitigation                                                            |
| ---------------------------- | ---------- | ------ | --------------------------------------------------------------------- |
| Auth‑implementation delays   | M          | H      | Start backend auth spike immediately; fallback to mocked JWT flow.    |
| Model training time > 10 min | M          | M      | Run training async; return immediate 202 and emit progress logs.      |
| Pipeline registry quota      | L          | M      | Retain only last 3 image tags; nightly cleanup job.                   |

---

## 7 · Sprint Review Checklist

* [ ] RC‑1 live demo: signup → login → predict → admin train/delete model.  
* [ ] Performance report: inference latency metrics; health checks pass.  
* [ ] CI/CD dashboard: build, test, deploy stages all green.  
* [ ] Documentation walk‑through: READMEs, diagrams, and release notes.

---

*Prepared by **team/random\_iceberg** · updated May 8 2025*
