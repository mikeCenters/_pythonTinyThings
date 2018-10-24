# Title and Column Names
title = input('Enter a title for the data: \n')
print('You entered: {}\n'.format(title))
header1 = input('Enter the column 1 header: \n')
print('You entered: {}\n'.format(header1))
header2 = input('Enter the column 2 header: \n')
print('You entered: {}\n'.format(header2))

# Gather the data
## Since the assignment uses two columns, I used a dictionary to ensure the string
## and integer are easily callable and this would prevent the data from being
## seperated. This is a major effort to keep the code simple and easy to read.
## For problem solving, the program requires the user to input data that will be
## used to later build a histogram and table, displaying the data for the user.
## I used a while loop to build the dictionary, because this would be the most
## sufficient way to perform the task and reduce bugs. While loops are supposed
## to execute, so long as a condition is true: In this case, the user wants to
## input data or does not want to input data. Because the data relies on integers
## to build the histogram, error checks are performed before building the dictionary
## and preventing an index out of range or similar bug from crashing the program.
## First, the loop checks to see if the user wants to stop input before proceeding
## for otherwise, we will get the 'Error: No comma in string.' message before the
## loop stops(e.g. a bug in the program). The loop is structured so that the loop
## acutally breaks with an if statement and the while condition should never see
## a false condition. This is so that if the program needs to be expanded or something
## unexpected occurs, the loop will not execute so long as the user inputs '-1';
## thus still building the table and histogram.
u_input = '0' # variable to determine our values
quit = '-1' # variable to end the loop and compare to u_input
dict = {} # empty dictionary for data input
while u_input != quit:
    ## The input is stripped of white spaces at the beginning and end of the string
    ## to prevent ' -1' or similar strings from not breaking the loop.
    u_input = input('Enter a data point (-1 to stop input): \n').strip()
    ## Errors must be checked first or as soon as possible to prevent empty
    ## elements or duplicate entries. If statements were used to perform this
    ## task, for this adds the ability to determine when to break if a condition
    ## is met.
    if quit == u_input: # offer a way to exit the input loop
        print()
        break
    if ',' not in u_input: # comma is used to seperate the list
        print('Error: No comma in string.\n')
        continue
    if u_input.count(',') > 1: # only one comma is necessary
        print('Error: Too many commas in input.\n')
        continue
    ## Once most of the errors have been checked, we can seperate the the input string
    ## to start preparing them for dictionary entry. First, a copy of the u_input is
    ## produced to prevent changes to the u_input variable, and is made into a list
    ## with .split to keep the code simple. The purpose of not changing the u_input
    ## variable is to prevent unexpected behavior from breaking the program
    working_input = u_input[:].split(',') # split u_input into a list for conversion
    ## The next two lines are to remove white spaces from the start and finish of the strings.
    ## This is to prevent white spaces from moving the text later in the table and histogram.
    data_str = working_input[0].strip()
    data_int = working_input[1].strip()
    ## The histogram requires an integer value to build the table. If the user input a wrong
    ## string, this will check and ensure the dictionary is built properly and also convert
    ## the string to an integer.
    if data_int.isdigit() is True: # our value needs to be an integer for the histogram
        data_int = int(data_int) # if the value is a number, convert string to integer
    else:
        print('Error: Comma not followed by an integer.\n')
        continue
    ## Display the input and build the dictionary. Perhaps a confirmatory prompt should
    ## be implemented to ensure data is correct from the user; a simple if/else statement
    ## could accomplish this task.
    print('Data string: {}'.format(data_str))
    print('Data integer: {}'.format(data_int))
    dict[data_str] = data_int # build the dictionary
    print()

# Table of Dictionary
print('%33s' % (title))
print('%-20s|%23s' % (header1, header2))
print('-' * 44)
## A for loop is used because we only want the loop to print each key/value once,
## and to also keep the code easy to read.
for i in dict: # print each key and value for the table
    print('%-20s|%23i' % (i, dict[i]))

print()

# Histogram of Dictionary
## A for loop is used because we only want the loop to print each key/value once,
## and to also keep the code easy to read.
for i in dict: # print each key and histogram of value
    print('%20s %s' % (i, '*' * dict[i]))
