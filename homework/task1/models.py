from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    age = models.IntegerField(default=18)

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    size = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    description = models.TextField(default='nothing')
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

