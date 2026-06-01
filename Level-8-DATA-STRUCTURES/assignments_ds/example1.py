"""
Part 1: Creating Lists and Tuples
Let's start by creating a list and a tuple to store some items. 
This will help acclimate us to these two data structures and how they work in Python.

Task:
 Create a list named cities_list containing the strings: "New York", "Los Angeles", and "Chicago".
 Create a tuple named cities_tuple containing the same strings.
 Print both cities_list and cities_tuple
 Print the type of cities_list and cities_tuple to validate the types are correct:
The type of a list should print: <class 'list'>
The type of a tuple should print: <class 'tuple'>
"""
# Your code here

# Create list and tuple
cities_list = ["New York", "Los Angeles", "Chicago"] 
cities_tuple = ("New York", "Los Angeles", "Chicago")

# Print both data collections
print("Cities List:", cities_list) # List variable here...
print("Cities Tuple:", cities_tuple)  # Tuple variable here...
      
# Print both data collections
print("Cities List Type:", type(cities_list)) # List variable here...
print("Cities Tuple Type:", type(cities_tuple))# Tuple variable here...

"""
Part 2: Accessing Elements with Indexing
Lists and tuples both support indexing, allowing you to access individual elements by their position.

Indexing is an important concept because if we need to count over a certain number of items or know that we'll always 
take the top item ("first"), or the last item in the list, indexing is a very handy tool in our Pythonic toolkit we can leverage.

In this exercise, let's practice using indexing with lists and tuples.
Task:
 Retrieve the 1st element of cities_list and store it in a variable named first_city_list
 Retrieve the last element of cities_list and store it in a variable named last_city_list
 Retrieve the 1st element of cities_tuple and store it in first_city_tuple
 Retrieve the last element of cities_tuple and store it in a variable named last_city_tuple
 Print the first elements: first_city_list and first_city_tuple
Each print statement should look like: print("First city in data_structure:", variable_here)
 Print the last elements: last_city_list and last_city_tuple
Each print statement should look like: print("Last city in data_structure:", variable_here)
Replace data_structure with actual structure (list for lists and tuple for tuples) print("First city in list:", variable_here)
"""
# Your code here

# Declare 4 variables
first_city_list = cities_list[0] #this will access the first element (index 0) of the cities_list, which is "New York", and store it in the variable first_city_list.
last_city_list = cities_list[-1] #this will access the last element (index -1) of the cities_list, which is "Chicago", and store it in the variable last_city_list.
first_city_tuple = cities_tuple[0] #this will access the first element (index 0) of the cities_tuple, which is "New York", and store it in the variable first_city_tuple.
last_city_tuple = cities_tuple[-1] #this will access the last element (index -

# 2 print statements for the first elements
print("First city in list:", first_city_list) #this will print the first city in the cities_list, which is stored in the variable first_city_list.
print("First city in tuple:", first_city_tuple) #this will print the first city in the cities_tuple, which is stored in the variable first_city_tuple.

# Include this break to separate loops
print('---------')

# 2 print statements for the last elements
print("Last city in list:", last_city_list) #this will print the last city in the cities_list, which is stored in the variable last_city_list.
print("Last city in tuple:", last_city_tuple) #this will print the last city in the cities_tuple, which is stored in the variable last_city_tuple.
