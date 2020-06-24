from django.shortcuts import render, HttpResponse



from .models import Clasificado

# Create your views here.
def clasificados(request):
    clasif = Clasificado.objects.all()
    return render(request, "core/home.html", {'clasif':clasif})


def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    return render(request, "core/contact.html")

