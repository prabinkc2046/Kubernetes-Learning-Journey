# Kubernetes Learning Journey: Deploying a Three-Tier Application on Linode
Kubernetes Logo

Welcome to my Kubernetes learning journey! In this demo, I'll walk you through the steps to deploy a three-tier application on Linode and access it using a LoadBalancer. The main objective of this project is to showcase how to set up a Kubernetes cluster and deploy a multi-tier application.

# Video Demonstration
Check out the video where I demonstrate the steps to create a Kubernetes cluster on Linode:

[Watch the Video](https://www.youtube.com/watch?v=r05mBNYymz4)

# Deployment Steps
Follow these steps to deploy the three-tier application on your Kubernetes cluster:

## Step 1: Create Kubernetes Cluster
Before deploying the application, make sure you have a Kubernetes cluster up and running. Refer to the video demonstration above to learn how to create a Kubernetes cluster on Linode.

### Step 2: Deploy MySQL
```
cd Data-tier
kubectl create -f Service/shapetracker-mysql-server-service.yaml
kubectl create -f Deployment/shapetracker-mysql-server.yaml
```
### Step 3: Deploy Application Backend (AP)
```
cd App-tier
kubectl create -f Service/shapetracker-flask-server-service.yaml
kubectl create -f Deployment/shapetracker-flask-server.yaml
```
### Step 4: Deploy Frontend
```
cd Presentation
kubectl create -f Service/shapetracker-web-server-service.yaml
kubectl create -f Deployment/shapetracker-web-server.yaml
```
### Step 5: Access the Application
After successfully deploying the three-tier application, you can access it using the external IP provided by the LoadBalancer.

# Conclusion
Congratulations on completing this Kubernetes learning journey! You have successfully deployed a three-tier application on Linode using Kubernetes. I hope this project has been valuable for your learning experience and has given you a better understanding of Kubernetes deployment and management.

Happy coding and deploying!

### Author
This project was completed as part of my Kubernetes learning journey. Connect with me on LinkedIn:[Prabin K C](https://www.linkedin.com/in/prabin-kc/)

