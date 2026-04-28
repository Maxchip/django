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

# api_project

-- Load the env
pipenv shell

-- Install packages
pip install -r requirements.txt

-- Create a new main project
django-admin startproject mysite

or

python3 -m django startproject mysite

-- Create the api project
cd mysite
python3 manage.py startapp api

-- Create model and urls

-- Create database
python3 manage.py makemigrations
python3 manage.py migrate

-- Run Server
python3 manage.py runserver

-- Install JWT Authentication

Add to the requirements.txt this
djangorestframework-simplejwt

pip install -r requirements.txt

python3 manage.py migrate

-- Create admin account

python3 manage.py createsuperuser

-- To start

pipenv shell
python3 manage.py runserver

-- Link

http://localhost:8000/admin/
http://localhost:8000/api/schema/swagger-ui/
http://localhost:8000/api/schema/redoc/

