# Three-Tier Application with Kubernetes
## Main Objective
The main objective of this project is to create a three-tier application and establish communication between the tiers using Kubernetes Service ClusterIP. The project will be implemented first in Docker alone, and then the same will be done in Kubernetes. Additionally, a Python script will be used to make five requests concurrently, and we will observe how Kubernetes-style deployment helps in scaling up and down to meet the traffic demands.

## Project Structure
The project is organized into three main tiers: Application-tier, Data-tier, and Presentation-tier. Each tier has its respective Docker image and Kubernetes deployment files. The project structure is as follows:
```
├── Application-tier
│   ├── Deployment
│   │   └── shapetracker-flask-server.yaml
│   ├── Service
│   │   └── shapetracker-flask-server-service.yaml
│   └── Shapetracker-flask-server
│       ├── app.py
│       ├── Dockerfile
│       ├── requirements.txt
│       ├── static
│       │   └── styles.css
│       └── templates
│           ├── form.html
│           ├── login.html
│           └── view_progress.html
├── Data-tier
│   ├── Deployment
│   │   └── shapetracker-mysql-server-deployment.yaml
│   ├── Service
│   │   └── shapetracker-mysql-server-service.yaml
│   └── Shapetracker-mysql-server
│       ├── create_table.sql
│       ├── custom-my.cnf
│       └── Dockerfile
├── make_request.py
├── Presentation-tier
│   ├── Deployment
│   │   └── shapetracker-web-server.yaml
│   ├── Service
│   │   └── shapetracker-web-server-service.yaml
│   └── Shapetracker-web-server
│       ├── Dockerfile
│       └── nginx.conf
└── README.md
```
## Building Docker Images
Before deploying the application in Kubernetes, we start by building Docker images for each tier and pushing them to Docker Hub. The images will be used later in the Kubernetes deployment process.

### Building Image for Data-tier (MySQL Server)
```bash
cd Data-tier/Shapetracker-mysql-server
docker build -t yourusername/shapetracker-mysql-server .
docker push yourusername/shapetracker-mysql-server
```
Replace yourusername with your Docker Hub username.

### Building Image for Application-tier (Flask Server)
```bash
cd Application-tier/Shapetracker-flask-server
docker build -t yourusername/shapetracker-flask-server .
docker push yourusername/shapetracker-flask-server
```
Replace yourusername with your Docker Hub username.

### Building Image for Presentation-tier (Nginx Web Server)
```bash
cd Presentation-tier/Shapetracker-web-server
docker build -t yourusername/shapetracker-web-server .
docker push yourusername/shapetracker-web-server
```
Replace yourusername with your Docker Hub username.

## Deploying in Docker (Local)
To test the application locally in Docker, we deploy each tier as a Docker container, and the tiers communicate using the respective container names.

###  Deploy Data-tier (MySQL Server)
```bash
docker run -d --name shapetracker-mysql-server --network mynetwork yourusername/shapetracker-mysql-server
```
### Deploy Application-tier (Flask Server)
```bash
docker run -d --name shapetracker-flask-server --network mynetwork yourusername/shapetracker-flask-server
```
### Deploy Presentation-tier (Nginx Web Server)
```bash
docker run -d --name shapetracker-web-server -p 80:80 --network mynetwork yourusername/shapetracker-web-server
```
Replace yourusername with your Docker Hub username.

## Deploying in Kubernetes
The project will be deployed in Kubernetes by creating Kubernetes Services and Deployments for each tier. The Services will allow communication between the tiers using ClusterIPs.

### Deploy Data-tier (MySQL Server)
```bash
kubectl create -f Data-tier/Service/shapetracker-mysql-server-service.yaml
kubectl create -f Data-tier/Deployment/shapetracker-mysql-server-deployment.yaml
```
### Deploy Application-tier (Flask Server)
```bash
kubectl create -f Application-tier/Service/shapetracker-flask-server-service.yaml
kubectl create -f Application-tier/Deployment/shapetracker-flask-server.yaml
```
### Deploy Presentation-tier (Nginx Web Server)
```bash
kubectl create -f Presentation-tier/Service/shapetracker-web-server-service.yaml
kubectl create -f Presentation-tier/Deployment/shapetracker-web-server.yaml
```
## Scaling with Kubernetes
The Python script make_request.py will be used to simulate multiple concurrent requests to the Presentation-tier service. Kubernetes-style deployment will demonstrate how the application can scale up and down based on the traffic load.

## Benefits
1. Separation of Concerns: Each tier is isolated, promoting better modularity and maintainability.
2. Security: Kubernetes provides a secure environment for running applications with RBAC and container isolation.
3. Scalability: Kubernetes allows easy scaling of application instances to meet varying traffic demands.
4. High Availability: Kubernetes supports replicating pods across nodes, ensuring high availability.
5. Service Discovery: Kubernetes Services enable automatic discovery of backend pods by frontend services.
6. Easy Rollback: Kubernetes allows easy rollback to previous versions in case of issues during deployments.
7. Load Balancing: Kubernetes can load balance traffic across multiple instances of the same service.

This project provides valuable insights into deploying and managing a three-tier application in Kubernetes and harnessing its powerful features for scalability and robustness.






