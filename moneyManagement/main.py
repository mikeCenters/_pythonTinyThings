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






income = incomeCalculator.Income()
expenses = monthlyExpenses.Expenses()


'''
    Income

    Set the value how to determine monthly income with incomeComparing
'''
prompt = "Monthly Net Income: $"

incomeComparing = income.conservativeMonthlyNetIncome
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
