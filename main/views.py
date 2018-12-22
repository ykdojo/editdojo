from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.views import finished_signup_flow

def home(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return render(request, 'login.html')

    # TODO: Initiate the Twitter initialization in the background.
    # Maybe use this: https://django-background-tasks.readthedocs.io/en/latest/

    # Then, show them the signup flow, including language selection.
    if not finished_signup_flow(current_user):
        return HttpResponseRedirect('/signup/')

    return render(request, 'main.html')