from django.contrib import admin
from .models import Account, Seller, Adspace, DemographicProfile

# Register your models here.
admin.site.register(Account)
admin.site.register(Seller)
admin.site.register(DemographicProfile)
