from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from .keys import *

def login(request):
    username = None
    if not request.user.is_authenticated:
        return render(request, 'login.html')

    username = request.user.username
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.create_friendship(username)
    # TODO: store some info about if we already follow them or not
    return render(request, 'login.html')
