from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)


class Wallet(models.Model):
    private_key = models.CharField(max_length=255, default=None, blank=True)
    public_key = models.CharField(max_length=255, default=None, blank=True)

class Vote(models.Model):
    timestamp = models.CharField(max_length=255, default=None, blank=True)
    vote = models.CharField(max_length=255, default=None, blank=True)
    hash = models.CharField(max_length=255, default=None, blank=True)
    hash_publique = models.CharField(max_length=255, default=None, blank=True)
