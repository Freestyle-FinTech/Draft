#Final Version Test


#Windows Set environment variable (globally)
#  setx TWITTER_API_KEY "F29b8D6lDVJ1T6BNzXN5a9xcX"

#Twitter Login: @TeamRobo2, 347-899-7331, RoboNYU1!
#Twitter Keys#


import os
import tweepy
import datetime
import time
import csv


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
startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
endDate = datetime.datetime(2017, 7, 31, 0, 0, 0)
#endDate = datetime.date.today()


client_user = input("Enter your Twitter ID: " + '\n',)
user = api.me() # get information about the currently authenticated user
tweets = api.user_timeline(screen_name=client_user, includerts=False)


tweets = []
for tweet in tweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweets.append(tweet.text)
for tweet in tweets:
    print (tweet, "\n")

#calltweets=[]
#tweetxt=[]
#for tweet in tweets:
#    calltweets.append(tweet)
#for tweet in tweets:
#    tweetxt.append(tweet.text)
#print (len(calltweets))
#for tweet in tweetxt:
#    print (tweet, "\n")

#tweets = []
#for tweet in tweets:
#    if tweet.created_at < endDate and tweet.created_at > startDate:
#        tweets.append(tweet.text)
#print (len(tweets))

#Set parameters
##keyword = "speaking", "@AIG", "@FourBlock", "RT"; #The desired keyword(s)
#tweetsXiteration = 100; #Where 100 is the max
#dateFrom = '2017-07-29'; ##Inclusive (YYYY-MM-DD)
#dateTo = '2017-07-31'; #Exclusive (YYYY-MM-DD)
#done = False; #Must be false







# ISSUE REQUESTS
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
