#coding:utf-8
from django.http import HttpResponse
 
def index(request):
    return HttpResponse(u"welcome to here!")
