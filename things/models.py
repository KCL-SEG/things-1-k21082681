from django.db import models
from django.db.models import Model

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(unique=False, 
                                   MinValueValidator= 0,
                                   MaxValueValidator= 100,)