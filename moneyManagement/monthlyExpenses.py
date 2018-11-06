'''
    Generate The Monthly Expenses
'''

class Expenses:

    def __init__(self):
        self.rent = 700.00
        self.vehiclePayment = 630.00
        self.electric_gas = 130.00
        self.internet = 90.00
        self.cellPhone = 60.00
        self.water = 25.00
        self.carInsurance = 120.00

        self.expenses = [self.rent,
                        self.vehiclePayment,
                        self.electric_gas,
                        self.internet,
                        self.cellPhone,
                        self.water,
                        self.carInsurance]

        self.costToLive = 0.00
        self.calculateCostToLive()

    def calculateCostToLive(self):
        for i in self.expenses:
            self.costToLive += i

        return
