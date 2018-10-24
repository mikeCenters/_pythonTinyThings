# Input an item, then output the information
item1Name = input('Enter food item name: \n')
item1Price = float(input('Enter item price: \n'))
item1Quantity = int(input('Enter item quantity: \n'))
item1Total = item1Quantity * item1Price

# Read an item information and output on receipt
print('\nRECEIPT')
print(item1Quantity, item1Name, '@ $', item1Price, '= $', item1Total)
print('Total cost: $', item1Total)

# Input/Output a second item
print()
print()
item2Name = input('Enter second food item name: \n')
item2Price = float(input('Enter item price: \n'))
item2Quantity = int(input('Enter item quantity: \n'))
item2Total = item2Quantity * item2Price

print('\nRECEIPT')
print(item1Quantity, item1Name, '@ $', item1Price, '= $', item1Total)
print(item2Quantity, item2Name, '@ $', item2Price, '= $', item2Total)
print('Total cost: $', item1Total + item2Total)

# Add a gratuity to the ticket and total the items
allItems = item1Total + item2Total
tip = allItems * 0.15

print()
print(r'15% gratuity: $', tip)
print('Total with tip: $', allItems + tip)
