---
title: Sprint 3 – Authentication & Production Release
revision: v1 · 16 June 2025
---

> **Context**  
> *Sprint 2 delivered a containerized application with basic model training and prediction capabilities, but lacks authentication, complete model management, and several critical UI components. Sprint 3 completes the project by implementing authentication, fixing structural issues, and preparing the final deliverable.*

---

## 1 · Sprint time-box & velocity

| Role                   | Member           | Allocation (hrs/3 w) |
|------------------------|------------------|----------------------|
| **Lead Dev / CI**      | **Lev @lm21363** | 21                   |
| Full-stack Dev         | Denisa @dv11079  | 21                   |
| Full-stack Dev         | Fares @fe18597   | 21                   |
| Full-stack Dev         | Huraira @ha06705 | 21                   |
| Full-stack Dev         | Kazi @kr09619    | 21                   |
| Back-end & ML          | Sameer @sk20179  | 21                   |

*Capacity = **126 h** (6 members × 7 h/week × 3 weeks).*

**Sprint window:** 16 June → 6 July 2025 (3 weeks)  
**Sprint introduction:** Friday, 20 June 2025

---

## 2 · Sprint Goal (definition of success)

Deliver a **production-ready application** that:
1. **Fixes critical structural issues**: Model synchronization, complete input forms, and multi-model selection
2. **Implements full authentication**: JWT-based signup/login with role-based access control (admin vs user)
3. **Meets all project requirements**: Complete feature set as specified in Project Requirements document
4. **Passes quality gates**: E2E test coverage, browser compatibility, and CI/CD pipeline
5. **Delivers presentation materials**: Demo video and presentation slides for final submission

**Week 1 Focus:** Critical fixes and codebase stabilization  
**Weeks 2-3 Focus:** Authentication implementation and presentation preparation

---

## 3 · Critical Issues (Week 1 Priority)

### 🚨 Epic A: Model Management Synchronization
**Problem:** Models exist as pickle files in model service but aren't visible in admin console due to backend-model service disconnect.

### 🚨 Epic B: Complete Calculator Input Form  
**Problem:** Missing fare (0-500$) and title (Master, Miss, Mr, Mrs, Rare) inputs in survival calculator.

### 🚨 Epic C: Multi-Model Selection & Prediction
**Problem:** No model selection UI; professor requires ability to run multiple models in single prediction call.

---

## 4 · Work breakdown structure

### 🔥 **WEEK 1: Critical Fixes (June 16-22)**

#### Epic A: Model Management Synchronization [CRITICAL]

| ID   | Task                                    | Owner   | Est h | Acceptance Criteria |
|------|-----------------------------------------|---------|-------|---------------------|
| **A1** | `fix/backend-model-service-sync`      | Huraira | 8     | Backend queries model service `/models` endpoint; admin console shows all trained models including defaults (rf, svm, lr, knn). |
| **A2** | `fix/model-metadata-persistence`      | Huraira | 4     | Model training updates both pickle files AND database records; consistent state between services. |

#### Epic B: Complete Calculator Input Form [CRITICAL]

| ID   | Task                                    | Owner | Est h | Acceptance Criteria |
|------|-----------------------------------------|-------|-------|---------------------|
| **B1** | `feat/fare-input-component`           | Kazi  | 4     | Add fare input (0-500$) to calculator form; remove hard-coded fare value from backend. |
| **B2** | `feat/title-input-component`          | Kazi  | 6     | Add title dropdown (Master, Miss, Mr, Mrs, Rare) to calculator; remove hard-coded title from backend. |
| **B3** | `fix/backend-remove-hardcoded-values` | Kazi  | 3     | Update backend prediction service to use actual fare/title from frontend instead of hardcoded values. |

#### Epic C: Multi-Model Selection & Prediction [CRITICAL]

| ID   | Task                                      | Owner   | Est h | Acceptance Criteria |
|------|-------------------------------------------|---------|-------|---------------------|
| **C1** | `feat/model-selection-ui`               | Huraira | 6     | Model selection checkboxes in calculator; anonymous users limited to RF/SVM; logged users can select multiple models. |
| **C2** | `feat/multi-model-prediction-backend`   | Huraira | 8     | Backend accepts array of model IDs; returns prediction results for each selected model. |
| **C3** | `feat/multi-model-results-display`      | Huraira | 4     | Frontend displays prediction results for each selected model in organized layout. |

#### Epic D: Codebase Revision & Polish [NON-ESSENTIAL]

