"""
List Duplication and Copying in Python
When working with lists in Python, duplication and copying are crucial to avoid data overwriting and loss. 

Why Duplicate lists?
To preserve original data while experimenting.
To safely modify a separate instance of a list.
To recover from errors efficiently.

Key Practices for Copying Lists:
Using list.copy() Method:
Creates a snapshot of the list items.
Ensures further updates do not affect the original list.

Applications in Code:
Avoid unwanted side-effects during operations.
Fortifies list management by knowing diverse methods for copying.

copy() which creates a new list thats a duplicate of the orginal. 
The two lists are independent chnaging one doesn't affect the other.
syntax: new_list = original_list.copy()
Note: copy() creates a shallow copy of the list. If the list contains mutable objects like other lists, 
the inner objects are not copied but referenced. So changes to mutable objects in one list will affect the other list.
"""
#example1: this is a mistake we cant go backwards to the original list if we change the new list because they are referencing the same list in memory.
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]

print(vegetables) #output: ['carrot', 'broccoli', 'spinach'] this is the original vegetables list.

vegitables = fruits 
print(vegitables) 
#output: ['apple', 'banana', 'cherry'] this is the vegitables list which is now referencing the same list as fruits.  

print(fruits) #output: ['apple', 'banana', 'cherry'] this is the original fruits list.
#==========================================================================================================================
#example2: to avoid this we can use the copy method to create a new list that is a copy of the original list.

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]

vegetables_clone = vegetables.copy() #this creates a new list called vegetables_clone that is a copy of the original vegetables list.
print(vegetables_clone) #output: ['carrot', 'broccoli', 'spinach'] this is the new vegetables_clone list which is a copy of the original vegetables list.  

vegetables.append("lettuce") #this will add "lettuce" to the vegetables list but not to the vegetables_clone list because they are now separate lists in memory.
print(vegetables) #output: ['carrot', 'broccoli', 'spinach', 'lettuce'] this is the original vegetables list which now includes "lettuce".
print(vegetables_clone) #output: ['carrot', 'broccoli', 'spinach'] this is the vegetables_clone list which does not include "lettuce" because it is a separate copy of the original vegetables list.
#=====================================================================================================
#example3: using slicing to create a copy of a list
vegetables_clone2 = vegetables[:] #this creates a new list called vegetables_clone2 that is a copy of the original vegetables list using slicing.
print(vegetables_clone2) #output: ['carrot', 'broccoli', 'spinach', 'lettuce'] this is the new vegetables_clone2 list which is a copy of the original vegetables list.