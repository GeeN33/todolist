# образ на основе которого создаём контейнер
FROM python:3.9.6-alpine

COPY .todolist/srv/www/todolist .
WORKDIR /srv/www/todolist

RUN pip install -r requirements.txt

