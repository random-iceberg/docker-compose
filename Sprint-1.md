# Sprint 1 – Foundational Setup and Core Implementation

**Sprint Duration:** 2 Weeks  
**Team Members & Hours:**  
- **Fullstack Developers (40h total):**  
  - John Doe  
  - Jane Smith  
  - Michael Brown  
  - Sarah Davis  
- **Backend & Model Specialists (20h total):**  
  - Emily Johnson  
  - David Williams  

---

## 1. Sprint Overview

**Sprint Goal:**  
Lay a **production-ready foundation** for the Titanic Survivor Prediction Application by ensuring all core services (Web Frontend, Web Backend, Model Backend, and Supabase) are integrated, containerized, and deployable with a single `docker-compose up --build` command. Deliver an initial React SPA with essential pages, baseline ML model endpoints, and Supabase integration for authentication scaffolding.

By Sprint’s end, we aim to:
1. **Containerize All Services**  
   - The entire system (Frontend, Backend, Model API, and Supabase) must build and launch without extra manual steps.  
2. **Bootstrap React SPA**  
   - Provide a minimal but functional SPA structure (landing page, placeholder routes, basic navigation).  
3. **Integrate Supabase**  
   - Establish the initial database schema (auth tables, user data, session management) and validate connectivity.  
4. **Provide Baseline ML Model Logic**  
   - Implement a simple training/inference pipeline in the Model Backend.  
5. **Establish CI/CD Essentials**  
   - Configure automated builds, linting, and basic unit tests in GitLab CI to ensure code quality and reproducibility.

---

## 2. Sprint Objectives

1. **Docker & Environment Configuration**  
   - Finalize a single `docker-compose.yml` to orchestrate all services without requiring a local `.env` file.  
   - Validate that all containers (Frontend, Backend, Model, Supabase) communicate over an isolated Docker network.  

2. **Frontend React Skeleton**  
   - Initialize a React + TypeScript SPA with Tailwind CSS.  
   - Include a landing page, rudimentary navigation, and placeholders for future pages (e.g., Admin Console).  

3. **Model Backend: Baseline Training & Inference**  
   - Integrate Titanic dataset acquisition (via `data_downloader.py`) into a persistent Docker volume.  
   - Implement a simple scikit-learn model (e.g., Logistic Regression) with a minimal training endpoint and an inference endpoint that returns mock or basic predictions.  

4. **Supabase Integration**  
   - Configure Supabase (Postgres + GoTrue) for basic user authentication workflows (scaffold only).  
   - Validate that the Web Backend can connect to Supabase and run basic CRUD operations or health checks.  

5. **CI/CD & Documentation**  
   - Set up basic GitLab CI pipelines for lint checks, Docker builds, and initial unit tests.  
   - Provide up-to-date documentation (in `docs/` and `.git.wikis` submodule) covering setup, branching, and coding guidelines.

---

## 3. Epics & Task Breakdown

Below are the major epics and tasks aligned with our Sprint Objectives. Each task should have a corresponding GitLab Issue, with clear acceptance criteria and tracked progress.

### Epic A: Docker & Environment Configuration

**Goal:** Ensure the entire application stack can be launched via `docker-compose up --build` with zero local configuration.

- **Task A1:** `feat/docker-compose-setup`  
  - **Description:**  
    - Create or refine `docker-compose.yml` to include services:  
      - **Web Frontend** (React + Nginx)  
      - **Web Backend** (FastAPI)  
      - **Model Backend** (FastAPI-based ML microservice)  
      - **Supabase** (Postgres + GoTrue)  
    - Configure shared Docker networks and volumes (e.g., for Postgres, model files, Titanic data).  
    - Remove any reliance on `.env` files; use Docker Compose environment blocks instead.  
  - **Acceptance Criteria:**  
    1. Running `docker-compose up --build` spins up all services without error.  
    2. Each service is accessible at its designated port, with correct internal networking.  
    3. Basic health checks confirm connectivity among containers.  
  - **Estimate:** 8 hours  
  - **Owner(s):** [Assign in GitLab]

### Epic B: Frontend React Skeleton

**Goal:** Establish a minimal React/TypeScript application using Tailwind CSS, with foundational navigation and placeholders.

- **Task B1:** `feat/react-skeleton-setup`  
  - **Description:**  
    - Scaffold React project with TypeScript, integrating Tailwind CSS.  
    - Implement a simple landing page with placeholder content describing the app’s purpose.  
    - Add a top-level navigation bar linking to the “Home” and “Dashboard” (placeholder).  
  - **Acceptance Criteria:**  
    1. The SPA compiles/runs successfully on port 3000 or container-exposed port.  
    2. Tailwind classes apply basic styling to the landing page.  
    3. Navigation works without errors.  
  - **Estimate:** 8 hours  
  - **Owner(s):** [Assign in GitLab]

### Epic C: Model Backend & Baseline ML Integration

**Goal:** Provide a baseline scikit-learn model pipeline for Titanic survival predictions, stored in the container with at least one training and one inference endpoint.

- **Task C1:** `feat/data-integration`  
  - **Description:**  
    - Update/validate `data_downloader.py` to retrieve the Titanic dataset.  
    - Mount the dataset in a Docker volume to ensure persistence across container restarts.  
    - Document any known data format constraints.  
  - **Acceptance Criteria:**  
    1. Running `data_downloader.py` automatically downloads (or verifies) Titanic data into the correct volume.  
    2. The dataset is accessible inside the Model Backend container.  
  - **Estimate:** 5 hours  
  - **Owner(s):** [Assign in GitLab]

