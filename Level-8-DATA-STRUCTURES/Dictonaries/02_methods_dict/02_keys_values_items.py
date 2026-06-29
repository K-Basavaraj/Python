"""
a dict has 3 things to look at: 
-> .keys() 
-> .values()
-> .items()

All three return "View" objects - like a live windows into the dict. they auto-update if the dict chnages. 

To use them as a list, wrap with list(..): list(d.keys())

- .keys() use to see/checks all keys
- .values() - use to check existence, sum min/max
-.items() -> use in loops with tuple unpacking (most common)
- wrap in list() if you need indexing or slicing 
- for k, v in d.items() is teh standad dict-walking pattern 
"""
#example1: .keys()
person ={
    "name": "Alice",
    "age": 30,
    "city": "Hyderabad"
}

print(person.keys()) #dict_keys(['name', 'age', 'city'])

#convert to list if you need indexing or slicing 
print(list(person.keys())) #['name', 'age', 'city']

#example3: loop through Keys
for key in person.keys():
    print(key)
"""
name
age
city

shortcut: looping a dict also gives keys. 
for key in person: same thing as for key in person.keys()
"""
#======================================================
#               .values()
#======================================================
#example3: Get all values 
person = {"name": "Alice", "age": 30, "city": "Banglore"}

print(person.values()) #dict_values(['Alice', 30, 'Banglore'])

print(list(person.values())) #['Alice', 30, 'Banglore']

#Loop through values 
prices = {
    "apple": 50,
    "banana": 30,
    "cherry": 80
}
for price in prices.values():
    print(price)
"""
50
30
80
"""
#check if a value exists 
print("apple" in prices.values()) #False
print(50 in prices.values()) #True
#======================================================
#               .items()
#======================================================
student = {
    "name": "Ajay",
    "age": 18,
    "city": "Pune"
}

print(student.items()) #dict_items([('name', 'Ajay'), ('age', 18), ('city', 'Pune')])
print(list(student.items())) #[('name', 'Ajay'), ('age', 18), ('city', 'Pune')]

#Loop through items 
for key, value in student.items():
    print(f"{key} = {value}")
"""
name = Ajay
age = 18
city = Pune
"""

#example8: check if key value pair exists 
prices = {
    "apple": 80,
    "banana": 50
}

print(("apple", 50) in prices.items()) #False 
print(("apple", 80) in prices.items()) #True