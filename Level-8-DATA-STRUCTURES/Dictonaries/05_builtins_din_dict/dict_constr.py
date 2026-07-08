#=================================================================
#                   dict()
#=================================================================
#The dict constroctor is a flexibile way to build dict 

#example1: empty dict 
d1 = dict()
d2 = {}
print(d1 == d2) #True botyh are empty dicts

#example2: from key word arguments
person = dict(name="Alice", age=30, city="hyderabad")
print(person)
#{'name': 'Alice', 'age': 30, 'city': 'hyderabad'} 
#simple readble only works when keys are valid varibale names.

#example3: from a list of (key, value) pairs 
pairs = [("name", "alice"), ("age", 30), ("city", "Pune")]
person = dict(pairs)
print(person) #{'name': 'alice', 'age': 30, 'city': 'Pune'}

#example4: from two lists using zip() 
keys = ["name", "age", "city"]
values = ["Alice", 30, "Hyderabad"]

person = dict(zip(keys, values))
print(person) #{'name': 'Alice', 'age': 30, 'city': 'Hyderabad'}

#example5: copy a dict (constructir style)
orginal = {"a": 1, "b": 2}
copy = dict(orginal) #same result as orgional .copy()

copy["c"] = 3
print(orginal) #{'a': 1, 'b': 2}
print(copy) #{'a': 1, 'b': 2, 'c': 3}

#example6: merge dicts (python 3.9+ short cut)
x = {"a": 1, "b": 2}
y = {"b": 99, "c": 3}

merged = {**x, **y} #spread both into a new dict
print(merged) #{'a': 1, 'b': 99, 'c': 3}

#in python 3.9+ also we can do a | b same resulot 