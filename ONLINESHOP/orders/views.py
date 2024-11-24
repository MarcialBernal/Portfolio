from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Items
from django.core.mail import send_mail
from django.conf import settings
from orders.forms import ContactForm

# Create your views here.

def item_search(request):
    
    return render(request, "search_item.html")

def search(request):
    
    if request.GET["item"]:
        #mesage = "Item searched: %r" %request.GET["item"]
        item = request.GET["item"]
        if len(item)>20:
            mesage = "Text too long"
            
        else:
            items = Items.objects.filter(name__icontains=item)
            return render(request, "search_results.html", {"items":items, "query":item})
        
    else:
        mesage = "No data has been provided"
    
    return HttpResponse(mesage)

def contact(request):
    
    if request.method == "POST":
        
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            info = contact_form.cleaned_data
            send_mail(info["about"], info["message"], info.get("email", ""), ["gmail.com"],)
            return render(request, "succes_contact.hmtl")  
        
        #subject = request.POST["About"]
        #message = request.POST["Message"] + " " + request.POST["Email"]
        #email_from = settings.EMAIL_HOST_USER
        #recipient_list = ["marcialb9328@gmail.com"]
        #send_mail(subject, message, email_from, recipient_list)
        
        #return render(request, "succes_contact.html")
      
    else:
        
       contact_form = ContactForm()   
       
       
    return render(request, "contact_form.html", {"form":contact_form})