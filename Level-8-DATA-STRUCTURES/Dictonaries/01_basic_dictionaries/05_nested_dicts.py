"""
nested Dict: 
This is useful of Json, API response, yaml configs and every data foremate

1) what is nested dict? 
A nested dict is a dict where one or more values are them selves dicts. 
"""
#examle1: basic nested dict: 
products = {
    "product1" : {    #<- nested dict as value
     "device" : "Mobile",
      "name": "Oneplus", 
      "Ram": 16
    },
    "product2" : {
     "device" : "laptop",
      "name": "Hp", 
      "Ram": 12
    },
}

print(products)
"""
{'product1': {'device': 'Mobile', 'name': 'Oneplus', 'Ram': 16}, 'product2': {'device': 'laptop', 'name': 'Hp', 'Ram': 12}}
"""
#access nested values with [] first level get whole inner dict 
print(products["product1"]) #{'device': 'Mobile', 'name': 'Oneplus', 'Ram': 16}
print(products["product2"]) #{'device': 'laptop', 'name': 'Hp', 'Ram': 12}

#get the value from the inner dict 
print(products["product1"]["name"]) #Oneplus
print(products["product2"]["name"]) #Hp

#from product, get products then from that, get the product1 of name 
############################################################################################################################
#multilevel nesting 
data = {          #level1
    "user": {      #level2
      "profile" : {  #level3
          "name": "Alice",
           "location": { #level4
              "city": "pune",
              "country": "india"
            }
        }
    }
}

#4 levels with 4 barckets  get the city 
print(data["user"]["profile"]["location"]["city"]) #pune

#modifying nested values
data["user"]["profile"]["location"]["city"] = "Banglore"
print(data)
#{'user': {'profile': {'name': 'Alice', 'location': {'city': 'Banglore', 'country': 'india'}}}}

#add a new nested key 
data["user"]["profile"]["age"] = 26
print(data["user"]["profile"]) #{'name': 'Alice', 'location': {'city': 'Banglore', 'country': 'india'}, 'age': 26}

#add a whole new nested dict 
data["user"]["student_data"] = {
    "student_name":  "Alice",
    "student_id": 101
}
print(data)
#{'user': {'profile': {'name': 'Alice', 'location': {'city': 'Banglore', 'country': 'india'}, 'age': 26}, 'student_data': {'student_name': 'Alice', 'student_id': 101}}}
############################################################################################################################
#examle3: loop through a nested dict 
student = {
    "name" : "raj",
    "id": 1, 
    "address": {
        "city": "Goa",
        "country": "India"
    }
}

#loop through the outer dict 
for key, value in student.items():
    print(f"{key}: {value}")
"""
name: raj
id: 1
address: {'city': 'Goa', 'country': 'India'}

#The inner dict gets printed as a whole its just a value to get need secodn loop 
"""
for key, value in student.items():
    if isinstance(value, dict):   #is the value a dict? 
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f" {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")
"""
name: raj
id: 1
address:
 city: Goa
 country: India

**Note:** `isinstance(value, dict)` checks whether the variable `value` is a **dictionary**.

This is especially useful when working with **nested dictionaries** or **JSON data**, where you may not know the structure beforehand.

* If `value` **is a dictionary**, you can loop through it using another `for` loop (for example, `value.items()`).
* If `value` **is not a dictionary** (such as a string, integer, list, etc.), you can process or print it directly.

Using `isinstance()` makes your code flexible because it can handle different types of values without causing errors.
"""
############################################################################################################################