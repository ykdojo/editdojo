import tweepy
import json
import sys

# Fix error: 'UCS-2' codec can't encode characters
# by converting 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

with open("config.json") as file:
    config = json.load(file)

# Account Configuration Steps
# 1. Go to apps.twitter.com
# 2. Apply for a developer account
# 3. Create New App
# 4. Get customer key from App -> Keys and Access Tokens
# 5. Generate access token
# 6. Add the keys and tokens to config.json file
consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

# account access
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# get the first 50 tweets that mention the account
for mention in api.mentions_timeline(count=50):
    # print the text from the tweet.  Replace emojis with other characters
    print(mention.text.translate(non_bmp_map))

    # send response tweet here
