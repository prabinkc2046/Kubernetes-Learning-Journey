# Kubernetes Concept

In this demo, I will demonstrate the concept I learnt after taking training on
the kubernetes from KodeKloud.

We will deploy my containerized flask app that says: Hello world when it is 
accessed from the browser.

## Pod

Pod is the smallest unit of Kubernetes architecture.

YAML defintion to create a Pod object:

```
apiVersion: v1
kind: Pod
metadata:
  name: flask-hello-world-pod
  labels:
    app: flask-hello-world
spec:
  containers:
    - name: flask-hello-world-pod
      image: prabinkc/flask-hello-world
```


To create a pod using this definition, run:

```
kubectl create -f pod-definition.yaml
```
This will create a pod named flask-hello-world-pod pulling an image prabinkc/flask-hello-world.


## ReplicaSet

The yaml defintion to create a desired state of pods at all time:

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: flask-hello-world-replicaset
  labels:
    app: flask-hello-world
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
        - name: flask-hello-world-pod
          image: prabinkc/flask-hello-world    
```

To create a replicaset object, run:
```
kubectl create -f replicaset-def.yaml
```

## Deployment

Defintion for creating a deployment object:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-hello-world-deployment
  labels:
    app: flask-hello-world
spec:
  selector:
    matchLabels:
      app: flask-hello-world
  replicas: 6
  template:
    metadata:
      name: flask-hello-world-pod
      labels:
        app: flask-hello-world
    spec:
      containers:
        - name: flask-hello-world-pod
          image: prabinkc/flask-hello-world
```








