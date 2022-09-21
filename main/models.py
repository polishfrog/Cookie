from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=24, default='Xd')
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=128, default='none@mail.com')
