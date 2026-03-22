"""
Tuples - Indexing, Slicing, Building, and Immutability
"""
#example: simple tuple
cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print(type(cities)) #output: <class 'tuple'> this will print the type of the variable cities, which is a tuple.
print(cities) #output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix') this will print the contents of the cities tuple, which is a collection of city names.

#example2: accessing specific elements in a tuple
print(cities[0]) #output: New York this will access the first element (index 0) of the cities tuple, which is "New York".
print(cities[1]) #output: Los Angeles this will access the second element (index 1) of the cities tuple, which is "Los Angeles".
print(cities[2]) #output: Chicago this will access the third element (index 2) of the cities tuple, which is "Chicago".
print(cities[3]) #output: Houston this will access the fourth element (index 3) of the cities tuple, which is "Houston".
print(cities[4]) #output: Phoenix this will access the fifth element (index 4) of the cities tuple, which is "Phoenix".
#print(cities[5]) #output: IndexError: tuple index out of range this will attempt to access the sixth element (index 5) of the cities tuple, which does not exist, resulting in an IndexError.

#example: slicing a tuple
print(cities[1:4]) #output: ('Los Angeles', 'Chicago', 'Houston') this will slice the cities tuple from index 1 to index 3 (index 4 is not included), resulting in a new tuple containing "Los Angeles", "Chicago", and "Houston".
print(cities[:3]) #output: ('New York', 'Los Angeles', 'Chicago') this will slice the cities tuple from the beginning (index 0) to index 2 (index 3 is not included), resulting in a new tuple containing "New York", "Los Angeles", and "Chicago".
print(cities[3:]) #output: ('Houston', 'Phoenix') this will slice the cities tuple from index 3 to the end of the tuple, resulting in a new tuple containing "Houston" and "Phoenix".
print(cities[2:5]) #output: ('Chicago', 'Houston', 'Phoenix') this will slice the cities tuple from index 2 to index 4 (index 5 is not included), resulting in a new tuple containing "Chicago", "Houston", and "Phoenix".
print(cities[:]) #output: ('New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix') this will slice the entire cities tuple, resulting in a new tuple that is identical to the original cities tuple.

#cities[0] = "San Francisco" #output: TypeError: 'tuple' object does not support item assignment this will attempt to change the first element (index 0) of the cities tuple to "San Francisco", but since tuples are immutable, this will raise a TypeError indicating that item assignment is not supported for tuples.