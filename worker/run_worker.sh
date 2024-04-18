#!/bin/sh

# wait for RabbitMQ server to start
sleep 5

# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
celery -A backend worker --loglevel=INFO
python manage.py runserver 0.0.0.0:8090
