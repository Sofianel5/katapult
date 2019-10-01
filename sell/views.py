from django.shortcuts import render
from .forms import PublishAdspaceForm
# Create your views here.
def sell(request):
    context = {}
    if request.method == "GET":
        context["form"] = PublishAdspaceForm()
        print(context)
        return render(request, "sell/sell.html", context)
    else:
        context["form"] = PublishAdspaceForm(request.POST)
        if form.is_valid():
            return redirect("main-landing")
    return render(request, "sell/sell.html", context)
