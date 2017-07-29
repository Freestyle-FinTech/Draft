#Import the required modules
from twython import Twython
import json
import csv

#Set parameters
keyword = 'kittens'; #The desired keyword(s)
tweetsXiteration = 100; #Where 100 is the max
dateFrom = '2014-02-01'; #Inclusive (YYYY-MM-DD)
dateTo = '2014-02-02'; #Exclusive (YYYY-MM-DD)
done = False; #Must be false

#Setting the OAuth
Consumer_Key = 'XXX';
Consumer_Secret = 'XXX';
Access_Token = 'XXX';
Access_Token_Secret = 'XXX';

#Connection established with Twitter API v1.1
twitter = Twython(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret);

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
