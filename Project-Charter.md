---
title: Project Charter
---
# Project Charter: Titanic Survivor Prediction Application

**Document Revision:** v2 
**Date:** June 2025  
**Based on:** Project Requirements (Summerterm 2025) & Production Codebase Analysis

---

## Table of Contents

1. Project Title and Description
2. Project Scope and Objectives
3. Detailed Functional Requirements
4. Non-Functional Requirements and Environment Specifications
5. System Architecture
6. Project Timeline and Sprint Structure
7. Interface and Dependency Documentation
8. Team Structure and Responsibilities
9. Detailed Technology Stack Justification
10. Agile Methodologies and Workflow
11. Risk Management Strategy
12. Communication Plan
13. Acceptance Criteria
14. Stakeholder Identification and Expectations
15. Final Sign-Off and Revision History

---

## 1. Project Title and Description

**Title:**  
**Titanic Survivor Prediction Application**

**Description:**  
The Titanic Survivor Prediction Application is a production-ready, containerized web application that predicts Titanic passenger survival using machine learning algorithms while simultaneously serving as an advertisement platform for AI courses. The application consists of four microservices—**Web Frontend** (React SPA), **Web Backend** (FastAPI), **Model Backend** (FastAPI ML service), and **PostgreSQL Database**—orchestrated via Docker Compose with Nginx reverse proxy integration.

The application implements real-time survival predictions, user authentication with role-based access control, an administrative console for model management, and comprehensive marketing integration. Built following agile methodologies and containerized for zero-configuration deployment, it demonstrates production-grade software engineering practices including automated CI/CD pipelines, comprehensive testing, and scalable microservices architecture.

---

## 2. Project Scope and Objectives

### Scope

- **Frontend (React SPA):**  
  Single Page Application using React, TypeScript, and Tailwind CSS, optimized for mobile and desktop with Nginx reverse proxy integration.

- **Backend (FastAPI):**  
  RESTful API service handling business logic, user authentication (JWT), prediction coordination, and admin operations.

- **Model Backend (FastAPI ML Service):**  
  Dedicated microservice for ML model training, inference, and persistence using scikit-learn with pickle serialization.

- **Database (PostgreSQL):**  
  Self-hosted PostgreSQL with custom initialization scripts, user management, prediction history, and model metadata storage.

- **Containerization & Orchestration:**  
  Complete Docker containerization with multi-environment compose configurations (development, production-local, production-registry).

- **CI/CD Pipeline:**  
  GitLab CI/CD with automated builds, testing (unit, integration, E2E), Docker image publishing, and deployment verification.

### Objectives

1. **Zero-Configuration Deployment:**  
   Single-command deployment (`docker compose up --build`) on Ubuntu Noble Numbat 24.04 LTS.

2. **ML-Powered Predictions:**  
   Implement 5 scikit-learn algorithms (Random Forest, SVM, Decision Tree, KNN, Logistic Regression) with model persistence and training capabilities.

3. **Role-Based Access Control:**  
   Anonymous users access limited models; authenticated users access all models and prediction history; admin users manage model lifecycle.

4. **Production-Grade Quality:**  
   Comprehensive testing coverage, structured logging, health monitoring, and security best practices.

5. **Marketing Platform:**  
   Integrated advertisement content promoting AI courses with engaging landing page and social sharing capabilities.

6. **Scalable Architecture:**  
   Microservices design enabling independent scaling, monitoring, and maintenance of each component.

---

## 3. Detailed Functional Requirements

### 3.1. Landing Page and User Engagement

**Implementation Status:** ✅ Complete  
- Interactive landing page explaining application functionality and AI course promotion
- Responsive navigation with mobile hamburger menu for screens < 1000px
- Marketing content integration with call-to-action buttons
- Social sharing buttons for Facebook, Twitter, LinkedIn
- Smooth animations and glassmorphism design elements

### 3.2. User Authentication and Account Management

**Implementation Status:**  ❎ In Progress  
- **Registration:** Email and password-based account creation with bcrypt hashing
- **Login:** JWT-based authentication with 1-hour token expiration
- **Session Management:** HTTP-only cookies for secure token storage
- **Role-Based Access:**
  - **Anonymous:** Access to Random Forest and SVM models only
  - **Authenticated Users:** Access to all models and prediction history
  - **Admin Users:** Full model management capabilities

