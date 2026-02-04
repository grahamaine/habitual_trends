#!/bin/bash

# Configuration
APP_NAME="habitual-trends-backend"
DOCKER_USER="your-docker-hub-username" # Change this!
TAG="latest"

echo "🚀 Starting deployment for $APP_NAME..."

# 1. Build the Rust binary (using a cross-compiler or Docker stage)
echo "📦 Building Docker image..."
docker build -t $DOCKER_USER/$APP_NAME:$TAG .

# 2. Push to Registry
echo "📤 Pushing image to Docker Hub..."
docker push $DOCKER_USER/$APP_NAME:$TAG

echo "✅ Deployment image ready!"