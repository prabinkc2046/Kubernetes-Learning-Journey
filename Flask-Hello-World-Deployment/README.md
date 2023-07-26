# Deploying Flask-Hello-World Using Kubernetes Concept

## Pod

Yaml file for our desired Pod.

```
apiVersion: v1
kind: Pod
metadata:
  name: flask-hello-world-pod
  labels:
    app: flask-hello-world
spec:
  containers:
    - name: flask-hello-world-container
      image: prabinkc/flask-hello-world

```

To create a Pod using this manifest file, run:

```
kubectl create -f pod-definition.yaml
```

## ReplicaSet

Yaml file for ReplicaSet

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: flask-hello-world-replicaset
spec:
  selector:
    matchLabels:
      app: flask-hello-world
  replicas: 5
  template:
    metadata:
      name: flask-hello-world-pod
      labels:
        app: flask-hello-world
    spec:
      containers:
        - name: flask-hello-world-container
          image: prabinkc/flask-hello-world    

```
To create a ReplicaSet, run:
```
kubectl create -f replicaset-definition.yaml
```

## Deployment

Yaml file to create a deployment

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-hello-world-deployment
spec:
  selector:
    matchLabels:
      app: flask-hello-world
  template:
    metadata:
      name: flask-hello-world-pod
      labels:
        app: flask-hello-world
    spec:
      containers:
        - name: flask-hello-world-container
          image: prabinkc/flask-hello-world
  replicas: 4

 ```
To create a deployment object, run:

```
kubectl crate -f deployment-definition.yaml
```

