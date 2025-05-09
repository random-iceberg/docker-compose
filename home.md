---
title: Home
revision: v3-sync‑guide · 09 May 2025
---

> **Context**  
> *This is the home page of the project documentation. It provides an overview of the project, its objectives, and links to various sections of the documentation.*

## 🔄 Sync Guide

Push your local `main` branch to the upstream `dev` branch:

### 🛠️ One-Time Setup
```bash
git remote add upstream https://mygit.th-deg.de/schober-teaching/student-projects/ain-23-software-engineering/ss-25/Random_Iceberg/project-management.git
````

### 🚀 Push Local Main to Remote Dev

```bash
git push upstream main:dev --force
```

> **⚠️ Warning:** This will **overwrite** the remote `dev` branch.

### ✅ Verify Remote

```bash
git remote -v
git branch -a
```

## 📋 Why Sync?

The project requirements mandate that **all** non-code resources (including documentation) live in the `project-management` repo via a submodule. Syncing `docker-compose.wiki` here ensures we meet those requirements and keep our docs and charters up to date.
