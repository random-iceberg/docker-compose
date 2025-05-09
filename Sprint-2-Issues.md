### [Epic A1] CI/CD & Container Registry: feat/ci-pipeline-prod-build

* **Assignee:** Lev Malets  
* **Labels:** `ci/cd` `registry` `sprint2` `epic-A`  
* **Estimate:** 6 h

**Branch**: `feat/ci-pipeline-prod-build`

**Description**  
Automate the build and publish of Docker images for all services (frontend, backend, model) on every commit, using semantic version tags and registry health checks:

- Extend GitLab CI to build images for frontend, backend, and model on each push  
- Tag images with semantic versions (`v<semver>`)  
- Push to GitLab Container Registry  
- Add a “smoke-up” stage in CI to start the compose stack and verify health  

**Acceptance Criteria**

1. **Automated Builds:** CI builds and pushes images for all services on every commit.  
2. **Semantic Tagging:** Images are tagged as `v<major>.<minor>.<patch>`.  
3. **Registry Push:** All images appear in the GitLab Container Registry.  
4. **Health Checks:** CI’s smoke-up stage confirms all services pass `/health` endpoints.

---

### [Epic A3] CI/CD: feat/ci-unit-e2e-integration

* **Assignee:** Lev Malets  
* **Labels:** `ci/cd` `testing` `sprint2` `epic-A`  
* **Estimate:** 6 h

**Branch**: `feat/ci-unit-e2e-integration`

**Description**  
Add CI stages for unit tests and automated end‑to‑end tests, ensuring pipelines block on failures and publish results:

- Configure Pytest unit + integration stages for Python and TypeScript code  
- Integrate Playwright/Cypress E2E suite against the full compose stack  
- Fail merge requests when any test stage fails  
- Publish test reports and artifacts  

**Acceptance Criteria**

1. **Unit Tests:** All unit and integration tests run in CI and pass.  
2. **E2E Tests:** Nightly headless E2E tests succeed against Docker Compose.  
3. **Pipeline Enforcement:** Failed tests block merges.  
4. **Reporting:** Test results and artifacts are published in the CI job.

---

### [Epic B4] Backend Authentication Core: feat/backend-auth-core

* **Assignee:** Kazi Rahman  
* **Labels:** `backend` `auth` `sprint2` `epic-B`  
* **Estimate:** 6 h

**Branch**: `feat/backend-auth-core`

**Description**  
Implement user signup/login endpoints with secure password hashing and JWT issuance:

- `POST /signup`: hash passwords using bcrypt, store users  
- `POST /login`: verify credentials, return JWT with 1 h TTL  
- Return HTTP 409 on duplicate email, HTTP 401 on invalid credentials  
- Log auth events for auditing  

**Acceptance Criteria**

1. **Signup:** `POST /signup` creates user with bcrypt-hashed password or returns 409.  
2. **Login:** `POST /login` returns a signed JWT (1 h expiry) or 401.  
3. **Security:** Passwords never logged or returned in responses.  
4. **Logging:** Auth attempts logged with timestamp and outcome.

---

### [Epic B5] DB User Schema: feat/db-user-schema

* **Assignee:** Lev Malets  
* **Labels:** `backend` `db` `sprint2` `epic-B`  
* **Estimate:** 2 h

**Branch**: `feat/db-user-schema`

**Description**  
Create and migrate the users table for authentication:

- Use Alembic to add `users` table with columns: `id`, `email`, `pw_hash`, `role`, `created_at`  
- Seed an initial admin user from environment variables  
- Ensure uniqueness constraint on `email`  

**Acceptance Criteria**

1. **Migration:** Alembic scripts create the `users` table with specified columns.  
2. **Seeding:** On first run, an admin user is created from ENV vars.  
3. **Constraints:** `email` is unique.  
4. **Rollback:** Migration can be reversed cleanly.

---

### [Epic B6] JWT Middleware & RBAC: feat/jwt-middleware-rbac

* **Assignee:** Huraira Ali  
* **Labels:** `backend` `auth` `sprint2` `epic-B`  
* **Estimate:** 4 h

**Branch**: `feat/jwt-middleware-rbac`

**Description**  
Enforce role‑based access control via JWT middleware:

- Validate JWT on protected routes  
- Extract `user.role` into request context  
- Reject unauthorized access (403) when role insufficient  
- Apply to `/admin/*`, `/models/*`, `/training/*`  

**Acceptance Criteria**

