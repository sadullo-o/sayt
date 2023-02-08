from django.db import models

# Create your models here.

class Video(models.Model):
    username = models.CharField(max_length=150)
    file = models.FileField()

    def __str__(self):
        return self.username


class Cartoon(models.Model):
    username = models.CharField(max_length=150)
    file = models.FileField()

    def __str__(self):
        return self.username