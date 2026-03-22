"""
Combining Collections
Lists can be nested within tuples, allowing modifications to the lists themselves.
Tuples can be components of lists, maintaining immutability of nested elements.
Examples
List Inside a Tuple

Tuple representing travel legs, containing lists of cities.
Cities can be updated but not tuple structure.
Tuple Inside a List

List of tuples, each holding city pairs.
Tuples are immutable, but list items can be added or removed.
Understanding when to use each structure optimizes data handling and maintains integrity based on requirements.

Lists within Tuples
Flexibility: Lists can be included as elements inside tuples.
Mutability: Although tuples are fixed, the contained lists can be altered.

Combining Features
Nested Structures: Combine tuples and lists to control which data remains static and which part can be dynamically modified. This enables optimal management of data integrity and flexibility.
"""

#example: list inside a tuple
travel_legs = (["New York", "Los Angeles"], ["Chicago", "Houston"], ["Phoenix", "San Francisco"])
print(travel_legs) #output: (['New York', 'Los Angeles'], ['Chicago', 'Houston'], ['Phoenix', 'San Francisco']) this will print the original travel_legs tuple, which contains three lists of city pairs.
print(travel_legs[0]) #output: ['New York', 'Los Angeles'] this will access the first element (index 0) of the travel_legs tuple, which is the list containing "New York" and "Los Angeles".
print(travel_legs[1]) #output: ['Chicago', 'Houston'] this will access the second element (index 1) of the travel_legs tuple, which is the list containing "Chicago" and "Houston".
print(travel_legs[2]) #output: ['Phoenix', 'San Francisco'] this will access the third element (index 2) of the travel_legs tuple, which is the list containing "Phoenix" and "San Francisco".

print(travel_legs[0][0]) #output: New York this will access the first element (index 0) of the first list (index 0) in the travel_legs tuple, which is "New York".
print(travel_legs[0][1]) #output: Los Angeles this will access the second element (index 1) of the first list (index 0) in the travel_legs tuple, which is "Los Angeles".
print(travel_legs[1][0]) #output: Chicago this will access the first element (index 0) of the second list (index 1) in the travel_legs tuple, which is "Chicago".
print(travel_legs[1][1]) #output: Houston this will access the second element (index 1) of the second list (index 1) in the travel_legs tuple, which is "Houston".
print(travel_legs[2][0]) #output: Phoenix this will access the first element (index 0) of the third list (index 2) in the travel_legs tuple, which is "Phoenix".
print(travel_legs[2][1]) #output: San Francisco this will access the second element (index 1) of the third list (index 2) in the travel_legs tuple, which is "San Francisco".

#modifying the list inside the tuple
travel_legs[0][0] = "San Francisco" #this will change the first element (index 0) of the first list (index 0) in the travel_legs tuple from "New York" to "San Francisco". This is allowed because the list itself is mutable, even though it is contained within an immutable tuple.
print(travel_legs) #output: (['San Francisco', 'Los Angeles'], ['Chicago', 'Houston'], ['Phoenix', 'San Francisco']) this will print the modified travel_legs tuple, showing that the first element of the first list has been changed to "San Francisco".

#----------------------------------------------------------------------------------------------------------------------
#example: tuple inside a list
city_pairs = [("New York", "Los Angeles"), ("Chicago", "Houston"), ("Phoenix", "San Francisco")]
print(city_pairs) #output: [('New York', 'Los Angeles'), ('Chicago', 'Houston'), ('Phoenix', 'San Francisco')] this will print the original city_pairs list, which contains three tuples of city pairs.
print(city_pairs[0]) #output: ('New York', 'Los Angeles') this will access the first element (index 0) of the city_pairs list, which is the tuple containing "New York" and "Los Angeles".
print(city_pairs[1]) #output: ('Chicago', 'Houston') this will access the second element (index 1) of the city_pairs list, which is the tuple containing "Chicago" and "Houston".
print(city_pairs[2]) #output: ('Phoenix', 'San Francisco') this will access the third element (index 2) of the city_pairs list, which is the tuple containing "Phoenix" and "San Francisco".

print(city_pairs[0][0]) #output: New York this will access the first element (index 0) of the first tuple (index 0) in the city_pairs list, which is "New York".
print(city_pairs[0][1]) #output: Los Angeles this will access the second element (index 1) of the first tuple (index 0) in the city_pairs list, which is "Los Angeles".
print(city_pairs[1][0]) #output: Chicago this will access the first element (index 0) of the second tuple (index 1) in the city_pairs list, which is "Chicago".
print(city_pairs[1][1]) #output: Houston this will access the second element (index 1) of the second tuple (index 1) in the city_pairs list, which is "Houston".
print(city_pairs[2][0]) #output: Phoenix this will access the first element (index 0) of the third tuple (index 2) in the city_pairs list, which is "Phoenix".
print(city_pairs[2][1]) #output: San Francisco this will access the second element (index 1) of the third tuple (index 2) in the city_pairs list, which is "San Francisco".

#adding to the list containing tuples
city_pairs.append(("Miami", "Orlando")) #this will add a new tuple ("Miami", "Orlando") to the end of the city_pairs list. This is allowed because the list itself is mutable, even though it contains immutable tuples.
print(city_pairs) #output: [('New York', 'Los Angeles'), ('Chicago', 'Houston'), ('Phoenix', 'San Francisco'), ('Miami', 'Orlando')] this will print the modified city_pairs list, showing that the new tuple ("Miami", "Orlando") has been added to the end of the list.

#modifying a tuple inside the list (this will raise an error)
#city_pairs[0][0] = "San Francisco" #output: TypeError: 'tuple' object does not support item assignment this will attempt to change the first element (index 0) of the first tuple (index 0) in the city_pairs list from "New York" to "San Francisco". However, since tuples are immutable, this will raise a TypeError indicating that item assignment is not supported for tuples.