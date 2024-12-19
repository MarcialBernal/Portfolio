from django.shortcuts import render, redirect
from .cart import Cart
from SHOP.models import Items


# Create your views here.

def add_item(request, item_id):
    cart = Cart(request)
    item = Items.objects.get(id=item_id)
    cart.add(item=item)
    
    return redirect("shop")
###
def delete_item(request, item_id):
    cart = Cart(request)
    item = Items.objects.get(id=item_id)
    cart.delete(item=item)
    
    return redirect("shop")
###
def substract_item(request, item_id):
    cart = Cart(request)
    item = Items.objects.get(id=item_id)
    cart.substract(item=item)
    
    return redirect("shop")
###
def clean_cart(request, item_id):
    cart = Cart(request)
    cart.clean()
    
    return redirect("shop")