1. **JWT Validation:** Requests without or with invalid JWT receive 401.  
2. **Role Extraction:** Middleware injects `user.role` into request.  
3. **RBAC Enforcement:** 403 returned for insufficient-role attempts.  
4. **Coverage:** Protected routes tested in integration suite.

---

### [Epic B7] Frontend Auth Hooks: feat/frontend-auth-hooks

* **Assignee:** Kazi Rahman  
* **Labels:** `frontend` `auth` `sprint2` `epic-B`  
* **Estimate:** 8 h

**Branch**: `feat/frontend-auth-hooks`

**Description**  
Build a React `AuthContext` to manage JWT in HttpOnly cookies, guard routes, and refresh tokens:

- Store JWT in an HttpOnly, secure cookie  
- Provide React hooks (`useAuth`) for login, logout, and auth state  
- Protect `/admin` and model-management routes from unauthenticated access  
- Redirect to login page when access is denied  

**Acceptance Criteria**

1. **AuthContext:** Exposes `login`, `logout`, `user`, and `isAuthenticated`.  
2. **Route Guards:** Protected routes redirect to `/signin` if not authenticated.  
3. **Cookie Usage:** JWT stored in HttpOnly cookie (no localStorage).  
4. **Tests:** Unit tests for core hook functionality.

---

### [Epic B8] Frontend Refresh Token: feat/frontend-refresh-token

* **Assignee:** Kazi Rahman  
* **Labels:** `frontend` `auth` `sprint2` `epic-B`  
* **Estimate:** 2 h

**Branch**: `feat/frontend-refresh-token`

**Description**  
Implement a token refresh flow to maintain user sessions:

- Backend endpoint `POST /token/refresh` issues new JWT  
- Client auto‑calls refresh on 401 or token expiry  
- Store refreshed token in HttpOnly cookie  
- Integrate into `AuthContext`  

**Acceptance Criteria**

1. **Refresh Endpoint:** Returns new JWT in HttpOnly cookie.  
2. **Auto‑Refresh:** Client refreshes token on 401 or shortly before expiry.  
3. **Persistence:** User remains logged in across page reloads.  
4. **Tests:** Simulate token expiry and verify auto‑refresh.

---

### [Epic C3] Backend Integration Tests: test/backend-integration-tests

* **Assignee:** Fares Elbermawy  
* **Labels:** `backend` `testing` `sprint2` `epic-C`  
* **Estimate:** 4 h

**Branch**: `test/backend-integration-tests`

**Description**  
Write Pytest integration tests for core backend endpoints, covering both success and error scenarios:

- `/predict` with valid/invalid payloads  
- `/models` list/create/delete flows (no auth in MVP)  
- Auth endpoints `/signup`, `/login`  

**Acceptance Criteria**

1. **Coverage:** All happy and error paths covered.  
2. **CI Pass:** Tests run in CI and pass consistently.  
3. **Isolation:** Use test database or fixtures to reset state.  
4. **Assertions:** Verify HTTP status codes and response schemas.

---

### [Epic C4] Structured Logging: feat/structured-logging

* **Assignee:** Denisa‑Iulia Vaidasigan  
* **Labels:** `backend` `observability` `sprint2` `epic-C`  
* **Estimate:** 3 h

**Branch**: `feat/structured-logging`

**Description**  
Standardize application logs to JSON format using Loguru:

- Include `timestamp`, `level`, `module`, and `correlation_id` (from JWT)  
- Replace print/logging with structured log calls  
- Configure global JSON formatter  

**Acceptance Criteria**

1. **JSON Logs:** All logs emitted as JSON objects.  
2. **Mandatory Fields:** Each log record has `timestamp`, `level`, `module`, `correlation_id`.  
3. **Integration:** Logs appear correctly in container stdout.  
4. **Tested:** Structured logging tested in integration suite.

---

### [Epic C5] Centralized Error Handler: feat/backend-error-handler

* **Assignee:** Denisa‑Iulia Vaidasigan  
* **Labels:** `backend` `error-handling` `sprint2` `epic-C`  
* **Estimate:** 3 h

**Branch**: `feat/backend-error-handler`

**Description**  
Implement a global exception handler in FastAPI to return consistent JSON errors:

- Catch all unhandled exceptions  
- Return payload `{ "detail": <error>, "message": <friendly> }` with correct HTTP status  
- Remove stack traces from responses (logged only)  

**Acceptance Criteria**

1. **Consistency:** All errors return the standard JSON schema.  
2. **Status Codes:** HTTP 4xx/5xx codes match error types.  
3. **Logging:** Original exception logged in structured logs.  
4. **Tests:** Error handler behavior covered by integration tests.

