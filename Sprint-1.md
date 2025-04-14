# Sprint 1 – Full MVP Delivery for Titanic Survivor Prediction Application

**Sprint Duration:** 2 Weeks  
**Team Members & Hours (Approx.):**  
- **Fullstack Developers (40h total each):**
  - John Doe
  - Jane Smith
  - Michael Brown
  - Sarah Davis
- **Backend & Model Specialists (40h total each):**
  - Emily Johnson
  - David Williams

---

## 1. Sprint Overview

**Sprint Goal:**  
Deliver the **complete, production-ready MVP** of the Titanic Survivor Prediction Application, encompassing all major features and integrated services. By the end of this sprint, every essential component—**frontend pages**, **backend logic**, **ML model pipeline**, **authentication and database setup**, **admin console**, and **marketing/advertisement integration**—must be **fully functional** and **packaged** in a single Docker Compose configuration.  

In other words, at Sprint 1 completion, the application should be ready to **deploy to a production environment** without missing functionality or placeholders.

**Key Deliverables:**
1. **Production-Ready Docker Infrastructure**  
   - A single `docker-compose.yml` that orchestrates all containers (frontend, backend, model, and Supabase).
2. **Complete Frontend (React + TypeScript)**  
   - Landing page, Survival Calculator, Advertisement/Marketing pages, and optional Admin Console UI.
3. **Backend (FastAPI) with Authentication**  
   - Endpoints for predictions, user registration/login, role-based access, and admin capabilities.
4. **ML Model Service**  
   - Endpoints for model inference, training (optional re-training), and version persistence.
5. **Admin Console**  
   - UI and endpoints to view, train, and manage ML models.
6. **User and Data Management (Supabase)**  
   - Production-level user authentication, session handling, and secure data storage.
7. **Marketing & Ads Integration**  
   - Frontend sections or modals featuring the promotional narrative for AI courses.
8. **Test Coverage & Final Documentation**  
   - Automated tests (unit + integration + initial E2E) with CI/CD pipeline checks passing.
   - Updated documentation (in `docs/` and any relevant wikis) reflecting the finalized MVP.

---

## 2. Sprint Objectives

1. **Finalize Docker Compose & Deployment**  
   - Ensure **zero local configuration** is required: `docker-compose up --build -d` fully deploys the MVP.
   - Configure environment variables within the Compose file or container definitions (no `.env` usage).
   - Validate all services communicate properly in the Docker network (frontend → backend → model, etc.).

2. **Complete Frontend Implementation**  
   - **Landing Page**: Production-quality design explaining the application and highlighting AI course ads.
   - **Survival Calculator**: Fully functional form with real-time or on-demand predictions.
   - **Authentication UI**: Registration and login flows, error handling, session persistence.
   - **Admin UI**: If user has admin privileges, show pages for model management (list, train, remove).
   - **Responsive Design**: Works on desktop and mobile.  
   - **Testing**: Basic component and user-flow tests (React Testing Library, Jest, or similar).

3. **Robust Backend (FastAPI) with Auth**  
   - **Prediction API**: Endpoints for calculating survival probability; must handle required features (age, sex, class, etc.).
   - **Auth & Role Management**: `POST /register`, `POST /login`, session/role checks for admin vs. standard user.
   - **Error Handling & Validation**: Proper status codes and descriptive messages for invalid requests.
   - **Admin Endpoints**: e.g., `GET /models`, `POST /models/train`, `DELETE /models/{id}`, etc.
   - **Logging & Monitoring**: Basic logs for auditing predictions, admin actions, and potential errors.

4. **ML Model Service**  
   - **Persisted Model**: A stable ML model (Random Forest, SVM, or Logistic Regression) trained on Titanic dataset.
   - **Inference Endpoint**: Exposed at `POST /inference/` with real predictions for given passenger data.
   - **Optional Training Endpoint**: `POST /training/` to initiate re-training or advanced usage.
   - **Production Configuration**: Ensure model loading, caching, or reloading does not impede performance.

5. **Supabase Integration**  
   - **User Accounts**: Fully operational sign-up, login, session management, password hashing (via GoTrue).
   - **Database**: Store user data, keep track of user roles (admin/regular), potentially save last predictions.
   - **Security**: Restrict admin actions, sensitive data, or logs to authorized roles only.

