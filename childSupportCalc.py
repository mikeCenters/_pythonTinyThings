import webbrowser

def monthlyGrossIncome(rateOfPay, hours, useOT):
    '''
        Determine Monthly Gross income based upon hours and rate.
            useOT should be 0 to not use overtime
            useOT should be 1 to use full overtime
            useOT should be 2 to use maximum of 50% of overtime pay.
    '''
    payPeriodPay = 0
    overtimeRate = rateOfPay * 1.5
    overtimeHours = []
    regularHours = []

    for i in hours:
        if i > 40:
            regularHours.append(i - (i - 40))

            if useOT == 0: # No overtime used
                overtimeHours.append(0)
            elif useOT == 1 or useOT == 2: # Overtime is applied
                overtimeHours.append(i - 40)
            else:
                print("Error with overtime option")
                stop
        else:
            regularHours.append(i)
            overtimeHours.append(0)

    for i, val in enumerate(regularHours):
        regularPay = regularHours[i] * rateOfPay
        overtimePay = overtimeHours[i] * overtimeRate

        if useOT == 0 or useOT == 1:
            weeklyPay = regularPay + overtimePay
            payPeriodPay = payPeriodPay + weeklyPay

        elif useOT == 2:
            weeklyPay = regularPay + (overtimePay / 2)
            payPeriodPay = payPeriodPay + weeklyPay

            # Do not use, reference only
            # if overtimePay > (regularPay / 2):
            #     weeklyPay = regularPay + (regularPay / 2)
            #     payPeriodPay = payPeriodPay + weeklyPay
            # else:
            #     weeklyPay = regularPay + overtimePay
            #     payPeriodPay = payPeriodPay + weeklyPay



    annualPay = payPeriodPay * 26
    grossMonthlyPay = annualPay / 12

    return grossMonthlyPay

def getBasicObligation(combinedMonthlyIncome):
    '''
        Table to determine basic obligation
    '''

    webbrowser.open("http://www.wvlegislature.gov/WVCODE/Code.cfm?chap=48&art=13")

    print("Combined Monthly Income is:\n" + str(combinedMonthlyIncome))

    print("\nEnter the Basic Obligation for the Combined Monthly Income:")
    basicObligation = input()

    return basicObligation

def overtimeRule():
    otMenu = "Enter 0 for no overtime.\n" \
            "Enter 1 for full overtime.\n" \
            "Enter 2 for overtime to be a maximum of 50 percent of" \
            " overtime pay.\n"

    otRule = int(input(otMenu))
    return otRule

def payConverter(pay, rule):
    '''
        Rules:
        0 is for bi-weekly to monthly
        1 is for monthly to bi-weekly
    '''
    if rule == 0: # Takes the bi-weekly amount and converts it to monthly
        payPeriodToMonthly = (pay * 26) / 12
        return int(round(payPeriodToMonthly))
    elif rule == 1: # Takes the monthly amount and converts it to bi-weekly
        monthlyToPayPeriod = (pay * 12) / 26
        return int(round(monthlyToPayPeriod))

basicObligationTable = { # Will need to implement this dictionary to automate lookup

}

'''
    Part 1:
    Basic Obligation
'''

partyARate = 13.75
partyAHours = [48, 72]

partyBRate = 7.60
partyBHours = [40, 40]

partyAOvernights = 182.5
partyBOvernights = 182.5

overtimeRule = overtimeRule()

grossMonthlyIncomeA = monthlyGrossIncome(partyARate, partyAHours, overtimeRule)
grossMonthlyIncomeB = monthlyGrossIncome(partyBRate, partyBHours, overtimeRule)

combinedMonthlyIncome = int(round(grossMonthlyIncomeA + grossMonthlyIncomeB))

# Percentage of total income made by each party
partyAShareIncome = grossMonthlyIncomeA / combinedMonthlyIncome
partyBShareIncome = grossMonthlyIncomeB / combinedMonthlyIncome

basicObligation = getBasicObligation(combinedMonthlyIncome)

'''
    Part 2:
    Shared Parenting Adjustment
'''
sharedParentingObligation = int(round(float(basicObligation) * 1.5))

partyAShare = int(round(sharedParentingObligation * partyAShareIncome))
partyBShare = int(round(sharedParentingObligation * partyBShareIncome))

percentWithPartyA = partyAOvernights / 365
percentWithPartyB = partyBOvernights / 365

retainedMoneyPartyA = partyAShare * percentWithPartyA
retainedMoneyPartyB = partyBShare * percentWithPartyB

partyAObligation = partyAShare - retainedMoneyPartyA
partyBObligation = partyBShare - retainedMoneyPartyB

amountTransferred = partyAObligation - partyBObligation
amountTransferred = abs(amountTransferred)

if partyAObligation > partyBObligation:
    whoOwes = "Party A owes "
elif partyBObligation > partyAObligation:
    whoOwes = "Party B owes "
else:
    whoOwes = "No one owes "

print("=" * 10)
print(whoOwes + str(amountTransferred) + " in child support")
print("\nThe expected bi-weekly pay will be:")
print("{}".format(payConverter(amountTransferred, 1)))
print("=" * 10)
