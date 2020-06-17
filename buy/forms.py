from django import forms
from .models import Campaign

class CampaignCreationForm(forms.ModelForm):
    start = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M %p'])
    end = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M %p'])
    class Meta:
        model = Campaign
        fields = ['budget', 'start', 'end']

class ReserveForm(forms.ModelForm):
    pass