# Titanic Survivor Prediction Application

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
│   Frontend  │────▶│   Backend   │────▶│ Model Service│
│   (React)   │     │  (FastAPI)  │     │  (FastAPI)   │
└─────────────┘     └──────┬──────┘     └──────────────┘
      Port 8080            │                Port 8000
                    ┌──────▼──────┐     ┌──────────────┐
                    │  PostgreSQL │────▶│   pgAdmin    │
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
cd compose
docker compose -f compose.dev.yaml up

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
cd compose
docker compose -f compose.prod-local.yaml up -d

# Main app: http://localhost:8080
```

### Running Tests

```bash
# All tests run automatically in CI/CD on push

# Or run tests inside containers:
docker compose exec backend uv run pytest
docker compose exec frontend npm test
docker compose exec model uv run pytest
```

## 🚢 Production Deployment

### Using Local Build
```bash
docker compose -f compose/compose.prod-local.yaml up -d
```

### Using Registry Images
```bash
export IMAGE_GROUP=registry.mygit.th-deg.de/...
export IMAGE_TAG=latest
docker compose -f compose/compose.prod-registry.yaml up -d
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

## 🔧 Optional: Local Development (without Docker)

If you prefer to run services locally for development:

### Backend
```bash
cd app/backend
uv sync --extra dev
uv run uvicorn main:app --reload
# API docs at http://localhost:8000/docs
```

### Frontend
```bash
cd app/frontend
npm install
npm start
# UI at http://localhost:3000
```

### Model Service
```bash
cd model
uv sync --extra dev
uv run uvicorn main:app --reload --port 8001
# API docs at http://localhost:8001/docs
```

**Note**: Local development requires PostgreSQL and proper environment configuration.

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
