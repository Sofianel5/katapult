from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="main-landing"),
    path("businesses/", views.businesses, name="businesses"),
    path("individuals/", views.individuals, name="individuals"),
    path("gate/", views.gate, name="gate"),
    path("profile/", views.profile, name="profile"),
    path("solutions-businesses", views.solutions_businesses, name="solutions-businesses"),
    path("solutions-individuals", views.solutions_individuals, name="solutions-individuals"),
    path("why-katapult/", views.whykatapult, name="whykatapult"),
    path("info-leadership/", views.info_leadership, name='info-leadership'),
]