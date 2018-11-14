from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("helloworld")


def weather(request, year, city):
    print(year,city)

    return HttpResponse("%s,,%s"%(year,city))

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a,b,alist)
    return HttpResponse('OK')