"""
overview: 
4 methods either remove or copy dict content 

.pop(key) -> remove one key by name, returns its value. 
.popitem() -> remove the last inserted (key, value) pair, returns it as a tuple.
.clear() -> remove everything (empty the dict)
.copy() -> make an independent copy of the dict (duplicate)

Quick Reference:
methods              what it removes                    returns                   safe? 
------------------------------------------------------------------------------------
.pop(key)            one key by name                    value of the key           yes(needs key to exist, or providedefault)
.pop(key, value)     one key by name                    value of the key           yes(providing default avoids KeyError)
.popitem()          last inserted (key, value)          (key, value) tuple          yes(only if dict is not empty)
.clear()            everything                          None                        yes
.copy()            nothing removed, just makes a copy   new dict                     yes
"""
#================================================================================================
#                                   .pop()
#================================================================================================
#example1: remove a key + return its value 
person = {"name": "John", "age": 30, "city": "New York"}
age = person.pop("age")
print(person)  # Output: {'name': 'John', 'city': 'New York'}
#unlike del, .pop() gives you the value of the removed key, so you can use it if needed
print(age)  # Output: 30    
#------------------------------------------------------------------------------------------------
#example2: missing key crashes 
#person.pop("email")  # KeyError: 'email' #if the key is not found, it raises a KeyError
#------------------------------------------------------------------------------------------------
#example3: missing key with default value
email = person.pop("email", "not found")  #if the key is not found, it returns the default value instead of raising an error
print(email)  # Output: not found
#------------------------------------------------------------------------------------------------

#================================================================================================
#                                   .popitem()
#================================================================================================
#example1: remove the last insted pair (key, value) and return it as a tuple
person = {"name": "John", "age": 30, "city": "New York"}
last_item = person.popitem()
print(person)  # Output: {'name': 'John', 'age': 30}
print(last_item)  # Output: ('city', 'New York') #returns the last inserted (key, value) pair as a tuple
#Note: .popitme() always removes from the end most recently added its usefull for LIFO (last in first out) scenarios, like undo functionality
#------------------------------------------------------------------------------------------------
#example2: empty dict crashes
#empty_dict = {}
#empty_dict.popitem()  # KeyError: 'popitem(): dictionary is empty' #if the dict is empty, it raises a KeyError
#------------------------------------------------------------------------------------------------
#================================================================================================
#                                   .clear()
#================================================================================================
#example1: empty the whole dict (keeps the varible alive)
person = {"name": "Alice", "age": 30}

person.clear()
print(person)  # Output: {} #the dict is now empty, but the variable still exists
#differen from del person which deletes the varible entirely, .clear() just empties the dict but keeps the variable alive
#------------------------------------------------------------------------------------------------
#================================================================================================
#                                   .copy()
#================================================================================================
#example1: make an independent copy of the dict
person = {"name": "Alice", "age": 30}
backup = person.copy()  #make a copy of the dict
print(backup)  # Output: {'name': 'Alice', 'age': 30}

backup["age"] = 31  #modify the copy
print(person)  # Output: {'name': 'Alice', 'age': 30} #original dict is unchanged
print(backup)  # Output: {'name': 'Alice', 'age': 31} #copy is modified independently
#------------------------------------------------------------------------------------------------
#exmple2: Common  mistake this creates two names pointing to the same dict, so changes to one affect the other
person = {"name": "Alice", "age": 30}
not_a_copy = person  #this is not a copy, just another reference to the same dict
not_a_copy["age"] = 31  #modify the "copy"
print(person)  # Output: {'name': 'Alice', 'age': 31} #original dict is changed too
print(not_a_copy)  # Output: {'name': 'Alice', 'age': 31} #the "copy" is actually the same dict

#Note: to truly copy use .copy() or the copy module for deep copies if needed.
#-------------------------------------------------------------------------------------------------
#example3: .copy() is shallow copy, so nested mutable objects are still shared between the original and the copy
data = {
    "name": "Alice",
    "age": 30,
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

backup = data.copy()  #shallow copy
print(backup)  # Output: {'name': 'Alice', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}}

#change a top level key in the copy
backup["age"] = 31
print(data["age"])  # Output: 30 #original dict is unchanged

#change a nested key 
backup["address"]["city"] = "Los Angeles"
print(data["address"]["city"])  # Output: Los Angeles #original dict is changed because the nested dict is shared

#for deeply nested mutable objects, use the copy module's deepcopy() to create a true independent copy
#example4: using the copy module for deep copies
import copy
safe_backup = copy.deepcopy(data)  #deep copy
safe_backup["address"]["city"] = "Chicago"
print(data["address"]["city"])  # Output: Los Angeles #original dict is unchanged
