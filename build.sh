#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python proton/manage.py collectstatic --no-input
python proton/manage.py migrate
