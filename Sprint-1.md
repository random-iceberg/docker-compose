# Sprint 1 – Full MVP Delivery for Titanic Survivor Prediction Application

**Sprint Duration:** 2 Weeks  
**Team Members & Hours (Approx.):**  
- **Fullstack Developers (40h total each):**
  - Denisa-Iulia Vaidasigan @dv11079
  - Fares Elbermawy @fe18597
  - Huraira Ali @ha06705
  - Kazi Rahman @kr09619
- **Backend & Model Specialists (40h total each):**
  - Lev Malets @lm21363
  - Sameer Kumar @sk20179

---

## 1. Sprint Overview

**Sprint Goal:**  
Deliver a **complete, production-ready MVP** of the Titanic Survivor Prediction Application that includes all major features and integrated services (frontend pages, backend prediction logic, ML model pipeline, admin console, marketing/advertisement integration, and Docker Compose orchestration), *without* incorporating user account or authentication flows (those will come in a later sprint). This sprint focuses on providing fully functional prediction capabilities, accessible immediately upon deployment.

**Key Deliverables:**
1. **Production-Ready Docker Infrastructure**  
   - A single `docker-compose.yml` that orchestrates all containers (frontend, backend, model, and Supabase for data storage).

2. **Complete Frontend (React + TypeScript)**
   - A production-grade landing page with marketing content.
   - A fully functional Survival Calculator UI that collects passenger attributes and displays prediction results.
   - An Admin Console UI for model management, accessible through a dedicated interface (no authentication restrictions yet).

3. **Backend (FastAPI) for Predictions**
   - A `POST /predict` endpoint that receives passenger data and returns survival predictions by calling the Model API.
   - Robust error handling and data validation for prediction requests.
   - Logging of prediction requests for auditing.

4. **ML Model Service**
   - Endpoints for real-time inference (`/inference/`) with a stable, cached ML model.
   - An optional `/training/` endpoint for retraining the model and storing artifacts.

5. **Marketing & Advertisement Integration**
   - Dedicated UI elements (banners, calls to action, etc.) on the landing page highlighting AI courses.

6. **Test Coverage & Final Documentation**
   - Automated unit and integration tests for both frontend and backend.
   - Updated documentation (in each service’s `README.md` and the `docs/` folder) reflecting the final MVP configuration.

---

## 2. Sprint Objectives

1. **Finalize Docker Compose & Deployment**
   - Achieve **zero local configuration**: running `docker-compose up --build -d` should fully deploy the MVP.
   - Define all essential environment variables within the Compose file (no `.env` usage).
   - Verify reliable network calls between containers (frontend → backend → model).

2. **Complete Frontend Implementation**
   - **Landing Page:** Deliver a production-quality design that explains the application’s purpose and highlights AI course ads.
   - **Survival Calculator:** Build a form-based component that collects the necessary passenger attributes (e.g., class, age, sex, fare, embarked) and displays the prediction result.
   - **Admin Console UI:** Implement a basic area to view available models and trigger training operations (no authentication barriers).
   - Ensure the UI is fully responsive on both desktop and mobile.
   - Include basic component and user-flow tests using React Testing Library or Jest.

3. **Robust Backend for Predictions**
   - **Prediction API:** Provide a `POST /predict` endpoint that validates incoming data and returns a structured prediction.
   - Use appropriate HTTP status codes and descriptive error messages.
   - Log all prediction requests for auditing.

4. **ML Model Service**
   - Load and cache a trained Titanic ML model (e.g., Random Forest or SVM) at startup.
   - Expose an `/inference/` endpoint for real-time predictions, returning numeric probabilities or classifications.
   - Provide a `/training/` endpoint to retrain the model, save artifacts, and (optionally) return metrics.
   - Optimize model loading and inference for production performance.

5. **Marketing & Advertisement**
   - Integrate engaging marketing visuals, text blocks, and calls to action that promote AI courses.
   - Deliver a consistent, polished design across all devices.

6. **Automated Testing & Documentation**
   - Implement robust unit and integration test coverage.
   - Update all documentation (`README.md` files, `docs/` folder) so new developers can deploy the MVP with a single command.
   - Ensure automated CI pipelines verify the entire system.

---

## 3. Epics & Task Breakdown

All tasks below must be completed for a production-ready MVP. Each task should map to a GitLab issue with clear acceptance criteria and an assigned owner.  

### Epic A: Production Docker & Environment Setup

- **Task A1: `feat/docker-compose-setup`** [x]
  - **Description:**  
    - Finalize the multi-service Docker Compose configuration for frontend, backend, model, and Supabase (data storage only).
    - Eliminate `.env` usage; define required environment variables directly in the Compose file.
    - Expose and map essential ports (e.g., `3000` for frontend, `8000` for backend, `5000` for model, `5432` for Supabase).
  - **Acceptance Criteria:**  
    1. Running `docker-compose up --build -d` starts all services without errors.
    2. Inter-container communication (e.g., backend ↔ model) is reliable.
    3. The application is reachable at `http://localhost:3000/` without manual config steps.
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab] (Lev Malets @lm21363)

