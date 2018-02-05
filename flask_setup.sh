#!/usr/bin/env bash

python3 -m venv webapp/flask-venv

source ./webapp/flask-venv/bin/activate

pip install -r ./webapp/requirements.txt
