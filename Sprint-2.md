---
title: Sprint 2 – Production Hardening & Authentication (RC-1)
revision: v3-final · 09 May 2025
---

> **Context**  
> *Sprint 1 delivered a containerised MVP that demos live predictions and basic  
> model management, but is still running in “open-house” mode with placeholder  
> ML code, no user accounts, and minimal observability.  
> Sprint 2 converts the MVP into a **Release Candidate 1** (RC-1) that anyone  
> can deploy with a single `docker compose up --build -d` and use securely in  
> production.*

---

## 1 · Sprint time-box & velocity

| Role                   | Member           | Allocation (hrs/3 w) |
|------------------------|------------------|----------------------|
| **Lead Dev / PM**      | **Alex**         | 15                   |
| Full-stack Dev         | Denisa @dv11079  | 15                   |
| Full-stack Dev         | Fares @fe18597   | 15                   |
| Full-stack Dev         | Huraira @ha06705 | 15                   |
| Full-stack Dev         | Kazi @kr09619    | 15                   |
| Back-end & ML          | Lev @lm21363     | 15                   |
| Back-end & ML          | Sameer @sk20179  | 15                   |

*Capacity = **105 h** (7 members × 5 h/week × 3 weeks).*

**Sprint window** 08 May → 29 May 2025 (3 weeks)

---

## 2 · Sprint Goal (definition of success)

Deliver **RC-1** that:
1. Authenticates real users (JWT) and locks down admin/model routes,
2. Completes inference + training flows with persisted models,
3. Ships full CI/CD (build → test → push-to-registry → compose-up smoke-test),
4. Exposes health & Prometheus metrics for every service,
5. Passes automated unit + integration + Playwright E2E suites (≥ 80 % cov).

The stack must spin up on **Ubuntu 24.04** with zero manual config, meet all
project requirements, and be demo-ready for stakeholders.

---

## 3 · High-level objectives

1. **Secure the platform** – signup/login, bcrypt-hashed passwords, JWT middleware, RBAC (~admin~, ~user~, ~anon~).
2. **Finish model micro-service** – fast inference (< 150 ms p95 locally) and async training with scikit-learn RF/SVM persisted under `/models`.
3. **CI/CD hardening** – semantic-versioned image tags, container registry pruning, and a one-shot “spin-up → smoke-test” stage that blocks merge.
4. **Observability & performance** – structured JSON logs, `/metrics` (Prometheus) & `/health` endpoints, Grafana dashboard bundle.
5. **Front-end polish** – protected routes, AuthContext, persistent tokens, toast notifications, and UX tweaks from Sprint-1 retro.
6. **Quality Gate** – unit + integration coverage ≥ 80 % (Back-end, Model, FE); green nightly Playwright run against Compose.
7. **Docs** – freeze architecture diagrams and publish RC-1 deployment guide.

---

## 4 · Work-break-down structure

### Epic A · CI/CD & container registry

| ID   | Task                                           | Owner | Est h | Acceptance-criteria                                                                                       |
|------|------------------------------------------------|-------|-------|-----------------------------------------------------------------------------------------------------------|
| **A1** | `feat/ci-pipeline-prod-build` (carry-over)  | Lev   | 6     | Builds & pushes images for frontend, backend, model on every commit; tags `v<semver>`; health-checks pass. |
| **A3** | `feat/ci-unit-e2e-integration`              | Lev   | 6     | CI stages for unit tests and Playwright E2E; pipeline blocks on failures; publishes results.              |

### Epic B · Authentication (FE + BE)

