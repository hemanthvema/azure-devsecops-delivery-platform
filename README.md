---

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
