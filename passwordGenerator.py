user_color = str(input('Enter favorite color: \n'))
user_pet = str(input('Enter pet\'s name: \n'))
user_number = int(input('Enter a number: \n'))

print()
print(user_color, user_pet, user_number)
print()

# Generate a password - (color_color)
password1 = ('%s_%s' % (user_color, user_pet))
print('First password:', password1)
# Generate a password - (NumberColorNumber)
password2 = ('%i%s%i' % (user_number, user_color, user_number))
print('Second password:', password2)
print()

# Determine the length of the given passwords
pass_len1 = len(password1)
pass_len2 = len(password2)
print('Number of characters in %s: %i' % (password1, pass_len1))
print('Number of characters in %s: %i' % (password2, pass_len2))
