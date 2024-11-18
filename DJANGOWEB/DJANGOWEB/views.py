from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

def home(request):
    
    colors = ["Blue", "Red", "Green", "Yellow"]
    
    today_date = datetime.datetime.now()
    #home_template = open("C:/Users/Marcial/Desktop/DEV/PORTFOLIO/DJANGOWEB/DJANGOWEB/templates/home.html")
    #plt = Template(home_template.read())
    #home_template.close()
    #home_template = loader.get_template("home.html")
    #ctx = Context({"today_date":today_date, "colors":colors})
    #home_render = plt.render(ctx)
    #home_render = home_template.render(ctx)
    #home_render = home_template.render({"today_date":today_date, "colors":colors})
    
    #return HttpResponse(home_render)
    return render(request, "home.html", {"today_date":today_date, "colors":colors} )

def bye(request):
    return HttpResponse("Good Bye")

def date(request):
    today_date = datetime.datetime.now()
    return HttpResponse(today_date)