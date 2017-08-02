import nltk
import csv
import numpy

tweets = [ ]

tweets_pub_path = "draft/hard_score_public.csv"

with open(tweets_pub_path, "r") as t:
    reader = csv.reader(t)
    for row in reader:
        tweets.append(str(row))

#print(tweets)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sa = SentimentIntensityAnalyzer()
scores = []
for tweet in tweets:
    score = sa.polarity_scores(tweet)
    scores.append(score)

write_to_sentiment = "draft/sentiment_score.csv"
with open(write_to_sentiment,"w") as write_sentiment:
    writer = csv.DictWriter(write_sentiment, fieldnames=["neg","neu","pos","compound"])
    writer.writeheader()
    for i in scores:
        writer.writerow(i)

diff_list = []
for row in scores:
    pos = row["pos"]
    neg = row["neg"]
    def dif(pos,neg):
        return float(pos-neg)
    diff = dif(pos,neg)
    diff_list.append(diff)
avg = numpy.mean([diff_list])
print("The avgerage sentiment score for public tweets is: " + str(round(avg,4)))
