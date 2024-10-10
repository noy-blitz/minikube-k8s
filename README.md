# Minikube Kubernetes Cluster Assignment

## Overview

This repository contains the necessary configurations and application code for setting up a Minikube-based Kubernetes cluster. The cluster includes two services:

- **Service-A**: Retrieves the current Bitcoin value in USD from an API every minute and prints it. Additionally, it calculates and prints the average value every 10 minutes.
- **Service-B**: A simple service that prints "Hello Microsoft!" every 10 seconds.

## Requirements

- Minikube installed on your local machine.
- Docker installed for building images.
- Kubernetes CLI (kubectl) installed for managing the cluster.

## Cluster Setup

   ```bash
   minikube start

   kubectl create namespace myapp

   kubectl apply -f service-a-deployment.yaml
   kubectl apply -f service-a-service.yaml
   kubectl apply -f service-b-deployment.yaml
   kubectl apply -f service-b-service.yaml
   kubectl apply -f ingress.yaml
   
   minikube IP
   ```
Accessing the Services: Make sure to update the host in the Ingress configuration to your domain or use Minikube’s IP with the appropriate paths:

Service-A: http://<minikube-ip>/service-a
Service-B: http://<minikube-ip>/service-b


