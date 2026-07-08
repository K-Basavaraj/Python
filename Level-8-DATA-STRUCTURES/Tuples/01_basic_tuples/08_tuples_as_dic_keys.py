"""
In python dictonories, every key must be immutable(can not be chnage after creation) 
-> Tuples are immutable -> so can be used as dict keys, where as
-> Lists are mutable -> can not be used as dict keys. 

Note: The rule which is Dictnory need keys that never change. 

from the dict module we learned that dictr keys must be: 

1. immutable (can not chnage)
2. unique( no duplicates)

allowed as keys: string, numbers tuples, booleans 
not allowed: lists, dicts, sets (they are mutable)
"""
#example1: A dictonary stores data as key value pairs. 
person = {
    "name" : "Basavaraj", 
    "age" : "29",
    "City" : "Hyderabad"
}
print(person["name"]) #o/p: Basavaraj (which is use the key get the value.)

#example2: Tuples as dict keys we use a tuple when we need a multi - part key made of multiple values
locations = {
    ("us-east-1", "Zone-1"): "server-A", 
    ("us-west-1", "oregon"): "server-B",
    ("us-east-1", "Zone-1"): "server-c", 
}
print(locations) #o/p: {('us-east-1', 'Zone-1'): 'server-c', ('us-west-1', 'oregon'): 'server-B'}
#here it doesnt print the 3rd one why because dictonery, "key must be unique" if we use the same key twice the 2nd value replace the first. only one remains you 

print(locations[("us-east-1", "Zone-1")]) #output: server-c
print(locations[("us-west-1", "oregon")]) #output: server-B
#The Key is a tuple of(region, zone) tuples can hold multiple piece of info and they're immutable.

"""
#example3: Lists as keys - failes 
===========================
#using a list as dict key - fails 
locations = {
    ["us-east-1", "vergina"]: "server-A", 
    ["us-west-1", "oregon"]: "server-B",
} #TypeError: unhashable type: 'list' this will raise a TypeError because lists are mutable and cannot be used as dictionary keys. The error message indicates that the list type is unhashable, meaning it cannot be used as a key in a dictionary.
"""
"""
Why does python Reject lists as keys? 
-> Dict find your data using something called a "hash"
-> If a key could chnage, its hash would change too and the dict would loase track of where the data is? 
-> Tuples cant chnage -> their hash is stable where as 
-> List can chnage -> their has would shift 
"""
##################################################################################################
#example:  caching API response or health checks by compsote keys 
cache = {
    ("auth-service", "us-east-1"): "healthy", 
    ("auth-service", "eu-west-1"): "digrade", 
    ("payment-service", "us-east-1"): "healthy", 
    ("payment-service", "eu-west-1"): "down", 
}

status = cache[("payment-service", "eu-west-1")]
print(f"Payment service in EU-West:{status}") #Payment service in EU-West:down

#example: map each (regioon, zone and server) to its deatils. 
servers = {
    ("us-east-1", "zone-a", "web-01"): {"cpu": 45, "memory": 70}, #tuple_key : dict_value
    ("us-east-1", "zone-a", "web-02"): {"cpu": 80, "memory": 85},
    ("eu-west-1", "zone-b", "db-01"): {"cpu": 30, "memory": 60},
}

target = ("us-east-1", "zone-a", "web-02")
print(servers[target]) #o/p{'cpu': 80, 'memory': 85}