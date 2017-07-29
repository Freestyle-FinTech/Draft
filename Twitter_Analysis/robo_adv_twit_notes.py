### REMINDER - GIT PULL UPSTREAM MASTER > GIT REMOTE -V > GIT STATUS
### COMMIT - git add . > git commit -m "Commit Title DB" > git push origin master

#Twitter Login: Team Robo, 347-899-7331, RoboNYU1!
#Twitter Keys#


# Notes: Look at use of Classes, "class baseballTeam():"
# Professor has put a list of different APIs on Notes/Software/APIs
#beautifulsoup.md - used for scraping web pages
# Psycopg - database postgress database
# pysysql - database for mysql database
# tkinter.md - to make a graphical user interface
# review "environment variables" from github repository

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
user = api.me() # get information about the currently authenticated user
tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user
youtweet = api.user_timeline(screen_name="@Mr_DamienB", count=10, includerts=False)
calltweets=[]# PARSE RESPONSES

#print("---------------------------------------------------------------")
#print("RECENT TWEETS BY @{0} ({1} FOLLOWERS / {2} FOLLOWING):".format(user.screen_name, user.followers_count, user.friends_count))
#print("---------------------------------------------------------------")
for tweet in youtweet:
    calltweets.append(tweet)
    print (tweet.text, tweet.created_at)

#for tweet in tweets:
#    created_on = tweet.created_at.strftime("%Y-%m-%d")
#    print(" + ", tweet.id_str, created_on, tweet.text)
