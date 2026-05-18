"""
#reverse() which is flips the list so the order is rerversed. Last Item becomes first and first becomes last. 
syntax: list_name.reverse()
Note: No return value because it modifies the original list in place and returns None.
No arguments needed because it just reverses the order of the items in the list.

Note: reverse() is not sorting in descending order. it just flips the exsting order.
i) want items in reverse of their current order use reverse() 
ii) want items sorted largest to smallest use sort(reverse=True) or sorted(list_name, reverse=True)
"""
#example1: 
servers = ["web-01", "web-02", "web-03", "db-01", "cache-01"]
servers.reverse()
print(servers) #['cache-01', 'db-01', 'web-03', 'web-02', 'web-01'] the order of the items in the list is reversed

#example2: withy numbers
nums = [3, 1, 4, 1, 5, 9, 2]
nums.reverse()
print(nums) #[2, 9, 5, 1, 4, 1, 3] the order of the items in the list is reversed not sorted. 

#example: sort(reverse=True) now sorts in descending order
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort(reverse=True)
print(nums) #[9, 5, 4, 3, 2, 1, 1] sorted in descending order from largest to smallest

servers = ["a", "b", "c"]
result = servers.reverse()
print(servers) #['c', 'b', 'a'] the order of the items in the list is reversed
print(result) #None because reverse() does not return a new list it modifies the original list in place and returns None.
new_list = servers[::-1] #create a new list that is the reverse of the original list using slicing
print(new_list) #['a', 'b', 'c'] new list is the reverse of the original list but the original list is unchanged
print(servers) #['c', 'b', 'a'] original list is unchanged
"""
[::-1] is a slicing technique that creates a new list that is the reverse of the original list.

Three ways to reverse 
-> list.reverse() methods: modifies the orginal and then returns None best for when you want to flip the list in place
-> reversed(list) method: it does not modify the orginal list and returns an iterator(wrap in list() when you need a new reversed list)
-> list[::-1] slicing technique: does not modify the orginal list and return new list quick one lines very common in python. 
"""

