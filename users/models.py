from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .managers import MyAccountManager
# Create your models here.

class Account(AbstractBaseUser):
    username = None
    email = models.EmailField(verbose_name="Email", max_length=150, unique=True)
    name = models.CharField(verbose_name="Company name", max_length=150)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = MyAccountManager()
    def __str__(self):
        return self.name
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

class Seller(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    # Payment info
class Buyer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
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
    direct_price = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    image = models.ImageField(default="default.jpg", upload_to="adspace_pics")
    description = models.TextField()
    renter = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING,null=True, blank=True)
    active = models.BooleanField(default=True)
