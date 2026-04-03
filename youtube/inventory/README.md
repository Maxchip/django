# django

Django project

# Activate the Enviroment

pipenv shell

or

source /Users/user/.local/share/virtualenvs/django-3PNZeuAl/bin/activate

# Create Project

django-admin startproject worldtour .

# Create a New App

python3 manage.py startapp myapp

# Run Server

python3 manage.py runserver

http://127.0.0.1:8000/admin/login/?next=/admin/

# Migration

python3 manage.py migrate

python3 manage.py showmigrations

python3 manage.py dbshell

python3 manage.py makemigrations

# Create Admin User

python3 manage.py createsuperuser