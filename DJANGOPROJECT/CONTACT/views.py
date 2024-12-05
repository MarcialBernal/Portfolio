from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact (request):
    contact_form = ContactForm()
    
    if request.method=="POST":
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            subject = request.POST.get("subject")
            email = request.POST.get("email")
            message = request.POST.get("message")
            
            email=EmailMessage(subject=subject, body= "{} \n {}".format(email, message), from_email= email, to= ["marcial9328@gmail.com"] )
            
            try:
                email.send()
                return redirect("/contact/?valid")
                
            except:
                return redirect("/contact/?novalid")
                
            
        
        
            
    return render(request, "contact.html", {"contact_form": contact_form})