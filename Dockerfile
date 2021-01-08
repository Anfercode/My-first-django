FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN pip3.8 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3.8", "manage.py", "runserver", "0.0.0.0:8000"]
