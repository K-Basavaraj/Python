#min() function is used to find the smallest item in an iterable or the smallest of two or more arguments. It can be used with various data types, including numbers, strings, and lists.
#example1: 
cpu_loads  = [45, 92, 30, 75, 88]
min_load = min(cpu_loads)
print(min_load) #output: 30 here we have used the min() function to find the smallest item in the cpu_loads list. The min() function takes an iterable (in this case, a list) as an argument and returns the smallest item in that iterable. In this case, the smallest item in the cpu_loads list is 30, so the output is 30.

#example2: 
servers = ["web1", "web2", "web3", "db-01"]
min_server = min(servers)
print(min_server) #output: db-01 here we have used the min() function to find the smallest item in the servers list. The min() function can also be used with strings, and it compares the strings based on their lexicographical order (similar to alphabetical order). In this case, "db-01" comes before "web1", "web2", and "web3" in lexicographical order, so the output is "db-01".

#example3: min() with key just like sort(key=..)
servers = [
    {"name": "web1", "load": 45},
    {"name": "web2", "load": 92},
    {"name": "web3", "load": 30},
    {"name": "db-01", "load": 75}
]
#find the server with the lowest cpu 
least_loaded = min(servers, key=lambda x: x["load"])
print(least_loaded) #output: {'name': 'web3', 'load': 30} 
"""
here we have used the min() function with the key argument to find the server with the lowest CPU load. 
The key argument takes a function (in this case, a lambda function) that specifies how to compare the items in the iterable.
The lambda function takes an item (a dictionary representing a server) and returns the value of the "load" key for that item.
The min() function then uses these values to determine which server has the lowest load. 
In this case, the server with the lowest load is "web3" with a load of 30, so the output is {'name': 'web3', 'load': 30}.
"""

#min with default value
empty_list = []
min_value = min(empty_list, default=0)
print(min_value) #output: 0 here we have used the min() function with the default argument to handle the case where the input list is empty. The default argument specifies a value to return if the iterable is empty. In this case, since empty_list is empty, the min() function returns the default value of 0 instead of raising a ValueError. This way we can avoid errors when working with empty iterables.