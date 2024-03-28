from datetime import datetime
from django.db import models


class Appointment(models.Model):
    date = models.DateTimeField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=29,
    )
    message = models.TextField()

