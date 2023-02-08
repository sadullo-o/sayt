from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=150, default='')
    category = models.CharField(max_length=70, default='')
    cost = models.CharField(max_length=150)


    def __str__(self):
        return self.title


# pip install djangorestframework