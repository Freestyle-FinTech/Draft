#Import the required modules

from twython import Twython
import json
import csv

import os
import tweepy

#Set parameters
keyword = "speaking", "@AIG", "@FourBlock", "RT"; #The desired keyword(s)
tweetsXiteration = 100; #Where 100 is the max
dateFrom = '2016-01-01'; ##Inclusive (YYYY-MM-DD)
dateTo = '2017-07-31'; #Exclusive (YYYY-MM-DD)
done = False; #Must be false

#Setting the OAuth
##Consumer_Key = '...';
##Consumer_Secret = '...';
##Access_Token = '...';
##Access_Token_Secret = '...';

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
# AUTHENTICATE
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# INITIALIZE API CLIENT
api = tweepy.API(auth)
#api = Twython.API(auth)
twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret);

#Twitter is queried
response = twitter.search(q = keyword, count = tweetsXiteration, since = dateFrom, until = dateTo, result_type = 'mixed');

#Results (partial)
countTweets = len(response['statuses']);

#If all the tweets have been fetched, then we are done
if not ('next_results' in response['search_metadata']):
    done = True;

#If not all the tweets have been fetched, then...
while (done == False):

    #Parsing information for maxID
    parse1 = response['search_metadata']['next_results'].split("&");
    parse2 = parse1[0].split("?max_id=");
    parse3 = parse2[1];
    maxID = parse3;

    #Twitter is queried (again, this time with the addition of 'max_id')
    response = twitter.search(q = keyword, count = tweetsXiteration, since = dateFrom, until = dateTo, max_id = maxID, include_entities = 1, result_type = 'mixed');

    #Updating the total amount of tweets fetched
    countTweets = countTweets + len(response['statuses']);

    #If all the tweets have been fetched, then we are done
    if not ('next_results' in response['search_metadata']):
        done = True;

print(countTweets);
