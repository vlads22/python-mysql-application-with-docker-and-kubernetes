#!/bin/bash

# Build image using the dockerfiles present in the folder.
docker build -f dockerfile -t image_mov_app_mysql .