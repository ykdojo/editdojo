from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
import os

# More about the following here: https://wsvincent.com/django-allauth-tutorial/
first_site = Site.objects.get(pk=1)
first_site.name = '127.0.0.1'
first_site.domain = '127.0.0.1'
first_site.save()

# More about the following here: https://django-allauth.readthedocs.io/en/latest/providers.html
social_app = SocialApp()
social_app.provider = 'twitter'
social_app.name = 'Twitter'
social_app.client_id = os.environ['TWITTER_CONSUMER_KEY']
social_app.secret = os.environ['TWITTER_CONSUMER_SECRET']
social_app.save()

social_app.sites.add(first_site)