6. **Marketing & Advertisement**  
   - Dedicated UI or integrated banners featuring the marketing text for AI courses.
   - Clear CTAs that link externally or provide pop-up details about the educational offerings.
   - Engaging visuals (images, infographics) to catch user interest.

7. **Automated Testing & CI/CD**  
   - **Unit Tests**: Frontend components, backend routes, model pipeline.
   - **Integration Tests**: Checking end-to-end data flow (prediction calls, user auth, etc.).
   - **(Optional) E2E Tests**: Basic flows with Cypress/Playwright to confirm major user journeys are intact.
   - **GitLab CI/CD**: Blocks merges on failing builds/tests. Docker images built automatically on push.

8. **Documentation**  
   - Updated `README.md` for each module (frontend, backend, model) plus central docs in `docs/`.
   - Clear instructions on how to run, test, and deploy the MVP.
   - Architecture diagrams in the wiki or `docs/` submodule for final MVP.

---

## 3. Epics & Task Breakdown

Below are the primary epics and tasks to achieve the **production-ready MVP** in this sprint. Each task should have a corresponding GitLab issue with clear acceptance criteria and assigned owner(s). All tasks must close before the sprint ends.

### Epic A: Production Docker & Environment Setup

**Goal:** A single, final `docker-compose.yml` that deploys the entire MVP with no extra steps.

- **Task A1: `feat/docker-compose-setup`**  
  - **Description:**  
    - Finalize the multi-service Docker Compose config (frontend, backend, model, supabase).
    - Remove `.env` usage; define all essential environment variables in the Compose file.
    - Expose proper ports (e.g., `3000` for frontend, `8000` for backend, `5000` for model, `5432` for Supabase).
  - **Acceptance Criteria:**  
    1. `docker-compose up --build -d` runs all services without error.  
    2. Network calls between containers (e.g., backend ↔ model, backend ↔ supabase) work reliably.  
    3. No local config/manual edits needed; the user sees the app on `http://localhost:3000/` post-spin-up.  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

- **Task A2: `feat/ci-cd-prod-build`**  
  - **Description:**  
    - Extend GitLab CI to build Docker images for all services on each commit.
    - Validate images by running short container tests (e.g., health checks).
    - Ensure pipeline fails if containers cannot build or start properly.
  - **Acceptance Criteria:**  
    1. Every push triggers a Docker build job for each service.  
    2. Automated container-level tests/health checks run and pass.  
    3. Pipeline blocks merges on failures.  
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab]

### Epic B: Frontend (React + TypeScript + Tailwind)

**Goal:** A polished, user-friendly SPA that covers all essential pages and flows.

- **Task B1: `feat/frontend-landing-marketing`**  
  - **Description:**  
    - Implement a production-grade landing page with marketing content.  
    - Integrate marketing visuals, CTA buttons, and disclaimers.  
    - Ensure responsiveness for mobile and desktop screens.
  - **Acceptance Criteria:**  
    1. Landing page design matches marketing specs (images, text blocks, CTAs).  
    2. Fully responsive layout with no major rendering issues.  
    3. Clear link to the Survival Calculator, registration/login, and admin console (if authorized).  
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab]

- **Task B2: `feat/survival-calculator-ui`**  
  - **Description:**  
    - Create a form-based component that collects passenger attributes (age, fare, etc.).  
    - On submit (or real-time), calls the backend for predictions.  
    - Displays the survival probability or result in a user-friendly manner.
  - **Acceptance Criteria:**  
    1. All relevant input fields (class, sex, age, embarked, etc.) are present and validated.  
    2. Prediction is displayed with a success/failure alert or probability.  
    3. Handles errors gracefully (e.g., server down, invalid input).  
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab]

- **Task B3: `feat/auth-ui-integration`**  
  - **Description:**  
    - Build user registration and login forms.  
    - Manage JWT tokens or cookies for session persistence (via Supabase).  
    - Show “Admin Console” menu item only if user is admin (role check).
  - **Acceptance Criteria:**  
    1. Users can register, log in, and stay logged in (session persisted).  
    2. Error messages displayed for invalid credentials or duplicate email.  
    3. Admin users see restricted routes to model management.  
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab]

