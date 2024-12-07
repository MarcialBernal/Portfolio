from django.shortcuts import render
from .models import ShopCategories

# Create your views here.

def shop (request):
    
    return render(request, "shop/shop.html")
