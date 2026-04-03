# django

Django project

# Activate the Enviroment

pipenv shell

or

source /Users/user/.local/share/virtualenvs/django-3PNZeuAl/bin/activate

# Create Project

django-admin startproject worldtour .

# Create a New App

python3 manage.py startapp asiatoursagency

# Run Server

python3 manage.py runserver

http://127.0.0.1:8000

# Migration

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py showmigrations

# Insert records by command

python3 manage.py shell

from asiatoursagency.models import Tour
to1 = Tour(origin_country="Portugal", destination_country="India", number_of_days=10, price=1000)
to1.save()  

# Create Admin User

python3 manage.py createsuperuser