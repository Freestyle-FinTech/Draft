import nltk
import csv
import numpy as np
from hard_score_pub import *
from survey_risk_tolerance_db import*

#nltk.download()

###Split, Tokenize & Tag
#must in txt

###score
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#must be in list
#this is individual's
tweets = [
    "RT @FourBlock: 94% of alumni say @FourBlock improved their transition from military to corporate life. Register today: https://t.co/zTtshYP",
    "@KirstieEnnis #VacationFromVacation.",
    "RT @MelissaEisenzim: Attn New Jersey veterans! We have an event coming your way in a few weeks with @FourBlock! @jointbasemdl @MAG49_JBMDL",
    "RT @FourBlock: 100% of surveyed employers say @FourBlock has made them more confident in hiring #veterans https://t.co/6dbnS5TJkG",
    "RT @FourBlock: Here's @tiaginc's Steve Vincent accepting the @FourBlock challenge coin for speaking to our summer cohort in Tacoma. You #in",
    "RT @FourBlock: We're thrilled to announce @FourBlock alum @MrBenjaminBoom has earned a spot on the @usahockey Nat'l Sled Team! https://t.co",
    "Article written by @JHartley2!",
    "FourBlock Veterans and transitioning Veterans at large - take a look at some great advice from one of our own cadre�https://t.co/T8UIDuR8Ul",
    "'I have KPIs!' Everyone wants a #dashboard. Found these simple questions 2 ask b4 making one. https://t.co/RrXKRfi778",
    "RT @AIGinsurance: Our new CEO Brian Duperreault shares why he believes AIG's best days are still ahead, & why he chose to come back"
    ]
sa = SentimentIntensityAnalyzer()
scores_ind = []
for tweet in tweets:
    score = sa.polarity_scores(tweet)
    print(score)
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