### 3.3. Survival Calculator

**Implementation Status:** ✅ Complete  
- **Required Input Fields:**
  - Passenger Class: 1st, 2nd, 3rd class selection
  - Sex: Male/Female selection
  - Age: 0-119 years (number input with validation)
  - Siblings/Spouses: 0-8 count
  - Parents/Children: 0-6 count
  - Embarkation Port: Cherbourg (C), Queenstown (Q), Southampton (S)
  - Traveled Alone: Boolean checkbox
  - Cabin Known: Boolean checkbox

- **User Experience:**
  - Real-time form validation with inline error messages
  - Reset button for clearing all inputs
  - Responsive grid layout for mobile and desktop
  - Prediction results with survival probability and clear status indication

- **Model Selection & Prediction Display:**
  - Anonymous users: Single model selection (RF or SVM)
  - Authenticated users: Multiple model selection
  - Clear "Survived" or "Did not survive" results with probability percentages

### 3.4. Prediction History

**Implementation Status:** ❎ In Progress  
- Persistent storage of last 10 predictions for authenticated users
- Tabular display with timestamp, input summary, and results
- Accessible via dedicated dashboard route
- Automatic cleanup of older predictions

### 3.5. Admin Console and Model Management

**Implementation Status:** ✅ Complete  
- **Model Listing:** View all trained models with metadata (algorithm, features, accuracy, creation date)
- **Model Training:** 
  - Feature selection from 8 available features
  - Algorithm selection (RF, SVM, DT, KNN, LR)
  - Custom model naming
  - Background training with progress indicators
- **Model Deletion:** Remove models with confirmation dialog
- **Model Persistence:** Automatic saving to Docker volumes for container restart survival

### 3.6. Advertisement and Marketing Integration

**Implementation Status:** ✅ Complete  
- Dedicated portfolio section showcasing AI course offerings
- Integrated marketing narrative throughout landing page
- Call-to-action buttons linking to course enrollment
- Visual testimonials and success story integration
- Mobile-optimized marketing content

---

## 4. Non-Functional Requirements and Environment Specifications

### 4.1. Containerization and Deployment

**Implementation Status:** ✅ Complete  
- **Docker Architecture:** All services containerized with multi-stage builds
- **Compose Configurations:**
  - `compose.dev.yaml`: Development with hot reload and volume syncing
  - `compose.prod-local.yaml`: Production build from local source
  - `compose.prod-registry.yaml`: Production deployment from GitLab registry
- **Network Isolation:** Services communicate over isolated Docker network
- **Volume Persistence:** PostgreSQL data, model artifacts, and pgAdmin configuration persisted

### 4.2. CI/CD and Automated Testing

**Implementation Status:** ✅ Complete  
- **GitLab CI/CD Pipeline:**
  - Automated builds triggered on every commit
  - Unit and integration tests (pytest for backend, Jest/React Testing Library for frontend)
  - Docker image builds and registry publishing
  - Code quality checks (ruff, prettier, eslint)
- **Testing Coverage:**
  - Backend: Comprehensive pytest suites with authentication, prediction, and model management tests
  - Frontend: Component testing and user flow validation
  - Model Service: ML pipeline and API endpoint testing
- **Image Management:** Semantic versioning with automated registry cleanup

### 4.3. Performance and Scalability

**Implementation Status:** ✅ Complete  
- **Model Caching:** ML models loaded once at startup for fast inference
- **Database Optimization:** Connection pooling and indexed queries
- **Static Asset Optimization:** Nginx serving with gzip compression
- **Health Monitoring:** Health check endpoints for all services
- **Resource Efficiency:** Alpine-based images and optimized container resource usage

---

## 5. System Architecture

The application follows a microservices architecture with clear separation of concerns:

```mermaid
architecture-beta
    group containers(cloud)[Docker Network]

    service postgres(disk)[PostgreSQL Database] in containers
    service pgadmin(database)[pgAdmin GUI] in containers
    service model(server)[Model Backend] in containers
    service frontend(internet)[Web Frontend + Nginx] in containers
    service backend(server)[Web Backend] in containers

    frontend:L -- R:backend
    backend:L -- R:postgres
    backend:T -- B:model
    postgres:B -- T:pgadmin
```

### Service Communication

