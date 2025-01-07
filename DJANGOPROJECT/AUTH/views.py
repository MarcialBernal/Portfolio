from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class VRegister(View):
    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "register/register.html", {"form":form})
    
    def post(post, self):
        pass





#def auth(request):
    #return render(request, "register/register.html")

