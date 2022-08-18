from django.db import models


class User(models.Model):
    google_id = models.CharField(max_length=255, unique=True)
    user_email = models.EmailField(max_length=40, unique=True)

class Word(models.Model):
    original = models.CharField(max_length=40)
    translation = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "words", null=True)

    class Meta:
        unique_together = ('original', 'user')


# Create your models here.
