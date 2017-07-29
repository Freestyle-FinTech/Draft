when running code of counting tweets:
You need to authenticate trough OAuth;
You can only fetch results no older than a week;
If you want to search for more than one word, you need to use "" if you are only interested in the results containing the two words in that particular order (e.g., '"Stack Overflow"').


more data on counting tweets, i found panda:
check: https://stackoverflow.com/questions/33466486/how-to-count-daily-word-frequency-from-twitter

>>>twitdata=pd.read_csv('D:\\twit-data.csv')
>>>twitdata

    tweet_id    user_id     user_name   t_date      t_time      tweets
    4.05323E+17 82142636    1nvestor    11/26/2013  8:12:00     Fidelity reports that $TSN stock gets called away. Position now closed.
    2.53585E+17 22042454    Kiplinger   10/3/2012   15:57:00    Did you know that every $100 bump in avg. home prices lifts consumer spending by $5? http://t.co/zXRbWJzR


##OR

import pandas as pd
import io # only needed to import sample data

data = """
    date          tweet_id    tweet
    2015-10-31    50230       tweet_1
    2015-10-31    48646       tweet_2
    2015-10-31    48748       tweet_3
    2015-10-31    46992       tweet_4
    2015-11-01    46491       tweet_5
    2015-11-01    45347       tweet_6
    2015-11-01    45681       tweet_7
    2015-11-01    46430       tweet_8
    """

df = pd.read_csv(io.StringIO(data), delimiter='\s+', \
                 index_col=False, parse_dates = ['date'])

# Tweet count starts here
df_count = df.set_index('date').resample('D', how='count') # 'D' for offset calendar day
df_count = df_count.drop(df_count.columns[1:], axis=1)
df_count.columns = ['count']

print(df)


###original df looks like

        date  tweet_id    tweet
0 2015-10-31     50230  tweet_1
1 2015-10-31     48646  tweet_2
2 2015-10-31     48748  tweet_3
3 2015-10-31     46992  tweet_4
4 2015-11-01     46491  tweet_5
5 2015-11-01     45347  tweet_6
6 2015-11-01     45681  tweet_7
7 2015-11-01     46430  tweet_8



##After we used resample

print(df_count)

                count
date                 
2015-10-31          4
2015-11-01          4
