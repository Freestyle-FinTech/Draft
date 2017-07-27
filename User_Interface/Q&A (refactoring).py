import pandas as pd
test = pd.read_excel(r'~/Documents/nyu-info-2335-70-201706/exercises/pandas-practice/jeter_stats.xlsx')
print(test)

def greeting():
    print("""
    Portfolio Recommendation
    ------------------------
    """)
def interface1():
    username = input("Please enter your username: ")
    print("Welcome " + username + "!")

def try_function():
    while True:
        x = input()
        try:
            x = eval(x)
            if type(x) == int:
                break
        except:
            print("Please input a number.")

def interface2():
    print("How old are you?")
    try_function()
#
# def interface2():
#     while True:
#         age = input("How old are you: ")
#         try:
#             age = eval(age)
#             if type(age) == int:
#                 print(age)
#                 break
#         except:
#             print("Please input a number.")

def interface3():
    print("What is your annul income (berofe tax): ")
    try_function()

def interface4():
    print("How much you plan to invest: ")
    try_function()

def interface5():
    choice = ["a","b","c","d","e"]
    print("""
    a. Single income, no dependents
    b. Single income, at least one dependent
    c. Dual income, no dependents
    d. Dual income, at least one dependent
    e. Retired or financially Independent
    """)
    while True:
        household = input("Which of the above describes your household? (Enter the letter only): ")
        if household in choice:
            print(household)
            break
        else:
            print("Please enter a valid choice!")

def interface6():
    choice = ["a","b","c","d"]
    print("""
    a. Sell all of your investments
    b. Sell worst performing stocks
    c. Do nothing, keep all of your stocks
    d. Buy more at a cheaper price
    """)
    while True:
        action = input("Stock markets can be volatile. If your portfolio lost 10% in a month during a market decline, what you would do? (Enter the letter only): ")
        if action in choice:
            print(action)
            break
        else:
            print("Please enter a valid choice!")

greeting()
interface1()
interface2()
interface3()
interface4()
interface5()
interface6()

###this is test part:
# def enlarge(i):
#     return i*100
#
# def run():
#     greeting()
#     interface1()
#     interface2()
# if __name__ == "__main__":
#    run()
