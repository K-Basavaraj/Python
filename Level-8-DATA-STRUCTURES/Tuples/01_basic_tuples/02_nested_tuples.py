"""
what is a nested tuple? 
A nested tuple is a tuple that contains other tuples as items. just like list inside lists you can have 
tuples inside tuples 
useful when we want to group related sets of data. 
"""
############################################################################################
#example1: basic nested tuple 
nested = ((1,2), (3,4), (5,6)) #The outer tuple has 3 iteams each times is itself a tuple of 2 numbers
print(nested) #o/p: ((1, 2), (3, 4), (5, 6))
print(len(nested)) #3

#How indexing works on nested tuples 
#fIRST LEVEL - GRAB ONE WHOLE INNER TUPLE
print(nested[0])  #(1, 2)
print(nested[1])  #(3, 4)
print(nested[2])  #(5, 6)

#SECOND LEVEL- GOING INTO INNER TUPLE
print(nested[0][0]) # 1(first item of first inner tuple)
print(nested[0][1]) # 2(second item of first inner tuple)
print(nested[1][0]) # 3(first item of second inner tuple)
print(nested[2][1]) # 6(second item of third inner tuple)

##############################################################################################
#Example6: Netsed tuples (tuples inside tuples)
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
#########################################################################################################
#Example: mixed type nested tuples
employees = (
    ("Alice", 30, "Engineer"), 
    ("Bob", 25, "Designer"), 
    ("Charli", 35, "Manager"),
) 
print(employees[0]) #('Alice', 30, 'Engineer')
print(employees[1][0]) #Bob
print(employees[2][2]) #Manager

#example4:
deep = (("a", "b"),("c",("d","e")), "f")
print(deep[0]) #('a', 'b')
print(deep[1]) #('c', ('d', 'e'))
print(deep[1][1]) #('d', 'e')
print(deep[1][1][0]) #d
print(deep[2]) #f
