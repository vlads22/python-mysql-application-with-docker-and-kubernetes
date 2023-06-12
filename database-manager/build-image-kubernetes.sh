#!/bin/bash

# Build image using the dockerfile present in the folder.
docker build -f dockerfile -t image_mov_app_python .

# Load the image to the Minikube cluster.
minikube image load image_mov_app_python:latest