from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    imageurl = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=8)
    desc = models.CharField(max_length=1000)
    disc = models.FloatField()
