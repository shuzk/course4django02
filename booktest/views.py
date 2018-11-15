from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("helloworld")


def weather(request, year, city):
    print(year, city)
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a, b, alist)
    c = HttpResponse()
    c.get('a')
    print(c)
    return HttpResponse("%s,,%s" % (year, city))


def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a, b, alist)
    c = HttpResponse()
    c.get('a')
    print(c)
    return HttpResponse('OK')


def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a,b,alist)
    return HttpResponse('OK')