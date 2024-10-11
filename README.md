# Minikube Kubernetes Cluster Assignment

## Overview

This repository contains the necessary configurations and application code for setting up a Minikube-based Kubernetes cluster. The cluster includes two services.

## Cluster Details

1. **Kubernetes Cluster:** Using Minikube with RBAC enabled.
2. **Services:** 
- **Service-A**: Retrieves the current Bitcoin value in USD from an API every minute and prints it. Additionally, it calculates and prints the average value every 10 minutes.
- **Service-B**: A simple service that prints "Hello Microsoft!" every 10 seconds.
3. **Ingress Controller:** Redirects traffic based on URL:
    - `xxx/service-A` → Service-A
    - `xxx/service-B` → Service-B
4. **Network Policy:** Service-A is blocked from communicating with Service-B.

## Prerequisites

- Minikube installed locally.
- Docker installed.
- A working internet connection (Service-A relies on an external API for Bitcoin data).

## Cluster Setup

   ```bash
   minikube start

   kubectl create namespace myapp

   kubectl apply -f k8s/
   
   minikube IP
   
   Use the Minikube IP and the ingress URL to access the services:

   minikube service --url <service-name>
   ```

Service-A: http://<minikube-ip>/service-a

Service-B: http://<minikube-ip>/service-b

Liveness Probe: Checks /health every 15 seconds to ensure Service-B is running correctly. If this fails, Kubernetes will restart the container.

Readiness Probe: Checks /ready every 10 seconds to ensure Service-B is ready to start serving traffic.


