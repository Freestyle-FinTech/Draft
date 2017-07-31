#input username/ answers and get the score for risk tolerance
# import pandas as pd
# test = pd.read_excel(r'~/Documents/nyu-info-2335-70-201706/exercises/pandas-practice/jeter_stats.xlsx')
# print(test)
import csv
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

#def interface3():
print("What is your annul income (berofe tax): ")
while True:
    income = input()
    try:
        income = eval(income)
        if type(income) == int:
#            return income
            break
    except:
        print("Please input a number.")

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
#        return preference
        break
    else:
        print("Please enter a valid choice!")


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

# greeting()
# interface1()
# interface2()
# interface3()
# interface4()
# interface5()
# interface6()
# interface7()
answers = []
answer = "draft/answers.csv"
with open(answer, "r") as a:
    reader = csv.DictReader(a)
    for row in reader:
        answers.append(row)

new_answer = {"username": username,"age": age,"income": income,"investment": invest,"preference": preference,"household": household,"action": action}
answers.append(new_answer)

answer = "draft/answers.csv"
with open(answer,"w") as a:
    writer = csv.DictWriter(a, fieldnames=["username","age","income","investment","preference","household","action"])
    writer.writeheader()
    for a in answers:
        writer.writerow(a)

###this is test part:
#
# def run():
#     greeting()
#     interface1()
#     interface2()
# if __name__ == "__main__":
#    run()