- **Task C2:** `feat/model-baseline`  
  - **Description:**  
    - Implement a simple logistic regression model in the Model Backend using scikit-learn.  
    - Train and serialize (`.pkl`) the model on the Titanic dataset as a baseline.  
    - Validate the model pipeline with minimal unit tests.  
  - **Acceptance Criteria:**  
    1. Model training code runs end-to-end without errors.  
    2. A `.pkl` file is generated and stored in a volume.  
    3. Tests confirm that inference can run on sample input.  
  - **Estimate:** 5 hours  
  - **Owner(s):** [Assign in GitLab]

- **Task C3:** `feat/training-inference-endpoints`  
  - **Description:**  
    - Provide at least two API routes (e.g., `POST /train` and `POST /predict`).  
    - `POST /train`: Accept model type or minimal config, trigger training (return simple JSON status).  
    - `POST /predict`: Accept basic features (e.g., Age, Sex) and return a dummy or baseline survival probability.  
    - Add logging and minimal validation checks for request payloads.  
  - **Acceptance Criteria:**  
    1. `POST /train` logs a training status and persists the model.  
    2. `POST /predict` returns a numeric probability or descriptive result.  
    3. Invalid payloads are gracefully rejected (HTTP 400).  
  - **Estimate:** 5 hours  
  - **Owner(s):** [Assign in GitLab]

### Epic D: Supabase Integration (Scaffold Only)

**Goal:** Ensure Supabase is running in Docker Compose and that the Web Backend can connect to a basic Postgres schema for user/auth data.

- **Task D1:** `feat/supabase-setup`  
  - **Description:**  
    - Include Supabase/Postgres service in `docker-compose.yml`.  
    - Configure minimal auth schema in Postgres (user table, roles).  
    - Confirm the Web Backend can communicate with Supabase (e.g., via a health check route).  
  - **Acceptance Criteria:**  
    1. Supabase container starts properly with Postgres and GoTrue.  
    2. The Web Backend can query or ping Supabase without error.  
    3. Documentation includes default credentials and connection details (secured as needed).  
  - **Estimate:** 5 hours  
  - **Owner(s):** [Assign in GitLab]

### Epic E: CI/CD & Reviews

**Goal:** Establish basic automated checks in GitLab CI, and ensure code merges follow best practices.

- **Task E1:** `feat/ci-cd-pipeline`  
  - **Description:**  
    - Configure a GitLab CI pipeline to:  
      - Lint/test the Web Backend (Pytest)  
      - Lint/test the Model Backend (Pytest)  
      - (Optional) Build the React Frontend in a separate job to ensure no compile errors  
    - Trigger Docker builds to confirm each service can build successfully.  
  - **Acceptance Criteria:**  
    1. On every push, the pipeline lints code, runs basic tests, and attempts a Docker build.  
    2. Pipeline failures block merges unless explicitly overridden.  
  - **Estimate:** 8 hours  
  - **Owner(s):** [Assign in GitLab]

---

## 4. Agile Workflow & Coordination

- **Standup Meetings (2x Weekly)**  
  - Quick 15-minute video calls on Tuesday and Friday to discuss progress, highlight blockers, and coordinate tasks.  

- **Task Management via GitLab**  
  - Each task above corresponds to a GitLab Issue.  
  - Use clear labels (e.g., `backend`, `frontend`, `model`, `supabase`, `docs`) to categorize work.  
  - A merge request must reference its corresponding Issue and receive review before merging.  

- **Code Reviews**  
  - All merge requests require at least one approval from another developer or the Project Manager (Alex).  
  - Emphasize consistent style, test coverage, and accurate commit messages as outlined in `CONTRIBUTING.md`.  

- **Continuous Integration**  
  - Address failing pipelines immediately; do not merge changes that break the build or tests.  
  - Each microservice must have at least minimal unit tests that run as part of CI.  

---

## 5. Sprint Review & Retrospective

### Sprint Review (End of Week 2)
1. **Live Demo**  
   - Showcase `docker-compose up --build` spinning up the four core services.  
   - Demonstrate the React SPA landing page and rudimentary navigation.  
   - Show the Model Backend responding to a basic `POST /predict` call.  
2. **Supabase Check**  
   - Verify that the Web Backend can access Supabase to retrieve or store simple data.  

### Retrospective  
- **What Went Well?**  
  - Discuss any successes in setup, collaboration, or CI/CD improvements.  
- **What Could Be Improved?**  
  - Identify blockers encountered (e.g., version conflicts, Docker volume issues) and propose solutions for the next sprint.  
- **Action Items**  
  - Assign follow-up tasks (e.g., refine auth workflows, expand ML model features) to Sprint 2 backlog.

---

## 6. Key Considerations

1. **No Local .env Files**  
   - In accordance with the Project Charter, all environment configurations must be encoded directly in `docker-compose.yml` or container environment blocks.

2. **Maintainability**  
   - Keep folder structures consistent.  
   - Each service should have its own `README.md` detailing how to run and test locally.

3. **Performance**  
   - Focus on correctness and stability for this sprint. Performance optimizations (e.g., caching) can wait until after the baseline is verified.

4. **Security & Access**  
   - Even though we’re only scaffolding Supabase auth in this sprint, secure credentials and minimal open ports in `docker-compose.yml` should be verified.

5. **Scope Alignment**  
   - All tasks align with **Sprint 1** deliverables from the Project Charter. Any additional feature requests will be deferred or added to future sprints as separate backlog items.

---

*This refined Sprint-1 plan ensures a complete, production-ready setup for the Titanic Survivor Prediction Application’s core architecture. By focusing on containerization, a minimal React SPA, a baseline ML pipeline, and an initial CI/CD foundation, the team will establish the solid groundwork needed for subsequent sprints to iterate quickly and add advanced functionality.*  