---

### [Epic C6] Prediction History API: feat/backend-prediction-history

* **Assignee:** Fares Elbermawy  
* **Labels:** `backend` `feature` `sprint2` `epic-C`  
* **Estimate:** 3 h

**Branch**: `feat/backend-prediction-history`

**Description**  
Provide `GET /predictions/history` to return the last 10 predictions for an authenticated user:

- Fetch stored history from database, ordered by timestamp desc  
- Include fields: `timestamp`, `input`, `output`  
- Paginate or limit to 10 records  

**Acceptance Criteria**

1. **Endpoint:** Returns up to 10 most recent predictions for the calling user.  
2. **Schema:** Response includes `timestamp`, `input`, `output`.  
3. **Auth:** Requires valid JWT.  
4. **Tests:** Integration tests cover history retrieval and empty state.

---

### [Epic D1] Inference Endpoint: feat/inference-endpoint

* **Assignee:** Sameer Kumar  
* **Labels:** `model-service` `inference` `sprint2` `epic-D`  
* **Estimate:** 6 h

**Branch**: `feat/inference-endpoint`

**Description**  
Load a scikit‑learn Random Forest model once at startup and expose `/inference`:

- Cache model in memory for fast access  
- Accept JSON payload of features, return `{ "probability": float, "survived": bool }`  
- Measure and log inference time, ensure p95 < 150 ms locally  

**Acceptance Criteria**

1. **Singleton Load:** Model loaded only on startup.  
2. **Response Schema:** Returns `probability` and `survived`.  
3. **Performance:** p95 latency < 150 ms.  
4. **Logging:** Each request logs inference duration.

---

### [Epic D2] Training Endpoint: feat/training-endpoint

* **Assignee:** Sameer Kumar  
* **Labels:** `model-service` `training` `sprint2` `epic-D`  
* **Estimate:** 7 h

**Branch**: `feat/training-endpoint`

**Description**  
Implement `/training` to retrain models asynchronously and persist `.pkl` files:

- Accept `{ algorithm, features, name }` payload  
- Trigger background task to train and save model under volume `models/`  
- Update Postgres metadata with new model UUID and name  
- Return HTTP 202 with status message  

**Acceptance Criteria**

1. **Async Processing:** Returns 202 immediately and trains in background.  
2. **Persistence:** New `.pkl` saved and available on next inference.  
3. **Metadata:** Postgres table updated with model record.  
4. **Tests:** Integration tests for job initiation and metadata update.

---

### [Epic D3] Model Registry Migration: chore/model-registry-migration

* **Assignee:** Lev Malets  
* **Labels:** `database` `chore` `sprint2` `epic-D`  
* **Estimate:** 4 h

**Branch**: `chore/model-registry-migration`

**Description**  
Finalize database schema migrations for the model registry:

- Ensure tables `model`, `feature`, and `model_feature_link` exist  
- Add index on `model.uuid` for fast lookups  
- Set foreign keys with `ON DELETE CASCADE` for cleanup  

**Acceptance Criteria**

1. **Migrations:** Alembic scripts create/alter tables as specified.  
2. **Indexes:** Unique index on `model.uuid`.  
3. **FK Constraints:** Cascading deletes configured.  
4. **Rollback:** Migrations reversible without errors.

---

### [Epic F1] Calculator Validation Tweaks: ui/calculator-validation-tweaks

* **Assignee:** Denisa‑Iulia Vaidasigan  
* **Labels:** `frontend` `ui` `sprint2` `epic-F`  
* **Estimate:** 4 h

**Branch**: `ui/calculator-validation-tweaks`

**Description**  
Improve form validation and mobile layout in the Survival Calculator:

- Add inline error messages under each field  
- Use HTML5 `min`/`max` on number inputs  
- Adjust spacing/padding for small screens  

**Acceptance Criteria**

1. **Inline Errors:** Invalid inputs show contextual messages.  
2. **Constraints:** Age, fare, and counts respect `min`/`max`.  
3. **Responsive:** Form displays nicely on mobile.  
4. **Tests:** UI tests verify validation behavior.

---

### [Epic F2] Frontend Integration Tests: test/frontend-integration-tests

* **Assignee:** Fares Elbermawy  
* **Labels:** `frontend` `testing` `sprint2` `epic-F`  
* **Estimate:** 4 h

**Branch**: `test/frontend-integration-tests`

**Description**  
Write Playwright or Cypress tests covering core UI flows:

- Landing page navigation to calculator and admin console  
- Calculator end‑to‑end flow (input → predict → display)  
- Admin console train and delete operations  

