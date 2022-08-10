from django.db import models


class Word(models.Model):
    original = models.CharField(max_length=40, unique=True)
    translation = models.CharField(max_length=40)


# Create your models here.
