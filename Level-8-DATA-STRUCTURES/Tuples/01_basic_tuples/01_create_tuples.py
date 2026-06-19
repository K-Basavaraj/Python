"""
A tuple is like a list but it is immutable(can not be changed after creation).\
-> once the tupe is created, it can not be modified.
-> list use[] and tuple use () to create a tuple.
-> tuple is like data is fixed dont touch it. 
-> tuples are faster that list because they are immutable and have a smaller memory footprint.
-> When functions returns multiple values, python automatically packs them into a tuple.

=> what is constructor? 
a constructor is a special function that is used to create an object. In python, 
the tuple() constructor is used to create a tuple from an iterable (like a list, string, etc). 
The constructor takes the iterable as an argument and returns a new tuple containing the elements of the iterable.
"""
#########################################################################################################################
#example: simple tuple
cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print(type(cities)) #output: <class 'tuple'> this will print the type of the variable cities, which is a tuple.
print(cities) #output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix') this will print the contents of the cities tuple, which is a collection of city names.


#example2: 2nd way of creation tunples without parentheses( also valid just comma is what makes it a tuple)
colors = "red", "green", "blue"
print(type(colors)) #output: <class 'tuple'> this will print the type of the variable colors, which is a tuple.
print(colors) #output: ('red', 'green', 'blue') this will print the contents of the colors tuple, which is a collection of color names.


#example3: empty tuple
empty1 = () #this will create an empty tuple using parentheses.
empty2 = tuple() #this will create an empty tuple using the tuple() constructor.
print(empty1, type(empty1)) #output: () <class 'tuple'> this will print the empty tuple and its type, which is a tuple.
print(empty2, type(empty2)) #output: () <class 'tuple'> this will print the empty tuple and its type, which is a tuple.


#example4: using the tuple() constructor to create a tuple from a list / convert a list to a tuple using tuple() 
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers_list) #or numbers_tuple = tuple([1, 2, 3, 4, 5]) this will create a tuple called numbers_tuple by converting the numbers_list using the tuple() constructor. The resulting tuple will contain the same elements as the original list.
print(type(numbers_tuple)) #output: <class 'tuple'> this will print the type of the variable numbers_tuple, which is a tuple.
print(numbers_tuple) #output: (1, 2, 3, 4, 5) this will print the contents of the numbers_tuple, which is a tuple containing the numbers from the original list.


#example5: tuple with mixed data types
mixed_tuple = ("Alice", 30, 5.5, True) #this will create a tuple called mixed_tuple that contains elements of different data types: a string ("Alice"), an integer (30), a float (5.5), and a boolean (True).
print(mixed_tuple) #output: ('Alice', 30, 5.5, True) this will print the contents of the mixed_tuple, which is a tuple containing elements of different data types.
print(type(mixed_tuple)) #output: <class 'tuple'> this will print the type
#Tuples can hold any combiniation of data types like lists. 