- **Frontend ↔ Backend:** RESTful API over Docker network with Nginx proxy
- **Backend ↔ Model Service:** Direct HTTP calls for inference and training
- **Backend ↔ PostgreSQL:** SQLAlchemy async ORM with connection pooling
- **External Access:** Only frontend (port 8080) and pgAdmin (port 5050) exposed

### Data Flow

1. **User Request:** Frontend → Nginx → Backend
2. **Prediction:** Backend → Model Service → ML Inference → Response
3. **Authentication:** Backend → PostgreSQL → JWT Generation
4. **Model Training:** Admin → Backend → Model Service → Async Training → Persistence

---

## 6. Project Timeline and Sprint Structure

**Methodology:** Scrum with 3 sprints of 3 weeks each

### Sprint Deliverables

| Sprint | Duration | Focus Area | Key Deliverables |
|--------|----------|------------|------------------|
| **Sprint 1** | Weeks 1-3 | Foundation & Core Infrastructure | Complete dockerized stack skeleton, admin console UI, survival calculator interface, backend API skeleton with basic endpoints |
| **Sprint 2** | Weeks 4-6 | Full Feature Implementation & Integration | Complete prediction flow, model training/management, polished UI/UX, CI/CD pipeline, comprehensive testing, production-ready deployment |
| **Sprint 3** | Weeks 7-9 | Authentication & Final Requirements | User authentication (login/signup), known issue resolution, final requirement completion, documentation finalization, stakeholder demo |

### Milestone Achievement

- **✅ Sprint 1 Complete:** Foundational architecture with skeleton implementations across all services
- **✅ Sprint 2 Complete:** Fully functional MVP with prediction capabilities, admin console, and production deployment
- **🔄 Sprint 3 In Progress:** Authentication implementation and final requirement completion

### Sprint Details

**Sprint 1 Achievements:**
- Docker Compose orchestration with all services
- Admin console user interface for model management
- Survival calculator form with input validation
- Backend API skeleton with health checks and basic structure
- Initial CI/CD pipeline setup

**Sprint 2 Achievements:**
- Complete prediction workflow (frontend → backend → model service)
- Model training and persistence functionality
- Polished landing page with marketing integration
- Comprehensive testing suite (unit, integration)
- Production-ready Docker configurations
- Full CI/CD pipeline with automated testing and registry publishing

**Sprint 3 Goals:**
- JWT-based user authentication system
- Login and signup functionality with secure password handling
- Resolution of identified technical debt and known issues
- Final requirement validation and completion
- Documentation updates and final presentation preparation

---

## 7. Interface and Dependency Documentation

### API Specifications

- **Backend API:** OpenAPI/Swagger documentation at `/docs` endpoint
- **Model Service API:** Dedicated Swagger UI for ML operations
- **Authentication Endpoints:** `/auth/signup`, `/auth/login`, `/auth/check`
- **Prediction Endpoints:** `/predict`, `/predict/history`
- **Admin Endpoints:** `/models/*` with RBAC protection

### Database Schema

- **Users Table:** Authentication and role management
- **Predictions Table:** Prediction history with JSON storage
- **Models Table:** ML model metadata and relationships
- **Features Table:** Available feature definitions

### External Dependencies

- **Container Images:** Python 3.13, Node 22, PostgreSQL 17, Nginx stable
- **ML Libraries:** scikit-learn, pandas, numpy (pinned versions)
- **Web Frameworks:** FastAPI, React 19, Tailwind CSS 3.4

---

## 8. Team Structure and Responsibilities

### Development Team (7 Members)

**Lead Developer & Project Manager:**
- **Alex** - Architecture design, CI/CD configuration, documentation coordination

**Full-Stack Developers:**
- **Denisa-Iulia Vaidasigan (@dv11079)** - Frontend components, form validation, UI/UX
- **Fares Elbermawy (@fe18597)** - Backend endpoints, authentication, testing
- **Huraira Ali (@ha06705)** - Admin console, component library, code refactoring
- **Kazi Rahman (@kr09619)** - Landing page, marketing integration, authentication hooks

**Backend & ML Specialists:**
- **Lev Malets (@lm21363)** - Database design, CI/CD, container orchestration
- **Sameer Kumar (@sk20179)** - ML model implementation, training pipeline, inference optimization

### Collaboration Model

