config = {
    "host": "10.0.0.0",
    "port": 3386
}

required_keys = ["host", "port", "user", "password"]

for key in required_keys:
    if key not in config: 
        print(f"Missing required config: {key}")

#Missing required config: user
#Missing required config: password

###########################################################
#example2: update only if the key already exists
server = {
    "status": "running", 
    "cpu": 45
}

#only update cpu if its already tracked 
if "cpu" in server: 
    server["cpu"] = 50 
    print("CPU updated") #CPU updated

if "memory" in server: 
    server["memory"] = 80 
else: 
    print("Memory is not being tracked yet")
#Memory is not being tracked yet

#add a key only if doesnt exist 
user = {
    "name": "sidarth", 
    "role": "Engineer"
}

if "status" not in user: 
    user["status"] = "active"
print(user)
#{'name': 'sidarth', 'role': 'Engineer', 'status': 'active'}
#######################################################################################################
#check for nmested keys safely 
employee = {
    "name": "Raj",
    "address": {
        "city": "Hyderabad",
    }
}

#check at each level before drilling deep 
if "address" in employee and "city" in employee["address"]:
    print(f"City: {employee['address']['city']}")
else:
    print("city not availaible") 

# o/p: City: Hyderabad
#######################################################################################################