**Acceptance Criteria**

1. **Coverage:** All major user journeys automated.  
2. **CI Integration:** Tests run headlessly in CI without failures.  
3. **Artifacts:** Screenshots/logs captured on failure.  
4. **Repeatable:** Tests stable across multiple runs.

---

### [Epic F3] Code Cleanup & Refactor: refac/code-cleanup

* **Assignee:** Huraira Ali  
* **Labels:** `frontend` `backend` `refactor` `sprint2` `epic-F`  
* **Estimate:** 6 h

**Branch**: `refac/code-cleanup`

**Description**  
Refactor FE and BE codebases for consistency and reusability:

- Consolidate duplicate components and utility functions  
- Enforce coding conventions (Prettier, ESLint, Black, Flake8)  
- Apply responsive design fixes across pages  
- Improve folder structure for production readiness  

**Acceptance Criteria**

1. **Reusability:** Shared components centralized and imported consistently.  
2. **Linting:** No lint or formatting errors in CI.  
3. **Structure:** Project layout follows agreed conventions.  
4. **Responsive:** UI remains responsive after cleanup.

---

### [Epic F4] Reusable Component Library: chore/reusable-component-library

* **Assignee:** Huraira Ali  
* **Labels:** `frontend` `chore` `sprint2` `epic-F`  
* **Estimate:** 2 h

**Branch**: `chore/reusable-component-library`

**Description**  
Extract common UI elements into a shared library:

- Buttons, Cards, Toast notifications  
- Update imports in FE code to use the shared library  
- Document usage in a central README  

**Acceptance Criteria**

1. **Library:** Common components live under `src/components/common`.  
2. **Imports:** All references updated; no duplicates remain.  
3. **Documentation:** README includes examples for each component.  
4. **Tests:** Basic snapshot tests for shared components.

---

### [Epic F5] Prediction History Component: ui/prediction-history-component

* **Assignee:** Denisa‑Iulia Vaidasigan  
* **Labels:** `frontend` `feature` `sprint2` `epic-F`  
* **Estimate:** 3 h

**Branch**: `ui/prediction-history-component`

**Description**  
Add a “Prediction History” view in the user dashboard:

- Fetch last 10 predictions via `GET /predictions/history`  
- Render in a responsive table with columns: timestamp, input summary, result  
- Include pagination or “Show more” if >10 records  

**Acceptance Criteria**

1. **Data Fetch:** Component calls the history endpoint correctly.  
2. **Display:** Table shows up to 10 records with all fields.  
3. **Responsive:** Table scrolls or adapts on small screens.  
4. **Tests:** UI tests verify correct rendering.

---

### [Epic F6] Social Sharing Buttons: ui/social-sharing-buttons

* **Assignee:** Kazi Rahman  
* **Labels:** `frontend` `feature` `sprint2` `epic-F`  
* **Estimate:** 2 h

**Branch**: `ui/social-sharing-buttons`

**Description**  
Add social share buttons to the landing page:

- Facebook, Twitter, LinkedIn icons  
- Open share dialogs with prefilled text in a new window  
- Style to match branding  

**Acceptance Criteria**

1. **Links:** Buttons open correct share URLs with page link and marketing copy.  
2. **UI:** Icons match design and change state on hover.  
3. **Accessibility:** Include `aria-label` on each button.  
4. **Tests:** Integration test confirms dialogs open (mocked).

---

### [Epic G1] Backend Auth Coverage: test/backend-auth-coverage

* **Assignee:** Huraira Ali  
* **Labels:** `backend` `testing` `sprint2` `epic-G`  
* **Estimate:** 4 h

**Branch**: `test/backend-auth-coverage`

**Description**  
Ensure 100 % branch coverage for authentication modules:

- Unit tests for signup, login, JWT middleware, and RBAC  
- Cover success and error paths  

**Acceptance Criteria**

1. **Coverage:** Auth module at 100 % branch coverage.  
2. **CI Pass:** Coverage reported and enforced in CI.  
3. **Tests:** All edge cases (duplicate signup, invalid token, insufficient role).

---

### [Epic G2] Model Service Tests: test/model-service

* **Assignee:** Sameer Kumar  
* **Labels:** `model-service` `testing` `sprint2` `epic-G`  
* **Estimate:** 3 h

**Branch**: `test/model-service`

**Description**  
Write pytest tests for the model microservice:

- Inference endpoint success and failure cases  
- Training endpoint job initiation and error handling  
- Achieve ≥ 80 % coverage on those modules  

