import math

# Dictionary of paint colors and cost per gallon
paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# Calculate and output the area of a wall
wallHeight = float(input('Enter wall height (feet): \n'))
wallWidth = float(input('Enter wall width (feet): \n'))
wallArea = str(wallHeight * wallWidth)

print('Wall area: %s square feet' % (wallArea))

# Calculate and output the amount of paint needed in gallons.
# Assume one gallons of paint covers 350 square feet.
## Float limits to 8 characters, while String will display everything.
gallonPaint = 350
requiredGallons = str(float(wallArea) / float(gallonPaint))

print('Paint needed: %s gallons' % (requiredGallons))

# Number of 1 gallon cans needed to paint the wall --- rounded up.
requiredGallons = float(requiredGallons)
paintCans = int(math.ceil(requiredGallons))

print('Cans needed: %i can(s)' % (paintCans))
print()
# Determine desired color to paint the walls and calculate the cost.
desiredColor = input('Choose a color to paint the wall: \n')
colorCost = paintColors[desiredColor] * paintCans

print('Cost of purchasing %s paint: $%i' % (desiredColor, colorCost))
