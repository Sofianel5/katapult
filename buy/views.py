from django.shortcuts import render
from .forms import CampaignCreationForm
from .models import Campaign
from .analysis import sortMatchingSegments, getCoordinates
from users.models import Buyer, Adspace
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.

@login_required
def buy(request):
    if request.method == "GET":
        """
        form = CampaignCreationForm(request.POST)
        context = {}
        context['form'] = form
        context['user'] = request.user
        print("FORM ", form)
        """
        lt200 = [a for a in Adspace.objects.all() if a.price_per_day < 200]
        lt100 = [a for a in Adspace.objects.all() if a.price_per_day < 100]
        groups = [
            {
                "adspaces": [Adspace.objects.get(pk=2), ],
                "title": "Featured Adspaces"
            },
            {
                "adspaces": Adspace.objects.all(),
                "title": "All",
            }, 
            {
                "adspaces": lt200,
                "title": "Spaces less than $200/day"
            },
            { 
                "adspaces": lt100,
                "title": "Spaces less than $100/day"
            },
        ]
        context = {
            "groups": groups
        }
        return render(request, "buy/landing.html", context)
    #FORM: take tags describing business, list of business locations
    else:
        form = CampaignCreationForm(request.POST)
        context = {}
        context['user'] = request.user
        context['form'] = form
        print("FORM ", form)
        if form.is_valid():
            if len(Buyer.objects.all().filter(user=request.user)) < 1:
                buyer = Buyer.objects.create(user=request.user)
                buyer.save()
            else:
                buyer = Buyer.objects.all().filter(user=request.user).first()
            result = form.save(commit=False)
            if result.marketSegment == None:
                context["errormessage"] = "Need to identify a market segment"
                return render(request, "buy/business_form.html", context)
            result.buyer = buyer
            matches = sortMatchingSegments(result.marketSegment, result.budget)
            if len(matches) < 1:
                context["errormessage"] = "Could not find any advertisments of specified price range."
                return render(request, "buy/business_form.html", context)
            result.save()
            context['matches'] = matches
            context['coordinates'] = getCoordinates(matches)
            context['budget'] = result.budget
            print(context)
            print(matches)
            return render(request, "buy/campaign.html", context)
        else:
            return render(request, "buy/business_form.html", context)

def business_form_2(request):
    return render(request, "buy/business_form_2.html")

def business_form_3(request):
    return render(request, "buy/business_form_3.html")

def view_space(request, pk):
    adspace = Adspace.objects.get(pk=pk)
    coordinates = getCoordinates([adspace])[0]
    context = {'adspace':adspace, 'coordinates': coordinates}
    return render(request, "buy/adspace.html", context)

def reserve(request, pk):
    if request.method == "GET":
        adspace = Adspace.objects.get(pk=pk)
        form = CampaignCreationForm()
        context = {'adspace':adspace, 'form': form}
        return render(request, "buy/reserve.html", context)
    else:
        adspace = Adspace.objects.get(pk=pk)
        form = CampaignCreationForm(request.POST)
        context = {'adspace':adspace, 'form': form}
        if form.is_valid():
            campaign = Campaign(**form.cleaned_data)
            send_mail(
                'New buy request',
                'email: ' +request.user.email + "\n" + "pk: " + str(campaign.pk),
                'admin@katapult.systems',
                ['slarbi10@stuy.edu', 'lkronman10@stuy.edu'],
                fail_silently=True,
            )
            return render(request, "buy/success.html")
        print(form.errors)
        return render(request, "buy/reserve.html", context)

