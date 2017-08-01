#import os
import psycopg2
import pandas
from pandas_datareader import data
from datetime import date, timedelta

#This is for my local databse
# PSQL_USERNAME = "postgres"
# PSQL_DATABASE = "RoboVest"
#PSQL_PASSWORD = "Getmoney88"

#This is for server DATABASE
Server_DB_Username = 'vnqyscaajfifeg'
Server_DB_Host = "ec2-54-163-254-143.compute-1.amazonaws.com"
Server_DB_Password = "6ee97dda964f794ee664a52ab7cd6ed367d8480ba496ebcc0647b3226c16a370"
Server_Port = "5432"
Server_DB_Name = "d7t1alfnvnuu63"


# OPEN DATABASE CONNECTION
conn = psycopg2.connect(
    dbname=Server_DB_Name,
    user=Server_DB_Username,
    password=Server_DB_Password,
    host=Server_DB_Host,
    port=Server_Port
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
