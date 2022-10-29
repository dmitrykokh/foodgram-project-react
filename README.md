# Foodgram - «Продуктовый помощник».

![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)
![Django](https://img.shields.io/badge/-Django-464646?style=flat&logo=Django&logoColor=56C0C0&color=008080)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat&logo=PostgreSQL&logoColor=56C0C0&color=008080)
![Docker](https://img.shields.io/badge/-Docker-464646?style=flat&logo=Docker&logoColor=56C0C0&color=008080)
![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat&logo=Yandex.Cloud&logoColor=56C0C0&color=008080)

## Описание

Онлайн-сервис для обмена рецептами. На этом сервисе пользователи смогут публиковать рецепты,
подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное»,
а перед походом в магазин скачивать сводный список продуктов,
необходимых для приготовления одного или нескольких выбранных блюд.

## Технологии

    Django==2.2.16
    djangorestframework==3.12.4
    django-filter==22.1
    django-templated-mail==1.1.1
    djangorestframework-simplejwt==4.8.0
    djoser==2.1.0
    drf-extra-fields==3.4.0
    isort==5.10.1
    Pillow==9.2.0
    python-dotenv==0.20.0
    requests==2.28.1
    psycopg2-binary==2.8.6
    gunicorn==20.0.4
    pytest==6.2.4
    pytest-django==4.4.0

## Запуск проекта:

### Для запуска проекта примените миграции, создайте суперпользователя, загрузите статику и добавьте данные в базу.
### Необходимо выполнить следующие команды:
    
    docker-compose up -d --build
    sudo docker-compose exec backend python manage.py migrate
    sudo docker-compose exec backend python manage.py createsuperuser
    sudo docker-compose exec backend python manage.py collectstatic --no-input
    sudo docker-compose exec backend python manage.py loaddata ingredient.json

панель админа будет доступна по адресу:  

    /admin/


для остановки и очистки контейнера запустите команду из папки infra:

     docker-compose down -v


## Документация с примером API запросов доступна:

    /api/docs/


Автор: [__Dmitry Kokh__](https://github.com/dmitrykokh)
