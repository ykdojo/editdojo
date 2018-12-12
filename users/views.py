from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import tweepy
from .keys import * # import keys for tweepy
from allauth.socialaccount.models import SocialAccount
from .models import Language

def login(request):
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

    # Then, show them the language selection page
    # TODO: Only show this if they haven't selected languages yet.
    return render(request, 'language_selection.html')

# Handle the POST request for selecting langauges
def select_languages(request):
    # First, make sure that the user is logged in.
    current_user = request.user
    if not current_user.is_authenticated:
        return HttpResponseRedirect('/')

    learning_languages = []
    fluent_languages = []
    
    # Then, retrieve the lists of learning/fluent languages.
    i = 1; key = 'learning1'
    while key in request.POST and i < 100:
        learning_languages.append(request.POST[key])
        i += 1
        key = 'learning' + str(i)

    j = 1; key = 'fluent1'
    while key in request.POST and j < 100:
        fluent_languages.append(request.POST[key])
        j += 1
        key = 'fluent' + str(j)
    
    # Create the set of valid languages from each list.
    learning_language_set = set()
    for language in set(learning_languages):
        try:
            l = Language.objects.get(english_representation=language)
            learning_language_set.add(l)
        except Language.DoesNotExist:
            pass
    
    fluent_language_set = set()
    for language in set(fluent_languages):
        try:
            l = Language.objects.get(english_representation=language)
            fluent_language_set.add(l)
        except Language.DoesNotExist:
            pass
    
    # Make sure that there's at least one valid language in each category.
    if not fluent_language_set or not learning_language_set:
        return HttpResponseRedirect('/')
    
    # Then, finally, add selected languages to the user's info.
    for language in learning_language_set:
        if not language in current_user.learning_languages.all():
            current_user.learning_languages.add(language)
    for language in fluent_language_set:
        if not language in current_user.fluent_languages.all():
            current_user.fluent_languages.add(language)
    current_user.save()
    return HttpResponseRedirect('/languageSelected/')