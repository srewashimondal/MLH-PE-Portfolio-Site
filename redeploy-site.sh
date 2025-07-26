#!/bin/bash

# Change directory into your project folder
cd ~/MLH-PE-Portfolio-Site

# Fetch latest changes from GitHub
git fetch
git reset origin/main --hard

# Shut down old containers to avoid memory issues
docker compose -f docker-compose.prod.yml down

# Rebuild and restart containers
docker compose -f docker-compose.prod.yml up -d --build
