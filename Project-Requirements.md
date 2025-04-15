---
title: Project Requirements
---
# Project Requirements: Summerterm 2025

**Prof. Dr. Christoph Schober**  
Email: christoph.schober@th-deg.de

**AIN-B Software Engineering**  
_PrA - Praktikumsleistung_

---

## Project Overview

Your task is to develop a web application powered by artificial intelligence to predict whether a passenger would have survived the Titanic disaster. The web app shall allow the user to play with different parameters and act as an advertisement for the AI courses your company is selling. Your goal is to promote the website using organic and paid social media advertisement in order to gain new customers and brand awareness.

### Product Story

> “Get ready to embark on an exciting journey with our cutting-edge web application, driven by the power of artificial intelligence! Discover if you would have survived the legendary Titanic disaster as you explore and tweak various intriguing parameters. This isn’t just a web app—it’s your gateway to experiencing firsthand the capabilities of AI in a fun and engaging way! Plus, it’s a fantastic showcase of the innovative AI courses we’re proud to offer. Join the adventure, spread the word through your favorite social media channels and help others join in on this unique journey!”  
> — Sam Altmaniac, Marketing Director

---

## General Rules

- **Complete Task 1 and Task 2 to complete the project work.**
- Attend Project Meetings (online) and the final Presentation (in presence in Deggendorf).
- Groups of 7 students must make a joint submission.
- The submission must include:
  - The names and matriculation numbers of all students in the team.
  - All source code, configuration files, documentation.
  - All Git repositories as downloaded from Gitlab according to the provided documentation.
  - A README file explaining how to build, run, and access the web application using the Docker images and Docker Compose specification.
  - A PDF of the team presentation. (We will use Figma Slide Deck for the presentation.)
- Submit the solution in the form of a ZIP archive via iLearn.
- Functional and non-functional requirements both contribute to the final grade.
- The project is only passed if 50% is reached in all contributions individually.
- Only the requirements outlined in this document are relevant.
- Any corrections or additions to these requirements are published in iLearn under the section **Project Requirement Updates**.
- Only submissions that build successfully without errors (Docker on Ubuntu Noble Numbat 24.04 LTS) are graded.
- Only commits using the official student email address (@stud.th-deg.de) are graded.

**Useful Resources and Hints:**

- Implementing all requirements within the term may be extremely challenging for many student teams, except the most experienced ones.
- Use an iterative approach and do not try to implement all requirements at once.
- Prioritize features from the product perspective: *How can you get to market as soon as possible? What is required for this? What is nice to have?*
- Distribute individual tasks, not responsibilities.  
  *(Wrong: "You are responsible for containerization, you for all backend, etc.")*
- Take care of the interfaces: Plan and document dependencies between tasks to minimize communication overhead.
- Make use of the extensive documentation of the frameworks (especially FastAPI), it may be easier than using ChatGPT & Co.

---

## Task 1 – Titanic Survivor App

### Functional Requirements

- **Landing Page:**
  - Shows a short explanation of the functionality.
  - Contains navigation (links) to all other pages.

- **User Account:**
  - Register an account using an email address and a password.
  - Log in using the username and password.

- **Advertisement Page:**
  - Promote your extremely successful online course on creating AI-powered web applications.

- **Survival Calculator:**
  - **Passenger Definition:**
    - **Class:** First, Second, Third.
    - **Sex:** Male or Female.
    - **Age:** 0-100.
    - **Fare:** 0-500 $.
    - **Traveled Alone:** Yes or No.
    - **Embarked:** Cherbourg, Queenstown, Southampton.
    - **Title:** Master, Miss, Mr, Mrs, Rare.
  - Each passenger property shall have an in-page explanation.
  - Continuously update the shown prediction after each input change.
  - Contains a reset button for the passenger inputs.
  - **Model Selection:**
    - For **Anonymous Users:** Allow selection of a single model from Random Forest or Support Vector Machines.
    - For **Logged In Users:** Allow selection of any combination of all available models.
  - Display the prediction (“Survived” or “Did not survive”) for each model.
  - **Prediction History:**  
    - For Logged In Users, show a persistent history of the last 10 passengers with prediction results.

- **Admin Features:**
  - View all existing trained models and delete a model.
  - Select any number of features from the feature list and train a new model.
  - After training, the model shall be available in the Survival Calculator's Model Selection under a name chosen by the user.

### Non-Functional Requirements

#### General

- The application consists of the following services:
  - **Web Frontend**
  - **Web Backend**
  - **Database**
  - **Model Backend**
