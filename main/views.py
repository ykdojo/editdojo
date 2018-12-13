from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import tweepy
from users.keys import * # import keys for tweepy
from allauth.socialaccount.models import SocialAccount

def home(request):
    current_user = request.user
    if not current_user.is_authenticated:
        return render(request, 'login.html')

    # If the user is authenticated, first, follow them on Twitter.
    # TODO: store some info about if we already follow them or not.
    twitter_account = SocialAccount.objects.filter(user = current_user)[0]
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.create_friendship(twitter_account.uid)

    # Then, show them the signup flow, including language selection.
    # TODO: Only show this if they haven't selected languages yet.
    return HttpResponseRedirect('/signup/')