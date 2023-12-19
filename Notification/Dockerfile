FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8002


CMD         ["uvicorn", "main:app", "--port", "8002", "--host", "0.0.0.0"]
