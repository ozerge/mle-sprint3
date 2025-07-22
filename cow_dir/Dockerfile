# возьмём образ, который мы скачали ранее и в котором уже установлен Python 
FROM python:3.11-slim

# копируем файлы в Docker
COPY . ./cow_dir

# изменяем рабочую директорию Docker
WORKDIR cow_dir 

# в Docker изначально нет библиотеки python-cowsay
# вам нужно написать инструкцию RUN, которая установит библиотеку с помощью pip
# установите версию библиотеки 1.1.0
RUN ["pip3", "install", "python-cowsay==1.1.0"]


# команда, которая должна исполняться при старте контейнера
CMD ["python3", "./main.py"]

# docker pull docker/whalesay
# docker image ls
# docker container run docker/whalesay
# docker run docker/whalesay cowsay "Hello Yandex"
# docker image build . --tag cow_image:0
# docker run cow_image:0