- **Task B4: `feat/admin-console-frontend`**  
  - **Description:**  
    - Provide an admin-specific area (accessible only if `role=admin`).  
    - Display list of models, allow new training, model deletion, or settings updates.  
    - Show training status, logs, or performance metrics (if available from backend).
  - **Acceptance Criteria:**  
    1. Admin sees a UI list of models with basic info (e.g., name, date trained, accuracy).  
    2. “Train Model” or “Delete Model” triggers the correct backend endpoints.  
    3. Non-admin users cannot access these pages (redirect or 403).  
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab]

### Epic C: Backend & Core APIs (FastAPI)

**Goal:** A complete set of production-ready endpoints for predictions, user management, and admin functionalities.

- **Task C1: `feat/backend-auth`**  
  - **Description:**  
    - Implement registration, login, session validation (JWT or token-based) with role assignment.  
    - Sync user credentials with Supabase’s GoTrue or any necessary DB calls.  
  - **Acceptance Criteria:**  
    1. `POST /register` and `POST /login` yield valid tokens or sessions.  
    2. Backend enforces role checks for admin-only routes.  
    3. Security best practices in place (hashed passwords, no plaintext storage).  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

- **Task C2: `feat/backend-prediction`**  
  - **Description:**  
    - Create a `POST /predict` endpoint that receives passenger data and calls the Model API for inference.  
    - Validate user input, handle errors, and return a structured response.  
    - Integrate optional logging (who predicted, what was predicted) in the DB.
  - **Acceptance Criteria:**  
    1. Endpoint responds with survival probability and status (e.g., “survived” or “not survived”).  
    2. Graceful handling of invalid data or missing fields (HTTP 400).  
    3. Works for both anonymous and authenticated users; if user is logged in, store or track predictions.  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

- **Task C3: `feat/backend-admin-endpoints`**  
  - **Description:**  
    - Endpoints for listing models (`GET /models`), training new models (`POST /models/train`), and deleting old ones (`DELETE /models/{id}`).  
    - Restrict all these routes to admin users only.  
    - Provide relevant logging for auditing changes.
  - **Acceptance Criteria:**  
    1. Admin endpoints respond only if `role=admin`; otherwise 403.  
    2. Standard JSON structures for listing/training/deleting.  
    3. Database or container volumes updated accordingly (models saved/deleted).  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

### Epic D: Model Microservice (FastAPI)

**Goal:** A production-level ML pipeline for inference and optional re-training.

- **Task D1: `feat/model-service-inference`**  
  - **Description:**  
    - Load a final, trained Titanic ML model (Random Forest or SVM) on service startup.  
    - `/inference/` endpoint to process feature input and return predictions.  
    - Handle model loading errors or missing model gracefully.  
  - **Acceptance Criteria:**  
    1. Model is loaded once at startup (caching).  
    2. Endpoint returns numeric probability or classification.  
    3. Standard logs exist for each request.  
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab]

- **Task D2: `feat/model-service-training`**  
  - **Description:**  
    - Expose a `/training/` endpoint that can re-train a model on the Titanic dataset.  
    - Save newly trained model artifacts (e.g., `.pkl`) into a shared volume.  
    - Optionally track training metrics (accuracy, F1, etc.) in a DB or local file.  
  - **Acceptance Criteria:**  
    1. Model re-training completes without freezing or container crash.  
    2. New model artifacts are stored properly for subsequent usage.  
    3. Endpoint returns training completion status and optional metrics.  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

### Epic E: Supabase Integration & Data Persistence

**Goal:** Fully functional user data and session management, plus optional logging of predictions or user interactions.

- **Task E1: `feat/supabase-setup-complete`**  
  - **Description:**  
    - Finish configuring Supabase (Postgres + GoTrue) for production.  
    - Migrate or seed database schemas for user accounts, roles, logs, or predictions.  
    - Verify connectivity from the backend services.  
  - **Acceptance Criteria:**  
    1. `docker-compose` starts Supabase with correct credentials and roles.  
    2. Backend can create/read/update user data and sessions.  
    3. Admin roles recognized by GoTrue or custom DB logic.  
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab]

- **Task E2: `feat/production-db-handlers`**  
  - **Description:**  
    - Implement robust DB interactions for storing predictions (optional), user logs, or admin events.  
    - Use transactions and handle potential DB errors gracefully.  
  - **Acceptance Criteria:**  
    1. Relevant data persists between app restarts, easily queryable for metrics or debugging.  
    2. Clear error messages returned if DB operations fail (e.g., 500 + logs).  
    3. CI tests confirm DB migrations or queries run successfully.  
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab]

