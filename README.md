# !!! Submission notes !!!

### Predefined users (new non-admins can be registered):
- **admin:** `email="admin@test"`, `password="apass"`
- **non-admin:** `email="user@test"`, `password="upass"`

### Run images from the registry

```bash
# 1. Checkout the latest 'main' commit (docker-compose repo alone is enough)
# 2. Make sure to `docker login` into `registry.mygit.th-deg.de`
# 3. Start
docker compose -f compose/compose.latest.yaml up --pull always -d
# 4. Access on http://localhost:8080
# 5. Do your shady business
# ...
docker compose -f compose/compose.latest.yaml down
```

### Build locally

```bash
# 1. Checkout the latest 'main' commits (docker-compose and all the submodules)
# 2. Start
docker compose up --build --pull always -d
# 3. Access on http://localhost:8080
# ...
docker compose down
```

### Notes on execution
- The services wait for each other to start, so the start can take a little time.
  - 30-40 seconds, +another few on a completely clean start (due to models training).
    - (computer-subjective time)
- The two above mentioned compose configs are both defined with `random-iceberg` project name.
  - So to share the volumes.

### Notes on functional requirements
- There is, intentionally, no delete option for the **default** models
  - All admin-user-trained models can still be deleted.
- Remidner: the advertisement is at the end of the landing page.

### Side notes

- pgAdmin, that is not required to run everything and that is mentioned below, will not start unless `--profile=pgadmin` is set

# Titanic Survivor Prediction Application

## Description

A production-ready web application that predicts Titanic passenger survival using machine learning models. Built with React, FastAPI, and scikit-learn.

![team/random_iceberg banner](./docs/random_iceberg.png)

## 🚀 Quick Start (Zero Configuration)

```bash
# Clone with submodules
git clone --recurse-submodules https://mygit.th-deg.de/schober-teaching/student-projects/ain-23-software-engineering/ss-25/Random_Iceberg/docker-compose.git
cd docker-compose

# Start all services (production test)
docker compose up --build -d

# Access the application
open http://localhost:8080
```

**That's it!** No environment setup, no dependencies to install, no configuration needed.

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│   Frontend  │────►│   Backend   │────►│ Model Service│
│   (React)   │     │  (FastAPI)  │     │  (FastAPI)   │
└─────────────┘     └──────┬──────┘     └──────────────┘
   Port 8080               │               Port 8000
   (exposed)        ┌──────▼──────┐     ┌──────────────┐
                    │  PostgreSQL │────►│   pgAdmin    │
                    └─────────────┘     └──────────────┘
                       Port 5432           Port 5050
```

## 📋 Features

- **Survival Prediction**: Real-time predictions based on passenger attributes
- **Model Management**: Train, evaluate, and delete ML models
- **User Authentication**: JWT-based secure authentication
- **Admin Console**: Model training and management interface
- **Responsive Design**: Mobile-first, accessible UI
- **Zero Config**: Works out of the box with Docker Compose

## 🛠️ Development Workflow

### Prerequisites
- Docker & Docker Compose
- Git with submodule support

### Development Mode (with hot reload)

```bash
# Start development environment with code syncing
docker compose -f 'compose/compose.dev.yaml' up -d --build

# Access services:
# - Frontend: http://localhost:8080
# - Backend Swagger: http://localhost:8000/docs
# - Model Swagger: http://localhost:8001/docs
# - pgAdmin: http://localhost:5050
#   - Email: team@random.iceberg
#   - Password: Cheezus123
```

### Testing Production Build Locally

```bash
# Test production build
docker compose -f 'compose/compose.prod-local.yaml' up -d

# Main app: http://localhost:8080
```

## 📁 Project Structure

```
docker-compose/
├── docker-compose.yaml   # Default (production) configuration
├── compose/              # Compose configurations
│   ├── compose.dev.yaml          # Development with hot reload
│   ├── compose.prod-local.yaml   # Production from local build
│   └── compose.prod-registry.yaml # Production from registry
├── app/
│   ├── frontend/        # React frontend (submodule)
│   └── backend/         # FastAPI backend (submodule)
├── model/               # ML service (submodule)
├── docs/                # Documentation (submodule)
└── postgres/            # Database initialization
```

## 🔗 Service Documentation

- [Frontend Documentation](./app/frontend/README.md)
- [Backend Documentation](./app/backend/README.md)
- [Model Service Documentation](./model/README.md)
- [Project Requirements](./docs/Project-Requirements.md)

## 📊 Development Tools

- **API Documentation**: Swagger UI at `/docs` for each FastAPI service
- **Database Management**: pgAdmin at port 5050
- **Logs**: `docker compose logs -f [service-name]`
- **Health Checks**: `GET /health` endpoint on each service

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for:
- Git workflow and branch strategy
- Commit message conventions
- Code review process
- Testing requirements

---

Built with ❤️ by **team/random_iceberg**
