# Docker Compose Orchestration for Titanic Survivor Prediction Application

![team/random_iceberg banner](./docs/random_iceberg.png)

This repository provides a centralized [Docker Compose](https://docs.docker.com/compose/) configuration to orchestrate the major services of the Titanic Survivor Prediction Application. The setup includes:

- **Frontend**: A React-based Single Page Application.
- **Backend**: A FastAPI server handling business logic and API endpoints.
- **Model Service**: A microservice dedicated to machine learning model inference.
- **Supabase**: A self-hosted service for authentication and data storage.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Running the Application](#running-the-application)
- [Updating and Maintenance](#updating-and-maintenance)
- [Troubleshooting](#troubleshooting)

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed on your system.
- [Docker Compose](https://docs.docker.com/compose/install/) available.

## Basic Setup

1. **Clone the Repository**:  
   ```bash
   git clone https://your.git.repo/docker-compose.git
   cd docker-compose
   ```

## Running the Application

To build and start all services, run:
```bash
docker-compose up --build -d
```
This command will:
- Build the Docker images for **frontend**, **backend**, and **model** services.
- Pull the latest image for Supabase if not already available.
- Create and attach the necessary volumes for persistent storage.

## Updating and Maintenance

- **Updating Services**:  
  Pull the latest changes in each submodule (frontend, backend, model) and rebuild images using:
  ```bash
  docker-compose pull
  docker-compose up --build -d
  ```

- **Restarting Services**:  
  To apply configuration changes:
  ```bash
  docker-compose down
  docker-compose up -d
  ```

- **Scaling**:  
  For horizontal scaling, adjust the service definitions and use Docker Compose’s scaling feature:
  ```bash
  docker-compose up --scale backend=3 -d
  ```

## Troubleshooting

- **Logs**:  
  View logs for a specific service:
  ```bash
  docker-compose logs backend
  ```
- **Service Health**:  
  Check the status of the services:
  ```bash
  docker-compose ps
  ```
- **Resetting Data**:  
  To remove volumes and reset the database:
  ```bash
  docker-compose down -v
  ```

---

> **Note:** This configuration is a draft. Further enhancements may be needed to meet production requirements, including stricter security configurations, resource limits, and more robust monitoring.