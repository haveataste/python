from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home.html')

def add(request):
    '''
    a = request.GET['a']
    b = request.GET['b']
    '''
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    return HttpResponse(str(int(a)+int(b)))
