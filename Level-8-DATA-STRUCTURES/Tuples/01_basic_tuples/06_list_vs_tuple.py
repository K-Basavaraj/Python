"""
-> Lists are mutable which can be chnaged after creation. 
-> Tuples are immutable which can not be chnaged after creation 
Both can store collection of items. But tuples are "locked" once created. 
Since tuples are immutable, these are the only specific methods availible directly to them which are only index() and count(). 

--> USE LIST=> when the data will chnage over the ti8me(add,sort,filer, items etc; )
--> USE TUPLE -> when the data is fixed and should not chnage(coordinates, config values, function returns.)
"""
#example1: List - mutable (changeable)
my_list = [1, 2, 3]
my_list[0] = 10  # This is allowed
print(my_list) #output: [10, 2, 3] this will print the modified list, which has the first element changed to 10 while the other elements remain unchanged.

#example2: Tuple - immutable (unchangeable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise an TypeError: 'tuple' object does not support item assignment because tuples do not allow modification of their elements after they have been created. Attempting to change an element of a tuple will result in a TypeError indicating that item assignment is not supported for tuples.
print(my_tuple) #output: (1, 2, 3) this will print the tuple as it is immutable and cannot be changed.

