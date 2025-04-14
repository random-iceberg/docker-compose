# Sprint 1 – Foundational Setup and Core Implementation

**Sprint Duration:** 2 Weeks  
**Team Members:**  
- **Fullstack Developers (40h total):** John Doe, Jane Smith, Michael Brown, Sarah Davis  
- **Backend & Model Specialists (20h total):** Emily Johnson, David Williams  

---

## Sprint Goal

Establish a robust and consistent project foundation by ensuring the Docker-based environment is fully configured, that the core frontend and backend structures are integrated, and that the Model API is primed for baseline functionality. By the end of this sprint:

1. **All services** (Frontend, Backend, Model, and Supabase) must launch successfully via `docker-compose up --build`.
2. **Core UI Skeleton** is in place for the React SPA, including rudimentary navigation and placeholders for future components.
3. **Model Service** supports a basic training endpoint and inference endpoint (both mocked or minimally functional).
4. **Initial documentation** is updated to reflect accurate setup, branching, and development guidelines.

---

## 1. Sprint Objectives

1. **Docker & Environment Configuration**  
   - Refine `docker-compose.yml` to ensure smooth local development and alignment with the final production architecture.
   - Confirm each container (frontend, backend, model, and Supabase) can be built and run without extra manual steps.

2. **Frontend React Skeleton**  
   - Create a React-based SPA structure in TypeScript with Tailwind CSS, featuring minimal navigation and placeholders (landing page, dashboard area, etc.).

3. **Baseline Model & Training**  
   - Establish a minimal baseline ML model pipeline using scikit-learn in the Model API service.
   - Verify `data_downloader.py` and Titanic dataset integration.

4. **Core CI/CD and QA**  
   - Integrate or refine basic CI/CD checks (linting, unit tests) to ensure code quality.
   - Perform initial code reviews and maintain an updated project documentation.

---

## 2. Epics, User Stories & Task Breakdown

### Epic 1: **Docker & Environment Configuration**  
**Goal:** Ensure every service (frontend, backend, model, Supabase) runs locally via a single command, with correct networking and shared volumes.

#### Tasks (Fullstack Developers – 8h)
- **Task Name:** `feat/docker-compose-setup`  
  - **Branch:** `feat/docker-compose-setup`  
  - **Description:**  
    - Update `docker-compose.yml` to enforce consistent naming and environment linkage.  
    - Validate the Compose file so that no additional `.env` files are required.  
    - Document any setup steps in `README.md`.  
  - **Estimate:** 8 hours
  - **Assignees:** TODO

### Epic 2: **Frontend React Skeleton**  
**Goal:** Build a foundational React structure in TypeScript with placeholders for future pages and minimal styling with Tailwind.

#### Tasks (Fullstack Developers – 8h)
- **Task Name:** `feat/react-skeleton-setup`  
  - **Branch:** `feat/react-skeleton-setup`  
  - **Description:**  
    - Scaffold the initial React SPA (landing page, simple navigation/header, placeholder for future pages).  
    - Integrate Tailwind CSS for basic styling.  
    - Verify the application compiles and runs on port 3000.  
  - **Estimate:** 8 hours
  - **Assignees:** TODO

### Epic 3: **Basic Auth Flow (Frontend) & Minimal Backend Integration**  
**Goal:** Lay the groundwork for user authentication in the frontend and test minimal endpoints from the backend for health checks.

#### Tasks (Fullstack Developers – 8h)
- **Task Name:** `feat/basic-auth-flow-frontend`  
  - **Branch:** `feat/basic-auth-flow-frontend`  
  - **Description:**  
    - Implement a basic form for login (placeholder or mock submission to a backend endpoint).  
    - Connect the form to a mock or simple FastAPI route (e.g., `/login` or `/health`) to confirm data flow.  
    - Outline a structure for storing JWT tokens or sessions (though no real logic is fully required yet).  
  - **Estimate:** 8 hours
  - **Assignees:** TODO

### Epic 4: **Model Service Baseline & Training Endpoint**  
**Goal:** Provide a minimal functional pipeline to test data ingestion and model training.

#### Tasks (Backend & Model Specialists – 5h each)

1. **Task Name:** `feat/data-integration`  
   - **Branch:** `feat/data-integration`  
   - **Description:**  
     - Validate or enhance `data_downloader.py` to properly download and unpack the Titanic dataset.  
     - Ensure that downloaded data is stored in a volume or accessible path within the model container.  
   - **Estimate:** 5 hours
   - **Assignees:** TODO

