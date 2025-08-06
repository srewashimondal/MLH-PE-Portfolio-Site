#!/bin/bash
set -e

# Detect platform and run with correct Python path
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  ./venv/Scripts/python.exe -m unittest discover -v tests/
else
  ./venv/bin/python -m unittest discover -v tests/
fi


