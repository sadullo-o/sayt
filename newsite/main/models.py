from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'yangilik'
        verbose_name_plural = 'Yangiliklar'



class Card(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'Biz haqimizda'


# python manage.py makemigrations

# python manage.py migrate

# pip install Pillow


class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    subject = models.TextField()

    def __str__(self):
        return self.firstname
