from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegisterForm
# Create your views here.
def signup(request):
    context = {}
    if request.method == "GET":
        context["form"] = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
        context["form"] = form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('signin')) # redirect to success: sell or buy
    return render(request, "users/signup.html", context)

def signin(request):
    context = {}
    if request.method == "GET":
        context["form"] = UserRegisterForm()
    return render(request, "users/signin.html", context)