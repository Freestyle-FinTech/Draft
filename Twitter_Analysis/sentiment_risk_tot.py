import nltk
import csv
import numpy as np
from hard_score_pub import *
from survey_risk_tolerance_db import*
from robo_adv_and_sentiment import*
#nltk.download()

###Split, Tokenize & Tag
#must in txt

###score
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#must be in list
#this is individual's
#tweets = [ ]
sa = SentimentIntensityAnalyzer()
scores_ind = []
for twit in tweetxt:
    score = sa.polarity_scores(twit)
#    print(score)
    scores_ind.append(score)

# score = sa.polarity_scores(tweets)
# print(tweets,str(score))

write_to_sentiment = "draft/sentiment_score.csv"
with open(write_to_sentiment,"w") as write_sentiment:
    writer = csv.DictWriter(write_sentiment, fieldnames=["neg","neu","pos","compound"])
    writer.writeheader()
    for i in scores_ind:
        writer.writerow(i)

#avg = 0.0091
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
