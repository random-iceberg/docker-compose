---
title: Sprint 2 – Production Hardening & Authentication (RC-1)
revision: v2-final · 08 May 2025
---

> **Context**  
> *Sprint 1 delivered a containerised MVP that demos live predictions and basic
> model management, but is still running in “open‐house” mode with placeholder
> ML code, no user accounts, and minimal observability.  
> Sprint 2 converts the MVP into a **Release Candidate 1** (RC-1) that anyone
> can deploy with a single `docker compose up --build -d` and use securely in
> production.*

---

## 1 · Sprint time-box & velocity

| - Role - | Member | Allocation<sub>hrs/2 w</sub> |
| -------- | ------ | ----------------------------- |
| **Lead Dev / PM** | **Alex** | 10 |
| Full-stack Dev | Denisa @dv11079 | 10 |
| Full-stack Dev | Fares @fe18597 | 10 |
| Full-stack Dev | Huraira @ha06705 | 10 |
| Full-stack Dev | Kazi @kr09619 | 15 |
| Back-end & ML | Lev @lm21363 | 10 |
| Back-end & ML | Sameer @sk20179 | 10 |

*Capacity = **75 h** (5 h above nominal 70 h, absorbed by Kazi’s extra time).*

**Sprint window** 08 May → 22 May 2025 (10 calendar days, 2 full working weeks)  

---

## 2 · Sprint Goal (definition of success)

> Deliver **RC-1** that  
> 1️. authenticates real users (JWT) and locks down admin/model routes,  
> 2️. completes inference + training flows with persisted models,  
> 3️. ships full CI/CD (build → test → push-to-registry → compose-up smoke-test),  
> 4️. exposes health & Prometheus metrics for every service, and  
> 5️. passes automated unit + integration + Playwright E2E suites (≥ 80 % cov).  

The stack must spin up on **Ubuntu 24.04** with **zero manual config**, meet all
project requirements, and be demo-ready for stakeholders.

---

## 3 · High-level objectives

1. **Secure the platform** – add signup / login, hashed passwords, JWT middleware, and route-level RBAC (`admin`, `user`, `anon`).
2. **Finish model micro-service** – fast inference (< 150 ms p95 locally) and asynchronous training with Scikit-learn RF/SVM persisted under `/models`.
3. **CI/CD hardening** – semantic-versioned image tags, container registry
   pruning, and a one-shot “spin-up → smoke-test” stage that blocks merge.
4. **Observability & performance** – structured JSON logs, `/metrics`
   (Prometheus) & `/health` endpoints, Grafana dashboard bundle.
5. **Front-end polish** – protected routes, auth context, persistent tokens,
   toast notifications, and UX tweaks from Sprint-1 retro.
6. **Quality Gate** – unit + integration coverage ≥ 80 % (Back-end, Model, FE);
   green nightly Playwright run against Compose.
7. **Docs** – freeze architecture diagrams and publish RC-1 deployment guide.

---

## 4 · Work-break-down structure

### Epic A · CI/CD & container registry

| ID | Task | Owner | Est h | Acceptance-criteria |
|----|------|-------|-------|---------------------|
| **A1** | **`feat/ci-pipeline-prod-build`** (⚠ carry-over) | Lev | 6 | GitLab pipeline builds & pushes signed images (`frontend`,`backend`,`model`) on **every** commit; tag pattern `v<semver>`; fails on health-check. |
| A3 | `chore/semantic-changelog` | Lev | 3 | Conventional‐commit → automatic CHANGELOG.md & Git tag; keep only last **3** RC images. |

### Epic B · Authentication (FE + BE)

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| **B4** | **`feat/backend-auth-core`** | Kazi | 6 | FastAPI endpoints `POST /signup`, `/login` (bcrypt, JWT 1 h TTL); proper 409/401 errors. |
| B5 | `feat/db-user-schema` | Lev | 2 | Alembic migration adds `user(id, email, pw_hash, role, created_at)`; seeds admin user from env. |
| B6 | `feat/jwt-middleware-rbac` | Huraira | 4 | Dependency that verifies JWT & injects `user.role`; 403 on protected routes if insufficient. |
| B7 | `feat/frontend-auth-hooks` | Kazi | 8 | React context storing JWT + refresh; guards `/admin` & model CRUD routes; persists in `localStorage`. |
| B8 | `feat/toast-notifications` | Lev | 3 | Reusable Tailwind toast; used for login/logout, errors, success. |

### Epic C · Back-end API upgrades

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| C3 | `feat/prometheus-metrics` | Fares | 4 | `fastapi_prometheus` middleware; metrics at `/metrics`; instrument inference latency & HTTP codes. |
| C4 | `feat/structured-logging` | Denisa | 3 | `loguru` JSON logs; log correlation ID from JWT. |

