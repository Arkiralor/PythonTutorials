#!/bin/bash

python -m pip install pip-tools
pip-compile --resolver=backtracking --upgrade --generate-hashes --output-file=requirements.txt requirements.in
python -m pip install -r requirements.txt