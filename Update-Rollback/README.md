# Update and Rollback with Kubernetes Deployment
This repository demonstrates how to perform updates and rollbacks on a Kubernetes Deployment using a simple "Hello World" application. The instructions below will guide you through the setup and the process of updating and rolling back the application.

## Prerequisites
Before proceeding, ensure you have the following installed:

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

## Creating and Deploying the Application

Clone this repository and navigate to the project directory.

Build the Docker image for the initial version of the application:

```
cd Hello-World
docker build -t prabinkc/app:v1 .
docker push prabinkc/app:v1
```

## Deploy the application on Kubernetes using the provided deployment.yaml file:

```
kubectl create -f deployment.yaml
```

Check the status of the deployment:

```
kubectl rollout status deployment hello-world-app
```

Verify the version of the image being used:

```
kubectl describe deployment hello-world-app
```

## Updating the Application

Suppose you want to add a new feature or make changes to the application. Here's how to update it:

Make the necessary changes to the application code.

Build and push the updated Docker image:

```
cd Hello-World
docker build -t prabinkc/app:v2 .
docker push prabinkc/app:v2
```

Edit the deployment to use the new image:

```
kubectl edit deployment hello-world-app
```

Within the spec section of the template of the Pod, change the image field to prabinkc/app:v2.

Save the changes and exit the editor.

Check the status of the update:

```
kubectl rollout status deployment hello-world-app
```

The application will now be running with the updated image.

# Rolling Back the Application
In case the update did not go as expected, you can roll back to the previous stable version:

Roll back the deployment:

```
kubectl rollout undo deployment hello-world-app
```

Check if the desired number of Pods are running:
```
kubectl get pods
```

Verify the version of the image being used after the rollback:
```
kubectl describe deployment hello-world-app
```

The application will be rolled back to the image prabinkc/app:v1.

# Conclusion

This project serves as a guide for demonstrating Kubernetes update and rollback functionalities. By following these instructions, you can gain hands-on experience with managing deployments, updating applications, and safely rolling back changes in Kubernetes.

Feel free to experiment further with different update strategies and explore other Kubernetes features to enhance your understanding of container orchestration. Happy learning!