| ID   | Task                                    | Owner  | Est h | Acceptance Criteria |
|------|-----------------------------------------|--------|-------|---------------------|
| **D1** | `refactor/frontend-component-cleanup`  | Fares  | 6     | Consolidate duplicate components; improve TypeScript types; mobile responsiveness fixes. |
| **D2** | `refactor/backend-error-handling`      | Fares  | 4     | Standardize error responses; improve validation messages; add request correlation IDs. |
| **D3** | `feat/prediction-history-enhancement`  | Denisa | 5     | Enhanced history view with filtering, sorting, export functionality. |
| **D4** | `feat/admin-dashboard-improvements`    | Denisa | 5     | Model training progress indicators; batch operations; training job queue. |
| **D5** | `test/model-service-integration`       | Sameer | 6     | Comprehensive integration tests for model training/inference endpoints. |
| **D6** | `feat/model-performance-metrics`       | Sameer | 6     | Display training metrics (precision, recall, F1) in admin console; model comparison tools. |
| **D7** | `feat/data-visualization-dashboard`    | Sameer | 8     | Charts showing prediction trends, model accuracy over time, feature importance. |
| **D8** | `chore/code-documentation`             | Lev    | 4     | Update API documentation; add inline code comments; improve README files. |

### 🔐 **WEEKS 2-3: Authentication & Finalization (June 23 - July 6)**

#### Epic E: Authentication System

| ID   | Task                                    | Owner | Est h | Acceptance Criteria |
|------|-----------------------------------------|-------|-------|---------------------|
| **E1** | `feat/user-registration-backend`      | Lev   | 6     | `/auth/signup` endpoint with email/password validation; bcrypt password hashing. |
| **E2** | `feat/jwt-authentication-backend`     | Lev   | 6     | `/auth/login` endpoint returning JWT tokens; token verification middleware. |
| **E3** | `feat/user-roles-rbac`                | Kazi  | 8     | User roles (admin/user); RBAC middleware protecting admin routes; database schema. |
| **E4** | `feat/frontend-auth-integration`      | Kazi  | 8     | Login/signup forms; JWT token management; protected route components. |
| **E5** | `feat/admin-route-protection`         | Huraira | 4   | Admin console requires authentication; model management restricted to admin users. |

#### Epic F: Quality Assurance

| ID   | Task                                | Owner | Est h | Acceptance Criteria |
|------|-------------------------------------|-------|-------|---------------------|
| **F1** | `test/e2e-authentication-flow`    | Lev   | 8     | Playwright tests covering signup → login → predict → admin workflows. |
| **F2** | `test/cross-browser-compatibility` | Lev   | 4     | Verify functionality on Chrome ≥119, Firefox ≥122, Safari ≥16.1. |
| **F3** | `ci/production-deployment-test`    | Lev   | 4     | CI pipeline tests full deployment on clean Ubuntu 24.04 environment. |

#### Epic G: Presentation & Documentation

| ID   | Task                                    | Owner  | Est h | Acceptance Criteria |
|------|-----------------------------------------|--------|-------|---------------------|
| **G1** | `docs/demo-video-production`          | Fares  | 8     | Professional demo video (5-10 min) showcasing all features; screen recording with narration. |
| **G2** | `docs/presentation-slides`            | Denisa | 8     | 10-15 slides covering architecture, features, individual contributions; professional design. |
| **G3** | `docs/final-documentation-update`     | Sameer | 6     | Complete README files; deployment instructions; architecture diagrams; feature documentation. |
| **G4** | `docs/individual-contribution-slides` | ALL    | 2×6   | Each team member creates personal contribution slide for presentation. |

*Total planned effort = **125 h** (within capacity 126 h).*

---

## 5 · Project Requirements Compliance Checklist

### Functional Requirements Status

#### ✅ Completed
- [x] Landing page with navigation
- [x] Basic survival calculator (partial)
- [x] Admin model training and deletion
- [x] Prediction history for logged users

#### 🔧 In Progress (Week 1)
- [ ] **Complete passenger definition**: Add fare (0-500$) and title inputs
- [ ] **Model selection**: Anonymous (RF/SVM only) vs Logged users (any combination)
- [ ] **Continuous prediction updates**: Real-time updates on input change

#### 🔐 Authentication (Weeks 2-3)
- [ ] User registration with email/password
- [ ] User login with authentication
- [ ] Role-based access control (admin vs user)

