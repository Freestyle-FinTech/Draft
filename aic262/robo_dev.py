#testing codes2


#Windows Set environment variable (globally)
#  setx TWITTER_API_KEY "F29b8D6lDVJ1T6BNzXN5a9xcX"

#Twitter Login: @TeamRobo2, 347-899-7331, RoboNYU1!
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

# ISSUE REQUESTS
##user = api.me() # get information about the currently authenticated user
##tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user
##youtweet = api.user_timeline(user_id="@TeamRobo2", count=10, includerts=False)
##costweets=[]# PARSE RESPONSES
#filepath = "Twitter_Analysis/tweet_attr.txt"
#print("---------------------------------------------------------------")
#print("RECENT TWEETS BY @{0} ({1} FOLLOWERS / {2} FOLLOWING):".format(user.screen_name, user.followers_count, user.friends_count))
#print("---------------------------------------------------------------")
#for tweet in youtweet:
    #costweets.append(tweet)
    #print (tweet.text, tweet.created_at)

#for tweet in tweets:
#    created_on = tweet.created_at.strftime("%Y-%m-%d")
#    print(" + ", tweet.id_str, created_on, tweet.text)
