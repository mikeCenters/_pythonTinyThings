cost_oil_change = int(35)
cost_tire_rotation = int(19)
cost_car_wash = int(7)

service_option = input('Enter desired auto service: \n')

print('You entered:', service_option)

if service_option == 'Oil change':
    print('\nCost of oil change: $%i' % (cost_oil_change))
elif service_option == 'Tire rotation':
    print('\nCost of tire rotation: $%i' % (cost_tire_rotation))
elif service_option == 'Car wash':
    print('\nCost of car wash: $%i' % (cost_car_wash))
else:
    print('\nError: Requested service is not recognized.')
