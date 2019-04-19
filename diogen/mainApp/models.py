from django.db import models

# Create your models here.

class Person(models.Model):
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    spec=models.IntegerField
    phone=models.CharField(max_length=200)
    email=models.EmailField

    def __str__(self):
        return self.name

