"""
Insert:
Places an item at a specific position (index) in the list, insted of just at the end of the list like append. 
This is useful for organizing items in a specific order, such as placing "orange" at index 1 in the fruits list.
Useful for organizing items, e.g., placing "orange" at index 1 in the fruits list.

list_name.insert(index, item)
index: where you want to put the item. 
item: what you want to insert.
"""
#example1: insert
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits) 
#output: ['apple', 'orange', 'banana', 'cherry', 'grapefruit'] now the banana is at index 2, cherry is at index 3 and grapefruit is at index 4.

#example2: 
servers = ["web1", "web2", "web3"]
servers.insert(0, "db-01")
print(servers)
#output: ['db-01', 'web1', 'web2', 'web3'] here we have inserted db-01 at index 0, which means that it is now the first item in the list. The rest of the items have been shifted to the right to make room for the new item. So web1 is now at index 1, web2 is at index 2 and web3 is at index 3.

#######################################################################################################################

#example3: what if the index is bigger than the list? 
#Note: python doesnt crash it just adds the item at the end of the list.

isinstance = ["web1", "web2", "web3"]
isinstance.insert(99, "db-01")
print(isinstance)
#output: ['web1', 'web2', 'web3', 'db-01'] here we have inserted db-01 at index 99, which is bigger than the length of the list. Python does not crash, it just adds the item at the end of the list like append. So db-01 is now the last item in the list.

#example4: what if the index is negative?
servers = ["web1", "web2", "web3"]
servers.insert(-1, "cache-01")
print(servers)
#output: ['web1', 'web2', 'cache-01', 'web3'] here we have inserted cache-01 at index -1, which means that it is now the second to last item in the list. The rest of the items have been shifted to the right to make room for the new item. So web1 is still at index 0, web2 is still at index 1, cache-01 is now at index 2 and web3 is now at index 3. 