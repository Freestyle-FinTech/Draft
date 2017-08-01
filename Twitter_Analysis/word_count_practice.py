###WORD COUNT PRACTICE###
#from collections import Counter
#import re

keywords=["speaking", "@AIG", "@FourBlock", "RT"]
keywords=sorted(keywords)
tweets = [
    "RT @FourBlock: 94% of alumni say @FourBlock improved their transition from military to corporate life. Register today: https://t.co/zTtshYP",
    "@KirstieEnnis #VacationFromVacation.",
    "RT @MelissaEisenzim: Attn New Jersey veterans! We have an event coming your way in a few weeks with @FourBlock! @jointbasemdl @MAG49_JBMDL",
    "RT @FourBlock: 100% of surveyed employers say @FourBlock has made them more confident in hiring #veterans https://t.co/6dbnS5TJkG",
    "RT @FourBlock: Here's @tiaginc's Steve Vincent accepting the @FourBlock challenge coin for speaking to our summer cohort in Tacoma. You #in",
    "RT @FourBlock: We're thrilled to announce @FourBlock alum @MrBenjaminBoom has earned a spot on the @usahockey Nat'l Sled Team! https://t.co",
    "Article written by @JHartley2!",
    "FourBlock Veterans and transitioning Veterans at large - take a look at some great advice from one of our own cadre�https://t.co/T8UIDuR8Ul",
    "'I have KPIs!' Everyone wants a #dashboard.    Found these simple questions 2 ask b4 making one. https://t.co/RrXKRfi778",
    "RT @AIGinsurance: Our new CEO Brian Duperreault shares why he believes AIG's best days are still ahead, & why he chose to come back"
    ]
all_tweet_text = " ".join(tweets)

for word in keywords:
    wordcount = all_tweet_text.count(word)
    print(word,wordcount)
