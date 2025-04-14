# Sprint 1 – Core Infrastructure & Basic Service Integration

**Sprint Duration:** 2 Weeks  
**Overall Project Duration:** 7–8 Weeks  
**Team Members:** John Doe, Jane Smith, Michael Brown, Sarah Davis, Emily Johnson, David Williams  

## Sprint Goal
Establish a robust foundation by setting up the Docker Compose environment, initializing a basic FastAPI backend with a health-check endpoint, and delivering a minimal React frontend landing page. This sprint provides a production-ready baseline that will be iteratively expanded in later sprints.

---

## 1. Sprint Objectives
- **Environment Configuration:**  
  Configure a Docker Compose setup to orchestrate the core services (frontend, backend, model, and Supabase). Verify that the entire environment runs locally without errors.
  
- **Backend Initialization:**  
  Develop a FastAPI project structure in `app/backend/` with a working `/health` endpoint and proper modularization (routers, models, services, tests). Create a unit test to verify the health-check functionality.
  
- **Frontend Prototype:**  
  Create a React SPA (TypeScript) in `app/frontend/` featuring a basic landing page (header, main content, and footer) styled with Tailwind CSS.
  
- **CI/CD Pipeline Setup:**  
  Configure a basic GitLab CI/CD pipeline to run linting and tests for both backend and frontend code.
  
- **Documentation Update:**  
  Update sprint-related documentation (architecture diagrams, CI/CD instructions, and task breakdown) to support clear communication and future development.

---

## 2. Epics and Tasks

### **Epic A: Environment & Docker Compose Setup**

#### Task A1: Configure Docker Compose ()
- **Description:**  
  Set up a Docker Compose configuration (`docker-compose.yml`) that defines the following services:
  - **Frontend:** React build stage and Nginx serve stage.
  - **Backend:** FastAPI service.
  - **Model:** Placeholder FastAPI ML service.
  - **Supabase:** PostgreSQL container with default credentials.
- **Acceptance Criteria:**  
  - All services build and start locally with a single command.
  - The backend `/health` endpoint is reachable and returns `{"status": "ok"}` (verified via a `curl` or browser test).
- **Assignees:** Jane Smith (primary) & Michael Brown (support)
- **Estimated Time:** 3 hours (including a buffer)

---

### **Epic B: Backend Initialization**

#### Task B1: Scaffold FastAPI Project
- **Description:**  
  Create a basic FastAPI project structure under `app/backend/` including directories for `routers`, `models`, `services`, and `tests`.
- **Acceptance Criteria:**  
  - A `/health` endpoint is implemented in `main.py` that returns `{"status": "ok"}`.
  - The code adheres to PEP 8, with inline comments and clear module separation.
- **Assignees:** Emily Johnson (primary) & David Williams (support)
- **Estimated Time:** 2 hours

#### Task B2: Write Unit Test for Health Endpoint
- **Description:**  
  Develop a unit test in `tests/test_health.py` using pytest, confirming that the `/health` endpoint returns HTTP 200 and the expected JSON response.
- **Acceptance Criteria:**  
  - The test passes consistently with no errors.
- **Assignee:** Emily Johnson  
- **Estimated Time:** 1 hour

---

### **Epic C: Frontend Prototype**

#### Task C1: Initialize React SPA (TypeScript)
- **Description:**  
  Initialize a new React project using Create React App with a TypeScript template in `app/frontend/`.
- **Acceptance Criteria:**  
  - The project builds successfully.
  - The development server is accessible at `http://localhost:3000`.
- **Assignees:** John Doe (primary) with Sarah Davis (support)  
- **Estimated Time:** 1.5 hours

#### Task C2: Implement Basic Landing Page
- **Description:**  
  Develop a landing page component that includes:
  - A header with the title “Titanic Survivor Prediction”
  - A main section with placeholder content
  - A footer with basic copyright.
- **Acceptance Criteria:**  
  - The landing page renders correctly and responsively.
- **Assignee:** Sarah Davis  
- **Estimated Time:** 2 hours

