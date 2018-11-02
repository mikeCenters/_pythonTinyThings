'''
    Gross and Net Income Calculator

    Creates an object that contains:
    regularRateOfPay
    overtimeRateOfPay
    hours # [weekOneHours, weekTwohours]

    Three forms of gross income:
        biWeekly, monthly, and annualGrossIncome

    Four forms of net income:
        biWeekly, monthly, annual and conservativeMonthlyNetIncome
            conservativeMonthlyNetIncome is a monthly income of two paychecks
            because there are 26 paychecks a year; leaving two checks as extra
            income. This helps with managing expenses and budgeting to create
            two free checks each year for debt management.
'''

class Income:

    def __init__(self):
        self.regularRateOfPay = 0.00
        self.overtimeRateOfPay = 0.00
        self.setRateOfPay()          # set regular and overtime rate of pay

        self.hours = []              # [weekOneHours, weekTwoHours]
        self.setHours()              # set the bi-weekly hours

        self.biWeeklyGrossIncome = 0.00
        self.annualGrossIncome = 0.00
        self.monthlyGrossIncome = 0.00
        self.grossIncomeCalculator()

        self.withholdingPercent = 0.00

        self.biWeeklyNetIncome = 0.00
        self.annualNetIncome = 0.00
        self.monthlyNetIncome = 0.00

        self.conservativeMonthlyNetIncome = 0.00 # Monthly income as two checks
        self.netIncomeCalculator()

    def setRateOfPay(self):
        self.regularRateOfPay = float(input("What is the hourly rate of pay?\n"))
        self.overtimeRateOfPay = (self.regularRateOfPay * 1.5)
        return


    def setHours(self):
        weekOneHours = int(input("How many hours are worked in week one?\n"))
        weekTwoHours = int(input("How many hours are worked in week two?\n"))

        self.hours = [weekOneHours, weekTwoHours]
        return

    def grossIncomeCalculator(self):
        _grossIncomeEachWeek = []       # [weekOneGross, weekTwoGross]
        for i in self.hours:
            if i > 40:
                _overtimeHours = i - 40
                _regularHours = 40

                _grossIncomeEachWeek.append(
                            (_overtimeHours * self.overtimeRateOfPay)
                            + (_regularHours * self.regularRateOfPay)
                            )
            else:
                _grossIncomeEachWeek.append(i * self.regularRateOfPay)

        self.biWeeklyGrossIncome = (_grossIncomeEachWeek[0] + _grossIncomeEachWeek[1])
        self.annualGrossIncome = self.biWeeklyGrossIncome * 26
        self.monthlyGrossIncome = self.annualGrossIncome / 12
        return

    def netIncomeCalculator(self):
        self.withholdingPercent = float(input("What percentage is withheld from the "
                                        "gross income? <0.24, 0.16>\n"))

        self.biWeeklyNetIncome = self.biWeeklyGrossIncome - (
                    self.withholdingPercent * self.biWeeklyGrossIncome
                    )
        self.annualNetIncome = self.biWeeklyNetIncome * 26
        self.monthlyNetIncome = self.annualNetIncome / 12

        self.conservativeMonthlyNetIncome = self.biWeeklyNetIncome * 2
        return
