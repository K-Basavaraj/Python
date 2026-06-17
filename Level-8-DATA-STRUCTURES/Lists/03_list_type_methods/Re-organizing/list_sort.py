"""
#sort() function re-arragnes the list in place, so items are in order(ascending by defult)
syntax: list_name.sort()
list_name.sort(reverse=True) #descending order and false for ascending order
list_name.sort(key=function) #custom sorting based on the return value of the function
list_name.sort(key=some_function, reverse=True) #custom sorting in descending order.
example of some_function: len, str.lower, lambda x: x[1] (sort by second character)
key ->  a function that tells python how to compare items. 

Note: sort() method does not return a new list it modifies the original list in place and returns None.
see example4 for how to sort a list without modifying the original list.

#sorted() function returns a new sorted list without modifying the original list.
syntax: sorted(list_name)
"""
#example1: with numbers
ports = [8080, 80, 443, 3306]
ports.sort()
print(ports) #[80, 443, 8080, 3306] sort ascending order smallest to largest

#example2: descending order reverse=True
ports = [8080, 80, 443, 3306]
ports.sort(reverse=True)
print(ports) #[8080, 3306, 443, 80] sort descending order largest to smallest

#example3: with strings
servers = ["web-02", "web-01", "web-03", "db-01", "cache-01"]
servers.sort()
print(servers) #['cache-01', 'db-01', 'web-01', 'web-02', 'web-03'] sort ascending order alphabetically(technically by unicode/ascii values)

#example4: sort a list without modifying the original list using sorted() function
ports = [443, 22, 8080]
result = ports.sort() #sort() returns None because it modifies the original list in place
print(ports) #[22, 443, 8080] original list is modified
print(result) #None because sort() does not return a new list

#example5: if you want a new sorted list without modifying the original list use sorted() function
ports = [443, 22, 8080]
sorted_ports = sorted(ports) #sorted() returns a new sorted list
print(ports) #[443, 22, 8080] original list is unchanged
print(sorted_ports) #[22, 443, 8080] new sorted list

# #example6: mixing types crashes you can only sort items that can be compared to each other/ only sort items of the same type
# mixed_list = [1, "two", 3]
# mixed_list.sort() #TypeError: '<' not supported between instances of 'str' and 'int'

#example7: to avoid crashing with mixed types we go with Soriting with "key", The key argument lets you tell python how to sort each item.
#example with sort string by length
servers = ["web-02", "web-01", "db", "cache-server-01"]
servers.sort(key=len) #sort by length of the string "use the length of each string as the sort the value"
print(servers) #output: ['db', 'web-02', 'web-01', 'cache-server-01']

items = ["banana", "Apple", "cherry"]
items.sort() #['Apple', 'banana', 'cherry'] default sort is case-sensitive so uppercase letters come before lowercase letters
print(items)
items.sort(key=str.lower) #['Apple', 'banana', 'cherry'] sort case-insensitive by converting each string to lowercase for comparison
print(items) #['Apple', 'banana', 'cherry'] sort case-insensitive by converting each string to lowercase for comparison

#example8: sort a list of dictionaries by a specific key using lambda function as the key
servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 30},
    {"name": "db-01", "cpu": 80}
]

#regular function to get cpu usage
# def get_cpu(server):
#     return server["cpu"]

# for s in servers:
#     print(get_cpu(s)) #45, 30, 80

#lambda function to get cpu usage
servers.sort(key=lambda s: s["cpu"]) #sort the list of dictionaries by the value of the "cpu" key using a lambda function as the key
for s in servers:
    print(s)
#print(servers) #[{'name': 'web-02', 'cpu': 30}, {'name': 'web-01', 'cpu': 45}, {'name': 'db-01', 'cpu': 80}] sorted in ascending order by cpu usage