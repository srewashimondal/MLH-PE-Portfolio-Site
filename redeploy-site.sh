#!/bin/bash

# Kill all existing tmux sessions
tmux kill-server

# Change directory into your project folder
cd ~/MLH-PE-Portfolio-Site

# Fetch latest changes from GitHub
git fetch
git reset origin/main --hard

# Enter python virtual environment and install dependencies
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached tmux session to run flask server
tmux new -d -s flask_session "cd ~/MLH-PE-Portfolio-Site && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"