#### Task C3: Integrate Tailwind CSS
- **Description:**  
  Configure Tailwind CSS in the project and ensure the landing page uses Tailwind-based responsive styling.
- **Acceptance Criteria:**  
  - All UI components render with Tailwind-styled classes.
- **Assignee:** Michael Brown  
- **Estimated Time:** 1.5 hours

---

### **Epic D: CI/CD Pipeline Setup**

#### Task D1: Basic CI/CD Configuration
- **Description:**  
  Create a basic `.gitlab-ci.yml` file that defines separate stages for:
  - Linting (using flake8 for backend and ESLint for frontend)
  - Running tests (pytest for FastAPI and Jest for React)
- **Acceptance Criteria:**  
  - The CI/CD pipeline runs on each commit and reports results without errors.
- **Assignee:** Jane Smith  
- **Estimated Time:** 2 hours

#### Task D2: Document CI/CD Process
- **Description:**  
  Update the project README to include concise CI/CD process instructions for team members.
- **Acceptance Criteria:**  
  - The README clearly explains how to monitor and interact with the CI/CD pipeline.
- **Assignee:** Jane Smith  
- **Estimated Time:** 0.5 hours

---

## 3. Agile Workflow & Coordination

- **Daily Standups:**  
  Hold 15-minute standups (e.g., Tuesday and Friday) to update task status, discuss progress, and address any blockers.

- **Task Management:**  
  Utilize GitLab Issues/Boards for tracking tasks with clear descriptions and acceptance criteria.

- **Code Reviews:**  
  All merge requests must be reviewed by the project manager to ensure quality and consistency with coding standards.

- **Collaboration:**  
  Pair programming is encouraged on challenging tasks (e.g., Docker configuration and CI/CD setup).

---

## 4. Sprint Review & Retrospective

- **Sprint Review (End of Week 2):**  
  - Demonstrate the complete Docker Compose environment with all core services running.
  - Verify the backend `/health` endpoint through the unit test.
  - Present the working landing page of the React SPA.
  - Confirm that the CI/CD pipeline executes as expected.
  - Review updated sprint documentation with the team.
  
- **Retrospective:**  
  - Discuss what worked well, any challenges in meeting the estimates, and improvements needed for future sprints.

---

## 5. Key Considerations

- **Maintainability:**  
  Focus on writing modular, well-documented code to facilitate future enhancements.
  
- **Scalability:**  
  Ensure that the Docker Compose setup is flexible enough to support horizontal scaling and later service integrations.
  
- **Flexibility:**  
  Be prepared to adjust time estimates and task assignments based on daily standup feedback.

---

*This Sprint 1 plan forms the baseline for the Titanic Survivor Prediction Application. Its successful execution provides a production-ready foundation on which subsequent features—such as enhanced authentication, full CI/CD integration, and admin functionality—will be developed.*


<!-- # Sprint 1 – Project Foundation for Titanic Survivor Prediction Application

**Sprint Duration:** 2 Weeks  
**Overall Project Duration:** 7–8 Weeks  
**Team Members:** John Doe, Jane Smith, Michael Brown, Sarah Davis, Emily Johnson, David Williams  
**Sprint Goal:** Establish the project’s foundation by configuring the Docker Compose environment, initializing backend & frontend prototypes, integrating initial Supabase settings, setting up CI/CD pipelines, and updating documentation. These efforts ensure maintainability, scalability, and robust performance for further iterations.

---

## 1. Sprint Objectives

- **Environment Configuration:**  
  Configure a Docker Compose environment that orchestrates core services (frontend, backend, model, and Supabase). Validate that the setup runs locally without errors.

- **Backend Initialization:**  
  Develop a basic FastAPI backend skeleton with a health-check endpoint and standardized project layout (routers, models, services). Prepare and run unit tests for the health-check endpoint.

- **Frontend Prototype:**  
  Create a React (TypeScript) SPA prototype featuring a simple landing page with placeholder components (header, main section, and footer).

- **Supabase Integration:**  
  Integrate basic Supabase configuration for authentication and data storage. Document the integration process to support future enhancements.

