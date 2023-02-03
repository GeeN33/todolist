FROM python:3.10-slim
MAINTAINER painassasin@icloud.com

WORKDIR /opt/

EXPOSE 8000

# Устанавливаем зависимости для Postgre
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

ENTRYPOINT ["bash", "entrypoint.sh"]