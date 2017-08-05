import os
import tweepy
import datetime
import nltk
import csv
import numpy as np
#from hard_score_pub import *
from survey_risk_tolerance_db import*

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
#user = api.me() # get information about the currently authenticated user

startDate = datetime.datetime(2017, 7, 1, 0, 0, 0)
endDate =   datetime.datetime(2017, 7, 31, 0, 0, 0)

tweetxt=[]
client_user = input("Enter client's Twitter ID: " + '\n',)
tweets = api.user_timeline(screen_name=client_user, count=1000, includerts=False)
###once testing done use the below format:

for tweet in tweets:
    if tweet.created_at < endDate and tweet.created_at > startDate:
        tweetxt.append(tweet.text)

print("THERE ARE IN TOTAL: ",len(tweetxt),"Tweets")

#nltk.download()

###score
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()
scores_ind = []
for twit in tweetxt:
    score = sa.polarity_scores(twit)
#    print(score)
    scores_ind.append(score)

# score = sa.polarity_scores(tweets)
# print(tweets,str(score))

write_to_sentiment = "Twitter_Analysis/sentiment_score.csv"
with open(write_to_sentiment,"w") as write_sentiment:
    writer = csv.DictWriter(write_sentiment, fieldnames=["neg","neu","pos","compound"])
    writer.writeheader()
    for i in scores_ind:
        writer.writerow(i)

avg = 0.0091
diff_ind_list = [ ]
for row in scores_ind:
    pos = row["pos"]
    neg = row["neg"]
    def dif(pos,neg):
        return float(pos-neg)
    diff_ind = dif(pos,neg)
    diff_ind_list.append(diff_ind)

avg_ind = np.mean([diff_ind_list])
def adj_sentiment(avg,avg_ind,std):
    return (avg_ind-avg)/(1.96*std)
adj_sentiment = adj_sentiment(avg,avg_ind,std)

def tot_risk_tolerance(score,adj_sentiment):
    return risk_score+adj_sentiment
tot_risk_tolerance = tot_risk_tolerance(score,adj_sentiment)
#print("The avgerage sentiment score for your tweets is: " + str(round(avg_ind,4)))
print("Your sentiment adjustment to risk tolerance is: " + str(round(adj_sentiment,4)))
print("Your Total Risk Tolerance is: " + str(round(tot_risk_tolerance,4)))
