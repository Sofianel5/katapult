from django import forms
from django.contrib.auth.models import User
from .models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Account
        fields = ['name', 'email', 'password1', 'password2', 'phone']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        name = self.cleaned_data.get('name')
        if email and Account.objects.filter(email=email).exclude(name=name).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class MoreInfoForm(forms.ModelForm):
    class Meta:
        model = Account 
        fields = ['description', 'logo', 'public_email', 'website', 'tags', 'address', 'is_seller', 'is_buyer']
    