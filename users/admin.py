from django.contrib import admin
from .models import Account, Seller, Adspace, DemographicProfile, AdspaceImage

# Register your models here.
class AdspaceImageInline(admin.TabularInline):
    model = AdspaceImage
    extra = 3

class AdspaceAdmin(admin.ModelAdmin):
    inlines = [ AdspaceImageInline, ]

admin.site.register(Adspace, AdspaceAdmin)
admin.site.register(Account)
admin.site.register(Seller)
admin.site.register(DemographicProfile)
