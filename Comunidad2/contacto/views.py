from django.shortcuts import render
from django.core.mail import send_mail
from contacto.forms import formularioContacto
# Create your views here.




def contacto(request):
     return render(request, "contacto/contacto.html")

