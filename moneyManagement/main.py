'''
    Controller For Income Management and Estimations
'''

import incomeCalculator
import monthlyExpenses


def monthlyPrintOut(prompt, value):
    print()
    print("#" * 30)
    print(prompt + str(round(value, 2)))
    print("\n")


def incomeMenuPrompt():
    menu = "\nPlease choose an option for calculating net income or to quit: \n" \
            "1: Conservative Monthly Income (Two Paycheck a month)\n" \
            "2: Monthly Net Income ( Annual Net Income / 12 months )\n" \
            "0: Quit the program\n"

    listOfOptions = list(range(0, 3))

    userInput = -1
    while userInput not in listOfOptions:
        while True:
          try:
             userInput = int(input(menu))
          except ValueError:
             print("\n", "#" * 25)
             print("Input must be an integer: [0 - {}]\n".format(listOfOptions[-1]))
             continue
          else:
             break

        if userInput not in listOfOptions:
            print("\n", "#" * 25)
            print("Please choose an option: [0 - {}]\n".format(listOfOptions[-1]))

    return userInput

def setIncomeComparing(userOption):
    if userOption == 1:
        return income.conservativeMonthlyNetIncome
    elif userOption == 2:
        return income.monthlyNetIncome


income = incomeCalculator.Income()     # Generate the user income
expenses = monthlyExpenses.Expenses()  # Generate the user expenses


'''
    Income

    Set the value how to determine monthly income with incomeComparing
'''
prompt = "Monthly Net Income: $"

userInput = incomeMenuPrompt()         # Determine how the program uses income

incomeComparing = setIncomeComparing(userInput)
monthlyIncome = str(round(incomeComparing))

monthlyPrintOut(prompt, incomeComparing)


'''
    Expenses
'''
prompt = "Monthly Expenses On Bills: $"

monthlyPrintOut(prompt, expenses.costToLive)



'''
    Leftover Income
'''
prompt = "Estimated Monthly Leftover\n<Income for food, gas, credit card, etc.>\n$"

leftoverIncome = (incomeComparing - expenses.costToLive)
monthlyPrintOut(prompt, leftoverIncome)
