FROM python:3.11-slim

LABEL author=${AUTHOR}
# ${AUTHOR} - это переменная среды

COPY . ./simple_fast_api

WORKDIR simple_fast_api 
# директория simple_fast_api скопирована в Docker
# укажем инструкцию по запуску микросервиса

RUN pip3 install -r requirements.txt
# устанавливаем библиотеки из файла requirements.txt
# который ранее был скопирован инструкцией COPY . ./simple_fast_api
# вместе со всем содержимым текущей директории в simple_fast_api

VOLUME /speeches
# указываем, что директория speeches внутри контейнера будет являться томом
# на этапе сборки docker создаст необходимые файлы на самой виртуальной машине
# в директории /var/lib/docker/volumes/

EXPOSE ${APP_PORT}
# указываем переменную среды
# эта инструкция указывает образу, 
# что порт 1702 должен быть открыт 'снаружи'



CMD uvicorn app.main:app --host  0.0.0.0 --port ${APP_PORT}
# изменили команду на простую строку


# docker image build . --tag simple_fast_api:with_env

# # перед запуском нового контейнера не забудьте выключить старый
# docker container ps
# docker container stop <id>

# # запускаем контейнер
# docker container run --publish 4600:1702 --env-file .env --volume=./speeches:/simple_fast_api/speeches  simple_fast_api:with_env
# # добавляем флаг --env-file и указываем, из какого файла брать перменные среды

# в режиме detached: в нём команда docker container run запустит контейнер в фоновом режиме.
# docker container run \
# --publish 4600:1702 \
# -d \
# --env-file .env \
# --volume=./speeches:/simple_fast_api/speeches \
# simple_fast_api:with_env