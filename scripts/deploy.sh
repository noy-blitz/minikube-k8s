#!/bin/bash

# Start Minikube
minikube start --extra-config=apiserver.authorization-mode=RBAC

# Create Namespace
kubectl create namespace myapp
kubectl config set-context --current --namespace=myapp

# Deploy Service-A
kubectl apply -f service-a-deployment.yaml
kubectl apply -f service-a-service.yaml

# Deploy Service-B
kubectl apply -f service-b-deployment.yaml
kubectl apply -f service-b-service.yaml

# Deploy Ingress
kubectl apply -f ingress.yaml

# Deploy role, role-binding and account for authorization
kubectl apply -f rbac.yaml

# Apply Network Policy
kubectl apply -f network-policy.yaml
