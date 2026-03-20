"""
Understanding the del Statement in Python
The del statement is a useful tool in Python for managing lists by removing items at specific positions:

Purpose: Deletes an item from a list by its index position.
Use Case: Helpful when needing to remove items, such as expensive products from a shopping cart.
"""
#example1: del statement
grocery_cart = ["veggies", "fruits", "desserts", "bread", "milk", "eggs", "cheese", "cereal", "juice", "snacks"]
print(grocery_cart) #output: ['veggies', 'fruits', 'desserts', 'bread', 'milk', 'eggs', 'cheese', 'cereal', 'juice', 'snacks'] this is the original grocery_cart list.
print(len(grocery_cart)) #output: 10 the len function counts the number of items in the grocery_cart list, which is 10.
del grocery_cart[3] #this will delete the item at index 3, which is "bread".
print(grocery_cart) #output: ['veggies', 'fruits', 'desserts', 'milk', 'eggs', 'cheese', 'cereal', 'juice', 'snacks'] after using the del statement, the item "bread" has been removed from the grocery_cart list.
#---------------------
# del grocery_cart["milk"] #this will raise a TypeError because the del statement requires an index position, not a value.
#-------------------------
print(len(grocery_cart)) #output: 9 the len function counts the number of items in the grocery_cart list, which is now 9 after deleting "bread".
print(grocery_cart[3]) #output: milk after deleting "bread", the item at index 3 is now "milk".