- **Task A2: `feat/ci-cd-prod-build`** [ ]
  - **Description:**  
    - Extend GitLab CI to auto-build Docker images for all services on each commit.
    - Validate images via container-level tests or health checks.
    - Ensure pipeline failures block merges if any container fails to build or start.
  - **Acceptance Criteria:**  
    1. Each push triggers Docker builds for all services.
    2. Automated container health checks pass.
    3. Merge requests are blocked if pipelines fail.
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab] (Lev Malets @lm21363)

### Epic B: Frontend (React + TypeScript + Tailwind)

- **Task B1: `feat/frontend-landing-marketing`** [ ]
  - **Description:**  
    - Deliver a production-grade landing page with integrated marketing content and visuals.
    - Include CTA buttons for the Survival Calculator and Admin Console.
    - Ensure the layout is fully responsive.
  - **Acceptance Criteria:**  
    1. The landing page meets marketing specifications (images, text blocks, CTAs).
    2. The layout is responsive on desktop and mobile.
    3. Users can easily navigate to the Survival Calculator and Admin Console.
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab] (Kazi Rahman @kr09619)

- **Task B2: `feat/survival-calculator-ui`** [ ]
  - **Description:**  
    - Implement a form-based component for collecting passenger attributes (e.g., class, sex, age, fare, embarked).
    - On submit (or in real-time), call the backend to retrieve a prediction.
    - Provide graceful error handling for server downtime or invalid inputs.
  - **Acceptance Criteria:**  
    1. All required input fields are present and validated.
    2. Prediction results are displayed clearly (e.g., success/failure alerts or probabilities).
    3. Errors are handled gracefully with descriptive user feedback.
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab] (Denisa-Iulia Vaidasigan @dv11079, Fares Elbermawy @fe18597)

- **Task B3: `feat/admin-console-frontend`** [x]
  - **Description:**  
    - Create an Admin Console UI showing a list of models (e.g., name, date trained, accuracy).
    - Allow “Train Model” or “Delete Model” actions (calling backend endpoints).
    - Provide a functional, responsive interface without user authentication.
  - **Acceptance Criteria:**  
    1. The admin console lists existing models and relevant metadata.
    2. “Train Model” or “Delete Model” triggers backend endpoints successfully.
    3. The interface is intuitive and responsive.
  - **Estimate:** 8h  
  - **Owner(s):** [Assign in GitLab] (Huraira Ali @ha06705)

### Epic C: Backend & Core APIs (FastAPI)

- **Task C2: `feat/backend-prediction`** [ ]
  - **Description:**  
    - Develop a `POST /predict` endpoint that accepts passenger data, forwards it to the Model API, and returns structured results.
    - Validate input data thoroughly.
    - Log prediction events for auditing.
  - **Acceptance Criteria:**  
    1. The endpoint returns a JSON response with survival probability or status.
    2. Invalid or missing data triggers an HTTP 400 with a descriptive message.
    3. All prediction requests are logged for future auditing.
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab] (Fares Elbermawy @fe18597, Denisa-Iulia Vaidasigan @dv11079)

- **Task C3: `feat/backend-admin-endpoints`** [x]
  - **Description:**  
    - Add endpoints to list models (`GET /models`), initiate training (`POST /models/train`), and delete models (`DELETE /models/{id}`).
    - No authentication is required for this MVP.
  - **Acceptance Criteria:**  
    1. All endpoints return standard JSON and update underlying data (model artifacts) as expected.
    2. Responses are logged for auditing.
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab] (Huraira Ali @ha06705)

### Epic D: Model Microservice (FastAPI)

- **Task D1: `feat/model-service-inference`** [ ]
  - **Description:**  
    - Load the final Titanic ML model (e.g., Random Forest or SVM) at service startup, caching it for performance.
    - Provide a `/inference/` endpoint receiving input features and returning predictions.
    - Handle errors gracefully (e.g., if model loading fails).
  - **Acceptance Criteria:**  
    1. The ML model is loaded only once at startup.
    2. The inference endpoint returns numeric probabilities or classification results.
    3. Logs detail each inference request for traceability.
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab] (Sameer Kumar @sk20179, Lev Malets @lm21363)

- **Task D2: `feat/model-service-training`** [ ]
  - **Description:**  
    - Implement a `/training/` endpoint to retrain the model with the Titanic dataset.
    - Store new model artifacts (`.pkl` files) on a shared volume.
    - Optionally return training metrics (e.g., accuracy, F1 score).
  - **Acceptance Criteria:**  
    1. Training completes without container crashes.
    2. Newly trained model artifacts are saved correctly and can replace or supplement existing ones.
    3. The endpoint returns a status message and (optionally) relevant metrics (e.g., “accuracy: 0.85”).
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab] (Sameer Kumar @sk20179, Lev Malets @lm21363)

