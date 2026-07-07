"""
#Two very different tools for building/modifying dicts:

.update(other) -> merge another dict into this one 
.fromkeys(iter) -> Build a new dict from a list of keys(all sharing the same value)

Key_takeaways:
-> .update() merge another dict into this one, overwriting existing keys if they exist.
    -> new keys are added, existing keys are updated with new values
    -> can also be used with keyword arguments to add/update keys
-> python 3.9+ has a new syntax for merging dicts using the | operator (creates a new dict) and |= operator (inplace merge)
-> .fromkeys() creates a new dict from a list of keys, all sharing the same value (default is None)
    -> be careful with mutable defaults (like lists or dicts) as they will be shared across all keys
    -> use a dict comprehension to create unique mutable values for each key if needed
"""

#example: .update() 
#=============================================================================================
#example1: merge another dict IN 
person = {"name": "John", "age": 30}
other = {"city": "New York", "country": "USA"}
person.update(other)

print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
#=============================================================================================
#example2: overwriting exiting keys 
person = {"name": "John", "age": 30}
other = {"age": 35, "city": "New York"}
person.update(other)
print(person)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}
#=============================================================================================
#example3: using .update() with keyword arguments
person = {"name": "John", "age": 30}
person.update(name="Jane", city="New York")
print(person)  # Output: {'name': 'Jane', 'age': 30, 'city': 'New York'}
#=============================================================================================
#example4: modern python 3.9+ syntax for merging dicts
a = {"x": 1, "y": 2}
b = {"y": 3, "z": 4}

merged = a | b #create a new dict with the merged values
print(merged)  # Output: {'x': 1, 'y': 3, 'z': 4}   

#Inplace version of the above is:
a |= b  #merge b into a
print(a)  # Output: {'x': 1, 'y': 3, 'z': 4}
#===============================================================================================
                        #.fromkeys()
#example1: build a dict with all same values Give it a list of keys + one shared value 
result = dict.fromkeys(["a", "b", "c"], 0)
print(result)  # Output: {'a': 0, 'b': 0, 'c': 0} #all three kets get the same value {0}
#===============================================================================================
#example2: default value if not specified 
result = dict.fromkeys(["x", "y", "z"])
print(result)  # Output: {'x': None, 'y': None, 'z': None} #default value is None
#===============================================================================================
#example: NOte: dont use mutable defaults (like lists[] or dicts) with .fromkeys()
data = dict.fromkeys(["a", "b", "c"], [])  #all keys share the same list object
data["a"].append(1)  #modifying the list for key "a"
print(data)  # Output: {'a': [1], 'b': [1], 'c': [1]} #all keys share the same list object, so all are modified

#bcz .fromkeys() shares one defult value across all keys. for mutable defaults, use a dict comprehension instead:
data = {key:[] for key in ["a", "b", "c"]}  #each key gets its own list object
data["a"].append(1)  #modifying the list for key "a"
print(data)  # Output: {'a': [1], 'b': [], 'c': []} #only key "a" is modified
#===============================================================================================
