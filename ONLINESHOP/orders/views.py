from django.shortcuts import render
from django.http import HttpResponse
from orders.models import Items

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
        
        return render(request, "succes_contact.html")
        
    return render(request, "contact.html")