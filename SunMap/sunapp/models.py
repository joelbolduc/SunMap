from django.db import models

# Create your models here.

class Site(models.Model):
    name = models.CharField(max_length=80)
    lat = models.FloatField()
    lon = models.FloatField()
    rating = models.IntegerField()
