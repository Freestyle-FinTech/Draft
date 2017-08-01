#import os
import psycopg2
import pandas
from pandas_datareader import data
from datetime import date, timedelta


PSQL_USERNAME = "postgres"
PSQL_DATABASE = "RoboVest"
PSQL_PASSWORD = "Getmoney88"

# OPEN DATABASE CONNECTION
conn = psycopg2.connect(
    dbname=PSQL_DATABASE,
    user=PSQL_USERNAME,password=PSQL_PASSWORD
    )

years = 15
week = 52
Horizon =years*week

# PERFORM A DATABASE OPERATION
ETF_Tickers=[]
#ETFs=["id","Date","MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM","SCHH","SCHM","SCHX","VWO","VWO","FENY","VNQI","VTIP","VGLT","ITE"]
with conn:
    with conn.cursor() as cursor:
        sql_query ="SELECT * From etf;"
        cursor.execute(sql_query)

        #print("ticker")

        for row in cursor.fetchall():
            print(row[0])
            ETF_Tickers.append(row[0])
            print(ETF_Tickers)
# # CLOSE DATABASE CONNECTION
# #conn.close()
#
##Import Prices
symbols=ETF_Tickers
data_source = 'google'
start = str(date.today() - timedelta(days=Horizon)) #> '2017-07-09'
end = str(date.today())
response = data.DataReader(symbols, data_source, start, end)
daily_closing_prices = response.ix["Close"] # ix() is a pandas DataFrame function
print(daily_closing_prices)
# print(daily_closing_prices.ix[0:5,0:5])
# test=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# Header=list(daily_closing_prices.columns.values)
# print(list(daily_closing_prices[1:100]))

# with conn:
#     with conn.cursor() as cursor:
#         cursor.execute("INSERT INTO test (mint) VALUES (%i)", (100))
#
#


# with conn:
#     with conn.cursor() as cursor:
#         for i in Header:
#             for j in (17):
#                 cursor.execute("INSERT INTO etf_prices (i) VALUES (%s)", (test[j]))


# sql_insert = "INSERT INTO etf_prices (i) VALUES (%s)", list(daily_closing_prices[i])
# cursor.execute(sql_insert,(int(daily_closing_prices.ix[0:5,0]),int(daily_closing_prices.ix[0:5,1])))
# # #
# #
#
# cur.execute('INSERT INTO %s (day, elapsed_time, net_time, length, average_speed, geometry) VALUES (%s, %s, %s, %s, %s, %s)', (escaped_name, day, time_length, time_length_net, length_km, avg_speed, myLine_ppy))
#

# with conn:
#     with conn.cursor() as cursor:
#         columns = ', '.join(Header)    # Where column names is a tuple or list of all the column headings you want in your query.
#         query = """ INSERT INTO %s("%s") VALUES(%%s); """ % (prices, columns)
#         params = [value]
#         cursor.execute(query, params)

# INSERT INTO "public"."prices"("id") VALUES('2017-07-25  59.08  87.76  42.27  76.29  57.79  49.26  42.69  79.19  ') RETURNING "id";
