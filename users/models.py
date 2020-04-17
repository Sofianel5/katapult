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
    email = models.EmailField(verbose_name=_("Email"), max_length=150, unique=True)
    name = models.CharField(verbose_name=_("Company name"), max_length=150)
    date_joined = models.DateTimeField(verbose_name=_("date joined"), auto_now_add=True)
    last_login = models.DateTimeField(verbose_name=_("last login"), auto_now=True)
    phone = models.CharField(_("Phone number"), max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    description = models.TextField(verbose_name=_("Company description"),blank=True, null=True)
    public_email = models.EmailField(verbose_name=_("Email"), blank=True, null=True)
    website = models.URLField(verbose_name=_("Website"),blank=True, null=True)
    tags = models.TextField(verbose_name=_("Tags"),blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    is_seller = models.BooleanField(default=True, blank=True, null=True)
    is_buyer = models.BooleanField(default=True,blank=True, null=True)
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

class DemographicProfile(models.Model):
    AgePercentUnder5 = models.FloatField(null=True, blank=True)
    AgePercent5To9 = models.FloatField(null=True, blank=True)
    AgePercent10To14 = models.FloatField(null=True, blank=True)
    AgePercent15To19 = models.FloatField(null=True, blank=True)
    AgePercent20To24 = models.FloatField(null=True, blank=True)
    AgePercent25To34 = models.FloatField(null=True, blank=True)
    AgePercent35To44 = models.FloatField(null=True, blank=True)
    AgePercent45To54 = models.FloatField(null=True, blank=True)
    AgePercent55To59 = models.FloatField(null=True, blank=True)
    AgePercent60To64 = models.FloatField(null=True, blank=True)
    AgePercent65To74 = models.FloatField(null=True, blank=True)
    AgePercent75To84 = models.FloatField(null=True, blank=True)
    AgePercent85AndOver = models.FloatField(null=True, blank=True)
    medianAge = models.FloatField(null=True, blank=True)
    IncomePercentUnder10000 = models.FloatField(null=True, blank=True)
    IncomePercent10000To14999 = models.FloatField(null=True, blank=True)
    IncomePercent15000To24999 = models.FloatField(null=True, blank=True)
    IncomePercent25000To34999 = models.FloatField(null=True, blank=True)
    IncomePercent35000To49999 = models.FloatField(null=True, blank=True)
    IncomePercent50000To74999 = models.FloatField(null=True, blank=True)
    IncomePercent75000To99999 = models.FloatField(null=True, blank=True)
    IncomePercent100000To149999 = models.FloatField(null=True, blank=True)
    IncomePercent150000To199999 = models.FloatField(null=True, blank=True)
    IncomePercent200000OrMore = models.FloatField(null=True, blank=True)
    medianIncome = models.FloatField(null=True, blank=True)
    PercentWhite = models.FloatField(null=True, blank=True)
    PercentBlack = models.FloatField(null=True, blank=True)
    PercentAmericanIndian = models.FloatField(null=True, blank=True)
    PercentAsian = models.FloatField(null=True, blank=True)
    PercentPacificIslander = models.FloatField(null=True, blank=True)
    PercentOtherRace = models.FloatField(null=True, blank=True)
    PercentHispanicOrLatinoOfAnyRace = models.FloatField(null=True, blank=True)
    PercentNotHispanicOrLatino = models.FloatField(null=True, blank=True)
    populationDensity = models.FloatField(null=True, blank=True)
    PercentMale = models.FloatField(null=True, blank=True)
    PercentFemale = models.FloatField(null=True, blank=True)
    BachDegree = models.FloatField(null=True, blank=True)
    GradDegree  = models.FloatField(null=True, blank=True)
    AssocDegree = models.FloatField(null=True, blank=True)
    SomeCollege = models.FloatField(null=True, blank=True)
    HighSchool = models.FloatField(null=True, blank=True)
    BelowHighSchool  = models.FloatField(null=True, blank=True)
    WhiteCollar = models.FloatField(null=True, blank=True)
    Unemployed = models.FloatField(null=True, blank=True)
    BlueCollar = models.FloatField(null=True, blank=True)
    avgHouseholdSize = models.FloatField(null=True, blank=True)

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
    STATES = (
        ("NY", "NY"),
    )
    date_posted = models.DateTimeField(default=timezone.now)
    term_length = models.CharField(max_length=2, choices=TERM_LENGTHS)
    title = models.CharField(max_length=100)
    direct_price = models.FloatField()
    height = models.FloatField()
    city = models.CharField(max_length=64,null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=2, choices=STATES,null=True, blank=True)
    width = models.FloatField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    image = models.ImageField(default="adspace_pics/default.jpg", upload_to="adspace_pics")
    description = models.TextField()
    renter = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING,null=True, blank=True)
    active = models.BooleanField(default=True)
    demographics = models.ForeignKey(DemographicProfile, on_delete=models.CASCADE,null=True, blank=True)

