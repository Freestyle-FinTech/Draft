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
client_user = input("Enter your Twitter handle here (enter the handle immediately after the '@', but do not include the '@'): " +
    '\n',)
user = api.me() # get information about the currently authenticated user
tweets = api.user_timeline(screen_name=client_user, count=10, includerts=False)


#Set parameters
##keyword = "speaking", "@AIG", "@FourBlock", "RT"; #The desired keyword(s)
#tweetsXiteration = 100; #Where 100 is the max
#dateFrom = '2017-07-29'; ##Inclusive (YYYY-MM-DD)
#dateTo = '2017-07-31'; #Exclusive (YYYY-MM-DD)
#done = False; #Must be false

##add timeline and not all
calltweets=[]
tweetxt=[]
for tweet in tweets:
    if (datetime.datetime.now() - tweet.created_at).days < 1:
        print (len(calltweets))


for tweet in tweets:
    calltweets.append(tweet)
for tweet in tweets:
    tweetxt.append(tweet.text)

print (len(calltweets))
for tweet in tweetxt:
    print (tweet, "\n")


# Open/Create a file to append data

csv_file_path = "tweets.csv"

with open(csv_file_path, "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        #print(row["id"], row["name"])
        tweetxt.append(row)

print(len(calltweets))

#csvFile = open('tweets.csv', 'a')
#Use csv Writer

other_path = "tweets.csv"
with open(other_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["id","name","tweets"])
    writer.writeheader()
    for tweet in tweets:
        writer.writerow(tweets)
#csvWriter = csv.writer(csvFile)


#with open('%s_tweets.csv' % screen_name, 'wb') as f:
	#writer = csv.writer(f)
	#writer.writerow(["id","created_at","text"])
	#writer.writerows(outtweets)
#pass
#if __name__ == '__main__':
	#pass in the username of the account you want to download
	#get_all_tweets("J_tsar")


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
