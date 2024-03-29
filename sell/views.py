from django.shortcuts import render, redirect
from .forms import PublishAdspaceForm
from users.models import Seller, AdspaceImage
from utils import createDemographicProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def sell(request):
    context = {}
    if request.method == "GET":
        context["form"] = PublishAdspaceForm()
        context['user'] = request.user
        print(context)
        return render(request, "sell/sell.html", context)
    else:
        form = PublishAdspaceForm(request.POST)
        context['user'] = request.user
        context["form"] = form
        if form.is_valid():
            if len(Seller.objects.all().filter(user=request.user)) < 1:
                seller = Seller.objects.create(user=request.user)
                seller.save()
            else:
                seller = Seller.objects.all().filter(user=request.user).first()
            result = form.save(commit=False)
            result.seller = seller
            result.demographics = createDemographicProfile(result.address, result.city, result.state, result.zip)
            result.save()
            for f in request.FILES:
                print(f)
                AdspaceImage.objects.create(image=f, adpace=result)
            return redirect("main-landing")
    return render(request, "sell/sell.html", context)
