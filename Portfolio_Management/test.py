import Markowitz_Frontier as mf
import csv
import numpy as np
import matplotlib.pyplot as plt
import Black_Litterman as bl
#from IPython import embed

print("""
Portfolio Recommendation
------------------------
""")
#def interface1():
username = input("Please enter your username: ")
print("Welcome " + username + "!")

#def interface2():
print("How old are you?")
while True:
    age = input()
    try:
        age = eval(age)
        if type(age) == int:
            break
    except:
        print("Please input a number.")
if age > 82 or age == 82:
    age_adj = 0
elif age < 35 or age == 35:
    age_adj = 1
else:
    age_adj = (-0.021)*(age-35+1)+1.02
#print(age_adj)

#def interface3():
print("What is your annul income (berofe tax): ")
while True:
    income = input()
    try:
        income = eval(income)
        if type(income) == int:
            break
    except:
        print("Please input a number.")
if income > 10500 or income == 10500:
    income_adj = 1
elif income < 3750 or income == 3750:
    income_adj = 0
else:
    income_adj = (-0.00015)*(10500-income)+1

#def interface4():
print("How much you plan to invest: ")
while True:
    invest = input()
    try:
        invest = eval(invest)
        if type(invest) == int:
#            return invest
            break
    except:
        print("Please input a number.")
if invest > 25000 or invest == 25000:
    invest_adj = 1
elif income < 5000 or income == 5000:
    invest_adj = 0
else:
    invest_adj = (-0.00005)*(25000-invest)+1

#def interface5():
choice1 = ["a","b","c"]
print("""
a. Maximize Return
b. Minimize Risk
c. Both Equally
""")
while True:
    preference = input("Which above best describes your preference for this investment? (Enter the letter only): ")
    if preference in choice1:
        break
    else:
        print("Please enter a valid choice!")
if preference == "b":
    q1 = 1
else:
    q1 = 2

#def interface6():
choice2 = ["a","b","c","d","e"]
print("""
a. Single income, no dependents
b. Single income, at least one dependent
c. Dual income, no dependents
d. Dual income, at least one dependent
e. Retired or financially Independent
""")
while True:
    household = input("Which of the above describes your household? (Enter the letter only): ")
    if household in choice2:
#        return household
        break
    else:
        print("Please enter a valid choice!")
if household == "b" or household == "d":
    q2 = 1.5
else:
    q2 = 2

#def interface7():
choice3 = ["a","b","c","d"]
print("""
a. Sell all of your investments
b. Sell worst performing stocks
c. Do nothing, keep all of your stocks
d. Buy more at a cheaper price
""")
while True:
    action = input("Stock markets can be volatile. If your portfolio lost 10% in a month during a market decline, what you would do? (Enter the letter only): ")
    if action in choice3:
#        return action
        break
    else:
        print("Please enter a valid choice!")
if action == "a":
    q3 = 1
elif action == "b":
    q3 = 2
elif action == "c":
    q3 = 2.5
else:
    q3 = 3

answers = []
answer = "answers.csv"
with open(answer, "r") as a:
    reader = csv.DictReader(a)
    for row in reader:
        answers.append(row)

new_answer = {"username": username,"age": age,"income": income,"investment": invest,"preference": preference,"household": household,"action": action}
answers.append(new_answer)

answer = "answers.csv"
with open(answer,"w") as a:
    writer = csv.DictWriter(a, fieldnames=["username","age","income","investment","preference","household","action"])
    writer.writeheader()
    for a in answers:
        writer.writerow(a)


def risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3):
     return age_adj+income_adj+invest_adj+q1+q2+q3


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
#daily_closing_prices = daily_closing_prices[list(daily_closing_prices.columns[:8])]
daily_closing_prices = daily_closing_prices[["MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM"]]
daily_closing_prices.to_csv("portfolio.csv", sep=',')
#print(daily_closing_prices)


# Mean_Variance Theory
## Initialize some parameters
rf = 0.02 #annualized risk-free rate
fq_adj = 52 #weekly data. for daily data, set fq_adj = 252.

score = risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3)
print("Your Risk Tolerance is: " + str(score))
risk_aversion = 0.1/score
#market_cap = [40,66,25,79,79]
market_cap = [1,2,1,4,3,2,3,1]

port_price = mf.read_prices("portfolio.csv")
#port_price = pandas.DataFrame(daily_closing_prices.values)
print(port_price)
#print(type(port_price))

returns = mf.get_return(port_price,return_type = "percentage") #or choose "log" as return_type
returns = np.asmatrix(returns)

port_risks, port_returns = mf.possible_portfolios(returns,1000,fq_adj)
ef_risks, ef_returns, ef_weights = mf.efficient_frontier(returns,risk_aversion,fq_adj)
max_sp, tangency_weight = mf.sharpe_ratio(returns,rf,fq_adj)

bl_expect_return = bl.bl_expect_return(market_cap,returns,rf,fq_adj)
print(bl_expect_return)
bl_port_risks, bl_port_returns = bl.bl_possible_portfolios(bl_expect_return,returns,1000,fq_adj)
bl_ef_risks, bl_ef_returns, bl_ef_weights = bl.bl_efficient_frontier(bl_expect_return,returns,risk_aversion,fq_adj)
bl_max_sp, bl_tangency_weight = bl.sharpe_ratio(bl_expect_return,returns,rf,fq_adj)

# Outputs

print("Recommendations\n----------------------------------\nBlack-Litterman Adjusted Portfolio (Expect from Market)\n")
print("Weights: ")
bl_ef_weights = bl_ef_weights.tolist()[0]
for i in range(len(bl_ef_weights)):
    print("  +  Asset",i+1,": {}%".format(round(bl_ef_weights[i]*100,2)))
print("Expected Return: {}%".format(round(bl_ef_returns[0]*100,2)))
print("Expected Risk: ",round(bl_ef_risks[0],2))
## Tangency Portfolio Sharpe Ratio
print("Expected Sharpe Ratio: ",round(bl_max_sp,4))

print("\n----------------------------------\nMean-Variance Portfolio (Expect from History)\n")
## Tangency Portfolio Weights
print("Weights: ")
ef_weights = ef_weights.tolist()[0]
for i in range(len(ef_weights)):
    print("  +  Asset",i+1,": {}%".format(round(ef_weights[i]*100,2)))
##print(ef_weights)
print("Expected Return: {}%".format(round(ef_returns[0]*100,2)))
print("Expected Risk: ",round(ef_risks[0],2))
## Tangency Portfolio Sharpe Ratio
print("Mean-Variance Portfolio Expected Sharpe Ratio: ",round(max_sp,4))
## possible portfolios: risks and returns
plt.plot(bl_port_risks, bl_port_returns, 'ro')
## efficient frontier: risks and returns
plt.plot(bl_ef_risks,bl_ef_returns,'bo')
##plt.plot([0,ef_risks[tangency_index]],[rf,ef_returns[tangency_index]],'y--o')
plt.title('Black Litterman Adjusted Portfolio')
plt.ylabel('Annualized Expected Return')
plt.xlabel('Standard Deviation as Risk')
plt.show()
plt.close()
