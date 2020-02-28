from django.shortcuts import render
from users.models import Adspace, Seller
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context = {}
    context['user'] = request.user
    return render(request, 'main/index.html', context)

def businesses(request):
    context = {}
    context['user'] = request.user
    return render(request, '/main/businesses.html', context)

def individuals(request):
    context = {}
    context['user'] = request.user
    return render(request, '/main/individuals.html', context)

def gate(request):
    context = {}
    context['user'] = request.user
    return render(request, 'main/gate.html', context)

def whykatapult(request):
    context = {}
    context['user'] = request.user
    return render(request, "main/whykatapult.html", context)

def solutions_businesses(request):
    context = {}
    context['user'] = request.user
    return render(request, 'main/solutions-businesses.html', context)

def solutions_individuals(request):
    context = {}
    context['user'] = request.user
    return render(request, 'main/solutions-individuals.html', context)

@login_required
def profile(request):
    context = {}
    context['user'] = request.user
    try:
        seller = Seller.objects.all().filter(user = request.user).first()
        print(seller)
        context['adspaces'] = Adspace.objects.all().filter(seller = seller)
        print(context)
    except:
        print("not a seller")
    return render(request, 'main/profile.html', context)
    
def info_leadership(request):
    context = {}
    return render(request, 'main/info-leadership.html', context)