from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    study = models.BooleanField()