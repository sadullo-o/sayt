import datetime

from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title