#!/bin/sh

python3 manage.py makemigrations api 
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000