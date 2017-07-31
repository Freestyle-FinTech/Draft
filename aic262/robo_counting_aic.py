##testing initial code

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
###user = api.me() # get information about the currently authenticated user
###tweets = api.user_timeline(screen_name="Mr_DamienB", count=10, includerts=False)

client_user = input("Enter your Twitter handle here (enter the handle immediately after the '@', but do not include the '@'): " +
    '\n',)
user = api.me() # get information about the currently authenticated user
#tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user
tweets = api.user_timeline(screen_name=client_user, count=10, includerts=False)



#input("What word are you counting: ",)

count_words=("speaking", "@AIG", "@FourBlock", "RT")
calltweets=[]# PARSE RESPONSES
tweetxt=[]
counted_words=[]

for tweet in tweets:
    calltweets.append(tweet)
    tweetxt.append(tweet.text)

all_tweet_text = " ".join(tweetxt)
tweet_words = all_tweet_text.split()

for w in tweet_words:
    for word in count_words:
        if w == word:
            counted_words.append(w)

cw_text = " ".join(counted_words)
cw_words = cw_text.split()
keywordfreq = [cw_words.count(w) for w in cw_words]

print(cw_words, "\n", keywordfreq)
#print ("\n","TWEET LOG FOR",len(tweets),"TWEETS:","\n")

#for tweet in tweetxt:
#    print (tweet, "\n")

#for tweet in tweets:
#    created_on = tweet.created_at.strftime("%Y-%m-%d")
#    print(" + ", tweet.id_str, created_on, tweet.text)
