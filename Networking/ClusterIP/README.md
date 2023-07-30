# Kubernetes Service (ClusterIP) Demonstration

## Introduction
This repository is part of my Kubernetes learning journey, where I demonstrate my understanding and implementation of Kubernetes Services with ClusterIP. The main goal is to deploy a stack application using Kubernetes, consisting of a frontend Nginx web server and a backend Flask server. In this project, I leverage Docker technology to build the required images and then deploy them using Kubernetes Service with ClusterIP.

## Docker Image Creation
### Backend Image
To begin, I created a Docker image for the backend Flask application. The Flask server handles the backend logic and serves as the foundation for the entire application.
```
cd Backend-Image-Creation
docker build -t prabinkc/backend .
docker push prabinkc/backend
```
**Inplace of prabinkc, use your username for Docker Hub.**

### Frontend Image
Next, I built a Docker image for the frontend Nginx web server. This image handles the frontend presentation and serves as the entry point for user interactions.
```
cd Frontend-Image-Creation
docker build -t prabinkc/frontend .
docker push prabinkc/frontend
```
**Inplace of prabinkc, use your username for Docker Hub.**

## Docker Implementation of the Stack Application
In this stage, I implemented the stack application using Docker, orchestrating the communication between the frontend and backend containers.

1. Set up Docker.

2. Create a network for the frontend and backend to communicate:

```bash
docker network create frontend-backend-network
```

Deploy the backend Flask server and check the logs:

```bash
docker run -d --name flask-server --network frontend-backend-network prabinkc/backend
```
```
docker logs -f flask-server
```

Deploy the frontend Nginx web server:
```bash
docker run -d --name frontend -p 80:80 --network frontend-backend-network prabinkc/frontend
```

Access the application by navigating to http://localhost in your web browser. You should see the frontend application served by Nginx, communicating with the backend Flask server.


## Kubernetes Implementation of the Stack Application
Having understood the Docker implementation, I decided to leverage the power of Kubernetes to manage and scale the application effectively.

Set up Minikube on my local machine to create a local Kubernetes cluster.

Created a Kubernetes Service named flask-server for the backend Flask server. This service uses ClusterIP to provide an internal IP address for communication within the cluster.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: flask-server
spec:
  type: ClusterIP
  ports:
    - port: 5000
      targetPort: 5000
  selector:
    app: backend-flask-pod
    type: backend
```
Deployed the backend Flask server as a Kubernetes Deployment named backend-flask. This ensures that the specified number of replicas (in this case, 10) are maintained.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend-flask
spec:
  replicas: 10
  selector:
    matchLabels:
      app: backend-flask-pod
      type: backend
  template:
    metadata:
      name: backend-flask-pod
      labels:
        app: backend-flask-pod
        type: backend
    spec:
      containers:
        - name: flask-container
          image: prabinkc/backend
          ports:
            - containerPort: 5000
```

Created a Kubernetes Service named frontend for the frontend Nginx web server. This service uses NodePort to make the application accessible externally.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30080
  selector:
    app: frontend-pod
    type: frontend
```
Deployed the frontend Nginx web server as a Kubernetes Deployment named frontend. Similar to the backend deployment, this ensures the specified number of replicas (10 in this case) are maintained.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
spec:
  replicas: 10
  selector:
    matchLabels:
      app: frontend-pod
      type: frontend
  template:
    metadata:
      name: frontend-pod
      labels:
        app: frontend-pod
        type: frontend
    spec:
      containers:
        - name: frontend-container
          image: prabinkc/frontend
          ports:
            - containerPort: 80
```
After deploying both frontend and backend, I verified the running services and pods using the following commands:

```bash
kubectl get services
```
```bash
kubectl get pods
```
Accessed the frontend application using the Minikube service command:

```bash
minikube service frontend
```
You should see:

![Screenshot: Accessing Web Server](./Screenshot-accessing%20web%20server.png)

This opened a browser displaying the frontend application served by Nginx, which communicated with the backend Flask server through the Kubernetes Service flask-service.

That concludes my Kubernetes learning journey, showcasing the implementation of Kubernetes Services with ClusterIP. I hope this project demonstrates my understanding of Kubernetes networking and how to deploy a stack application effectively using containers and Kubernetes.

