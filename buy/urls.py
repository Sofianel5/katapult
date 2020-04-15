from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.buy, name="buy"),
    path("form2", views.business_form_2, name="form2"),
    #path("/campaign", views.campaign, name="campaign")
]