### Epic F: Final Testing & Documentation

**Goal:** Validate the entire MVP is stable and properly documented.

- **Task F1: `test/unit-integration-e2e`**  
  - **Description:**  
    - Ensure all code paths have unit tests (frontend + backend).  
    - Write integration tests to verify user flows: registering, logging in, predicting, admin actions.  
    - (Optional) Add E2E tests using Cypress/Playwright for a minimal “happy path” scenario.  
  - **Acceptance Criteria:**  
    1. No critical path remains untested (basic coverage at minimum).  
    2. Merging code that breaks tests is blocked in GitLab CI.  
    3. E2E tests pass for main user stories.  
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab]

- **Task F2: `docs/finalize-mvp`**  
  - **Description:**  
    - Update all `README.md` files (frontend, backend, model, root) to reflect final usage.  
    - Provide detailed instructions in the `docs/` or wiki (e.g., architecture diagrams, environment variables, usage instructions).  
    - Document the final architecture, including how the services communicate and data flows.  
  - **Acceptance Criteria:**  
    1. All references to “placeholder” or “TBD” are removed.  
    2. New developers can clone and run the entire app solely using the documentation.  
    3. The final doc set matches the completed features for the MVP.  
  - **Estimate:** 4h  
  - **Owner(s):** [Assign in GitLab]

---

## 4. Agile Workflow & Coordination

- **Standup Meetings (2x Weekly):**  
  Short 15-minute calls to discuss progress, blockers, and next steps.

- **Task Management:**  
  All tasks tracked as GitLab issues with clear acceptance criteria, estimates, and owners. Use labels (e.g., `backend`, `frontend`, `model`, `supabase`) for easy filtering.

- **Code Reviews:**  
  - Each merge request must be peer-reviewed for quality, adherence to style, and robust testing.
  - All merges require passing CI checks.

- **Continuous Integration (GitLab CI):**  
  - On every push, run:
    1. Lint and unit tests for backend, frontend, and model.
    2. Docker image builds for all services.
    3. Short container-level integration checks.
  - Pipeline failures block merges unless explicitly overridden.

---

## 5. Sprint Review & Retrospective

**Sprint Review (End of Week 2):**  
1. **Live End-to-End Demo:**  
   - Demonstrate the entire user flow: a new user registers, logs in, accesses the survival calculator, obtains predictions, and (if admin) manages models in the console.  
   - Confirm marketing content is visible and user-friendly on the landing page.  
2. **Production-Ready Check:**  
   - Spin up the system on a clean environment using `docker-compose up --build -d`.  
   - Show no missing steps or manual config is required.  
3. **Testing Verification:**  
   - Confirm that unit, integration, and minimal E2E tests pass with no regressions.  

**Retrospective:**  
- **What Went Well?**  
  - Identify successes in delivering the entire MVP in one sprint.  
- **What Could Be Better?**  
  - Discuss any blockers or challenges in time management or collaborative coding.  
- **Action Items**  
  - Document improvement steps for future expansions or maintenance.

---

## 6. Key Considerations

1. **Fully Production-Ready**  
   - No placeholder code or partial features left incomplete.  
   - Both technical (scalability, security) and design (UI/UX, marketing) must be polished.

2. **Supabase & Security**  
   - Strictly ensure user and admin roles are respected throughout the stack.  
   - Credentials or secrets must be stored securely (no plain text in code repos).

3. **Performance & Stability**  
   - Load model once, handle concurrency gracefully.  
   - Docker Compose resource limits can be tuned if needed, but correctness is the priority.

4. **Delivery on Time**  
   - The sprint must conclude with the final version.  
   - No second sprint for core MVP—any additional improvements or refactoring can follow in maintenance sprints if desired.

5. **Documentation Completeness**  
   - Thorough, up-to-date docs enabling any developer or stakeholder to run, test, and evaluate the final product.

---

*This revised Sprint-1 plan ensures that a **fully functional MVP** is delivered by the end of this two-week window. By combining all critical features—Docker Compose orchestration, a polished React frontend, robust FastAPI backend, ML-driven inference microservice, and Supabase authentication/data layer—into a single sprint, the team commits to producing a final, production-ready application without placeholders or missing elements.*
