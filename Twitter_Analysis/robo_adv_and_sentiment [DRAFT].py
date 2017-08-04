import os
import tweepy
import csv
import datetime
#Twitter Login: Team Robo, 347-899-7331, RoboNYU1!

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

startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
endDate =   datetime.datetime(2017, 7, 31, 0, 0, 0)

tweetxt=[]
client_user = input("Enter client's Twitter ID: " + '\n',)
tweets = api.user_timeline(screen_name=client_user, count=1000, includerts=False)
###once testing done use the below format:

for tweet in tweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweetxt.append(tweet.text)
###print("YOU CALLED",len(tweetxt),"Tweets")

#for tweet in tweetxt:
#    print(tweet, "\n")
print("THERE ARE IN TOTAL: ",len(tweetxt),"Tweets")
