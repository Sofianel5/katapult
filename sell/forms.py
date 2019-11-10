from django import forms
from django.contrib.auth.models import User
from users.models import Adspace
from django.contrib.auth.forms import UserCreationForm


class PublishAdspaceForm(forms.ModelForm):
    class Meta:
        model = Adspace
        fields = ['title', 'term_length', 'direct_price', 'height', 'width', 'address', 'image', 'description', 'state', 'zip', 'city']