### Epic E: Supabase Integration & Data Persistence

*Note: For this sprint, user account management is deferred, but basic Supabase configuration for data storage is included.*

- **Task E1: `feat/supabase-setup-complete`** [ ]
  - **Description:**  
    - Configure Supabase (Postgres + GoTrue) in production mode.
    - Migrate or seed any required database schemas (e.g., logs or model references).
    - Verify backend connectivity to Supabase.
  - **Acceptance Criteria:**  
    1. `docker-compose` successfully starts Supabase with correct credentials.
    2. The backend can create/read/update relevant data and logs.
    3. Any roles or privileges are set appropriately (if needed).
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab] (Lev Malets @lm21363)

- **Task E2: `feat/production-db-handlers`** [x]
  - **Description:**  
    - Implement stable database operations for storing predictions, logs, or admin events.
    - Use transactions and handle potential DB failures gracefully.
  - **Acceptance Criteria:**  
    1. Data persists across app restarts and is queryable for metrics/debugging.
    2. Database errors produce clear error messages and logs.
    3. CI tests confirm successful migrations or queries.
  - **Estimate:** 5h  
  - **Owner(s):** [Assign in GitLab] (Lev Malets @lm21363)

<!-- ### Epic F: Final Testing & Documentation

- **Task F1: `test/unit-integration-e2e`**  
  - **Description:**  
    - Write comprehensive unit tests for backend, frontend, and model microservice components.
    - Create integration tests for key user flows (e.g., prediction requests, model management in the admin console).
    - (Optionally) implement basic E2E tests with Cypress or Playwright on the main “happy paths.”
  - **Acceptance Criteria:**  
    1. All critical code paths have adequate unit and integration test coverage.
    2. CI pipelines block merges if any test fails.
    3. E2E tests pass on the core user journeys.
  - **Estimate:** 6h  
  - **Owner(s):** [Assign in GitLab] 

- **Task F2: `docs/finalize-mvp`**  
  - **Description:**  
    - Refresh all `README.md` files (frontend, backend, model, and root) to reflect final usage instructions.
    - Provide thorough documentation in `docs/` for deploying via `docker-compose up --build -d` and an overview of each service.
  - **Acceptance Criteria:**  
    1. All placeholder references are removed.
    2. A new developer can deploy and test the MVP end to end with the provided instructions.
    3. Documentation accurately represents the final state of the MVP.
  - **Estimate:** 4h  
  - **Owner(s):** [Assign in GitLab] -->

---

## 4. Agile Workflow & Coordination

- **Standup Meetings (2x Weekly):**  
  Brief 15-minute calls to report progress, clear blockers, and plan the next steps.

- **Task Management:**  
  All tasks appear as GitLab issues with acceptance criteria, time estimates, and labels (e.g., `frontend`, `backend`, `model`).

- **Code Reviews:**  
  - Every merge request undergoes peer review for code quality, style adherence, and testing sufficiency.
  - Merges are only allowed if all CI checks pass.

- **Continuous Integration (GitLab CI):**  
  - Each push triggers:
    1. Linting and unit tests for backend, frontend, and model.
    2. Docker builds for all services.
    3. Container-level integration checks.
  - Merge requests are blocked on CI failures.

---

## 5. Sprint Review & Retrospective

**Sprint Review (End of Week 2):**  
1. **Live End-to-End Demo:**  
   - Demonstrate the complete workflow: using the Survival Calculator to obtain predictions and the Admin Console to manage models.
   - Verify that landing-page marketing content displays correctly.
2. **Production-Ready Check:**  
   - Deploy on a fresh environment via `docker-compose up --build -d`; confirm no manual config steps are required.
3. **Testing Verification:**  
   - All unit, integration, and (if implemented) E2E tests pass without regressions.

**Retrospective:**  
- **What Went Well?**  
  - Celebrate successes in delivering a production-ready MVP within one sprint.
- **What Could Be Improved?**  
  - Discuss any time-management challenges or technical blockers.
- **Action Items:**  
  - Document key takeaways for future sprints.

---

## 6. Key Considerations

1. **Production-Ready Features**  
   - No placeholder code remains.
   - The entire system (prediction logic, model management, marketing) is fully operational.

2. **Separation of Concerns**  
   - User registration and authentication will be introduced in Sprint 2.
   - The current MVP focuses on essential predictions, model management, and marketing integration.

3. **Performance & Stability**  
   - Load the ML model once; cache it to ensure high-performance inference.
   - Confirm reliable Docker networking among services.

4. **Documentation Completeness**  
   - All relevant instructions are included so new team members can deploy and test the MVP in one step.

---

*This plan ensures the project achieves a fully functional MVP for Titanic survival predictions—complete with Docker-based deployment, model management, marketing integration, thorough testing, and clear documentation—within the first two-week sprint.* 
