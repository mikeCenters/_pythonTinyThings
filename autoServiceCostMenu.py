# Auto service cost.
# This program requires variables to store the costs of various services.
# The best practice is to keep the code simple and easy to understand.
oil_change = int(35)
tire_rotation = int(19)
car_wax = int(12)
car_wash = int(7)

# Print service menu and input option.
# This program requires an interactive menu for user to determine needs.
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()
option1 = input('Select first service: \n\n')
option2 = input('Select second service: ')
print()
print()
print()

# Print user options with cost and assign costs to new variables.
# This program requires the confirmation of choice and the creation of variables
# to allow a calculation of the total cost.
# The best practice is to keep the code simple and easy to understand, also
# to test each option.
option1cost = int(0)
option2cost = int(0)
print('Davy\'s auto shop invoice\n')
if option1 == 'Oil change':
    print('Service 1: Oil change, $%i' % (oil_change))
elif option1 == 'Tire rotation':
    print('Service 1: Tire rotation, $%i' % (tire_rotation))
elif option1 == 'Car wax':
    print('Service 1: Car wax, $%i' % (car_wax))
elif option1 == 'Car wash':
    print('Service 1: Car wash, $%i' % (car_wash))
elif option1 == '-':
    print('Service 1: No service')

# Assign cost for option1 to new variable
if option1 == 'Oil change':
    option1cost = oil_change
elif option1 == 'Tire rotation':
    option1cost = tire_rotation
elif option1 == 'Car wax':
    option1cost = car_wax
elif option1 == 'Car wash':
    option1cost = car_wash

# Print the cost of option2
if option2 == 'Oil change':
    print('Service 2: Oil change, $%i' % (oil_change))
elif option2 == 'Tire rotation':
    print('Service 2: Tire rotation, $%i' % (tire_rotation))
elif option2 == 'Car wax':
    print('Service 2: Car wax, $%i' % (car_wax))
elif option2 == 'Car wash':
    print('Service 2: Car wash, $%i' % (car_wash))
elif option2 == '-':
    print('Service 2: No service')

# Assign cost for option2 to new variable
if option2 == 'Oil change':
    option2cost = oil_change
elif option2 == 'Tire rotation':
    option2cost = tire_rotation
elif option2 == 'Car wax':
    option2cost = car_wax
elif option2 == 'Car wash':
    option2cost = car_wash

# Total cost of service.
total_cost = int(option1cost + option2cost)
print('\nTotal: $%i' % (total_cost))
