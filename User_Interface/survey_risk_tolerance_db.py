import psycopg2
import csv
import numpy as np

Server_DB_Username = 'vnqyscaajfifeg'
Server_DB_Host = "ec2-54-163-254-143.compute-1.amazonaws.com"
Server_DB_Password = "6ee97dda964f794ee664a52ab7cd6ed367d8480ba496ebcc0647b3226c16a370"
Server_Port = "5432"
Server_DB_Name = "d7t1alfnvnuu63"

conn = psycopg2.connect(
    dbname=Server_DB_Name,
    user=Server_DB_Username,
    password=Server_DB_Password,
    host=Server_DB_Host,
    port=Server_Port
    )

#def greeting():
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

answers = [ ]
new_answer = {"username": username,"age": age,"income": income,"investment": invest,"preference": preference,"household": household,"action": action}
answers.append(new_answer)

def risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3):
     return age_adj+income_adj+invest_adj+q1+q2+q3
score = risk_tolerance(age_adj, income_adj, invest_adj, q1, q2, q3)

with conn:
    with conn.cursor() as cursor:
        sql_query = "CREATE TABLE SURVEY (username text, age integer, income integer, invest integer, preference text, household text, action text);"
        cursor.execute(sql_query)
