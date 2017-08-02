import os
import tweepy
import csv
import datetime

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
# AUTHENTICATE
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# INITIALIZE API CLIENT
api = tweepy.API(auth)

# ISSUE REQUESTS
#client_user = input("Enter your Twitter handle" +
#    '\n'+"(enter the handle immediately after the '@', but do not include the '@'): ",)
user = api.me() # get information about the currently authenticated user

# startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
# endDate =   datetime.datetime(2017, 7, 31, 0, 0, 0)

tweetxt=[]
tweets = api.user_timeline(screen_name="Team Robo", count=1000, includerts=False)
for tweet in tweets:
    tweetxt.append(tweet.text)
#    print(tweetxt)
