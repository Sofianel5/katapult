from django.db import models
from users.models import Buyer, DemographicProfile, Adspace

# Create your models here.
class Constants():
    BUSINESS_TYPES =[("Cars", "Cars")]

class MarketSegment(models.Model):
    business_type = models.CharField(max_length=10, choices=Constants.BUSINESS_TYPES)
    demographics = models.ForeignKey(DemographicProfile, on_delete=models.CASCADE)
    def __str__(self):
        return self.business_type

class Campaign(models.Model):
    #comma delimited list of tags
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    marketSegment = models.ForeignKey(MarketSegment, blank=True, null=True, on_delete=models.CASCADE)
    #comma delimited list of business locations in address form
    #give option to upload csv
    #locations_of_business = models.TextField(blank=True)
    adspace = models.ForeignKey(Adspace, on_delete=models.CASCADE, related_name="campaigns")
    budget = models.FloatField()
    start = models.DateField()
    end = models.DateField()
    def __str__(self):
        return self.marketSegment.__str__()