"""
1. What is DICTIONARY? 
A Dictionary stores KEY -> Value pairs.
- The key is how we look something up
- The value is what you store

syntax:
  my_dict = {
     key: value,
     key: value, ...
  }

==> KEY-RULES:
-----------
*WHAT CAN BE A DICTIONARY 'KEY' which means key must be immutable
-> allowed(immutable types)
strings, numbers, booleans,  and Tuples

*WHAT CAN NOT BE A DICTIONARY 'KEY'
->not allowed (mutable types): 
lists, dicts, sets which gives TypeError

NOTE: KEY MUST BE HASHABLE(stable idenenity)
Values can be anything
KEY must be UNIQUE -> If we use same key twoce, the second value replaces the first. 
its like overright the previous value. 
DICT can never have two entries with the same key.
"""
#example1: 
person = {
    "name": "Basava",
    "age": 30, 
    "city": "Hyderabad"
}
print(person)  #output: {'name': 'Basava', 'age': 30, 'city': 'Hyderabad'}
print(type(person)) #output: <class 'dict'>


#example2: Empty dictionary
empty1 = {}
empty2 = dict() #using the dict() constructor

print(empty1) #o/p: {} creates an empty DICT not an empty set 
print(empty2) #o/p: {}
print(type(empty1)) # o/p: <class 'dict'>

#example3: using the dict() constructor with keyword arguments 
person = dict(name="Basava", age=30, city="Pune")
print(person) #o/p: {'name': 'Basava', 'age': 30, 'city': 'Pune'}

#example4: using dict() with a list of tuple (Each inner tuple becomes a key-value pair )
student = dict([
    ("name", "Basava"),
    ("age", 30),
    ("city", "Hyderabad"),
])
print(student) #o/p: {'name': 'Basava', 'age': 30, 'city': 'Hyderabad'} 
#it is usedful when we already have data as a list of pairs

#example5: mixed data-types - Keys AND Values can be any immutable type. 
mixed = {
    "name": "Prabhas",
    "age": 38,
    "is_actor": True,
    "Height": 6.0, 
    "movies": ["Bahubali", "Sahoo", "Salaar"], #str -> list (a list as value is ok)
    101: "actor-id", #int -> str (yes, int can be a key)
}
print(mixed)
print(mixed["name"])
print(mixed[101])

"""
output: 
{'name': 'Prabhas', 'age': 38, 'is_actor': True, 'Height': 6.0, 'movies': ['Bahubali', 'Sahoo', 'Salaar'], 101: 'actor-id'}
Prabhas
actor-id
"""

#exsmple6: Nested dict (dict inside dict)
#This most useful in devo9sp work - api responses, config-file, json data are usually nested dicts.

employee = {
    "name": "Karna",
    "role": "DevOps Engineer",
    "address": {
        "city": "Delhi",
        "Country": "India",
        "pincode": "50001"
    },
}
print(employee)
#access mested values with multiple keys 

print(employee["address"])
print(employee["address"]["city"])
print(employee["address"]["pincode"])
"""
output: 
{'name': 'Karna', 'role': 'DevOps Engineer', 'address': {'city': 'Delhi', 'Country': 'India', 'pincode': '50001'}}
{'city': 'Delhi', 'Country': 'India', 'pincode': '50001'}
Delhi
50001
"""

#EXAPLE7: from two parallel lists (using zip + dict)
#it is usefull when keys and values comes from separate sources.
keys = ["name", "age", "city"]
values = ["Alice", 30, "Chenai"]

person = dict(zip(keys, values))
print(person) #o/p: {'name': 'Alice', 'age': 30, 'city': 'Chenai'}
#zip() pairs them up -> dict() turns the pairs into a dict.i its usefull for parsing CSV data. 

data=dict(zip(["a","b"], [1,2]))
print(data) #{'a': 1, 'b': 2}


#example8: Dict comprehnsion(Advnacved)
#Like a list Comprehension, but build a dict.
squares = {n: n * n for n in range(1,6)}
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}