- **Cross-functional ownership:** All members contribute to testing and code review
- **Expertise areas:** Specialized knowledge while maintaining full-stack awareness
- **Pair programming:** Complex features developed collaboratively
- **Knowledge sharing:** Regular technical discussions and documentation updates

---

## 9. Detailed Technology Stack Justification

### Frontend Stack

**React 19 + TypeScript + Tailwind CSS**
- **React 19:** Latest features including concurrent rendering and improved hydration
- **TypeScript:** Type safety ensuring production code quality and developer experience
- **Tailwind CSS:** Utility-first styling enabling rapid, consistent UI development
- **Custom Components:** Reusable component library (Alert, Button, Card, Input, etc.)

### Backend Stack

**Python + FastAPI + SQLAlchemy**
- **FastAPI:** High-performance async framework with automatic OpenAPI documentation
- **SQLAlchemy (Async):** Type-safe ORM with async/await support for PostgreSQL
- **Pydantic:** Data validation and serialization ensuring API contract compliance
- **Pytest:** Comprehensive testing framework with async support

### ML Stack

**scikit-learn + Pickle Persistence**
- **scikit-learn:** Industry-standard ML library implementing required algorithms
- **Pickle Serialization:** Model persistence across container restarts
- **Feature Engineering:** Comprehensive preprocessing pipeline matching Titanic dataset
- **5 Algorithm Support:** RF, SVM, DT, KNN, LR with configurable hyperparameters

### Infrastructure Stack

**Docker + PostgreSQL + Nginx**
- **Docker Multi-stage Builds:** Optimized images for development and production
- **PostgreSQL 17:** ACID-compliant database with custom initialization scripts
- **Nginx:** High-performance reverse proxy and static file serving
- **GitLab CI/CD:** Automated testing, building, and registry management

---

## 10. Agile Methodologies and Workflow

### Scrum Implementation

**Sprint Ceremonies:**
- **Planning:** Sprint backlog creation with story point estimation
- **Daily Standups:** 2x weekly progress updates and blocker identification
- **Sprint Review:** Stakeholder demonstrations and feedback collection
- **Retrospectives:** Process improvement and team development

**Development Practices:**
- **Git Workflow:** Feature branches with mandatory code review
- **Conventional Commits:** Semantic commit messages for automated changelog
- **CI/CD Integration:** Automated testing blocking merge on failures
- **Issue Tracking:** GitLab issues with clear acceptance criteria

### Quality Assurance

**Testing Strategy:**
- **Unit Tests:** ≥80% coverage requirement for all services
- **Integration Tests:** API endpoint and database interaction validation
- **E2E Tests:** Playwright automation for critical user journeys
- **Manual Testing:** UI/UX validation and edge case verification

---

## 11. Risk Management Strategy

### Technical Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|-------------------|
| **Model Training Performance** | Medium | High | Async processing, timeout handling, progress indicators |
| **Database Connection Issues** | Low | High | Connection pooling, retry logic, health checks |
| **Container Resource Limits** | Medium | Medium | Resource monitoring, horizontal scaling capability |
| **Authentication Security** | Low | High | JWT best practices, bcrypt hashing, HTTPS enforcement |

### Project Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|-------------------|
| **Scope Creep** | Medium | Medium | Strict backlog management, stakeholder approval process |
| **Integration Complexity** | Low | High | Early integration testing, API contract validation |
| **Team Coordination** | Low | Medium | Regular standups, clear documentation, pair programming |
| **Deployment Issues** | Low | High | Multi-environment testing, rollback procedures |

---

## 12. Communication Plan

### Internal Communication

**Regular Meetings:**
- **Standups:** Tuesdays & Fridays, 15-minute progress updates
- **Sprint Planning:** Start of each 2-week sprint cycle
- **Technical Discussions:** Ad-hoc for architecture and implementation decisions

**Communication Channels:**
- **WhatsApp Group:** `team/random_iceberg` for immediate coordination
- **GitLab Issues:** Formal task tracking and requirement documentation
- **Code Reviews:** Technical discussions via merge request comments

### External Communication

**Stakeholder Engagement:**
- **Sprint Reviews:** Bi-weekly demonstrations to course instructor
- **Documentation Updates:** Real-time updates in GitLab wiki
- **Final Presentation:** Comprehensive project demonstration and individual contributions

---

## 13. Acceptance Criteria

