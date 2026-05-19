#max() function is used to find the largest item in an iterable or the largest of two or more arguments. It can be used with various data types, including numbers, strings, and lists.

#example1:
cpu_loads  = [45, 92, 30, 75, 88]
max_load = max(cpu_loads)
print(max_load) #output: 92 here we have used the max() function to find the largest item in the cpu_loads list. The max() function takes an iterable (in this case, a list) as an argument and returns the largest item in that iterable. In this case, the largest item in the cpu_loads list is 92, so the output is 92.

#example2: with key just like sort(key=..)
servers = [
    {"name": "web1", "load": 45},
    {"name": "web2", "load": 92},
    {"name": "web3", "load": 30},
    {"name": "db-01", "load": 75}
]
#find the server with the highest cpu
most_loaded = max(servers, key=lambda x: x["load"])
print(most_loaded) #output: {'name': 'web2', 'load': 92} here we have used the max() function with the key argument to find the server with the highest CPU load. The key argument takes a function (in this case, a lambda function) that specifies how to compare the items in the iterable. The lambda function takes an item (a dictionary representing a server) and returns the value of the "load" key for that item. The max() function then uses these values to determine which server has the highest load. In this case, the server with the highest load is "web2" with a load of 92, so the output is {'name': 'web2', 'load': 92}.

#example3: max with default value
empty_list = []
max_value = max(empty_list, default=0)
print(max_value) #output: 0 here we have used the max() function with the default argument to handle the case where the input list is empty. The default argument specifies a value to return if the iterable is empty. In this case, since empty_list is empty, the max() function returns the default value of 0 instead of raising a ValueError. This way we can avoid errors when working with empty iterables.