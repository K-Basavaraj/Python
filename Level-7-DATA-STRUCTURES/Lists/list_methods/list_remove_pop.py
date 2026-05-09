"""
#remove() removes the first occurrence of a specified value from a list. If the value is not found, it raises a ValueError. The remove() method modifies the original list and does not return any value (it returns None).
#synatx: list.remove(value) Note: you give it a vlaue, not an index. (Thst the differnce from pop() method)


#pop(): removes an item by index(position) and gives that item back you you unlike remove(). you dont lose the item you can use it after removing it.
#synatx: list.pop(index) Note: you give it an index, not a value. (Thst the differnce from remove() method)

-> diff: 
remove() works by value and pop() works by index.
remove() returns None when it removes an item, while pop() returns the removed item.
remove() must pass a value where pop() removes the last item 
remove() gives ValueError if the value is not found, while pop() gives IndexError if the index is out of range.
"""
#######################################################################################################################
#example1: remove
servers = ["web1", "web2", "web3", "db-01"]
servers.remove("web2")
print(servers) #output: ['web1', 'web3', 'db-01'] here we have removed web2 from the servers list using the remove method. The remove method takes the value "web2" as an argument and removes the first occurrence of that value from the list. So now we are left with web1, web3 and db-01 in the list.  

#example2: what if the value are duplicated in the list?
servers = ["web1", "web2", "web3","web2", "db-01"]
servers.remove("web2")
print(servers) #output: ['web1', 'web3', 'web2', 'db-01'] here we have removed the first occurrence of web2 from the servers list using the remove method. to remove all occurrences, need a loop or a list comprehension. 
#######################################################################################################################

#example3: value error if the item does not exist in the list
servers = ["web1", "web2", "web3", "db-01"]
#servers.remove("web4") #this will raise a ValueError because web4 is not in the servers list. The remove method only removes the first occurrence of the specified value, so if the value is not found in the list, it raises a ValueError. To avoid this error, you can check if the value exists in the list before trying to remove it.
if "web4" in servers:
    servers.remove("web4")
else:
    print("web4 is not in the servers list, cannot remove it.") #output: web4 is not in the servers list, cannot remove it. here we have checked if web4 is in the servers list before trying to remove it. Since web4 is not in the list, we print a message saying that it cannot be removed. This way we avoid the ValueError that would have been raised if we had tried to remove web4 without checking for its existence first.

#example4: using try except block to handle the ValueError
servers = ["ec2-01", "ec2-02"]
try:
    servers.remove("ec2-03") #this will raise a ValueError because ec2-03 is not in the servers list.
except ValueError:
    print("ec2-03 is not in the servers list, cannot remove it.") #output: ec2-03 is not in the servers list, cannot remove it. here we have used a try except block to handle the ValueError that would be raised if we tried to remove ec2-03 from the servers list. Since ec2-03 is not in the list, the except block is executed and we print a message saying that it cannot be removed. This way we can handle the error gracefully without crashing the program.
#######################################################################################################################

#example5: POP 
servers = ["web1", "web2", "web3", "db-01"]
removed = servers.pop()
print(removed) #output: db-01 here we have used the pop method to remove the last item from the servers list, which is db-01. The pop method returns the removed item, so we can store it in a variable called removed and print it out. Now we have the value of db-01 stored in the removed variable, and it is no longer in the servers list.
print(servers) #output: ['web1', 'web2', 'web3'] 

#example6: pop froma specific position(index)
servers = ["web1", "web2", "web3", "db-01"]
first = servers.pop(1)
print(first) #output: web2
print(servers) #output: ['web1', 'web3', 'db-01'] here we have used the pop method with an index argument to remove the item at index 1, which is web2. The pop method returns the removed item, so we can store it in a variable called first and print it out. Now we have the value of web2 stored in the first variable, and it is no longer in the servers list. The remaining items in the list are web1, web3 and db-01.

#example7: negative index with pop
servers = ["web1", "web2", "web3", "db-01"]
second_last = servers.pop(-2)
print(second_last) #output: web2 here we have used the pop method with a negative index argument to remove the item at index -2, which is web2. The pop method returns the removed item, so we can store it in a variable called second_last and print it out. Now we have the value of web2 stored in the second_last variable, and it is no longer in the servers list. The remaining items in the list are web1, web3 and db-01.
print(servers) #output: ['web1', 'web3', 'db-01'] here we have used the pop method with a negative index argument to remove the item at index -2, which is web2. The pop method returns the removed item, so we can store it in a variable called second_last and print it out. Now we have the value of web2 stored in the second_last variable, and it is no longer in the servers list. The remaining items in the list are web1, web3 and db-01.

#example: pop() indexerror if the index is out of range
servers = ["web-01"]
try:
    servers.pop(5)  # This will raise an IndexError
except IndexError:
    print("Index is out of range.") #output: Index is out of range. here we have used a try except block to handle the IndexError that would be raised if we tried to pop an item from an index that is out of range. Since index 5 is out of range for the servers list, the except block is executed and we print a message saying that the index is out of range. This way we can handle the error gracefully without crashing the program.