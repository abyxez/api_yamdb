# API_YAMDB

Авторы проекта:
- Константин Питонов 
- [Максим](https://github.com/BoomBot987)
- [Игорь Бобров](https://github.com/makaimura000)
***

Проект выполнялся в команде из 3-ёх человек, я выполнял обязанность тимлида. Данная работа имитирует соц. сеть с возможностью регистрации по API, без фронтенд части. Можно оставлять отзывы про различные произведения искусства с разделением на категории и жанры. Реализована система подписок, комментариев к постам-отзывам;

***

## Tecnhologies

- Python 3.10
- Django 3.2
- Django REST framework 3.2.14

***

Локальзый запуск проекта:
```
git clone

cd api_yamdb/
```

Cоздать и активировать виртуальное окружение (macOS/Linux) : 
```
python3 -m venv env

source venv/bin/activate
```

or (Windows)
```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt: 

```
python3 -m pip install --upgrade pip

pip install -r requirements.txt
```

Выполнить миграции: 
```
cd api_yamdb/

python3 manage.py migrate

python3 manage.py runserver
```

Все возможные API (e.g. Postman) запросы к серверу доступны в документации по адресу:

127.0.0.1:8000/redoc/