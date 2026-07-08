"""
Three gneral purpose python tools that work withy dicts 

len(d) -> how many key value pairs are in the dict? 
x in d -> is x a key? 
dict(..) -> the dict constroctor (multiple ways to build)

all three are called like functiuons or opertors not methods.
"""
#=================================================================
#                   len()
#=================================================================
#example1: how many pairs 
person = {"name": "raj", "age": 30, "city": "hyderabad"}
print(len(person)) #3

empty = {}
print(len(empty)) #0

#example2: nested -len() only counts the top level 
data = {
    "user": {
        "name": "raj", 
        "age": 28,
    }, 
    "session": "abc1234"
}
print(len(data)) #2 <- top level pairs
print(len(data["user"])) #2 <- inner dict, separtly 
#en() never drills into nested dict

#example3: quick "is it empty?" check
config = {}

if len(config) == 0: 
    print("config is empty") #config is empty

#cleaner
if not config: 
    print("config is empty (cleaner)") #config is empty (cleaner)

#an empty dict is falsy. "if not d is idiomatics python"
#=================================================================
#                   in/not in 
#=================================================================
#example1: check if key exists 
person = {"name": "rakesh", "age": 40}

print("name" in person) #True
print("email" in person) #false
print("email" not in person) #True
#in checks keys by default not values 

#example2: check for values with .values() 
prices = {"apple": 50, "banana": 30}
print("apple" in prices) #True <- apple is a key 
print(50 in prices) #False its a vlue not a key 
print(50 in prices.values()) #True < now chekcing avlues

#example3: check for a specific (key, value) pair 
print(("apple", 50) in prices.items())#True
print(("apple", 99) in prices.items())#False

#example3: use in as a safe guard
if "cherry" in prices:
    print(prices["cherry"])
else: 
    print("No cherry in list")
    #No cherry in list