| ID   | Task                                        | Owner | Est h | Acceptance-criteria                                                                                                                       |
|------|---------------------------------------------|-------|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| **B4** | `feat/backend-auth-core`                  | Kazi  | 6     | FastAPI `POST /signup` & `/login` with bcrypt + JWT (1 h TTL); 409 on duplicate, 401 on bad creds.                                          |
| **B5** | `feat/db-user-schema`                     | Lev   | 2     | Alembic migration for `users` table (id, email, pw_hash, role, created_at); seeds admin from env vars.                                      |
| **B6** | `feat/jwt-middleware-rbac`                 | Huraira | 4   | JWT verification dependency; injects `user.role`; 403 on insufficient role for protected routes.                                            |
| **B7** | `feat/frontend-auth-hooks`                 | Kazi  | 8     | React AuthContext with JWT + refresh logic; guards `/admin` & model routes; persists token in HttpOnly cookie.                              |
| **B8** | `feat/frontend-refresh-token`              | Kazi  | 2     | Implement refresh-token endpoint `/token/refresh`; HttpOnly secure cookies; auto-refresh logic in AuthContext.                               |

### Epic C · Back-end API upgrades

| ID   | Task                                           | Owner | Est h | Acceptance-criteria                                                                                                      |
|------|------------------------------------------------|-------|-------|--------------------------------------------------------------------------------------------------------------------------|
| **C3** | `test/backend-integration-tests`             | Fares | 4     | Pytest integration tests for core backend endpoints; all defined scenarios (success + error) pass.                      |
| **C4** | `feat/structured-logging`                    | Denisa| 3     | JSON-formatted logs (via loguru); include timestamp, level, module, correlation_id from JWT.                            |
| **C5** | `feat/backend-error-handler`                 | Denisa| 3     | Centralised error-handler middleware returning consistent JSON `{ detail, message }` with correct HTTP status codes.   |
| **C6** | `feat/backend-prediction-history`            | Fares | 3     | `GET /predictions/history` returns last 10 predictions for authenticated users; includes timestamp and result.           |

### Epic D · Model micro-service

| ID   | Task                                           | Owner  | Est h | Acceptance-criteria                                                                                             |
|------|------------------------------------------------|--------|-------|---------------------------------------------------------------------------------------------------------------|
| **D1** | `feat/inference-endpoint` (carry-over)       | Sameer | 6     | Load RF at startup; `/inference` returns `{"probability":float,"survived":bool}`; p95 < 150 ms locally.      |
| **D2** | `feat/training-endpoint` (carry-over)        | Sameer | 7     | `/training` accepts `{algorithm,features,name}`; async retrain, persists `.pkl`, updates Postgres; 202 Accepted. |
| **D3** | `chore/model-registry-migration`             | Lev    | 4     | Complete migrations for `model`, `feature`, `model_feature_link`; enforce index on `uuid`; FK `ON DELETE CASCADE`.            |

### Epic F · Front-end integration & polish

| ID   | Task                                         | Owner   | Est h | Acceptance-criteria                                                                                                    |
|------|----------------------------------------------|---------|-------|------------------------------------------------------------------------------------------------------------------------|
| **F1** | `ui/calculator-validation-tweaks`         | Denisa  | 4     | Inline validation messages; HTML5 number constraints; mobile spacing fixes.                                            |
| **F2** | `test/frontend-integration-tests`          | Fares   | 4     | Playwright/Cypress integration tests for core UI flows (landing, calculator, admin) based on slides & project requirements. |
| **F3** | `refac/code-cleanup`                       | Huraira | 6     | Refactor FE & BE for reusable components, consistent styling, production-ready structure, full mobile/desktop responsiveness.         |
| **F4** | `chore/reusable-component-library`         | Huraira | 2     | Extract shared UI components (buttons, cards, toasts) into a common library; update imports.                          |
| **F5** | `ui/prediction-history-component`          | Denisa  | 3     | Add Prediction History view showing last 10 predictions in a table, accessible on user dashboard.                      |
| **F6** | `ui/social-sharing-buttons`                | Kazi    | 2     | Add Facebook, Twitter, LinkedIn share buttons on landing page; open share dialog with prefilled text in new window.  |

### Epic G · Testing & Quality Gate

| ID   | Task                                | Owner  | Est h | Acceptance-criteria                                                                 |
|------|-------------------------------------|--------|-------|-------------------------------------------------------------------------------------|
| **G1** | `test/backend-auth-coverage`      | Huraira| 4     | Pytest for signup/login & RBAC; 100 % branch coverage on auth module.               |
| **G2** | `test/model-service`              | Sameer | 3     | Pytest inference + error cases; coverage ≥ 80 % on model endpoints.                 |
| **G3** | `test/playwright-e2e`             | Lev    | 6     | Login → predict → admin train/delete flow; headless in CI; artifacts on failure.   |
| **G4** | `ci/coverage-gate`                | Lev    | 2     | Pipeline fails if overall coverage < 80 %; badge reflects status.                   |

