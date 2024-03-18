from django.db import models
from datetime import datetime


class Investment(models.Model):
    investment = models.TextField(max_length=255)
    value = models.FloatField()
    paid = models.BooleanField(default=False)
    date = models.DateField(default=datetime.now)