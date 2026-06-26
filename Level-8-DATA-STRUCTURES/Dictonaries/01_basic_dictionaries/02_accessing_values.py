"""
Two ways to access values 

1. dict[key] -> fast, but crashes if key doesnt exist
2. dict.get(key) -> safe, returns None if key doesnt exist 

\\quick-reference- acces spaterns 
d[key] -> fast, crashes if mssing 
d.get(key) -> return None if missing 
d,get(key, deafult) -> returns default is mssing 
d.get("a", {}).get("b") -> safe 

"""

#example1: way 1 basic access with []
employee = {
    "name": "Raj",
    "age" :28, 
    "city": "Mumbai",
}

print(employee["name"]) #Raj
print(f"employee_name: {employee['name']}, age is: {employee['age']}") #employee_name: Raj, age is: 28
# print(employee["salary"])  #KeyError: 'salary' program crashes if the key doesnt exist 
#or use try/except 
try:
    print(employee["salary"])
except KeyError: 
    print("salary filed not found")

#example2: safe pattern check first with in 
student = {
    "name": "mahesh",
    "class": 5,
    "id_num": 101,
    "city": "pune"
}
if "age" in student: 
    print(student["age"])
else: 
    print("age is not fount for this student") #age is not fount for this student

###########################################################################################################################
#example3: Basic access with .get() 
actor = {"name": "Prabhas", "age": 40}

print(actor.get("name")) #Prabhas
print(actor.get("age")) #40

#.get() NEVER CRASHES ON MISSING KEYS 
print(actor.get("movie_name")) #o/p: None it gives none

"""
Note: if the key doesnt exist the safer way to access dict values using .get() 
this will return None if the key doesnt exist. and never crashes. 

But if we use noraml accessing like [] we have to define condition or handleing 
with try/excetpt to withoyt crashless 
"""

#Example provide a default Value with .get() 
#pass a second argument used if the key is not found 
movie_name = actor.get("movie", "sahoo")
print(movie_name) #sahoo 
###########################################################################################################################
#example4: access values inside nested dicts 
doctor = {
    "name": "Alice", 
    "address": {
        "city": "Berlin",
        "Country": "Germany"
    }
}

print(doctor["address"]) #{'city': 'Berlin', 'Country': 'Germany'}
print(doctor["address"]["city"]) #Berlin

#with.get() 
print(doctor.get("address"))

print(doctor.get("address").get("age")) #None
#print(doctor.get("email").get("age")) #AttributeError: 'NoneType' object has no attribute 'get'  
#safe chained pattern with deafult dict 
age = doctor.get("adress", {}). get("age", 29)
print(age) #29 
#.get("address", {}) returns if 'address' is missing then we can call .get("age", 29) safely on it. 