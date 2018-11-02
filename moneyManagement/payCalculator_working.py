
'''
    Pay Calculator to determine bi-weekly gross and net income
'''

def grossPayCalculator(rateOfPay, weekOneHours, weekTwoHours):
    overtimeRate = rateOfPay * 1.5
    hours = [weekOneHours, weekTwoHours]
    grossPayWeeks = []

    for i in hours:
        if i > 40:
            overtimeHours = i - 40
            regularHours = 40

            grossPayWeeks.append((overtimeHours * overtimeRate) + (regularHours * rateOfPay))
        else:
            grossPayWeeks.append(i * rateOfPay)

    return grossPayWeeks[0] + grossPayWeeks[1]

def netIncomeCalculator(grossPay, withholdings):
    return (grossPay - (grossPay * withholdings))


'''
    Obtain the variables
'''

rateOfPay = float(input("Enter the rate of pay:\n"))
weekOneHours = int(input("Enter week 1 hours:\n"))
weekTwoHours = int(input("Enter week 2 hours:\n"))

withholdings = 0.18 # Amount withheld from gross income (net / gross)

grossIncome = grossPayCalculator(rateOfPay, weekOneHours, weekTwoHours)
netIncome = netIncomeCalculator(grossIncome, withholdings)

print("\n\n")
print("#" * 30)
print("Estimated Bi-Weekly Income\n")
print("Gross Income: " + str(round(grossIncome, 2)))
print("Net Income: " + str(round(netIncome, 2)))
print("#" * 30)
print()

'''
    Monthly Expenses
'''

rent = 700.00
rav4 = 630.00
electric_gas = 120.00
internet = 90.00
cellPhone = 50.00
water = 20.00
insurance = 120.00

expenses = [rent, rav4, electric_gas, internet, cellPhone, water, insurance]

costToLive = 0.00
for i in expenses:
    costToLive += i

print("\n\n")
print("#" * 30)
print("Total Monthly Expenses\n")
print("Monthly Expenses: " + str(round(costToLive, 2)))
print("#" * 30)
print()

'''
    Monthly Leftover Income
'''
print("\n\n")
print("#" * 30)
print("Estimated Monthly Leftover\n<Income for food, gas, credit card, etc.>\n")

montlyNetIncome = ((netIncome * 26) / 12)
leftoverIncome = (montlyNetIncome - costToLive)

print("Monthly Leftover Income: " + str(round(leftoverIncome, 2)))
print("#" * 30)
print("\n\n")
