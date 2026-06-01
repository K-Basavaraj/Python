"""
python has a built-in id() function that shows the memory adress of an object.
if two variables have the same id(). they are point to the same object in memory, 
if two variables have different id() they are pointing to different objects in memory.
syntax: id(object)
"""
#example: without copy() function
orginal = [1, 2, 3]
backup = orginal #backup is not a copy of the original list it is a reference to the same list in memory
print(id(orginal)) #140353303644224
print(id(backup)) #140353303644224 same id because both orginal and backup are referencing the same list in memory
#so same list in memory they are not two lists, just two names for one list. 

#example2: with copy() function
orginal = [1, 2, 3]
backup = orginal.copy() #create a new list that is a copy of the original list
print(id(orginal)) #140353303644224
print(id(backup)) #140353303644288 different id because backup is a copy of the original list it is a reference to a different list in memory