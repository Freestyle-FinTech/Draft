#testing codes2


#Twitter Login: @TeamRobo2, 347-899-7331, RoboNYU1!

import os
import tweepy

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
client_user = input("Enter your Twitter handle here (enter the handle immediately after the '@', but do not include the '@'): " +
    '\n',)
user = api.me() # get information about the currently authenticated user
#tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user
tweets = api.user_timeline(screen_name=client_user, count=10, includerts=False)


calltweets=[]# PARSE RESPONSES
tweetxt=[]
for tweet in tweets:
    calltweets.append(tweet)
for tweet in tweets:
    tweetxt.append(tweet.text)

print (len(calltweets))
for tweet in tweetxt:
    print (tweet, "\n")
