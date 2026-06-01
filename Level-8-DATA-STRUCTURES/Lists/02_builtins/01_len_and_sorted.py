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

#example2:len function with express checkout
grocery_cart = ["veggies", "fruits", "desserts", "bread", "milk", "eggs", "cheese", "cereal", "juice", "snacks"]
print(len(grocery_cart)) #output: 10 the len function counts the number of items in the grocery_cart list, which is 10.


#How many items are in the list?
#example2: leangth of the list
servers = ["web1", "web2", "web3", "db-01"]
print(len(servers)) #output: 4 here we have used the len() function to get the number of items in the servers list. The len() function takes a list as an argument and returns the number of items in that list. In this case, there are 4 items in the servers list, so the output is 4.

#example2: 
print(f"Active servers: {len(servers)}") 
#output: Active servers: 4    here we have used an f-string to format the output message. The len() function is called inside the curly braces {} to get
###############################################################################
"""
Sorted Function in Python
Purpose: Helps sort items in ascending order by default.
Real-world example:
Useful for arranging numbers from lowest to highest,
sorting student marks, prices, ages, or names alphabetically.
Practical application:
Makes data easier to read, compare, search, and analyze.
The sorted() function creates a new sorted list and does not modify the original list.
"""
sorted_cart = sorted(grocery_cart)
print(sorted_cart) #output: ['bread', 'cereal', 'cheese', 'desserts', 'eggs', 'fruits', 'juice', 'milk', 'snacks', 'veggies'] the sorted function sorts the items in the grocery_cart list in alphabetical order and returns a new sorted list.

#example1: sorting withn numbers 
prices = [500, 200, 1000, 300, 700]

sorted_prices = sorted(prices)
print(sorted_prices)
# output: [200, 300, 500, 700, 1000]
# sorted() arranges the numbers from lowest to highest.

print(prices)
# output: [500, 200, 1000, 300, 700]
# Original list remains unchanged.
##################################################################################
#another example of len and sorted functions
numbers = [5, 2, 9, 1, 5, 6]
print(len(numbers)) #output: 6 the len function counts the number of items in the numbers list, which is 6.
print(sorted(numbers)) #output: [1, 2, 5, 5, 6, 9] the sorted function sorts the items in the numbers list in ascending order and returns a new sorted list.

#example3: final example of len and sorted functions
numbers = [5, 2, 9, 1]
print(len(numbers), sorted(numbers)) #output: 4 [1, 2, 5, 9] the len function counts the number of items in the numbers list, which is 4, and the sorted function sorts the items in the numbers list in ascending order and returns a new sorted list.