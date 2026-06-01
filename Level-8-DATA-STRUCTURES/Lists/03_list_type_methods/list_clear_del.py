"""
#clear() remove all items from the list, leaving it completely empty. The list itself still exists, but it has no elements in it.
#synatx: list.clear() No arguments, no return value, it just empties the list.

Note: Claer vs Reassignent these two look similar but behave differently. 

#del() destroy the list entirely, removing it from memory. After using del on a list, you cannot access it anymore because it no longer exists.
#synatx: del list_name
"""


#example1: clear
servers = ["web1", "web2", "web3", "db-01"]
servers.clear() #this will remove all items from the servers list, leaving it empty. The clear method does not take any arguments and does not return any value, it simply empties the list.
print(servers) #output: [] here we have printed the servers list after calling the clear method, and it shows that the list is now empty, with no items in it. nut the list itself still exists, so we can add new items to it if we want to.


#example2: del
servers = ["web1", "web2", "web3", "db-01"]
del servers #this will destroy the servers list entirely, removing it from memory. After using del on the servers list, we cannot access it anymore because it no longer exists.
#print(servers) #this will raise a NameError because the servers list has been deleted and no longer exists in memory. The del statement removes the variable servers from the namespace, so trying to access it after deletion will result in a NameError indicating that the name 'servers' is not defined.
try:
    print(servers) #this will raise a NameError because the servers list has been deleted and no longer exists in memory. The del statement removes the variable servers from the namespace, so trying to access it after deletion will result in a NameError indicating that the name 'servers' is not defined.
except NameError:
    print("The servers list has been deleted and cannot be accessed.") #output: The servers list has been deleted and cannot be accessed. here we have used a try except block to handle the NameError that would be raised if we tried to access the servers list after it has been deleted. Since the servers list has been deleted, the except block is executed and we print a message indicating that the list cannot be accessed because it has been deleted. This way we can handle the error gracefully without crashing the program.


#example: clear() vs reassignment
servers = ["web1", "web2", "web3", "db-01"]
servers.clear() #this will clear the servers list, leaving it empty but the list itself still exists in memory.
print(servers) #output: [] here we have printed the servers list after calling the clear

servers = ["web1", "web2", "web3", "db-01"]
servers = [] #this will reassign the servers variable to a new empty list, effectively discarding the original list and creating a new one. The original list still exists in memory until it is garbage collected, but the servers variable now points to a new empty list.
#they look same but if other vcariable point to the same list, clear() affects them too. while reassignment doesnt. 

#example2: clear() vs reassignment 
a = ["x" , "y"]
b = a 
a.clear()
print(a) #[]
print(b) #[]

#with re-assignment
p = ["x" , "y"]
q = p
p = [] #p now points to a new empty list 
print(p) #[]
print(q) #['x', 'y']

##########################################################################
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