FROM python:3.10


WORKDIR /usr/src/manager


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


COPY  requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .