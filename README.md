# 🚀 Azure DevOps CI Pipeline – FastAPI Application

## 📌 Project Overview

This project demonstrates an end-to-end DevOps workflow for deploying a containerized FastAPI application using Azure and GitHub Actions.

The pipeline automatically builds a Docker image, pushes it to Azure Container Registry (ACR), and deploys the application to Azure Container Instances (ACI), making it publicly accessible.

---

## 🏗️ Architecture
GitHub Repository
↓
GitHub Actions (CI)
↓
Docker Build
↓
Azure Container Registry (ACR)
↓
Azure Container Instance (ACI)
↓
Public Endpoint---


---

## ⚙️ Technologies Used

- Python (FastAPI)
- Docker
- GitHub Actions (CI)
- Microsoft Azure
  - Azure Container Registry (ACR)
  - Azure Container Instance (ACI)
- Azure CLI

---

## 🔄 CI Pipeline

The CI pipeline is triggered on every push to the `main` branch.

### Workflow Steps:

1. Checkout source code
2. Authenticate with Azure using Service Principal
3. Build Docker image
4. Push image to Azure Container Registry

---

## 🐳 Dockerization

The FastAPI application is containerized using Docker.

### Build Image

```bash
docker build -t ops-demo:latest ./app

## 🌐 Live Application

The application is deployed and accessible via a public endpoint.

### Example Endpoints:

- `/` → Root  
- `/health` → Health check  
- `/ready` → Readiness check  

---

## 🔐 Authentication

Azure authentication is handled using a **Service Principal**, stored securely as a GitHub Actions secret:

---

## 💡 Key Learnings

- Containerizing applications using Docker  
- Building CI pipelines with GitHub Actions  
- Managing container images with Azure Container Registry  
- Deploying containers to Azure Container Instances  
- Handling authentication using Service Principals  
- Debugging cloud and networking issues  

---

## 🧹 Cleanup

To avoid unnecessary costs, resources can be deleted using:

```bash
az group delete --name rg-devsecops-lab --yes --no-wait

## 👤 Author

**Hemanth Kumar Vema**  
Aspiring Cloud & DevOps Engineer