- **CI/CD Pipeline Setup:**  
  Implement a GitLab CI/CD configuration for automated builds, linting, tests, and deployments for both frontend and backend code.

- **Documentation & Architecture Update:**  
  Update the documentation in the `docs/` folder with architecture diagrams and sprint backlog details to ensure clear communication and future development direction.

---

## 2. Epics, User Stories & Task Breakdown

### **Epic 1: Environment Configuration & Docker Compose Setup**

**User Story 1.1:**  
_As a developer, I want to configure the Docker Compose environment so that all core services run locally with minimal configuration and clear documentation._

#### Tasks:
- **Task 1.1.1:**  
  **Description:** Create a new Git branch for Docker Compose setup.  
  **Branch Name:** `feature/docker-compose-setup`  
  **Assignee:** Jane Smith (primary), Michael Brown (support)  
  **Estimate:** 0.5 hour

- **Task 1.1.2:**  
  **Description:** Define and set up the `docker-compose.yml` file to include the following services:  
  - **Frontend:** React (build stage) and Nginx (serve stage)  
  - **Backend:** FastAPI service  
  - **Model:** FastAPI ML service  
  - **Supabase:** PostgreSQL container with default credentials  
  **Acceptance Criteria:**  
  - Correct port mapping and network configuration  
  - Inline comments explaining environment variables and service roles  
  **Branch Name:** `feature/docker-compose-setup`  
  **Assignee:** Michael Brown and John Doe  
  **Estimate:** 3 hours  
  _If any subtask (e.g., port mapping documentation or Nginx configuration) exceeds 3 hours, break it further into:_
  - **Task 1.1.2a:** Docker Compose file structure and basic service definitions  
  - **Task 1.1.2b:** Detailed inline documentation and variable mapping

- **Task 1.1.3:**  
  **Description:** Run `docker-compose up --build` locally, validate that each service (Frontend, Backend, Model, Supabase) starts without errors, and record any issues encountered.  
  **Branch Name:** `feature/docker-compose-setup`  
  **Assignee:** Jane Smith  
  **Estimate:** 1 hour

---

### **Epic 2: Backend Initialization & Health Check Endpoint**

**User Story 2.1:**  
_As a backend developer, I want to create a basic FastAPI project structure with a `/health` endpoint so that the API framework is ready for further expansion._

#### Tasks:
- **Task 2.1.1:**  
  **Description:** Create a new branch for backend initialization.  
  **Branch Name:** `feature/backend-init`  
  **Assignee:** Emily Johnson (primary), David Williams (support)  
  **Estimate:** 0.5 hour

- **Task 2.1.2:**  
  **Description:** Scaffold the project structure under `app/backend/` with the following folders and files:  
  - `main.py`  
  - Folders: `routers`, `models`, `services`, `tests`  
  **Acceptance Criteria:**  
  - Clearly separated folder structure with placeholder `__init__.py` files as needed  
  **Branch Name:** `feature/backend-init`  
  **Assignee:** Emily Johnson  
  **Estimate:** 1 hour

- **Task 2.1.3:**  
  **Description:** Implement a `/health` endpoint in `main.py` that returns `{ "status": "ok" }`.  
  **Branch Name:** `feature/backend-init`  
  **Assignee:** David Williams  
  **Estimate:** 1 hour

- **Task 2.1.4:**  
  **Description:** Write a unit test in `tests/test_health.py` to verify that the `/health` endpoint returns status code 200 and the correct JSON response.  
  **Branch Name:** `feature/backend-init`  
  **Assignee:** Emily Johnson  
  **Estimate:** 1 hour

- **Task 2.1.5:**  
  **Description:** Ensure code follows PEP 8 guidelines and add inline comments/documentation.  
  **Branch Name:** `feature/backend-init`  
  **Assignee:** David Williams  
  **Estimate:** 0.5 hour

---

### **Epic 3: Frontend Prototype Development**

