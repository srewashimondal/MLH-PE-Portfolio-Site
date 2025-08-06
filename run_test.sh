#!/bin/bash
set -e

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  $PWD/venv/Scripts/python.exe -m unittest discover -v tests/
else
  $PWD/venv/bin/python -m unittest discover -v tests/
fi



