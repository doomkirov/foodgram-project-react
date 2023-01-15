![API for Foodgram project workflow!](https://github.com/doomkirov/foodgram-project-react/actions/workflows/foodgram-project-react_workflow.yml/badge.svg)
# Проект Foodgram

Адрес проекта: http://158.160.35.198
Доступ к admin-панели: admin@admin.ru - admin123

## Описание

Foodgram - продуктовый помощник с базой кулинарных рецептов. Позволяет публиковать рецепты, сохранять избранные, а также формировать список покупок для выбранных рецептов. Можно подписываться на любимых авторов.

## Шаблон заполнения .env файла

DB_ENGINE=*<тип БД>*

DB_NAME=*<имя базы данных>*

POSTGRES_USER=*<логин для подключения к базе данных>*

POSTGRES_PASSWORD=*<пароль для подключения к БД>*

DB_HOST=*<название сервиса (контейнера)>*

DB_PORT=*<порт для подключения к БД>*

SECRET_KEY=*<SECRET_KEY Django>*

## Установка

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/doomkirov/foodgram-project-react.git
```

```
cd foodgram-project-react
cd infra
```

Запустить проект в контейнерах Docker

```
docker-compose up -d
```
Провести миграции: 

```
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate
```

Создать суперпользователя:

```
docker-compose exec bakend python manage.py createsuperuser
```
Собрать статику:

```
docker-compose exec backend python manage.py collectstatic --no-input
```

## Заполнение базы данными

```
docker-compose exec backend python manage.py add_ingridients
```
## Доступ к сайту на локальной машине
```
http://localhost/
```
Документация
```
http://localhost/api/docs/redoc.html
```
### Автор
Проект выполнен совместно c сервисом Яндек.Практикум.
Я, Шилов Иван, занимался разработкой всего, что связано с серверной частью
проекта (папка backend), настройкой собственного сервера и нужных для 
его работы файлов (default.conf, docker-compose.yml, Dockerfile)