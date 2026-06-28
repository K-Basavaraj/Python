# """
# 1)Why we need to check keys? 
# Accessing a missing key with d[key] crashes your program. 
# So before risky operations, we often need to ask: 

# "Does this key exist?" 

# Python give us a clean way :The `in` opertor. it returns True or False - no crash, no exception. 
# """
# #Example1: The `in` Opertor 

# person = {"name": "Rajesh", "Age": "30"}
# print("name" in person) #True 
# print("email" in person) #False
# #Key in dict -> returns True if the key exists, False otherwise. 

# #example1a: with `in` opertor with contdions
# employee = {
#     "name": "Srikanth", 
#     "age": 29,
#     "salary": 40000
# }

# if "emp_id" in person: 
#     print(f"Employee id: {employee["emp_id"]}")
# else:
#     print("Employee_id not found") #Employee_id not found

# #example1b: `in` only looks at the keys 
# student = {
#     "name": "Basavaraj",
#     "student_id": 101,
#     "age": 25,
# }
# print("name" in student) #True
# print("Basavaraj" in student) #False -> its a value 
# #NOTE: tHE `in` opertor only checks KEYS by Defult to check if a value exists, use .value() 

# #example1c: .values()
# print(101 in student.values()) #True
# print("Basavaraj" in student.values())  #True

# #######################################################################################################################
# #example2: The opposite is `not in` 
# print("email" not in person) #True
# print("name" not in person ) #False
# #######################################################################################################################

# #example3: to check if a (key, value) pair exist use .item()
# electronics = {
#     "product": "Mobile",
#     "name": "Oneplus", 
#     "Ram": 16
# }

# print(("name", "Oneplus") in electronics.items()) #True
# print(("storage", 256) in electronics.items()) #False
#######################################################################################################################
#Example4: Comparing `in`, .get(), and try/except 
#Three ways to handle missing keys safely
products = {
    "product1" : {
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

#way1 `in` check 
if "storage" in products["product1"]:
    storage = products["product1"]["storage"]
else:
    storage = "not found"

print(storage) #not found

print(products) #{'product1': {'device': 'Mobile', 'name': 'Oneplus', 'Ram': 16}, 'product2': {'device': 'laptop', 'name': 'Hp', 'Ram': 12}}

#way2: .get() with default 
storage = products["product2"].get("stoarge", "not found") #not found
check_ram = products["product1"].get("Ram", "not found") #None
print(storage) #not found
print(check_ram) #16

#way3: try/except 
try: 
    storage = products["product1"]["stoarge"]
except KeyError: 
    stoarge = "notfound"
