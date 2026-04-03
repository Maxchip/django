# django
Django project


# Install PIPENV

brew install pipenv

python3 --version
pipenv --version

# Install DJANGO

pipenv install django

pipenv shell

django-admin startproject inesctec .

pipenv --venv

# Activate the Enviroment

source /Users/user/.local/share/virtualenvs/django-3PNZeuAl/bin/activate

# Run Server

python3 manage.py runserver

http://127.0.0.1:8000/admin/login/?next=/admin/

# Install Debug

pipenv install django-debug-toolbar

# Create a New App

python3 manage.py startapp playground

# Migration

python3 manage.py migrate

python3 manage.py showmigrations

python3 manage.py dbshell

python3 manage.py makemigrations

# Create Admin User

python3 manage.py createsuperuser