**Acceptance Criteria**

1. **Coverage:** Model service tests ≥ 80 % coverage.  
2. **Test Cases:** Include invalid input and exception scenarios.  
3. **CI Pass:** Tests run and pass in CI.

---

### [Epic G3] Playwright E2E: test/playwright-e2e

* **Assignee:** Lev Malets  
* **Labels:** `testing` `e2e` `sprint2` `epic-G`  
* **Estimate:** 6 h

**Branch**: `test/playwright-e2e`

**Description**  
Automate full end‑to‑end flow with Playwright:

- Signup → login → navigate to calculator → predict → view history  
- Switch to admin → train a model → verify new model appears → delete model  
- Run headless in CI, capture artifacts on failure  

**Acceptance Criteria**

1. **Flow Coverage:** Full core user journey automated.  
2. **Stability:** Tests pass reliably in local and CI.  
3. **Artifacts:** Screenshots/logs on CI failures.  
4. **CI Integration:** E2E stage green in pipeline.

---

### [Epic G4] Coverage Gate: ci/coverage-gate

* **Assignee:** Lev Malets  
* **Labels:** `ci/cd` `coverage` `sprint2` `epic-G`  
* **Estimate:** 2 h

**Branch**: `ci/coverage-gate`

**Description**  
Fail CI when overall test coverage falls below 80 % and publish a coverage badge:

- Aggregate coverage reports from backend, frontend, and model tests  
- Enforce 80 % threshold in pipeline  
- Generate markdown badge for README  

**Acceptance Criteria**

1. **Threshold:** Pipeline fails if combined coverage < 80 %.  
2. **Badge:** Coverage badge displayed in project README.  
3. **CI Tests:** Verified in merge requests.

---

### [Epic H1] Architecture Diagram Update: docs/architecture-update

* **Assignee:** Alex  
* **Labels:** `docs` `architecture` `sprint2` `epic-H`  
* **Estimate:** 3 h

**Branch**: `docs/architecture-update`

**Description**  
Refresh the Mermaid architecture diagram in `docs/Project-Charter.md` to reflect RC‑1 service layout:

- Update container names, ports, and service dependencies  
- Date the diagram **29 May 2025**  

**Acceptance Criteria**

1. **Accuracy:** Diagram matches current Docker Compose topology.  
2. **Formatting:** Renders correctly in GitLab Wiki.  
3. **Versioning:** Revision note added under diagram.

---

### [Epic H2] RC‑1 Deployment Guide: docs/rc1-deployment-guide

* **Assignee:** Alex  
* **Labels:** `docs` `deployment` `sprint2` `epic-H`  
* **Estimate:** 1 h

**Branch**: `docs/rc1-deployment-guide`

**Description**  
Write a concise deployment guide for RC‑1 in `docs/README.md`:

- Clone repo with submodules  
- `git submodule update --init --recursive`  
- `docker compose up --build -d`  

**Acceptance Criteria**

1. **Steps:** Clearly documented in one section.  
2. **Verification:** Links to `/health` for verification.  
3. **No Gaps:** No external configuration required.

---

### [Epic H3] Pull Request Review: pull-request-review

* **Assignee:** Alex  
* **Labels:** `process` `review` `sprint2` `epic-H`  
* **Estimate:** 5 h

**Branch**: N/A

**Description**  
Perform a comprehensive review of all Sprint 2 merge requests:

- Ensure each MR closes its corresponding issue  
- Verify conventional commit messages  
- Confirm CI checks, tests, and code style compliance  

**Acceptance Criteria**

1. **Linkage:** Every MR references and closes an issue.  
2. **Commits:** All commits follow the Conventional Commits spec.  
3. **CI Green:** All checks pass before approval.  
4. **Approvals:** At least one peer LGTM on each MR.

---

### [Epic H4] Metrics Setup Guide: docs/metrics-setup-guide

* **Assignee:** Alex  
* **Labels:** `docs` `observability` `sprint2` `epic-H`  
* **Estimate:** 3 h

**Branch**: `docs/metrics-setup-guide`

**Description**  
Document how to enable and import Prometheus metrics and Grafana dashboards:

- Describe `/metrics` endpoint on each service  
- Provide Grafana JSON dashboard file and import instructions  
- Add usage examples to root `docs/README.md`  

**Acceptance Criteria**

1. **Documentation:** Step‑by‑step guide in `docs/`.  
2. **Dashboard:** JSON file committed and referenced.  
3. **Verification:** Tested import in local Grafana.  
4. **Clarity:** New users can follow without assistance.

---
