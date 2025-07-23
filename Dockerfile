FROM python:3.11-slim
# возьмите образ, который скачали ранее и в котором уже установлен Python

LABEL author=${AUTHOR}
# добавьте label, используя переменную среды

COPY . ./churn_app
# скопируйте файлы в Docker
# название директории внутри контейнера: churn_app

WORKDIR /churn_app 
# измените рабочую директорию Docker 

RUN pip3 install -r requirements.txt
# инструкция для установки библиотек

EXPOSE ${APP_PORT}
# инструкции для открытия порта, указанного в переменной среды


VOLUME /models
# примонтируйте том с моделями


CMD uvicorn app.churn_app:app --reload --port ${APP_PORT} --host 0.0.0.0
# измените команду запуска, учитывая порт из .env