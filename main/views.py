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

import json

from allauth.socialaccount.app_settings import QUERY_EMAIL
from allauth.socialaccount.providers.oauth.client import OAuth
from allauth.socialaccount.providers.oauth.views import (
    OAuthAdapter,
    OAuthCallbackView,
    OAuthLoginView,
)

from allauth.socialaccount.providers.twitter.provider import TwitterProvider

class TwitterAPI(OAuth):
    """
    Verifying twitter credentials
    """
    _base_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    url = _base_url + '?include_email=true' if QUERY_EMAIL else _base_url

    def get_user_info(self):
        user = json.loads(self.query(self.url))
        return user


class TwitterOAuthAdapter(OAuthAdapter):
    provider_id = TwitterProvider.id
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    # Issue #42 -- this one authenticates over and over again...
    # authorize_url = 'https://api.twitter.com/oauth/authorize'
    authorize_url = 'https://api.twitter.com/oauth/authenticate'

    def complete_login(self, request, app, token, response):
        client = TwitterAPI(request, app.client_id, app.secret,
                            self.request_token_url)
        extra_data = client.get_user_info()
        return self.get_provider().sociallogin_from_response(request,
                                                             extra_data)


oauth_login = OAuthLoginView.adapter_view(TwitterOAuthAdapter)
oauth_callback = OAuthCallbackView.adapter_view(TwitterOAuthAdapter)