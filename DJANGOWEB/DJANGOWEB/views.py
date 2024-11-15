from django.http import HttpResponse
import datetime

def greeting(request):
    return HttpResponse("HI")

def bye(request):
    return HttpResponse("Good Bye")

def date(request):
    today_date = datetime.datetime.now()
    return HttpResponse(today_date)