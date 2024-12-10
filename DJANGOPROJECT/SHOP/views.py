from django.shortcuts import render
from .models import Items

# Create your views here.

def shop (request):
    
    items = Items.objects.all()
    
    return render(request, "shop/shop.html", {"items": items})
