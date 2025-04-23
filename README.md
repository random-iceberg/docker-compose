# Docker Compose Orchestration for Titanic Survivor Prediction Application

![team/random_iceberg banner](./docs/random_iceberg.png)

This repository provides a centralized Docker Compose configuration to orchestrate the major services of the Titanic Survivor Prediction Application. The architecture consists of:

- **Frontend**: A React-based Single Page Application.
- **Backend**: A FastAPI server managing business logic and API endpoints.
- **Model Service**: A dedicated microservice for machine learning model inference.
- **Supabase**: A self-hosted service for user authentication and data storage.

## Project Directory Structure

The project follows a modular structure to ensure maintainability and scalability. Below is a high-level layout of the repository:

```
docker-compose/
├── CONTRIBUTING.md          # Guidelines for contributing and commit message conventions
├── dir_to_json.py           # Utility to convert the directory structure to JSON
├── docker-compose.yml       # Orchestrates all services (frontend, backend, model, supabase)
├── README.md
├── docs/                    # Documentation and Project Charter submodule
│   ├── home.md
│   ├── Project-Charter.md
│   └── random_iceberg.png
├── app/                     # Application code for web services
│   ├── backend/             # FastAPI backend service
│   │   ├── README.md
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   ├── routers/         # API route definitions
│   │   ├── models/          # Data models and schemas
│   │   ├── services/        # Business logic and integration layers
│   │   └── tests/           # Unit and integration tests
│   └── frontend/
│       ├── README.md
│       ├── package.json
│       ├── src/             # Source files: components, assets, etc.
│       └── public/          # Public assets and HTML templates
└── model/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── training/            # Scripts and configuration for model training
    ├── inference/           # Inference logic and endpoints
    └── tests/               # Tests for model training and inference
```

## Table of Contents

- [Prerequisites](#prerequisites)
- [Running the Application](#running-the-application)
- [Updating and Maintenance](#updating-and-maintenance)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed.
- [Docker Compose](https://docs.docker.com/compose/install/) must be available.

## Getting Started

<!-- TODO -->

## Running the Application

To build and start all services, run:

```bash
docker compose -f ./compose/prod-local.yaml up --build -d
```

This command will:
- Build Docker images for **frontend**, **backend**, and **model**.
- Pull the latest image for Supabase if unavailable.
- Create and attach the necessary volumes for persistent data storage.

## Updating and Maintenance

- **Updating Services**:  
  Update each submodule (frontend, backend, model) and rebuild using:
  ```bash
  docker compose -f ./compose/prod-local.yaml pull
  docker compose -f ./compose/prod-local.yaml up --build -d
  ```

- **Restarting Services**:  
  To apply configuration changes, run:
  ```bash
  docker compose -f ./compose/prod-local.yaml down
  docker compose -f ./compose/prod-local.yaml up -d
  ```

<!-- - **Scaling**:   -->
<!--   For horizontal scaling, adjust service definitions as needed. For example, to scale the backend: -->
<!--   ```bash -->
<!--   docker-compose up --scale backend=3 -d -->
<!--   ``` -->

## Troubleshooting

- **Viewing Logs**:  
  To view logs for a specific service:
  ```bash
  docker compose -f ./compose/prod-local.yaml logs [service_name]
  ```

- **Checking Service Health**:  
  Verify the status of all containers with:
  ```bash
  docker compose -f ./compose/prod-local.yaml ps
  ```

- **Resetting Data**:  
  To remove volumes and reset the environment:
  ```bash
  docker compose -f ./compose/prod-local.yaml down -v
