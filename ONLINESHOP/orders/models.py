from django.db import models

# Create your models here.

class Clients(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=50)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    
class Items(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()
    
class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    deliverer = models.BooleanField()
    