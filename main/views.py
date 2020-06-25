from django.shortcuts import render
from django.http import JsonResponse
from users.models import Adspace, Seller
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm
from .utils import legality_check
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    context = {}
    context['user'] = request.user
    context['form'] = UserRegisterForm()
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

def blog(request):
    context = {}
    return render(request, 'main/blog.html', context)

@csrf_exempt
def legality(request):
    context = {}
    if request.method == "POST":
        address = request.POST['address']
        return JsonResponse({"legal": legality_check(address)}, safe=False)
    return render(request, 'main/legality.html', context)


def soon(request):
    return render(request, "main/coming-soon.html")