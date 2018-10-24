from itertools import groupby

### Problem-solving approaches:
### The dictionary ultimately needs to be sorted and because dictionaries cannot
### be sorted, we will convert the dictionary into a list. Because the values have
### variance in the number of lists and the lists can have duplicate values, a key
### will be placed as the first index of the outer list, and the inner list will
### maintain structure across different sorting outcomes. Next, we will need to
### group the artificial keys together when sorting, and put the list of movie data
### inside of the inner list with it's corresponding key in the outside list.

# Dictionary of movie year, title, director
meta_d = {
    '2005' : ['Munich', 'Steven Spielberg'],
    '2006' : [['The Prestige', 'Christopher Nolan'], ['The Departed', 'Martin Scorsese']],
    '2007' : ['Into the Wild', 'Sean Penn'],
    '2008' : ['The Dark Knight', 'Christopher Nolan'],
    '2009' : ['Mary and Max', 'Adam Elliot'],
    '2010' : ['The King\'s Speech', 'Tom Hooper'],
    '2011' : [['The Artist', 'Michel Hazanavicius'], ['The Help', 'Tate Taylor']],
    '2012' : ['Argo', 'Ben Affleck'],
    '2013' : ['12 Years a Slave', 'Steve McQueen'],
    '2014' : ['Birdman', 'Alejandro G. Inarritu'],
    '2015' : ['Spotlight', 'Tom McCarthy'],
    '2016' : ['The BFG', 'Steven Spielberg'],
}

## Because dictionaries cannot be sorted, the class produces a list with a tuple.
## The first index of the tuple is the element used to sort, while the second index
## is a list with the data corresponding to the first index, inside of a tuple. The
## end result is: [(<sortBy>, [(year, title, director), ...]), ...)]. The first index
## of the outer tuple is used for sorting. In regards to best coding practices, the
## use of a class allows the code to be easy to read and explicit. The objects created
## with this class will maintain a uniform structure, and if the code needs to be
## extended or features need to be implemented, the programmer will easily be able
## to call a desired data entry. Next, the class is built in regards to the given
## dictionary, but the class allows for new entries into the dictionary and extention
## of any year beyond one or two lists. This is to prevent hard coding the class and
## cause errors when sorting the values.

### When the class is initialized, the first stage is to seperate the data into a
### tuple, then place the tuple inside of a list.
class Sorter:
    def __init__(self, source):
        self._wList = []
        # Dict to list [(year, title, director), ...]
        for year, movie in source.items():
            ### Build a working list, and if movie[0] is not a list, movie is placed in a list for the iteration.
            ### This is because when the dictionary is split with .items(), some values in the dictionary will
            ### only be one list, while others will have multiple lists. Because we are spliting the value into
            ### title and director in the next line, the iteration will not work because movie would otherwise
            ### not be able to be split into seperate variables. The working list is an object used to build the
            ### sorted lists.
            for title, director in movie if isinstance(movie[0], list) else [movie]:
                self._wList.append((year, title, director))

### These private variables are used to determine the index of the object to use for sorting, or the first index.
### Next, if another programmer needs to edit the code, the code is easily understood for future features. The
### variables are private to prevent changes to these variables, because it will break the structure of the list.
    def _byYear(self, x):
        return x[0]
    def _byTitle(self, x):
        return x[1]
    def _byDirector(self, x):
        return x[2]
### Here, the sort is performed based upon the first index. Because we will have duplicate years and directors,
### the groupby() function is used to consolidate the movie data into one list.
### e.g. [('2006', [('2006', 'The Prestige', 'Christopher Nolan')]), ('2006', [('2006', 'The Departed', 'Martin Scorsese')]), ...]
### becomes
### [('2006', [('2006', 'The Prestige', 'Christopher Nolan'), ('2006', 'The Departed', 'Martin Scorsese')]), ...]
    def sort(self, sortFn):
        ## Sorted data [(key, [(... movie_data ...)]), ...]
        groups = []
        data = sorted(self._wList, key=sortFn)
        for k, g in groupby(data, sortFn):
            groups.append((k, list(g)))
        return groups

### These functions are to be used when the desired outcome is established by the user. They are used in conjunction with
### the previous sort function.
    def sortByYear(self):
        return self.sort(self._byYear)
    def sortByTitle(self):
        return self.sort(self._byTitle)
    def sortByDirector(self):
        return self.sort(self._byDirector)

sorted_list = Sorter(meta_d)

u_input = input('Enter a year between 2005 and 2016:\n')

# We need to check if the year for input exists in the dictionary.
check_year = meta_d.get(u_input, 'N/A')

# If the year exists, utilize the sortByYear function to print the movies of desired year.
### A for loop is used to iterate over the entire list and once the year is found, we print
### the title and directors of that year. This method allows for multiple movies within a
### year to be present in the dictionary for the print function. Next, an if/else statement
### is utilized to determine if the loop needs to be used. Because the assignment required
### a 'N/A' response if no year is found, the following structure is used.
if check_year != 'N/A':
    for year, meta in sorted_list.sortByYear(): # sorted_list.sortByYear() = [(year, [(year, title, director), ...]), ...]
        if year == u_input: # Searching for the user input year.
            for movie in meta: # Iterating over the year to print the movie(s).
                print('{}, {}'.format(movie[1], movie[2])) # movie = (year, title, director)
else:
    print(check_year) # If user input a year that is not in the dictionary, print 'N/A'.
print()

# sort by choice menu
menu = (
    'MENU\n'
    'Sort by:\n'
    'y - Year\n'
    'd - Director\n'
    't - Movie title\n'
    'q - Quit\n'
    ''
    )

### Because a quit option is available, we will be using a while loop to continually execute the following lines
### until the user decides to end the program. The best practice of this structure is to maintain an easy to read
### coding structure so that any programmer can understand what is being implemented.
print(menu)
u_input = input('Choose an option:\n')

while u_input != 'q':
    if u_input == 'q': # This has to be the first if statement to determine if the user wants to stop the program.
        break
    elif u_input == 'y': # Sort the movies by year.
        for year, meta in sorted_list.sortByYear(): # sorted_list.sortByYear() = [(year, [(year, title, director), ...]), ...]
            print('{}:'.format(year))
            for movie in meta: # Iterate over the tuple with movie data to print title and director.
                print('\t{}, {}'.format(movie[1], movie[2]))
            print()
    elif u_input == 'd': # Sort the movies by director.
        for director, meta in sorted_list.sortByDirector(): # sorted_list.sortByDirector() = [(director, [(year, title, director), ...]), ...]
            print('{}:'.format(director))
            for movie in meta: # Iterate over the tuple with movie data to print title and year.
                print('\t{}, {}'.format(movie[1], movie[0]))
            print()
    elif u_input == 't': # Sort the movies by title.
        for title, meta in sorted_list.sortByTitle(): # sorted_list.sortByTitle() = [(title, [(year, title, director), ...]), ...]
            print('{}:'.format(title))
            for movie in meta: # Iterate over the tuple with movie data to print director and year.
                print('\t{}, {}'.format(movie[2], movie[0]))
            print()
    print(menu)
    u_input = input('Choose an option:\n')
