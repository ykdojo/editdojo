from django.shortcuts import render

def login(request):
    print('yk1')
    return render(request, 'login.html')
