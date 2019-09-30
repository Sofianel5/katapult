from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Payment info
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)

class Adspace(models.Model):
    TERM_LENGTHS = (
        ("2w", "Two week"),
        ("1m", "One month"),
        ("3m", "Three months"),
        ("6m", "Six months"),
        ("1y", "One year"),
        ("2y", "Two year"),
        ("3y", "Three year"),
    )
    date_posted = models.DateTimeField(default=timezone.now)
    term_length = models.CharField(max_length=2, choices=TERM_LENGTHS)
    title = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="adspace_pics")
    description = models.TextField()
    renter = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    active = models.BooleanField()
