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

#example3: using the tuple() constructor to create a tuple from a list
numbers_list = [1, 2, 3, 4, 5]
numbers_tuple = tuple(numbers_list) #or numbers_tuple = tuple([1, 2, 3, 4, 5]) this will create a tuple called numbers_tuple by converting the numbers_list using the tuple() constructor. The resulting tuple will contain the same elements as the original list.
print(type(numbers_tuple)) #output: <class 'tuple'> this will print the type of the variable numbers_tuple, which is a tuple.
print(numbers_tuple) #output: (1, 2, 3, 4, 5) this will print the contents of the numbers_tuple, which is a tuple containing the numbers from the original list.

#example4: empty tuple
empty1 = () #this will create an empty tuple using parentheses.
empty2 = tuple() #this will create an empty tuple using the tuple() constructor.
print(empty1, type(empty1)) #output: () <class 'tuple'> this will print the empty tuple and its type, which is a tuple.
print(empty2, type(empty2)) #output: () <class 'tuple'> this will print the empty tuple and its type, which is a tuple.

#example5: tuple with mixed data types
mixed_tuple = ("Alice", 30, 5.5, True) #this will create a tuple called mixed_tuple that contains elements of different data types: a string ("Alice"), an integer (30), a float (5.5), and a boolean (True).
print(mixed_tuple) #output: ('Alice', 30, 5.5, True) this will print the contents of the mixed_tuple, which is a tuple containing elements of different data types.
print(type(mixed_tuple)) #output: <class 'tuple'> this will print the type
#Tuples can hold any combiniation of data types like lists. 
#########################################################################################################################

#example6: List - mutable (changeable)
my_list = [1, 2, 3]
my_list[0] = 10  # This is allowed
print(my_list) #output: [10, 2, 3] this will print the modified list, which has the first element changed to 10 while the other elements remain unchanged.

#example7: Tuple - immutable (unchangeable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise an TypeError: 'tuple' object does not support item assignment because tuples do not allow modification of their elements after they have been created. Attempting to change an element of a tuple will result in a TypeError indicating that item assignment is not supported for tuples.
print(my_tuple) #output: (1, 2, 3) this will print the tuple as it is immutable and cannot be changed.

#tuples can be dictoary keys because they are immutable, while lists cannot be dictionary keys because they are mutable.
locations = {
    ("us-east-1", "vergina"): "server-A", 
    ("us-west-1", "oregon"): "server-B",
}
print(locations[("us-east-1", "vergina")]) #output: server-A this will access the value associated with the key ("us-east-1", "vergina") in the locations dictionary, which is "server-A".

"""
#using a list as dict key - fails 
locations = {
    ["us-east-1", "vergina"]: "server-A", 
    ["us-west-1", "oregon"]: "server-B",
} #TypeError: unhashable type: 'list' this will raise a TypeError because lists are mutable and cannot be used as dictionary keys. The error message indicates that the list type is unhashable, meaning it cannot be used as a key in a dictionary.
"""
#########################################################################################################################
#Example8: Netsed tuples (tuples inside tuples)
nested = (("Alice", 30), ("Bob", 25), ("Charlie", 35)) #this will create a nested tuple called nested, which contains three inner tuples. Each inner tuple represents a person's name and age.
print(nested) #output: (('Alice', 30), ('Bob', 25), ('Charlie', 35)) this will print the contents of the nested tuple, which is a tuple containing three inner tuples with names and ages.
print(nested[0]) #output: ('Alice', 30) this will access the first inner tuple (index 0) of the nested tuple, which contains the name "Alice" and the age 30.
print(nested[1]) #output: ('Bob', 25) this will access the second inner tuple (index 1) of the nested tuple, which contains the name "Bob" and the age 25.
print(nested[2]) #output: ('Charlie', 35) this will access the third inner tuple (index 2) of the nested tuple, which contains the name "Charlie" and the age 35.
print(nested[0][0]) #output: Alice this will access the first element (index 0) of the first inner tuple (index 0) of the nested tuple, which is the name "Alice".
print(nested[0][1]) #output: 30 this will access the second element (index 1) of the first inner tuple (index 0) of the nested tuple, which is the age 30.
print(nested[1][0]) #output: Bob this will access the first element (index 0) of the second inner tuple (index 1) of the nested tuple, which is the name "Bob".
print(nested[1][1]) #output: 25 this will access the second element (index 1) of the second inner tuple (index 1) of the nested tuple, which is the age 25.
print(nested[2][0]) #output: Charlie this will access the first element (index 0) of the third inner tuple (index 2) of the nested tuple, which is the name "Charlie".
print(nested[2][1]) #output: 35 this will access the second element (index 1) of the third inner tuple (index 2) of the nested tuple, which is the age 35.
