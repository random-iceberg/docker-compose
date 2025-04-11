# Sprint 1 – Project Foundation for Titanic Survivor Prediction Application

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

## 2. Sprint Backlog & Task Assignments

The following tasks remain for completion and are aligned with GitLab Issues/Boards. Each task includes a suggested short branch name.

| **Task ID** | **Task Description** | **Acceptance Criteria** | **Responsible Members** | **Branch Name** |
|-------------|----------------------|-------------------------|-------------------------|-----------------|
| **T1.2** | **Docker Compose Setup (Core Services):** Create and validate the `docker-compose.yml` to orchestrate the frontend, backend, model, and Supabase. | - All services (frontend, backend, model, supabase) are defined and correctly port-mapped.<br> - Local validation with `docker-compose up --build` completes without errors. | *John Doe* and *Sarah Davis* | `feature/docker-compose` |
| **T1.3** | **Backend Initialization:** Build a FastAPI project skeleton including a health-check endpoint, basic routing, and a modular project structure (routers, models, services). | - A `/health` endpoint returns `{ "status": "ok" }`.<br> - The project structure follows best practices.<br> - Unit tests for the health-check endpoint pass successfully. | *Michael Brown* and *Sarah Davis* | `feature/backend-init` |
| **T1.4** | **Frontend Prototype Development:** Initialize a React project with TypeScript and create a simple landing page with placeholder components (header, main section, and footer). | - A minimal React SPA renders without errors.<br> - Basic component structure is established and responsive.<br> - Code adheres to React and Tailwind CSS best practices. | *John Doe* and *Jane Smith* | `feature/frontend-prototype` |
| **T1.5** | **Supabase Preliminary Integration:** Configure environment variables and initial authentication settings to integrate Supabase into the backend, along with clear documentation of the integration process. | - Supabase configuration is integrated in the backend (with placeholders for sensitive data).<br> - Documentation clearly explains setup steps and environment variable configuration. | *Emily Johnson* | `feature/supabase-integration` |
| **T1.6** | **CI/CD Pipeline Configuration:** Develop a GitLab CI/CD configuration to automate builds, linting, tests, and deployments for both the frontend and backend services. | - The CI/CD pipeline triggers on commits.<br> - Jobs include linting, testing, and build stages.<br> - Updated pipeline documentation is available in the repository. | *David Williams* and *Emily Johnson* | `feature/cicd-config` |
| **T1.7** | **Documentation & Architecture Update:** Prepare initial architecture diagrams and update project documentation (including sprint goals, backlog items, and task progress) in the `docs/` folder. | - Updated architecture diagrams are present.<br> - Sprint goals and backlog items are clearly documented.<br> - Updates are confirmed during daily standups. | *David Williams* (lead), with contributions from all team members | `feature/docs-update` |

*Note: Tasks that have been completed (e.g., Repository & Branch Strategy) are omitted from this sprint backlog.*

---

## 3. Agile Workflow & Coordination

- **Daily Standups:**  
  Conduct 15-minute daily meetings to discuss progress, identify blockers, and synchronize efforts.

- **Task Management:**  
  Utilize GitLab Issues and Boards to track the progress of each task. Ensure each GitLab Issue includes clear descriptions, acceptance criteria, and status updates.

- **Code Reviews:**  
  All merge requests must undergo code reviews by at least one team member to maintain quality and adherence to coding standards.

- **Continuous Integration:**  
  Monitor the CI/CD pipeline regularly to verify that automated tests and builds succeed after each commit.

- **Collaboration:**  
  Encourage pair programming on complex tasks (e.g., Docker configuration and CI/CD setup) to promote knowledge sharing and enhance maintainability.

---

## 4. Sprint Review & Retrospective Planning

- **Sprint Review (End of Week 2):**  
  Demonstrate the following:
  - A fully functional Docker Compose environment with core services running.
  - A basic FastAPI backend with a working health-check endpoint.
  - A React SPA displaying a placeholder landing page.
  - Preliminary Supabase configuration integrated into the backend.
  - A fully operational CI/CD pipeline.
  - Updated documentation with sprint goals and architectural diagrams.

- **Retrospective:**  
  Gather feedback on the sprint process, identify challenges or impediments, and discuss improvements for subsequent sprints. Focus on maintainability, scalability, and performance issues.

---

## 5. Key Considerations

- **Maintainability:**  
  Write modular code with clear separation of concerns. Ensure proper documentation and inline comments to support future scalability.

- **Scalability:**  
  Design architecture and Docker Compose configurations to easily scale individual services as load increases. Utilize Docker best practices for horizontal scalability.

- **Performance:**  
  Integrate performance monitoring from the start and plan for asynchronous processing when applicable, particularly for API endpoints and CI/CD processes.

---

*This document serves as the collaborative guide for Sprint 1. All team members should update their GitLab Issues/Boards regularly and provide feedback during daily standups and sprint reviews. The successful completion of these tasks will create a strong foundation for the project, with all critical components operational and well-documented.*

---