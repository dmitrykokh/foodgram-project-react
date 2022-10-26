# Foodgram - a social network for sharing recipes

![Django-app workflow](https://github.com/dmitrykokh/foodgram-project-react/actions/workflows/main.yml/badge.svg)

![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)
![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)
![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)
![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)

## Description

To exchange recipes, you need to log in (create an account) and click the "create recipe"
button To add a recipe to your shopping list or favorites and subscribe to the
author's recipes, you need to open the appropriate tabs, or click
the appropriate buttons on the recipe.

## Technologies

    Django==2.2.16
    djangorestframework==3.12.4
    django-filter==22.1
    django-templated-mail==1.1.1
    djangorestframework-simplejwt==4.8.0
    djoser==2.1.0
    drf-extra-fields==3.4.0
    filter==0.0.0.20200724
    isort==5.10.1
    Pillow==9.2.0
    python-dotenv==0.20.0
    requests==2.28.1
    psycopg2-binary==2.8.6
    gunicorn==20.0.4
    pytest==6.2.4
    pytest-django==4.4.0

## The template for filling the env file is located at: 

[infra/example.env](./infra/example.env)

To run CI, the DOCKER_USERNAME=example variable must be present in the Github secrets environment

## Project launching:

### To launch a project, apply migrations, create a superuser, load static and add data from fixtures to the database, respectively, you need to run the commands in the infra folder:
    
    docker-compose up -d --build
    sudo docker-compose exec backend python manage.py migrate
    sudo docker-compose exec backend python manage.py createsuperuser
    sudo docker-compose exec backend python manage.py collectstatic --no-input
    sudo docker-compose exec backend python manage.py loaddata ingredient.json

after that, the container will be assembled and launched, the admin panel is available at:  

    /admin/


to stop and clean the container, run in the infra folder:

     docker-compose down -v


## Documentation with examples of API requests is available at:

    /api/docs/


Author: [__Dmitry Kokh__](https://github.com/dmitrykokh)
