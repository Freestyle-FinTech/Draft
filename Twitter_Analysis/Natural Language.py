import nltk
import csv
#nltk.download()

###Split, Tokenize & Tag
#must in txt
tweets_text = """
    "RT @FourBlock: 94% of alumni say @FourBlock improved their transition from military to corporate life. Register today: https://t.co/zTtshYP",
    "@KirstieEnnis #VacationFromVacation.",
    "RT @MelissaEisenzim: Attn New Jersey veterans! We have an event coming your way in a few weeks with @FourBlock! @jointbasemdl @MAG49_JBMDL",
    "RT @FourBlock: 100% of surveyed employers say @FourBlock has made them more confident in hiring #veterans https://t.co/6dbnS5TJkG",
    "RT @FourBlock: Here's @tiaginc's Steve Vincent accepting the @FourBlock challenge coin for speaking to our summer cohort in Tacoma. You #in",
    "RT @FourBlock: We're thrilled to announce @FourBlock alum @MrBenjaminBoom has earned a spot on the @usahockey Nat'l Sled Team! https://t.co",
    "Article written by @JHartley2!",
    "FourBlock Veterans and transitioning Veterans at large - take a look at some great advice from one of our own cadre�https://t.co/T8UIDuR8Ul",
    "'I have KPIs!' Everyone wants a #dashboard.    Found these simple questions 2 ask b4 making one. https://t.co/RrXKRfi778",
    "RT @AIGinsurance: Our new CEO Brian Duperreault shares why he believes AIG's best days are still ahead, & why he chose to come back",
    """
token = nltk.word_tokenize(tweets_text)
#print(token)
tag = nltk.pos_tag(token)
chunk = nltk.ne_chunk(tag)
#print(tag)
print(chunk)

###score
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#must be in list
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
scores = []
for tweet in tweets:
    score = sa.polarity_scores(tweet)
    print(score)
    scores.append(score)


# score = sa.polarity_scores(tweets)
# print(tweets,str(score))

write_to_sentiment = "draft/sentiment_score.csv"
with open(write_to_senntiment,"w") as write_sentiment:
    writer = csv.DictWriter(write_sentiment, fieldnames=["neg","neu","pos","compound"])
    writer.writeheader()
    for i in scores:
        writer.writerow(i)
