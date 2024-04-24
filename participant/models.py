from django.db import models

# Create your models here.

class Participant (models.Model):
    nick = models.CharField(max_length=255,unique=True)
    email=  models.CharField(max_length=255,unique=True)
    winner = models.BooleanField(default=False)