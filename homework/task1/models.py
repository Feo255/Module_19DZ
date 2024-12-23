from django.db import models
from django.db.models import ForeignKey


# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField
    age = models.IntegerField

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField
    size = models.DecimalField
    description = models.TextField
    age_limited = models.BooleanField(default=False)

