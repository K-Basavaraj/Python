cpu_loads = [45, 92, 30, 75, 88]
servers = [
    {"name": "web1", "load": 45},
    {"name": "web2", "load": 92},
    {"name": "web3", "load": 30},
    {"name": "db-01", "load": 75}
]

# How many server are in cpu_loads list?
print(len(cpu_loads)) #output: 5 here we have used the len() function to get the number of items in the cpu_loads list. The len() function takes a list as an argument and returns the number of items in that list. In this case, there are 5 items in the cpu_loads list, so the output is 5.

#is 30 in the cpu_loads list?
print(30 in cpu_loads) #output: True here we have used the in operator to check if the value 30 is present in the cpu_loads list. The in operator returns True if the specified value is found in the list, and False otherwise. In this case, since 30 is indeed present in the cpu_loads list, the output is True.    

#what is highest cpu load?
max_load = max(cpu_loads)
print(max_load) #output: 92 here we have used the max() function to find

#what is the average cpu load?
average_load = sum(cpu_loads) / len(cpu_loads)
print(f"Average CPU Load: {average_load}") #output: Average CPU Load: 66.0 here we have calculated the average CPU load by using the sum() function to get the total of all the CPU loads and then dividing that total by the number of CPU loads, which we get using the len() function. The result is the average CPU load, which is 66.0 in this case.

#which server has the lowest cpu? (whole dictionary)
least_loaded = min(servers, key=lambda x: x["load"])
print(least_loaded) #output: {'name': 'web3', 'load': 30} here we have used the min() function with the key argument to find the server with the lowest CPU load. The key argument takes a function (in this case, a lambda function) that specifies how to compare the items in the iterable. The lambda function takes an item (a dictionary representing a server) and returns the value of the "load" key for that item. The min() function then uses these values to determine which server has the lowest load. In this case, the server with the lowest load is "web3" with a load of 30, so the output is {'name': 'web3', 'load': 30}.

#is any server above 90% cpu load?
any_above_90 = any(server["load"] > 90 for server in servers)
print(any_above_90) #output: True here we have used the any() function