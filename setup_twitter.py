from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
import os

# More about the following here: https://wsvincent.com/django-allauth-tutorial/
first_site = Site.objects.get(pk=1)
first_site.name = os.environ['TWITTER_HOST']
first_site.domain = os.environ['TWITTER_HOST']
first_site.save()

# More about the following here: https://django-allauth.readthedocs.io/en/latest/providers.html
social_app = SocialApp.objects.filter(provider='twitter')
if not social_app:
    social_app = SocialApp()
else:
    social_app = social_app[0]
social_app.provider = 'twitter'
social_app.name = 'Twitter'
social_app.client_id = os.environ['TWITTER_CONSUMER_KEY']
social_app.secret = os.environ['TWITTER_CONSUMER_SECRET']
social_app.save()

social_app.sites.add(first_site)