**User Story 3.1:**  
_As a frontend developer, I want a minimal React SPA with TypeScript to display a placeholder landing page so that the UI structure is in place for further development._

#### Tasks:
- **Task 3.1.1:**  
  **Description:** Create a new branch for the frontend prototype.  
  **Branch Name:** `feature/frontend-prototype`  
  **Assignee:** John Doe (primary), Sarah Davis (support)  
  **Estimate:** 0.5 hour

- **Task 3.1.2:**  
  **Description:** Initialize the React project using Create React App (with TypeScript template) in the `app/frontend/` directory.  
  **Branch Name:** `feature/frontend-prototype`  
  **Assignee:** John Doe  
  **Estimate:** 1 hour

- **Task 3.1.3:**  
  **Description:** Develop a simple landing page component that includes:  
  - A header with the title “Titanic Survivor Prediction”  
  - A main section with placeholder content  
  - A footer with copyright details  
  **Acceptance Criteria:**  
  - The landing page renders without errors on [http://localhost:3000](http://localhost:3000)  
  **Branch Name:** `feature/frontend-prototype`  
  **Assignee:** Sarah Davis  
  **Estimate:** 2 hours

- **Task 3.1.4:**  
  **Description:** Integrate Tailwind CSS for responsive styling.  
  **Branch Name:** `feature/frontend-prototype`  
  **Assignee:** Michael Brown  
  **Estimate:** 1.5 hours

- **Task 3.1.5 (Optional):**  
  **Description:** Add a basic unit test for the landing page using Jest and React Testing Library.  
  **Branch Name:** `feature/frontend-prototype`  
  **Assignee:** John Doe  
  **Estimate:** 1 hour

---

### **Epic 4: Supabase Preliminary Integration**

**User Story 4.1:**  
_As a backend developer, I want placeholder Supabase configuration integrated so that future authentication and data storage can be built upon with minimal friction._

#### Tasks:
- **Task 4.1.1:**  
  **Description:** Create a new branch for Supabase integration.  
  **Branch Name:** `feature/supabase-integration`  
  **Assignee:** Emily Johnson (primary), David Williams (support)  
  **Estimate:** 0.5 hour

- **Task 4.1.2:**  
  **Description:** Set up a secure `.env` file with placeholder Supabase credentials (e.g., URL, API key) and update `app/backend/config.py` to read these variables.  
  **Acceptance Criteria:**  
  - On startup, the backend service logs (or prints) the Supabase configuration values for validation (without exposing secrets in logs).  
  **Branch Name:** `feature/supabase-integration`  
  **Assignee:** Emily Johnson  
  **Estimate:** 1.5 hours

- **Task 4.1.3:**  
  **Description:** Document the Supabase integration process in the README and in a dedicated documentation file (e.g., `docs/supabase-setup.md`).  
  **Branch Name:** `feature/supabase-integration`  
  **Assignee:** David Williams  
  **Estimate:** 1 hour

---

### **Epic 5: CI/CD Pipeline Configuration**

**User Story 5.1:**  
_As a DevOps engineer, I want an automated CI/CD pipeline in GitLab that lints, tests, and builds both the frontend and backend so that integration issues are caught early._

#### Tasks:
- **Task 5.1.1:**  
  **Description:** Create a new branch for CI/CD pipeline configuration.  
  **Branch Name:** `feature/cicd-config`  
  **Assignee:** Jane Smith (primary), Michael Brown (support)  
  **Estimate:** 0.5 hour

- **Task 5.1.2:**  
  **Description:** Write a `.gitlab-ci.yml` file defining separate stages for linting (using flake8 for Python and ESLint for React), running tests (pytest for FastAPI and Jest for React), and building Docker images.  
  **Acceptance Criteria:**  
  - Pipeline executes the defined stages on commit without errors  
  **Branch Name:** `feature/cicd-config`  
  **Assignee:** Jane Smith  
  **Estimate:** 2 hours

- **Task 5.1.3:**  
  **Description:** Test the CI/CD pipeline by committing changes and verifying that the pipeline passes in GitLab.  
  **Branch Name:** `feature/cicd-config`  
  **Assignee:** Michael Brown  
  **Estimate:** 1 hour

- **Task 5.1.4:**  
  **Description:** Update the project documentation with clear instructions on the CI/CD process.  
  **Branch Name:** `feature/cicd-config`  
  **Assignee:** Jane Smith  
  **Estimate:** 0.5 hour

---

### **Epic 6: Documentation & Architecture Update**

**User Story 6.1:**  
_As a team, we need updated documentation that includes refined architecture diagrams and a detailed sprint backlog so that everyone clearly understands Sprint 1 goals and deliverables._

#### Tasks:
- **Task 6.1.1:**  
  **Description:** Create a new branch for documentation updates.  
  **Branch Name:** `feature/docs-update`  
  **Assignee:** Sarah Davis (primary), John Doe (support)  
  **Estimate:** 0.5 hour

- **Task 6.1.2:**  
  **Description:** Update architecture diagrams in `docs/` (using Mermaid or a similar tool) to reflect the current Docker Compose setup and project structure.  
  **Branch Name:** `feature/docs-update`  
  **Assignee:** Sarah Davis  
  **Estimate:** 1.5 hours

- **Task 6.1.3:**  
  **Description:** Merge the sprint backlog (this finalized document) into a dedicated sprint document (e.g., `docs/sprint_1_plan.md`) and make it ready for GitLab issue creation.  
  **Branch Name:** `feature/docs-update`  
  **Assignee:** John Doe  
  **Estimate:** 1 hour

- **Task 6.1.4:**  
  **Description:** Conduct a review of the updated documentation during the daily standup and collect any team feedback.  
  **Branch Name:** `feature/docs-update` (documentation branch; review meeting is tracked in GitLab)  
  **Assignee:** All team members  
  **Estimate:** 0.5 hour (collective feedback session)

---

## 3. Agile Workflow & Coordination

- **Daily Standups:**  
  Short 15-minute sessions (e.g., Tuesday and Friday) to sync on progress, update GitLab issues, and resolve blockers.

- **Task Management:**  
  Utilize GitLab Issues and Boards to track the progress of each task. Ensure each GitLab Issue includes clear descriptions, acceptance criteria, and status updates.

- **Code Reviews:**  
  All merge requests must undergo code reviews by the Project Manager to maintain quality and adherence to coding standards.

- **Continuous Integration:**  
  Monitor the CI/CD pipeline regularly to verify that automated tests and builds succeed after each commit.

- **Collaboration:**  
  Encourage pair programming on complex tasks (e.g., Docker configuration and CI/CD setup) to promote knowledge sharing and enhance maintainability.

---

## 4. Sprint Review & Retrospective Planning

- **Sprint Review (End of Week 2):**  
- Demonstrate the Docker Compose environment with all core services running.
- Show the FastAPI backend with a working `/health` endpoint (with unit tests passing).
- Present the React SPA that displays the landing page.
- Verify that the Supabase configuration is integrated (even as placeholders).
- Confirm that the CI/CD pipeline is executing correctly.
- Review the updated documentation (architecture diagrams and sprint plan) with the team.

- **Retrospective:**  
- Discuss challenges, tasks that exceeded or fell short of estimates, and any process improvements.
- Decide on adjustments for upcoming sprints to further balance workload and enhance maintainability/scalability.

---

## 5. Key Considerations

- **Maintainability:**  
  Write modular code with clear separation of concerns. Ensure proper documentation and inline comments to support future scalability.

- **Scalability:**  
  Design architecture and Docker Compose configurations to easily scale individual services as load increases. Utilize Docker best practices for horizontal scalability.

- **Performance:**  
  Integrate performance monitoring from the start and plan for asynchronous processing when applicable, particularly for API endpoints and CI/CD processes.

---

*This document serves as the collaborative guide for Sprint 1. All team members should update their GitLab Issues/Boards regularly and provide feedback during daily standups and sprint reviews. The successful completion of these tasks will create a strong foundation for the project, with all critical components operational and well-documented.* -->
