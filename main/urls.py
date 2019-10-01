from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-landing"),
    path("businesses/", views.businesses, name="businesses"),
    path("individuals/", views.individuals, name="individuals"),
    path("gate/", views.gate, name="gate"),
]
