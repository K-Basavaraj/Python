"""
Index:
Locates the index of a specific item within a list.
Example: Finding the index of "banana" after new additions to the list.
syntax: list_name.index(value) or list_name.index(value, start, stop) occasionally useful when you want to find the next occrence after a known postion.


Note: if the value appears multiple times, index() only tells you about the first one.
index() can take optional start and stop arguments to search only part of the list: 
"""
#EXAMPLE1: index
fruits = ["apple", "banana", "cherry"]
index_of_banana = fruits.index("banana")
print(index_of_banana) #output: 1  

#example2: 
logs = ["INFO", "ERROR", "INFO", "ERROR"]
print(logs.index("ERROR"))

#example3: 
servers = ["web01", "web02"]

if "web-99" in servers: 
    pos = servers.index("web-99")
    print(f"Found at index {pos}")
else: 
    print("not in the list")

#try:
#     pos = servers.index("web-99")
#     print(f"Found at index {pos}")
# except ValueError:
#      print("not in the list")

#example4: 
servers = ["web01", "web02", "web-01", "db-01"]
pos = servers.index("web-01", 1)
print(pos) #2 why beacuse we told it to skip index 0 and start looking from index 1.

"""
its used less often than the other methods, because most of the time when working with lists we already know the index because we are looping or we dont care about the position.
-> you need to modify the list relative to a known item(insert after x, delete before x)
-> you want to check where something is for looging/reporting 
-> you rworkiking with orderd sequences like queues or steps. 
"""