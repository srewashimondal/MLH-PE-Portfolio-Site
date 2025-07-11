#!/bin/bash

# Change directory into your project folder
cd ~/MLH-PE-Portfolio-Site

# Fetch latest changes from GitHub
git fetch
git reset origin/main --hard

# Enter python virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Restart myportfolio service
systemctl restart myportfolio.service
