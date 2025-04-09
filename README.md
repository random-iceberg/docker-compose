# Docker Compose Orchestration for Titanic Survivor Prediction Application

![team/random_iceberg banner](./docs/random_iceberg.png)

This repository provides a centralized Docker Compose configuration to orchestrate the major services of the Titanic Survivor Prediction Application. The architecture consists of:

- **Frontend**: A React-based Single Page Application.
- **Backend**: A FastAPI server managing business logic and API endpoints.
- **Model Service**: A dedicated microservice for machine learning model inference.
- **Supabase**: A self-hosted service for user authentication and data storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Running the Application](#running-the-application)
- [Updating and Maintenance](#updating-and-maintenance)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) must be installed.
- [Docker Compose](https://docs.docker.com/compose/install/) must be available.

## Running the Application

To build and start all services, run:

```bash
docker-compose up --build -d
```

This command will:
- Build Docker images for **frontend**, **backend**, and **model**.
- Pull the latest image for Supabase if unavailable.
- Create and attach the necessary volumes for persistent data storage.

## Updating and Maintenance

- **Updating Services**:  
  Update each submodule (frontend, backend, model) and rebuild using:
  ```bash
  docker-compose pull
  docker-compose up --build -d
  ```

- **Restarting Services**:  
  To apply configuration changes, run:
  ```bash
  docker-compose down
  docker-compose up -d
  ```

- **Scaling**:  
  For horizontal scaling, adjust service definitions as needed. For example, to scale the backend:
  ```bash
  docker-compose up --scale backend=3 -d
  ```

## Troubleshooting

- **Viewing Logs**:  
  To view logs for a specific service:
  ```bash
  docker-compose logs [service_name]
  ```

- **Checking Service Health**:  
  Verify the status of all containers with:
  ```bash
  docker-compose ps
  ```

- **Resetting Data**:  
  To remove volumes and reset the environment:
  ```bash
  docker-compose down -v
  ```

> **Note:** This configuration is designed as a starting point. Further enhancements (such as advanced security configurations, resource limits, and monitoring) may be required for production deployments.
