from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
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
    
    sender_mail(order = order, 
              order_line = order_lines,
              user_name = request.user.username,
              user_email = request.user.email,)
    
    messages.success(request, "Order created succesfully")
    
    return redirect("../shop")

def sender_mail(**kwargs):
    about = "Thanks for your order"
    message = render_to_string("emails/order.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "user_name": kwargs.get("username")
    })
    
    message_text = strip_tags(message)
    from_email = "shopemail@shopemail.com"
    to = kwargs.get("user_email")
    
    send_mail(about, message_text, from_email, [to], html_message=message)
    