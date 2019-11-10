from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.buy, name="buy"),
    #path("/campaign", views.campaign, name="campaign")
]
