""""
unlike tuples, dicts are mutable - we can chnage them any time 
-> ADD -> PUT A NEW KEY-VAULE PAIR INTO EXISTING DICT 
-> UPDATE-> CHNAGE THE VALUE OF ANY EXISTING KEY 
-> REMOVE-> DELETE A KEY AND ITS VALUE 


removal methods
---------
method      removed by              returns         safe with missing
--------------------------------------------------------------------
del d[k]        key                  nothing        KeyError
d.pop(k)        key                 The Value       KeyError
d.pop(k, def)   key(or default)     value/default    safe 
d.popitem()     last item           (key,value)     KeyError if empty 
d.clear         everything          nothing         safe

-> key-takeaway: 
1) d[key] = value       (=> adds new key , or update existing key (same synatx))
2) d.update({..})       (=> add/update many kkeys in one call)
3) del d[key]           (=> remove a key (crashes if missing)
4) d.pop(key)           (=> remove + return the value (crashes if missing))
5) d.pop(key, defualt)  (=> safe version withd ewfault)
6) d.popitem()          (=> remove + return last insterted(key, value))
7) d.clear()            (=> empty the enitre dict)
8) use .pop() when you need the value; use del when you dont
"""
#EXAMPLE1: ADDA KEY-VALUE PAIR WITH []
person = {"name": "Rajesh", "age": 26, "email": "" }

#add a new key using [] syntax as accessing 
person["city"] = "Pune"
print(person) #o/p: {'name': 'Rajesh', 'age': 26, 'city': 'Pune'} if the key doesnt exist its added 


"""
person = {"name": "Rajesh", "age": 26, "email": "" }
print["email"] = "rajesh@123"
print(person)
o/p: 
 print["email"] = "rajesh@123"
    ~~~~~^^^^^^^^^
TypeError: 'builtin_function_or_method' object does not support item assignment
"""

#example2: add multiple keys one at a time 
employee = {}  #start with empty 

employee["name"] = "Alice"
employee["age"] = 30
employee["role"] = "Engineer"
print(employee) #{'name': 'Alice', 'age': 30, 'role': 'Engineer'}
######################################################################################################################
#example3: update the value of an existing key 
student = {"name": "Ram", "age": 25}
student["age"] = 28 # it overwrites 
print(student) #{'name': 'Ram', 'age': 28} If key exist value is updated if key doesnt exist new key is added 

#example4: updating any value (inbcluding nested)
actor = {
    "name": "Ramcharn",
    "address": {
        "city": "Hyderabad",
    },
}
#update a value inside a nested dict
actor["address"]["city"] = "Banglore"
print(actor)  #o/p: {'name': 'Ramcharn', 'address': {'city': 'Banglore'}}

#example5: update multiple keys at once with .update() 
#the .update method lets you merge multiple chnages in one shot.
teachers = {"name": "Rani"}
teachers.update(age=28, subject="Maths")
print(teachers)
#o/p: {'name': 'Rani', 'age': 28, 'subject': 'Maths'}

#another example
cars = {
    "car1": {
        "name": "BMW", 
        "color": "Black"
    },
     "car2": {
        "name": "XUV700", 
        "color": "Blue"
    },
}

cars["car1"].update({
  "color": "Blue",
  "city": "germany"
})

print(cars)
#{'car1': {'name': 'BMW', 'color': 'Blue', 'city': 'germany'}, 'car2': {'name': 'XUV700', 'color': 'Blue'}}

cars["car2"].update({
  "color": "white",
  "city": "germany",
  "year": 2026
})
print(cars) 
#{'car1': {'name': 'BMW', 'color': 'Blue', 'city': 'germany'}, 'car2': {'name': 'XUV700', 'color': 'white', 'city': 'germany', 'year': 2026}}
######################################################################################################################
#Remove items 

#example1: using del - keyword which is delete a key permanently 
guns = {"name":"ak-47", "bullets": 40, "reload": "medium", "price": 1000000}
print(guns) #o/p:   {'name': 'ak-47', 'bullets': 40, 'reload': 'medium', 'price': 1000000}
del guns["reload"]
print(guns) #o/p:   {'name': 'ak-47', 'bullets': 40, 'price': 1000000}

#example2: .pop() remove and return the value
removed_price = guns.pop("price")
print(removed_price) #1000000
print(guns) #{'name': 'ak-47', 'bullets': 40} 
#.pop() removes the key but also give you the removed value back, useful when we need to use the value before forgeeting it. 

#example3: pop() with a default 
# guns.pop("size") 
# print(guns) #KeyError: 'size'

#example4: missing key with default  -> returns default  (no crash)
size = guns.pop("size", "not-mention")
print(size) #not-mention like .get() and .pop() takes an optional default value.


#example5: .popitem() -remove and return the last inserted pair
electronics = {"name": "laptop", "brand": "Hp", "Color":"silver", "Price": 60000.00}
print(electronics)
#o/p: {'name': 'laptop', 'brand': 'Hp', 'Color': 'silver', 'Price': 60000.0}

last_pair = electronics.popitem()
print(last_pair) #('Price', 60000.0) return a tuple 
print(electronics) # {'name': 'laptop', 'brand': 'Hp', 'Color': 'silver'}
#NOTE: CRASHES if the dict is empty: {}.popitem() KeyError


#example6: .clear() remove everything 
electronics.clear()
print(electronics) #{} .clear() empties the dict completely. same dict, no contents 

######################################################################################################################
