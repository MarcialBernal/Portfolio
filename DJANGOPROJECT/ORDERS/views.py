from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CART.cart import Cart
from .models import Orders, OrdersLine
from django.contrib import messages


# Create your views here.

@login_required(login_url="/auth/login")
def process_order(request):
    order = Orders.objects.create(user=request.user)
    cart = Cart(request)
    order_lines = list()
    for key, value in cart.cart.items():
        order_lines.append(OrdersLine(
            item_id = key,
            quantity = value["quantity"],
            user = request.user,
            order = order
        ))
        
    OrdersLine.objects.bulk_create(order_lines)
    
    send_mail(order = order, 
              order_line = order_lines,
              user_name = request.username,
              email = request.useremail,)
    
    messages.success(request, "Order created succesfully")
    
    return redirect("../shop")