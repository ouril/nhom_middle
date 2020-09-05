#!/bin/bash

python_path=$(which python3)

echo "Path to python $python_path"

virtualenv venv -p $python_path

source venv/bin/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser