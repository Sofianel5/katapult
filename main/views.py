from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def businesses(request):
    context = {}
    return render(request, '/main/businesses.html', context)
def individuals(request):
    context = {}
    return render(request, '/main/individuals.html', context)
def gate(request):
    context = {}
    return render(request, 'main/gate.html', context)
