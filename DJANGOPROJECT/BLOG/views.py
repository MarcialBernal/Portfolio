from django.shortcuts import render
from BLOG.models import Posts, Categories

# Create your views here.

def blog (request):
    
    posts = Posts.objects.all()
    return render(request, "blog.html", {"posts":posts})


def categories (request, categories_id):
    
    category = Categories.objects.get(id=categories_id)
    posts = Posts.objects.filter(categories=categories_id)
    return render(request, "categories.html", {"category":category, "posts":posts})
