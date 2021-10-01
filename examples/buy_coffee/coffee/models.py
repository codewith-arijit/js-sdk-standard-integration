from django.db import models

# Create your models here.

class Coffee(models.Model):
    cups = models.IntegerField()
    name = models.CharField(max_length=255)