### Deployment Requirements ✅

- [x] **Zero-Configuration Deployment:** `docker compose up --build` successful on Ubuntu 24.04 LTS
- [x] **Service Health:** All containers start successfully with passing health checks
- [x] **Network Connectivity:** Internal service communication functioning correctly
- [x] **External Access:** Application accessible at `http://localhost:8080`

### Functional Requirements ✅

- [ ] **User Authentication:** Registration, login, JWT token management
- [x] **Survival Calculator:** All required input fields with validation
- [x] **Model Selection:** Role-based access to different model sets
- [ ] **Prediction History:** Last 10 predictions for authenticated users
- [x] **Admin Console:** Model listing, training, deletion with background processing
- [x] **Landing Page:** Marketing content with navigation and social sharing

### Technical Requirements ✅

- [x] **ML Algorithms:** RF, SVM, DT, KNN, LR implemented and functional
- [x] **Model Persistence:** Trained models survive container restarts
- [x] **Database Integration:** PostgreSQL with proper schema and relationships
- [x] **CI/CD Pipeline:** Automated testing and Docker image publishing
- [x] **Code Quality:** Unit test coverage ≥80%, linting, formatting checks

### Browser Compatibility ✅

- [x] **Chrome ≥ 119:** Full functionality and responsive design
- [x] **Firefox ≥ 122:** Complete feature support and performance
- [x] **Safari ≥ 16.1:** Mobile and desktop compatibility

---

## 14. Stakeholder Identification and Expectations

### Primary Stakeholders

**Course Instructor (Prof. Dr. Christoph Schober)**
- **Expectation:** Production-quality application demonstrating agile methodologies and ML integration
- **Success Criteria:** All project requirements met, comprehensive documentation, successful deployment
- **Engagement:** Sprint reviews, final presentation, technical assessment

**Development Team (7 Members)**
- **Expectation:** Collaborative learning environment with clear technical guidance
- **Success Criteria:** Individual contribution demonstration, skill development, project completion
- **Engagement:** Daily development, code reviews, knowledge sharing sessions

**End Users (Prof. Dr. Christoph Schober)**
- **Expectation:** Intuitive, reliable prediction interface with educational value
- **Success Criteria:** Seamless user experience, accurate predictions, responsive design
- **Engagement:** UI/UX testing, feedback incorporation, accessibility validation

### Secondary Stakeholders

**Marketing Director (Conceptual)**
- **Expectation:** Effective AI course promotion through engaging application experience
- **Success Criteria:** Compelling landing page, integrated marketing content, social sharing capabilities
- **Engagement:** Content review, brand alignment, promotional strategy validation

---

## 15. Final Sign-Off and Revision History

### Document Revision History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| **v1.0** | May 2025 | Initial charter creation | Development Team |
| **v1.5** | May 2025 | Sprint planning and architecture refinement | Development Team |
| **v2** | June 2025 | Requirements alignment and codebase accuracy | Project Team |

### Technical Validation

This charter has been validated against:
- ✅ **Project Requirements Document** (Summerterm 2025)
- ✅ **Production Codebase** (Docker Compose, Services, Documentation)
- ✅ **Sprint Deliverables** (Completed features and implementations)
- ✅ **Architecture Implementation** (Actual microservices and database design)

### Sign-Off Confirmation

The development team confirms this charter accurately represents the implemented solution and meets all specified project requirements for the Titanic Survivor Prediction Application.

**Team Leads:**
- **Alex** – Lead Developer & Project Manager
- **Lev Malets** – Backend & Infrastructure Specialist  

**Full-Stack Development Team:**
- **Denisa-Iulia Vaidasigan** – Frontend Architecture & Components
- **Fares Elbermawy** – Backend API & Authentication
- **Huraira Ali** – Admin Console & Component Library
- **Kazi Rahman** – Landing Page & Marketing Integration
- **Sameer Kumar** – ML Model Implementation & Training Pipeline

---

*This revised charter represents the final, production-validated specification for the Titanic Survivor Prediction Application. All sections reflect actual implementation status, proven technology choices, and validated architecture decisions. The document serves as the definitive reference for project completion assessment and future maintenance activities.*

---

*Prepared by team/random_iceberg • Updated June 2025 • Based on Project Requirements (Summerterm 2025) and Production Codebase Analysis*