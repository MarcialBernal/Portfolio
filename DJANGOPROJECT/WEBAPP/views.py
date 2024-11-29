from django.shortcuts import render
from SERVICES.models import Service

# Create your views here.

def home (request):
    return render(request, "home.html")

def services (request):
    
    services = Service.objects.all()
    return render(request, "services.html", {"services":services})

def shop (request):
    return render(request, "shop.html")

def contact (request):
    return render(request, "contact.html")

def blog (request):
    return render(request, "blog.html")