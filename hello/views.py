from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('Hello, World Ahhh!')

def home_view(request):
    return HttpResponse('This is home page')
