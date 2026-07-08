"""
what is set? 

A set is an unorderd collection of unique itmes 

- no duplicates allowed
- no indexing (unordered cant do s[0])
- mutable ( can add/remove items)
- items inside must be immuatble (strings, numbers, tuples)

synatx: 
    my_Set = {1,2,3}

no indexing sets have no order
"""

#creating sets 
fruits = {"apple", "banana", "cherry"}
print(fruits) #{'cherry', 'banana', 'apple'}
print(type(fruits)) #<class 'set'>

#from a list auto removes duplicates 
fruits = set(["apple", "rajesh", "banana", "cherry", "apple", "rajesh"])
print(fruits)
# {'cherry', 'banana', 'apple', 'rajesh'} 

#example2: empty set - use set() not {}
empty1 = set() #empty set 
empty2 = {}
print(type(empty1)) #<class 'set'>
print(type(empty2)) #<class 'dict'>

#example3: duplicates disaaper automatically 
s = {"a", "b", "a", "c", "b"}
print(s) #{'a', 'b', 'c'}

#items must be immutable (like dict keys!)

ok = {1, "text", (1,2), True}
#bad = {1, [2, 3]} TypeError: unhashable type: 'list' not allowed mutanle itmes 