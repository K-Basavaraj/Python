"""
Python provides several built-in methods that simplify list management. Here's a brief overview:

Append:
Adds an item to the end of a list.
Example: Adding "grape" to a list of fruits.

Insert:
Places an item at a specified index.
Useful for organizing items, e.g., placing "orange" at index 1 in the fruits list.

Index:
Locates the index of a specific item within a list.
Example: Finding the index of "banana" after new additions to the list.
"""
#example1: append
fruits = ["apple", "banana", "cherry"]
fruits.append("grapefruit")
print(fruits) #output: ['apple', 'banana', 'cherry', 'grapefruit'] here banana is at index 1, so when we insert orange at index 1, it will be placed before banana and the rest of the items will be shifted to the right.

#example2: insert
fruits.insert(1, "orange")
print(fruits) #output: ['apple', 'orange', 'banana', 'cherry', 'grapefruit'] now the banana is at index 2, cherry is at index 3 and grapefruit is at index 4.

#EXAMPLE3: index
index_of_banana = fruits.index("banana")
print(index_of_banana) #output: 2  after inserting orange, the index of banana is now 2 instead of 1.

print(fruits.index("grapefruit")) #output: 4 the index of grapefruit is 4.

print(fruits) #output: ['apple', 'orange', 'banana', 'cherry', 'grapefruit']