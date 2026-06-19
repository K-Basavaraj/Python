"""
zip() pairs up items from 2 or more iterable, position by position. 
like a real -world zipper brining two sides toigether 

syntax: 
 for x, y in zip(tup1, tup2): 
 for x, y, z in zip(tup1, tup2, tup3): 
"""

#example1: old way 
names = ("Alice", "Bob", "Charle")
ages = (30, 40, 25)

for i in range(len(names)):
    print(names[i], ages[i])
"""
Alice 30
Bob 40
Charle 25
"""

#example2: the clean way 
for name, age in zip(names, ages): 
    print(name, age)
"""
Alice 30
Bob 40
Charle 25
"""

#example4: zip 3 or more 
names =("Rajesh", "Ramesh", "Prabhs")
ages = (30, 25, 35)
cities = ("Mumabi", "delhi", "rebal city")

for name, age, city in zip(names, ages, cities): 
    print(f"{name}, {age}, from {city}")

"""
Rajesh, 30, from Mumabi
Ramesh, 25, from delhi
Prabhs, 35, from rebal city
"""

#NOTE: ALWAYS MASKE SURE YOUR TUPLES ARE THE SAME LENGTH OR EXPLICTLY CHECK WITH LENG() BEFORE ZIPPING 

#EXAMPLE: ENUMERATE AND ZIP 
names = ("Alice", "Bob", "Charle")
roles = ("Admin", "Editor", "Viewer")

for i, (name, role) in enumerate(zip(names, roles), start=1): 
    print(f"{i}, {name} ({role})")
"""
1, Alice (Admin)
2, Bob (Editor)
3, Charle (Viewer)

Note the paramns around (name,role) needed bcz zip gives us a tupel and we need to unpack it within enumartes
"""