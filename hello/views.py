from django.shortcuts import render
from django.http import HttpResponse

def myView(request):
    return HttpResponse('Hello, World Ahhh!')
    
def hommeView(request):
    return HttpResponse('This is home page')