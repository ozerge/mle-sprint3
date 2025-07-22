FROM ubuntu:latest
# вы указываете, что ваш образ будет основан на образе ubuntu:latest

RUN ["mkdir", "/my_super_dir"]
# создавая образ, docker должен будет также создать диреторию в корневой папке

# FROM ubuntu:latest
# RUN ["mkdir", "/my_super_dir"]
# RUN echo "Hello world!" > /my_super_dir/super_file.txt

FROM python:3.11-slim
# возьмём образ, который мы скачали ранее и в котором уже установлен Python

LABEL author="mle-student"
# инструкция LABEL задаёт метаданные для контейнера
# можно указать своё имя

COPY . ./my_super_dir
# инструкция COPY копирует содержимое текущей директории в директорию, 
# которую указали второй командой - в данном случае это my_super_dir
# если такой директории не было, docker её создаст

WORKDIR my_super_dir 
# изменяем рабочую директорию Docker 
# эта команда похожа на инструкцию RUN ["cd", "./my_super_dir"]
# в документации Docker рекомендуется использовать именно WORKDIR

CMD ["python3", "./main.py"]
# эта инструкция указывает ту команду, которая должна выполниться при старте контейнера 