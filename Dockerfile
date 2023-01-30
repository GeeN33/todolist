# образ на основе которого создаём контейнер
FROM python:3.9.6-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/code

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

# копируем содержимое текущей папки в контейнер
COPY . .

