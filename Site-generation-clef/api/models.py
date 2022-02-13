from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    rating = models.IntegerField(
        default=None, null=True, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    picture_url = models.CharField(max_length=1024, default=None, blank=True, null=True)
    password = models.CharField(max_length=255)


class Wallet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    private_key = models.CharField(max_length=255, default=None, blank=True)
    public_key = models.CharField(max_length=255, default=None, blank=True)
    funds = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True)


class Asset(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    image_url = models.CharField(max_length=1024, default=None, blank=True, null=True)
    rating = models.IntegerField(
        default=None, null=True, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )


class Posting(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    date_posted = models.DateTimeField(default=None, blank=True)
    last_modified = models.DateTimeField(default=None, blank=True)
    starting_date = models.DateField()
    end_date = models.DateField()
    cost_per_day = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Reservation(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    starting_date = models.DateField()
    end_date = models.DateField()
    date_booked = models.DateTimeField(default=None, blank=True)
    last_modified = models.DateTimeField(default=None, blank=True)
    total_cost = models.DecimalField(
        default=0, max_digits=5, decimal_places=2, blank=True
    )
