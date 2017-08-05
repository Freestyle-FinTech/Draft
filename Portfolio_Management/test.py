import Markowitz_Frontier as mf
import csv
import numpy as np
import matplotlib.pyplot as plt
import Black_Litterman as bl
from IPython import embed

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
ETF_MktCap=[]
ETF = []
#ETFs=["id","Date","MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM","SCHH","SCHM","SCHX","VWO","VWO","FENY","VNQI","VTIP","VGLT","ITE"]
with conn:
    with conn.cursor() as cursor:
        sql_query ="SELECT * From etf;"
        cursor.execute(sql_query)

        #print("ticker")

        for row in cursor.fetchall():
#            print(row[0],row[8])
            ETF_Tickers.append(row[0])
#            print(ETF_Tickers)
            ETF_MktCap.append(row[8])
#            print(ETF_MktCap)

for id, txt in enumerate(ETF_Tickers):
    ETF.append({"name": txt, "mkt_cap":ETF_MktCap[id]})
#print(ETF)

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
tickers = ["MINT","EMB","IAU","VCIT","MUB","SCHA","VEA","VYM","SCHH","VWO","FENY","VTIP","VGLT","ITE"]
daily_closing_prices = daily_closing_prices[tickers]
daily_closing_prices.to_csv("portfolio.csv", sep=',')
#print(daily_closing_prices)


# Mean_Variance Theory
## Initialize some parameters
def find_mkt(etf_nm,ETF):
    for etf in ETF:
        if etf["name"] == etf_nm: mkt = etf["mkt_cap"]
    return mkt

def del_nan(port_price):
    port_price = np.asarray(port_price.T)
    for row in port_price:
        for id, value in enumerate(row):
            if np.isnan(value)==True: row[id] = (row[id-1]+row[id+1])/2
    return np.asmatrix(port_price).T

def filter_ef(ef_risks,ef_returns,ef_weights):
    r = []
    s = []
    w = []
    for id,value in enumerate(ef_returns):
        if value > 0:
            r.append(ef_returns[id])
            s.append(ef_risks[id])
            if len(ef_weights) > 0: w.append(ef_weights[id])

    ef_risks = s
    ef_returns = r
    ef_weights = w

    return ef_risks, ef_returns, ef_weights

rf = 0.02 #annualized risk-free rate
fq_adj = 252 #weekly data. for daily data, set fq_adj = 252.

score = risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3)
print("Your Risk Tolerance is: " + str(score))

market_cap = []
for i in tickers: market_cap.append(find_mkt(i,ETF))

port_price = mf.read_prices("portfolio.csv")
port_price = del_nan(port_price)
#port_price = pandas.DataFrame(daily_closing_prices.values)
#print(port_price)
#print(type(port_price))

returns = mf.get_return(port_price,return_type = "percentage") #or choose "log" as return_type
returns = np.asmatrix(returns)

port_risks, port_returns = mf.possible_portfolios(returns,1000,fq_adj)

ef_risks, ef_returns, ef_weights = mf.efficient_frontier(returns,fq_adj)

ef_risks, ef_returns, ef_weights = filter_ef(ef_risks,ef_returns,ef_weights)
port_risks, port_returns, []= filter_ef(port_risks, port_returns, [])


bl_expect_return = bl.bl_expect_return(market_cap,returns,rf,fq_adj)
bl_port_risks, bl_port_returns = bl.bl_possible_portfolios(bl_expect_return,returns,1000,fq_adj)
bl_ef_risks, bl_ef_returns, bl_ef_weights = bl.bl_efficient_frontier(bl_expect_return,returns,fq_adj)

bl_ef_risks, bl_ef_returns, bl_ef_weights = filter_ef(bl_ef_risks,bl_ef_returns,bl_ef_weights)
bl_port_risks, bl_port_returns, []= filter_ef(bl_port_risks, bl_port_returns, [])


# Outputs

position1 = int((score-2.5)/(11-2.5)*len(bl_ef_weights))
position2 = int((score-2.5)/(11-2.5)*len(ef_weights))

print("Recommendations\n----------------------------------\nMarket Implied Portfolio\n")
print("Weights: ")
for i in range(len(bl_ef_weights[position1])):
    print("  +  ",tickers[i],": {}%".format(round(bl_ef_weights[position1][i]*100,2)))
print("Expected Return: {}%".format(round(bl_ef_returns[position1]*100,2)))
print("Expected Risk: ",round(bl_ef_risks[position1],2))

print("\n----------------------------------\nHistory Based Portfolio\n")
## Tangency Portfolio Weights
print("Weights: ")
#ef_weights = ef_weights.tolist()[0]
for i in range(len(ef_weights[position2])):
    print("  +  ",tickers[i],": {}%".format(round(ef_weights[position2][i]*100,2)))
##print(ef_weights)
print("Expected Return: {}%".format(round(ef_returns[position2]*100,2)))
print("Expected Risk: ",round(ef_risks[position2],2))
## possible portfolios: risks and returns

plt.plot(bl_port_risks,bl_port_returns, 'ro')
## efficient frontier: risks and returns
line1, = plt.plot(bl_ef_risks,bl_ef_returns,'b-',label='Market Implied Assumption')
plt.plot(bl_ef_risks[position1],bl_ef_returns[position1],'bo')
line2, = plt.plot(ef_risks,ef_returns,'y-',label='History Based Assumption')
plt.plot(ef_risks[position2],ef_returns[position2],'yo')
first_legend = plt.legend(handles=[line1], loc=1)
ax = plt.gca().add_artist(first_legend)
plt.legend(handles=[line2], loc=4)
plt.title('Efficient Frontiers')
plt.ylabel('Annualized Expected Return')
plt.xlabel('Standard Deviation as Risk')
plt.show()