### Epic D · Model micro-service

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| **D1** | **`feat/inference-endpoint`** (⚠ carry-over) | Sameer | 6 | Loads RF at startup, `/inference` returns `{"prob": float,"survived": bool}`; p95 < 150 ms (loc). |
| **D2** | **`feat/training-endpoint`** (⚠ carry-over) | Sameer | 7 | `/training` accepts JSON `{algorithm,features,name}`; async task trains, persists `.pkl`, updates Postgres (`model` & link table); returns `202 Accepted {job_id}`. |
| D3 | `chore/model-registry-migration` | Lev | 4 | Finish `model`,`feature`,`model_feature_link` migrations; add index on `(uuid)` and FK cascades. |

### Epic F · Front-end polish

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| F1 | `ui/calculator-validation-tweaks` | Denisa | 4 | Inline validation messages; numeric spinners; mobile layout gap fixes. |
| F2 | `ui/admin-table-pagination` | Kazi | 2 | Show 10 models / page, client-side pagination. |

### Epic G · Testing & Quality Gate

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| G1 | `test/backend-auth-coverage` | Alex | 4 | pytest for signup/login, RBAC, 100 % branch on auth module. |
| G2 | `test/model-service` | Sameer | 3 | pytest on inference happy-path & invalid input. |
| G3 | `test/playwright-e2e` | Alex + FE team | 6 | Login → predict → admin train/delete flow; run headless in CI; store artefacts on failure. |
| G4 | `ci/coverage-gate` | Lev | 2 | Pipeline fails if global cov < 80 %. |

### Epic H · Documentation & Release

| ID | Task | Owner | Est h | Acceptance criteria |
|----|------|-------|-------|---------------------|
| H1 | `docs/architecture-update` | Alex | 3 | Update Mermaid diagram (`docs/Project-Charter.md`, section 5). |
| H2 | `docs/rc1-deployment-guide` | Alex | 1 | Step-by-step: clone → `git submodule update --init --recursive` → `docker compose up --build -d`. |
| H3 | `slide-deck-sprint2-review` | All | 2 | 10-min demo script + 3 key metrics slides. |

*Total planned effort = **75 h** (matches capacity).*

---

## 5 · Definition of Done (DoD for RC-1)

| Area | DoD criterion |
|------|---------------|
| **Deployment** | Fresh Ubuntu 24.04 VM → `docker compose up --build -d` → all containers healthy; FE at <http://localhost:8080>. |
| **Security** | Signup/login issues JWT; `/admin/*`, `/models/*`, `/training/*` require `role=admin`; password hashed with bcrypt&nbsp;12. |
| **Model** | RF & SVM pickles stored in volume `model-artifacts`; inference p95 < 150 ms; training job persists metadata and returns accuracy. |
| **Observability** | `/metrics` exposed on each service; Grafana dashboard `services_overview.json` committed in `docs/`. |
| **Quality** | Unit + integration coverage ≥ 80 %; nightly Playwright suite green; pipeline blocks on regression. |
| **CI/CD** | Images tagged `vX.Y.Z[-rcN]`; pushed to GitLab Container Registry; “smoke-up” stage runs `docker compose up` inside CI and hits `/health`. |
| **Docs** | All READMEs and `docs/` sections accurate; architecture diagram dated **22 May 2025**; CHANGELOG lists RC-1. |

---

## 6 · Risks & mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|-----------|
| Auth scope creep (refresh tokens, password reset) | M | M | Ship **MVP auth** (JWT + bcrypt) only; backlog extras for Sprint 3. |
| Training job exceeds CI time-outs | M | H | Run training **async**; CI only unit-tests training pipeline; nightly job does full train. |
| Image registry quota exceeded | L | M | Retain last 3 RC images; cron cleanup (`registry-retention.yml`). |
| Metric stack adds memory overhead | L | L | Use `prom/prometheus:v2-alpine`, scrap every 30 s; set 256 MiB limit. |

---

## 7 · Ceremonies

* **Stand-ups:** Tue + Fri 16 : 00 CEST (15 min)  
* **Backlog refinement:** Wed 17 : 00 CEST  
* **Sprint review + retro:** Thu 22 May 16 : 00 CEST

Merge policy: ≥ 1 peer LGTM + green CI + linked issue + conventional commit.

---

## 8 · Sprint-review checklist

- [ ] Live demo (sign-up → login → predict → admin train/delete).  
- [ ] Metrics dashboard shows <150 ms inference & <5 % error-rate.  
- [ ] CI pipeline summary: build, test, publish, smoke-up all green.  
- [ ] CHANGELOG & docs updated → tag **`v0.9.0-rc1`**.  

---

*Prepared by **team/random_iceberg** · Approved 08 May 2025*
