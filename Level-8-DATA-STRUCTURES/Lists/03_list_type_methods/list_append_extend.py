"""
Append:
Adds an item to the end of a list.
Example: Adding "grape" to a list of fruits.

Note: the append method only takes one argument, if you are trying to pass three arguments or more get TypeError. 
To fix this, we can use the extend method instead of append, which allows us to add multiple items to the list at once.


# extend() add multiple items to the end of a list by taking them from another iterable(another list, tuple, set, etc.) and adding them to the end of the list.
extend() works with any iterable, not just lists. You can extend a list with items from a tuple, set, or even a string. When you extend a list with a string, each character in the string is added as a separate item to the list.
it modifies the original list and does not return a new list. The extend method does not return any value (it returns None), it simply modifies the original list in place.
"""
#################################################################################################################
#example1: append
fruits = ["apple", "banana", "cherry"]
fruits.append("grapefruit")
print(fruits) #output: ['apple', 'banana', 'cherry', 'grapefruit'] here banana is at index 1, so when we insert orange at index 1, it will be placed before banana and the rest of the items will be shifted to the right.

#example2: append
deployment_apps = []
#deployment_apps.append("nginx", "redis", "postgres") #this will raise a TypeError because the append method only takes one argument, but we are trying to pass three arguments. To fix this, we can use the extend method instead of append, which allows us to add multiple items to the list at once.
deployment_apps.append("nginx") 
deployment_apps.append("redis")
deployment_apps.append("postgres")
deployment_apps.append("redditmq")
print(deployment_apps) #output: ['nginx', 'redis', 'postgres', 'redditmq'] this is the list of deployment apps that we have added to the list using the append method. Each app is added as a separate item in the list.

#################################################################################################################
#example3: extend
prod_servers = ["web1", "web2", "web3"]
new_servers = ["web4", "web5", "web6"]
prod_servers.extend(new_servers)
print(prod_servers) #output: ['web1', 'web2', 'web3', 'web4', 'web5', 'web6'] here we have extended the prod_servers list with the new_servers list, which means that all the items in the new_servers list have been added to the end of the prod_servers list.            

#example4: extend with a tuple 
servers = ["web1"]
servers.extend(("db-01", "cache-01"))
print(servers) #output: ['web1', 'db-01', 'cache-01'] here we have extended the servers list with a tuple containing db-01 and cache-01. The extend method takes each item in the tuple and adds it as a separate item to the servers list.

#example5: extend with a string
letters = ["a", "b", "c"]
letters.extend("def")
print(letters) #output: ['a', 'b', 'c', 'd', 'e', 'f'] here we have extended the letters list with a string "def". The extend method takes each character in the string and adds it as a separate item to the letters list. So we end up with a list of individual characters instead of a single string item.  
