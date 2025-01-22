from django.shortcuts import render
from CART.cart import Cart

# Create your views here.

def home (request):
    cart = Cart(request)
    return render(request, "home.html")




