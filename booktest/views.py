from django.shortcuts import render
from django.http import HttpResponse
# from rest_framewor
import rest_framework


# Create your views here.
from django.template import loader


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

    d = request.POST.get('d')
    e = request.POST.get('e')
    print(d, e)

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
    print(a, b, alist)
    return HttpResponse('OK')


import json


def get_body_json(request):
    json_str = request.body
    json_str = json_str.decode()
    req_data = json.loads(json_str)
    # print(req_data['a'])
    # print(req_data['b'])
    # print(req_data['a'],req_data['b'])
    a = req_data.get("a")
    b = req_data.get("b")
    print(a, b)
    return HttpResponse('OK')

    # json_str = request.body
    # json_str = json_str.decode()  # python3.6 无需执行此步
    # req_data = json.loads(json_str)
    # print(req_data['a'])
    # print(req_data['b'])
    # return HttpResponse('OK')


def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')



from django.http import HttpResponse

def demo_view(request):
    return HttpResponse('itcast python', status=400)
    # 或者
    response = HttpResponse('itcast python')
    response.status_code = 400
    response['Itcast'] = 'Python'
    return response

from django.http import JsonResponse

def demo_view2(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'})


from django.shortcuts import redirect

def demo_view3(request):
    # return redirect('/booktest/index')
    # return redirect('/index.html')

    template = loader.get_template('index.html')
    return HttpResponse(template)


def demo_view4(request):
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')
    response.set_cookie('itcast2', 'python2', max_age=3600)
    return response

def demo_view5(request):
    cookie1 = request.COOKIES.get('itcast1')
    print(cookie1)
    return HttpResponse('OK')