"""
There are 4 common ways to loop through a dict in python.

1. for key in dict  -> loops over keys (default)
2. for key in dict.keys() -> loops over keys (explicit)
3. for value in dict.values() -> loops over values
4. for key, value in dict.items() -> loops over key-value pairs(best for most cases)

the .items() version is the most common and recommended way to loop through a dict, as it gives 
you both the key and value in each iteration.

Key-takeways: 
----------
- Looping a dict dircetly gives you the keys 
- use .values() when you only care about values 
- use .items() to get both key value pairs 
- tuple unpcaking makes .items() clean for k, v in d.items() 
- combine with enumarate() for numberd output
- never modify a dict while looping - loop over list(d) insted
"""

#example1: looping a dict directly gives you the keys 
person = {"name": "John", "age": 30, "city": "New York"}

for key in person: 
    print(key)  # Output: name, age, city (each on a new line)
#Note: By default, "for x in dict" loops over the keys of the dict, you dont need to write .keys() explicitly.
#------------------------------------------------------------------------------------------------

#example2: same result with .keys() method (explicitly looping over keys)

for key in person.keys():
    print(key)  # Output: name, age, city (each on a new line)
#------------------------------------------------------------------------------------------------
#example3: looping through values only 
prices = {"apple": 0.5, "banana": 0.3, "orange": 0.7}

for price in prices.values():
    print(price)  # Output: 0.5, 0.3, 0.7 (each on a new line)

#use .values() when you only care about the values and not the keys.
#------------------------------------------------------------------------------------------------
#example4:  sum, min, max of values in a dict

cpu_usage = {"server1": 75, "server2": 60, "server3": 90}

#you can just use sum(cpu_usage.values()) to get the total CPU usage across all servers (better)
#But you could also do it manually with a loop like this:

total_usage = 0
for usage in cpu_usage.values():
    total_usage += usage
print(total_usage)  # Output: 225
#------------------------------------------------------------------------------------------------
#example5: loop throgh key value pairs with .items() (most common and recommended way)
person = {"name": "John", "age": 30, "city": "New York"}

for key, value in person.items(): 
    print(f"{key} = {value}")

"""
output: 
name = John
age = 30
city = New York

The most common way to walk a dict in real code the tuple (key, value) unpacks right in the loop. 
"""

#------------------------------------------------------------------------------------------------
# Example6: filter dict while looping with .items()
servers = {"server1": "active", "server2": "inactive", "server3": "active"}

for name, status in servers.items():
    if status == "active":
        print(f"{name} is active")

"""
output: 
server1 is active
server3 is active
"""
#------------------------------------------------------------------------------------------------
#example7: build a filtered dict 
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

#get only the students who passed 
passing = {}
for name, score in scores.items():
    if score >= 80:
        passing[name] = score

print(passing)  # Output: {'Alice': 85, 'Bob': 92, 'David': 90}
#------------------------------------------------------------------------------------------------

#example8: dont modify a dict while looping through it. 
d = {"a": 1, "b": 2, "c": 3}

# for key in d: 
#     del d[key]
#RuntimeError: dictionary changed size during iteration

#to modify the looping -> loop over a copy of the keys 
for key in list(d.keys()):
   del d[key]
print(d) #{}