from django.db import models


# Create your models here.
class Hash(models.Model):
    class Status(models.TextChoices):
        in_progress = "IN_PROGRESS"
        ready = "READY"
        error = "ERROR"
    request_id = models.CharField(max_length=128)
    status = models.CharField(max_length=15, choices=Status.choices)
    data = models.CharField(max_length=40, null=True)