2. **Task Name:** `feat/model-baseline`  
   - **Branch:** `feat/model-baseline`  
   - **Description:**  
     - Implement a simple baseline ML model (e.g., Logistic Regression) in the Model API.  
     - Store the trained model as a `.pkl` file using scikit-learn’s serialization.  
     - Provide a short test verifying that training completes and the model file is created.  
   - **Estimate:** 5 hours
   - **Assignees:** TODO

3. **Task Name:** `feat/training-endpoint`  
   - **Branch:** `feat/training-endpoint`  
   - **Description:**  
     - Expand `training_endpoint.py` to accept a minimal set of parameters (e.g., model type).  
     - Return a status indicating the model is training (mock if real-time progress is complex).  
     - Add initial error handling and logging for training requests.  
   - **Estimate:** 5 hours
   - **Assignees:** TODO

4. **Task Name:** `feat/logging-validation`  
   - **Branch:** `feat/logging-validation`  
   - **Description:**  
     - Add robust logging statements in both `inference_endpoint.py` and `training_endpoint.py`.  
     - Implement minimal validation checks (e.g., missing fields in the request body) to avoid silent failures.  
   - **Estimate:** 5 hours
   - **Assignees:** TODO

### Epic 5: **CI/CD, Reviews & Documentation**  

#### Tasks (Fullstack Developers – 16h total)

1. **Task Name:** `feat/ci-cd-setup`  
   - **Branch:** `feat/ci-cd-setup`  
   - **Description:**  
     - Configure GitLab CI (or an existing pipeline) to run lint checks and minimal unit tests on each commit.  
     - Ensure Docker build is triggered to verify images can be built.  
   - **Estimate:** 8 hours
   - **Assignees:** TODO

2. **Task Name:** `docs-and-code-review`  
   - **Branch:** `chore/docs-and-code-review`  
   - **Description:**  
     - Refine `CONTRIBUTING.md` and `README.md` to capture branching conventions, commit messages, etc.  
     - Conduct at least one code review for each of the tasks above.  
     - Summarize findings in a short retrospective document at the end of the sprint.  
   - **Estimate:** 8 hours
   - **Assignees:** TODO

---

## 3. Agile Workflow & Coordination

- **Standup Meetings (2x Weekly):**  
  Short 15-minute calls on Tuesday and Friday for progress updates, issue tracking, and clarifying blockers.

- **Task Management via GitLab Issues/Boards:**  
  - Each task above should have a corresponding GitLab Issue referencing its branch name.  
  - Issues must include acceptance criteria, responsible assignee(s), and progress updates.

- **Code Reviews:**  
  - All merge requests require approval from at least one other developer or from the Project Manager (Alex).  
  - Emphasize best practices, consistent coding style, and thorough commit messages (per `CONTRIBUTING.md`).

- **Continuous Integration:**  
  - Verify that all commits pass automated tests and Docker builds.  
  - Address failing pipelines promptly to avoid blocking subsequent work.

---

## 4. Sprint Review & Retrospective

- **Sprint Review (End of Week 2)**  
  - Demo the Compose setup showing all services running in tandem.  
  - Present the minimal React UI skeleton and a mock login flow.  
  - Show a simple training run within the Model API that saves a baseline model.  

- **Retrospective:**  
  - Discuss which tasks exceeded or fell short of initial estimates.  
  - Identify any major pain points (e.g., environment quirks, service integration issues).  
  - Propose immediate fixes or improvements for the next sprint (e.g., advanced authentication, refined model logic).

---

## 5. Key Considerations

1. **Maintainability:**  
   - Use clear, consistent folder structures.  
   - Keep each service’s `README.md` up-to-date as it evolves.

2. **Scalability:**  
   - Ensure `docker-compose.yml` is structured for potential horizontal scaling in future sprints.

3. **Performance:**  
   - For now, focus on correctness. Advanced optimizations (e.g., concurrency, caching) can be deferred to later sprints.

4. **Team Collaboration:**  
   - Less-experienced Fullstack Developers will focus on tasks with moderate complexity (UI, Docker environment, CI/CD).  
   - More-experienced Backend & Model Specialists will handle core model logic, data pipelines, and advanced logging.

---

*This finalized Sprint 1 plan ensures the project is set up with a robust, production-friendly foundation, minimal friction in local development, and a clear path for future enhancements. All tasks are sized to fit within a two-week sprint, reflecting the team’s available capacity and skill levels.*  
