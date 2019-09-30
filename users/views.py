from django.shortcuts import render
from .forms import UserRegisterForm
# Create your views here.
def signup(request):
    context = {}
    if request.method == "GET":
        try:
            type = request.GET["type"]
            if type == "businesses":
                context["type"] = "businesses"
            elif type == "individuals":
                context["type"] = "individuals"
        except:
            type = None
        context["form"] = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
    return render(request, "users/signup.html", context)
