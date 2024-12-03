from django.shortcuts import render
from SERVICES.models import Service

# Create your views here.

def home (request):
    return render(request, "home.html")

def shop (request):
    return render(request, "shop.html")



