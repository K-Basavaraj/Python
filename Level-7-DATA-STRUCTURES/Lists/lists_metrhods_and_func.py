"""
Len Function in Python
Purpose: Helps find the total number of elements in a list.
Real-world example: Useful for tracking items like veggies, fruits, or desserts in a grocery cart.
Practical application: Ensures compliance with express checkout conditions, such as having 10 or 15 items.

he len function simplifies list management in Python by allowing quick assessment of list length, 
facilitating various practical tasks.
"""
#example1: len function
grocery_cart = ["veggies", "fruits", "desserts"]
number_of_items = len(grocery_cart)
print(number_of_items) #output: 3 the len function counts the number of items in the grocery_cart list, which is 3.

#Understanding List Functions: len() and sorted()
#example2:len function with express checkout
grocery_cart = ["veggies", "fruits", "desserts", "bread", "milk", "eggs", "cheese", "cereal", "juice", "snacks"]
print(len(grocery_cart)) #output: 10 the len function counts the number of items in the grocery_cart list, which is 10.

sorted_cart = sorted(grocery_cart)
print(sorted_cart) #output: ['bread', 'cereal', 'cheese', 'desserts', 'eggs', 'fruits', 'juice', 'milk', 'snacks', 'veggies'] the sorted function sorts the items in the grocery_cart list in alphabetical order and returns a new sorted list.

#another example of len and sorted functions
numbers = [5, 2, 9, 1, 5, 6]
print(len(numbers)) #output: 6 the len function counts the number of items in the numbers list, which is 6.
print(sorted(numbers)) #output: [1, 2, 5, 5, 6, 9] the sorted function sorts the items in the numbers list in ascending order and returns a new sorted list.

#example3: final example of len and sorted functions
numbers = [5, 2, 9, 1]
print(len(numbers), sorted(numbers)) #output: 4 [1, 2, 5, 9] the len function counts the number of items in the numbers list, which is 4, and the sorted function sorts the items in the numbers list in ascending order and returns a new sorted list.