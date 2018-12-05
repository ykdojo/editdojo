from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from .keys import * # import keys for tweepy
from allauth.socialaccount.models import SocialAccount

def login(request):
    username = None
    current_user = request.user
    if not current_user.is_authenticated:
        return render(request, 'login.html')

    twitter_account = SocialAccount.objects.filter(user = current_user)[0]
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.create_friendship(twitter_account.uid)
    # TODO: store some info about if we already follow them or not.
    return render(request, 'login.html')
