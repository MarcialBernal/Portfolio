from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth import logout as user_logout
from django.contrib import messages

# Create your views here.

class VRegister(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {"form":form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, "register/register.html", {"form":form})


def logout(request):
    user_logout(request)
    return redirect("home")


def login_view(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get("username")
            user_password = form.cleaned_data.get("password")
            user = authenticate(username = user_name, password = user_password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "User its not valid")
        else:
            messages.error(request, "Data its not valid")
    else:        
        form = AuthenticationForm()
        
    return render(request, "login/login.html", {"form":form})