from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.
def inicio(request):
    return HttpResponse("Hola")

def familiar(request):
    familiar1 = Familiar(nombre="Juan", edad= 54, fecha_nacimiento= "1968-10-11")
    familiar1.save()
    return render(request, "padre.html", {"familiar1": familiar1})