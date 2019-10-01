from django.shortcuts import render, redirect
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
            return redirect('main-landing') # redirect to success: sell or buy
    return render(request, "users/signup.html", context)

def signin(request):
    context = {}
    if request.method == "GET":
        context["form"] = UserRegisterForm()
    return render(request, "users/signin.html", context)