### Epic H · Documentation & Release

| ID   | Task                                    | Owner | Est h | Acceptance-criteria                                                                                          |
|------|-----------------------------------------|-------|-------|---------------------------------------------------------------------------------------------------------------|
| **H1** | `docs/architecture-update`            | Alex  | 3     | Refresh Mermaid diagram in `docs/Project-Charter.md` (section 5) to reflect RC-1 architecture.               |
| **H2** | `docs/rc1-deployment-guide`           | Alex  | 1     | Clear steps: clone → `git submodule update --init --recursive` → `docker compose up --build -d`.             |
| **H3** | `pull-request-review`                 | Alex  | 5     | Review all PRs for Sprint 2; ensure each links to and closes an issue per convention.                         |
| **H4** | `docs/metrics-setup-guide`            | Alex  | 3     | Document `/metrics` endpoint usage and Grafana dashboard import steps; add to root `docs/README.md`.         |

*Total planned effort = **104 h** (under capacity 105 h, leaving ~1 h buffer).*

---

## 5 · Definition of Done (RC-1)

| Area             | DoD criterion                                                                                                                                   |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Deployment**   | Fresh Ubuntu 24.04 VM → `docker compose up --build -d` → all services healthy; FE at <http://localhost:8080>.                                     |
| **Security**     | `POST /signup` & `/login` issue JWT; `/admin/*`, `/models/*`, `/training/*` require `role=admin`; passwords bcrypt 12.                         |
| **Model**        | RF & SVM pickles stored in volume `model-artifacts`; inference p95 < 150 ms; training job persists metadata, returns accuracy.                   |
| **Observability**| `/metrics` exposed on each service; Grafana dashboard `services_overview.json` committed in `docs/`.                                             |
| **Quality**      | Unit + integration coverage ≥ 80 %; nightly Playwright suite green; pipeline blocks on regressions.                                              |
| **CI/CD**        | Images tagged `vX.Y.Z[-rcN]`; pushed to GitLab Registry; “smoke-up” stage runs `docker compose up` in CI and hits `/health`.                       |
| **Docs**         | All READMEs and `docs/` content accurate; architecture diagram dated **29 May 2025**; CHANGELOG lists RC-1.                                       |

---

## 6 · Risks & mitigation

| Risk                                      | Likelihood | Impact | Mitigation                                                           |
|-------------------------------------------|------------|--------|----------------------------------------------------------------------|
| Auth scope creep (refresh tokens, resets) | Medium     | Medium | Ship MVP auth (JWT + bcrypt) only; defer extras to Sprint 3.         |
| Training job exceeds CI time-outs        | Medium     | High   | Run training async; CI only unit-test; nightly job runs full train. |
| Registry quota exceeded                   | Low        | Medium | Prune old RC images; keep last 3; schedule cleanup.                  |
| Metrics stack memory overhead             | Low        | Low    | Use alpine Prometheus; scrape every 30 s; cap at 256 MiB.            |

---

## 7 · Ceremonies

- **Stand-ups:** Tue + Fri 16:00 CEST (15 min)  
- **Backlog refinement:** Wed 17:00 CEST  
- **Sprint review + retro:** Fri 29 May 16:00 CEST  

**Merge policy:** ≥ 1 peer LGTM + green CI + linked issue + conventional commit.

---

## 8 · Sprint-review checklist

- [ ] Live demo (sign-up → login → predict → admin train/delete).  
- [ ] Metrics dashboard shows < 150 ms inference & < 5 % error-rate.  
- [ ] CI pipeline summary: build, test, publish, smoke-up all green.  
- [ ] CHANGELOG & docs updated → tag **v0.9.0-rc1**.  

---

*Prepared by **team/random_iceberg** · Approved 10 May 2025*  
