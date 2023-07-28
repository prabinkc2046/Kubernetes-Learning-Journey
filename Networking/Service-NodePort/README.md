# Kubernetes Learning Journey - Service with NodePort

## Introduction

This repository contains code samples and configuration files for learning Kubernetes concepts related to services and NodePort.

## Getting Started

Follow the steps below to create a Pod, deploy it, and expose it using a Service with NodePort.

### Step 1: Create a Pod

Create a Pod definition file (`hello-world-pod.yaml`) with the following content:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hello-world
  labels:
    app: hello-world
    type: front-end
spec:
  containers:
    - name: hello-world
      image: prabinkc/app:v3
```

Apply the Pod definition:

kubectl create -f hello-world-pod.yaml
Check the status of the Pod:

kubectl get pods -o wide

Step 2: Access the Application
As the Pod is exposed on port 5000, let's try accessing the application:

curl http://$(minikube ip):5000

If you encounter a connection refused error, don't worry. We'll resolve this in the next step.

Step 3: Create a Service with NodePort
To enable communication between external users and the Pod, we'll create a Service with NodePort.

Create a Service definition file (hello-world-service.yaml) with the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 5000 # The container is exposed on port 5000
      nodePort: 30500
  selector:
    app: hello-world
    type: front-end 
```

Apply the Service definition:

kubectl create -f hello-world-service.yaml
Check if the Service is created:

kubectl get services

Step 4: Access the Application Again
Now, let's try accessing the application using the NodePort:

curl http://$(minikube ip):30500

You should see "Hello world!" as the response, indicating that the application is accessible.

# Conclusion
Congratulations! You have successfully created a Pod, exposed it using a Service with NodePort, and accessed your application running on Kubernetes. Feel free to explore more Kubernetes concepts and dive into other exciting topics.

Happy learning!





