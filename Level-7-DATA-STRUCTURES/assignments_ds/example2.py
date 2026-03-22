"""
Part 3: Modifying Lists and Demonstrating Tuple Immutability
The major difference to note when comparing lists and tuples is that lists are mutable, which means you can change their elements, 
while tuples are immutable and do not allow modifications.

For lists, once they're initialized in a Jupyter Notebook or within a Python environment (i.e. a cell is run creating it), 
you can add and remove items at will. But for tuples, they cannot be edited after being deployed to the Python environment, 
preserving their values.

task:
 Change the first element in cities_list to "San Francisco" and print the updated cities_list
 Bonus : Attempt to change the first element in cities_tuple to "San Francisco"
Use a try-except block to try the tuple modification, and then catch the error with a TypeError as e for the except statement 
to print an error for e about tuples not being able to be modified

Hint: You might see an error. Why is this?
 Add a new city "Orlando" to cities_list using the .append() method and print the updated cities_list
 Remove a city, "Chicago", from cities_list using the .remove() method and print the updated cities_list
"""

cities_list = ["New York", "Los Angeles", "Chicago"] 
cities_tuple = ("New York", "Los Angeles", "Chicago")

# Step 1 - Modify the first element in the list
cities_list[0] = "San Francisco" #this will change the first element (index 0) of the cities_list from "New York" to "San Francisco". This is allowed because lists are mutable.
print("After changing the first city in list:", cities_list) #this will print the updated cities_list, showing that the first element has been changed to "San Francisco".


# Step 2 - Attempt to modify the first element in the tuple
try:
    cities_tuple[0] = "San Francisco" #this will attempt to change the first element (index 0) of the cities_tuple from "New York" to "San Francisco". However, since tuples are immutable, this will raise a TypeError indicating that item assignment is not supported for tuples.
except TypeError as e:
    print("Error when attempting to modify tuple:", e) #this will catch the TypeError raised when trying to modify the cities_tuple and print the error message, which indicates that tuples do not support item assignment.

# Step 3 - Add a new city "Orlando" to the list
cities_list.append("Orlando") #this will add the new city "Orlando" to the end of the cities_list using the .append() method. This is allowed because lists are mutable.
print("After adding a new city to the list:", cities_list) #this will print the updated cities_list, showing that "Orlando" has been added to the end of the list.

# Step 4 - Remove a city from the list
cities_list.remove("Chicago") #this will remove the city "Chicago" from the cities_list using the .remove() method. This is allowed because lists are mutable.
print("Cities List after removing Chicago:", cities_list) #this will print the updated cities_list, showing that "Chicago" has been removed from the list.

# Expected Output:
# After changing the first city in list: ['San Francisco', 'Los Angeles', 'Chicago']
# Error when attempting to modify tuple: 'tuple' object does not support item assignment
# After adding a new city to the list: ['San Francisco', 'Los Angeles', 'Chicago', 'Orlando']
# After removing a city from the list: ['San Francisco', 'Los Angeles', 'Orlando']

print("-------------------------------------------------------")
"""
Part 4: Appending to a List and Converting Tuples to Lists
As we just saw, only lists can be modified by appending new items. However, we can convert a tuple to a list if 
we need to modify its content.

Let's practice this handy strategy so that we know how to work with lists and tuples interchangeably.

Task:
 Convert cities_tuple to a list named cities_tuple_as_list using the list() function
 Append "Houston" to the new cities_tuple_as_list list and print cities_tuple_as_list with the label "Modified Tuple (as a list):"
 to see the changes
 Convert cities_tuple_as_list back to a tuple and assign it to the original cities_tuple variable, updating its content with what 
 is in this new data structure
 Print cities_tuple to confirm that the originally-created tuple now includes "Houston" and has been updated with new contents
"""
# Step 1 - Convert tuple to list
cities_tuple_as_list = list(cities_tuple) #this will convert the cities_tuple from a tuple to a list using the list() function and store it in the variable cities_tuple_as_list.
# Step 2 - Append new city to the new list and print the new list
cities_tuple_as_list.append("Houston") #this will add the new city "Houston" to the end of the cities_tuple_as_list using the .append() method.
print("Modified Tuple (as a list):", cities_tuple_as_list) #this will print the updated cities_tuple_as_list, showing that "Houston" has been added to the end of the list.

# Step 3 - Convert the modified list back to a tuple and assign it to the original tuple variable
cities_tuple = tuple(cities_tuple_as_list) #this will convert the cities_tuple_as_list from a list to a tuple using the tuple() function and assign it to the original cities_tuple variable.

# Step 4 - Print the contents of the newly updated original tuple
print("Modified Original Tuple:", cities_tuple) #this will print the updated cities_tuple, showing that it now includes "Houston" and has been updated with the new contents from the modified list.

print("-------------------------------------------------------")
# Expected Output:
# Modified Tuple (as a list): ['New York', 'Los Angeles', 'Chicago', 'Houston']
# Modified Original Tuple: ('New York', 'Los Angeles', 'Chicago', 'Houston')