- Use a reverse proxy such as:
  - [Caddy](https://caddyserver.com/)
  - [Nginx](https://nginx.org/en/)
  - [Traefik](https://traefik.io/traefik/)
- All services shall be containerized using Docker containers.
- Docker images shall be built with Gitlab CI and pushed to the Gitlab Container Registry.
- Application containers shall be orchestrated using a single Docker Compose specification (`compose.yaml`).
- The application shall be accessible at [http://localhost:8080](http://localhost:8080).
- Unit and Integration tests shall be automatically executed in a Gitlab pipeline on every commit.
- End2end tests shall be automatically run in a nightly pipeline of the docker-compose project.

#### Docker Compose

- Managed in the docker-compose repository.
- All other required repositories are included in this repository via git submodules ([Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)).

#### Project Management

- The project shall be conducted according to the Scrum framework with a total of 3 sprints (each with a sprint length of 3 weeks). (We have adjusted it to 4 sprints of 2 weeks each.)
- A Product Backlog shall be created and maintained according to this document.
- All non-code project resources shall be managed and maintained within the Gitlab project **project-management**. (we are using the docker-compose.wiki repo instead)
  - At any time, the assets in Gitlab shall reflect the current state of the project.
- The dates and deadlines published in iLearn under the section **Dates and Deadlines** shall apply. All deadlines are hard.
- The source code shall be actively managed in mygit ([Mygit Portal](https://mygit.th-deg.de)) using the provided team Gitlab group. (we are using [Team/Random_Iceberg](https://mygit.th-deg.de/schober-teaching/student-projects/ain-23-software-engineering/ss-25/Random_Iceberg) group).
- From the official start of the project, at least one git commit with code is done per week.

#### Web Frontend (Refer to Project Charter)

- The frontend shall work in the following browser versions:
  - Chrome >= 119
  - Firefox >= 122
  - Safari >= 16.1
- The frontend can be created in Javascript or Typescript, using HTML and CSS as appropriate.
- The source code for the frontend shall be written as a Single Page Application (SPA) using either:
  - [React](https://react.dev/)
  - [Vue](https://vuejs.org/)
- The frontend shall be optimized for mobile screens.
- Unit and Integration tests for all JavaScript/TypeScript code shall be written using the respective test frameworks for Vue or React.
- All functional requirements for the web app shall be verified in terms of E2E tests.
- End2End tests shall be written using:
  - [Cypress](https://www.cypress.io/) or
  - [Playwright](https://playwright.dev/)
- The reverse proxy shall be part of the web frontend service.
  - It shall route all external traffic to the respective internal service and serve the static files for the web frontend.  
    *(Note: No `npm run dev` in production code!)*

#### Web Backend (Refer to Project Charter)

- Code shall be written in Python using [FastAPI](https://fastapi.tiangolo.com/).
- Unit and Integration tests for all Python code shall be written using the [pytest framework](https://docs.pytest.org/en/8.0.x/).

#### Model Backend (Refer to Project Charter)

- Code shall be written in Python using FastAPI as the framework for the RESTful API.
- The prediction model inference shall be accessible via a RESTful API ([REST](https://en.wikipedia.org/wiki/REST)) within the Docker network.
- The provided models shall use the exact implementation from the proof-of-concept notebook  
  *(see iLearn: titanic-data-science-solutions.ipynb)*.
  - At least the following base algorithms are available:
    - Random Forest
    - Decision Tree
    - KNN
    - Support Vector Machines
    - Logistic Regression
  - The following features from the notebook are used for the default model training:
    - Survived, Pclass, Sex, Age, Fare, Embarked, Title, IsAlone, Age*Class.
  - For each available trained model, the name, used features, and algorithm are stored in a database table.
- **First Start:**  
  - All default models shall be trained and stored as Pickle files  
    *(see [Scikit-Learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html))*.
- **Subsequent Start-ups:**  
  - The existing pickle files are loaded from disk  
    *(requires the use of Docker volumes)*.
- Any additional trained models by an admin user are persisted over container re-creation.
- The prediction model service API shall be inaccessible from the outside of the Docker network.
- Unit and Integration tests for all Python code shall be written using the [pytest framework](https://docs.pytest.org/en/8.0.x/).

---

## Task 2 – Presentation

- Create a presentation document of **10-15 slides**.
- The presentation shall:
  - Demonstrate the software developed in Task 1.
  - Provide insights on the architecture of the system.
  - Highlight aspects that make the solution special.
- **Individual Contributions:**  
  - Each group member is tasked to create and present a slide listing their personal contribution to the project.

---

## References

1. [Caddy Server](https://caddyserver.com/)
2. [Nginx](https://nginx.org/en/)
3. [Traefik](https://traefik.io/traefik/)
4. [Git Submodules Documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
5. [Mygit Portal](https://mygit.th-deg.de)
6. [React](https://react.dev/)
7. [Vue.js](https://vuejs.org/)
8. [Cypress](https://www.cypress.io/)
9. [Playwright](https://playwright.dev/)
10. [FastAPI](https://fastapi.tiangolo.com/)
11. [Pytest Documentation](https://docs.pytest.org/en/8.0.x/)
12. [REST Wikipedia](https://en.wikipedia.org/wiki/REST)
13. [Scikit-Learn Model Persistence](https://scikit-learn.org/stable/model_persistence.html)

---

*Note: This document was extracted from a PDF and later formatted by ChatGPT. No changes were made to the original content.*
