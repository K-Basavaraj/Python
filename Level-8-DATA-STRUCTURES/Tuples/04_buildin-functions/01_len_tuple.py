"""
builtin functions are glopbal tools that come with python, unlike methods (which use dot notation like tup.count()), 
built-in are clled by name, with the tuple as input. 

methods style: tup.count(x) 
built-in style: len(tup)

len() function: 
len(tuple) returns the number of items in the tuple. 
syntax: len(tuple_name) 
returns : an integer (the count of items)
"""
#example1: 
fruits = ("apple", "banana", "cherry", "date")
print(len(fruits))
#o/p: 4

#example2: nested tuple - len() count the outer level only 
nested = ((1,2), (3,4,5), (6,))
print(len(nested)) #3
print(len(nested[1])) #3

#example: use len() with indexing 
data = ("a", "b", "c", "d")
print(data[len(data)-1]) #data[3] o/p d
print(data[-1]) #d