### Non-Functional Requirements Status

#### ✅ Infrastructure Completed
- [x] Docker containerization
- [x] FastAPI backend
- [x] React frontend with TypeScript
- [x] GitLab CI/CD pipeline
- [x] Docker Compose orchestration

#### 🔧 In Progress
- [ ] **E2E Tests**: Cypress/Playwright implementation
- [ ] **Browser Compatibility**: Chrome ≥119, Firefox ≥122, Safari ≥16.1
- [ ] **Mobile Optimization**: Complete responsive design

---

## 6 · Weekly Focus Areas

### Week 1 (June 16-22): 🔥 Critical Fixes
**Primary Owners:** Huraira, Kazi  
**Support:** Fares, Denisa, Sameer, Lev

**Must Complete:**
- Model synchronization between backend and model service
- Complete calculator form (fare + title inputs)
- Multi-model selection and prediction

**Secondary Tasks:**
- Code cleanup and polish (non-blocking)
- Enhanced features and documentation

### Week 2 (June 23-29): 🔐 Authentication
**Primary Owners:** Lev, Kazi, Huraira  
**Support:** Others on presentation prep

**Must Complete:**
- User registration and login system
- JWT authentication with role-based access
- Protected admin routes

### Week 3 (June 30 - July 6): 📋 Finalization
**All Team Members**

**Must Complete:**
- E2E test suite
- Demo video and presentation slides
- Final documentation and deployment verification

---

## 7 · Definition of Done (Final Release)

| Area             | Completion Criteria |
|------------------|---------------------|
| **Functionality** | All Project Requirements implemented; calculator accepts all inputs; multi-model prediction working |
| **Authentication** | Complete signup/login flow; admin routes protected; JWT token management |
| **Quality** | E2E tests covering main user journeys; cross-browser compatibility verified |
| **Deployment** | Single-command deployment (`docker compose up --build -d`) on clean Ubuntu 24.04 |
| **Documentation** | Complete README files; demo video; presentation slides ready |
| **Presentation** | 10-15 slides; individual contribution slides; demo video 5-10 minutes |

---

## 8 · Risk Management

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Week 1 critical fixes not completed** | High | Daily standups; pair programming; scope reduction if needed |
| **Authentication complexity underestimated** | Medium | Start simple with basic JWT; defer advanced features |
| **E2E test implementation delays** | Medium | Focus on core user journeys; parallel development |
| **Demo video quality issues** | Low | Early draft review; professional editing tools |

---

## 9 · Sprint Ceremonies

- **Daily Standups:** Mon/Wed/Fri 16:00 CEST (15 min)
- **Sprint Introduction:** Fri 20 June 16:00 CEST (Sprint 3 kickoff)
- **Mid-sprint Review:** Fri 27 June 16:00 CEST (Authentication checkpoint)
- **Final Sprint Review:** Fri 4 July 16:00 CEST (Final demo & presentation)
- **Project Retrospective:** Sun 6 July 15:00 CEST (Project closure)

**Merge Policy:** ≥1 peer review + green CI + linked issue + conventional commits

---

## 10 · Success Metrics

### Technical Metrics
- [ ] All 3 critical epics (A, B, C) completed by June 22
- [ ] Authentication system fully functional by June 29
- [ ] E2E test coverage ≥80% of main user flows
- [ ] Zero-config deployment working on fresh Ubuntu 24.04

### Project Metrics
- [ ] Demo video showcasing all features (5-10 min)
- [ ] Presentation slides completed (10-15 slides)
- [ ] All team members have individual contribution slides
- [ ] Final ZIP submission includes all required components

### Quality Metrics
- [ ] Cross-browser compatibility verified
- [ ] Mobile responsiveness working
- [ ] All Project Requirements checklist items completed
- [ ] Documentation updated and accurate

---

## 11 · Final Deliverables

**Technical Deliverables:**
1. Complete Titanic Survivor Prediction Application
2. Docker Compose deployment configuration
3. Source code with Git repositories
4. Comprehensive documentation

**Presentation Deliverables:**
1. Demo video (5-10 minutes)
2. Presentation slides (10-15 slides)
3. Individual contribution slides (6 slides)
4. Architecture overview and technical highlights

**Submission Package:**
- ZIP archive with all source code
- README with build/run instructions
- PDF of team presentation
- All Git repositories as required

---

*Final sprint prepared by **team/random_iceberg** · Sprint 3 begins 16 June 2025*
