"""
Both .get() and set() methods deal with "What to do if a key is missing": 
.get(key, default) -> just read; never modifies the dict. 
.setdefault(key, default) -> reads. and adds the key if missing. 

Both return a value. the difference is wether the dict chnages. 

key_takeaways: 
- .get(Key, default) -> safe read, never modifies dict 
- .setdefault(key, default) -> reads + adds the key if missing 
- use .get() for read-only lookup (config, api data)
- use .setdefault() to initialize a key on first use perfect for grouping items into dict of list.
"""
##############.get()############################
#example1: 
person = {"name": "Alice", "age": 30}
print(person.get("name"))
print(person.get("email")) #Key is missing but no crash 
print(person.get("email", "N/A")) #N/A is default value

#example2: .get() does not modify the dict 
email = person.get("email", "no-email")
print(email) #no-email
print(person) #{'name': 'Alice', 'age': 30}
#.get() is purely a read operation 

#example3: nested dicts 
data = {
    "user": {
        "profile": {
            "city": "Hyderabad"
        }
    }
}
city =  data.get("user", {}).get("profile", {}).get("city", "unknown")
print(city) #Hyderabad
#############################################################################################
                ##############.set()############################
#example1: basic r- read but add if missing (.setdefault())
person = {"name": "alice"}

#if age is missing -> adds it with the given default 
age = person.setdefault("age", 30)

print(age) #30
print(person) #{'name': 'alice', 'age': 30}

#example2: if the key exists - just return it (no chnages)
age = person.setdefault("age", 99) #already exists so igonres default 
print(age) #30
print(person) #{'name': 'alice', 'age': 30}

#example2: when .setdefault() shines - building lists in a dict 
#group items by category in one clean loop 
items = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]

grouped ={}

for category, item in items:
    grouped.setdefault(category, []).append(item)
print(grouped)  #{'fruit': ['apple', 'banana'], 'veg': ['carrot']}

#Note: without setdefaulot. youd have to check if the key exists, create a list if not, then append, setdefault does both at once
