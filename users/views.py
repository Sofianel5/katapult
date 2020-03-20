from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, MoreInfoForm
# Create your views here.
def signup(request):
    context = {}
    if request.method == "GET":
        context["form"] = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
        context["form"] = form
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('more-info')) # redirect to success: sell or buy
    return render(request, "users/signup.html", context)

@login_required
def more_info(request):
    context = {}
    if request.method == "GET":
        context["form"] = MoreInfoForm(instance=request.user)
    else:
        form = MoreInfoForm(request.POST, instance=request.user)
        context["form"] = form 
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect(reverse('profile'))
    return render(request, "users/moreinfo.html", context)

@login_required
def enable_buying(request):
    if request.method == "POST":
        user = request.user 
        user.is_buyer = True
        user.save()
        return HttpResponse(status=200)

@login_required
def enable_selling(request):
    if request.method == "POST":
        user = request.user 
        user.is_seller = True
        user.save()
        return HttpResponse(status=200)