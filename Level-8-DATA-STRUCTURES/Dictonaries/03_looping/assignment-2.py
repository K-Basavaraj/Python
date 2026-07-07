#Pattern2: loop through nested dicts 

employees = {
    "alice": {
        "role": "Engineer", 
        "salary": 90000,
    },
    "bob": {
        "role": "Designer", 
        "salary": 57000,
    },
    "charli": {
        "role": "Manager", 
        "salary": 110000,
    },
}

for name, info in employees.items(): 
    print(f"{name} -> {info['role']} (${info['salary']})")

"""
output: 
alice -> Engineer ($90000)
bob -> Designer ($57000)
charli -> Manager ($110000)

The value itself is a dict- you access nested field with []
"""