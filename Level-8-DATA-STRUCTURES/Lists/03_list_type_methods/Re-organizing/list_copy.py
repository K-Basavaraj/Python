"""
copy() which creates a new list thats a duplicate of the orginal. 
The two lists are independent chnaging one doesn't affect the other.
syntax: new_list = original_list.copy()
Note: copy() creates a shallow copy of the list. If the list contains mutable objects like other lists, 
the inner objects are not copied but referenced. So changes to mutable objects in one list will affect the other list.
"""
#example: 
orginal = ["web-01", "web-02", "web-03"]
backup = orginal.copy() #create a new list that is a copy of the original list
print(orginal) #['web-01', 'web-02', 'web-03']
backup.append("db-01") #add a new item to the backup list
print(backup) #['web-01', 'web-02', 'web-03', 'db-01'] backup list is modified
print(orginal) #['web-01', 'web-02', 'web-03'] original list is unchanged because backup is a copy of the original list not a reference to the original list

#Assignment is not a copy! it creates a new reference to the same list. So changes to one list will affect the other list because they are both referencing the same list in memory.
orginal = ["web-01", "web-02", "web-03"]
backup = orginal #backup is not a copy of the original list it is a reference to the same list in memory
backup.append("db-01") #add a new item to the backup list
print(orginal) #['web-01', 'web-02', 'web-03', 'db-01'] original list is modified because backup is a reference to the same list in memory
print(backup) #['web-01', 'web-02', 'web-03', 'db-01'] backup list is modified because it is a reference to the same list in memory

"""
Why this happens? 
in python varibales dont hold lists they hold references to lists.
When you do backup = orginal, you are not creating a new list you are creating a new reference to the same list in memory.
So both orginal and backup are referencing the same list in memory. When you modify the list through either reference, 
you are modifying the same list in memory, which is why both orginal and backup show the change.

when you do backup = orginal.copy(), you are creating a new list that is a copy of the original list. 
So backup is a reference to a new list in memory that has the same items as the original list
"""

#example3: 
orginal = [["web-01", "web-02"], ["db-01", "db-02"]]
backup = orginal.copy() #create a new list that is a copy of the original list
backup[0].append("web-03") #add a new item to the first inner list in the backup list
print(backup) #[['web-01', 'web-02', 'web-03'], ['db-01', 'db-02']] backup list is modified
print(orginal) #[['web-01', 'web-02', 'web-03'], ['db-01', 'db-02']] original list is also modified because copy() creates a shallow copy of the list. The inner lists are not copied but referenced. So changes to the inner lists in one list will affect the other list because they are both referencing the same inner lists in memory.

#ways to copy a list(ALL equavlent for simple lists)
orginal = ["web-01", "web-02", "web-03"]

#way1: using copy() method
backup1 = orginal.copy()

#way2: using list() constructor
backup2 = list(orginal)

#way3: using slicing
backup3 = orginal[:] #create a new list that is a copy of the original list using slicing

#way4 using list comprehension 
backup4 = [ item for item in orginal] #create a new list that is a copy of the original list using list comprehension

#example4: 
import copy

servers = [ ["web-01", "running"], ["db-01", "running"] ]
index_servers = [servers.index(item) for item in servers]
print(index_servers) #[0, 1] index() method returns the index of the first occurrence of each item in the list

backup = copy.deepcopy(servers) #create a deep copy of the servers list using copy.deepcopy() to ensure that all nested objects are also copied
backup[0][1] = "stopped" #modify the status of the first server in the backup list
print(backup) #[['web-01', 'stopped'], ['db-01', 'running']] backup list is modified
print(servers) #[['web-01', 'running'], ['db-01', 'running']] original list is unchanged because we used copy.deepcopy() to create a deep copy of the original list, so all nested objects are also copied and changes to the backup list do not affect the original list.