import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery("backend")
# app.conf["task_time_limit"] = 5800
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

