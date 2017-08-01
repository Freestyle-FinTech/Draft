### REMINDER - GIT PULL UPSTREAM MASTER > GIT REMOTE -V > GIT STATUS
### COMMIT - git add . > git commit -m "Commit Title DB" > git push origin master
#Twitter Login: Team Robo, 347-899-7331, RoboNYU1!

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
#user = api.me() # get information about the currently authenticated user


fname = "Twitter_Analysis/twit_feed.csv"
tweetxt=[]
tweets = api.home_timeline(count=1000, includerts=False)
#startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
#endDate =   datetime.datetime(2017, 8, 1, 0, 0, 0)
for tweet in tweets:
    tweetxt.append(tweet.text)

# print tweets and save to csv file
with open(fname, 'w', newline='', encoding='utf-8') as csvFile:
    Writer = csv.writer(csvFile)
    for tweet in tweetxt:
        Writer.writerow([tweet])

print("YOU HAVE PULLED",len(tweets), "TWEETS!")
#for tweet in tweets:
#    calltweets.append(tweet)
#for tweet in tweets:
#    created_on = tweet.created_at.strftime("%Y-%m-%d")
#    print(" + ", tweet.id_str, created_on, tweet.text)
