git clone 
cd api_yamdb/
Cоздать и активировать виртуальное окружение:

python3 -m venv env
source venv/bin/activate (macOS)
or 
source venv/Scripts/activate ( WIN )
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

cd api_yamdb/
python3 manage.py migrate
Запустить проект:

python3 manage.py runserver
Этот проект имитирует работу социальной сети без front-end части с использованием API cервисов.

Все возможные запросы к серверу доступны в документации по адресу:

127.0.0.1:8000/redoc/

