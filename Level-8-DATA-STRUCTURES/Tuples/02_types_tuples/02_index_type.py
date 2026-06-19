"""
what is .index() ? 
.index() is the second (and last) tuple method. 
it tells us the position(index) of the first occurrence of a value in the tuple. 

returns: an integer (the index)

syntax: 
 tuple_name.index(value)
 tuple_name.index(value, start)
 tuple_name.index(value, start, stop)

Reverse of bracket indexing:" 
- [] indexing give position, get the value  
-.index() -> give value, get position
"""
#example1: find the values position 
fruits = ("apple", "banana", "cherry", "date")
print(fruits.index("apple"))  # 0
print(fruits.index("banana"))# 1
print(fruits.index("cherry"))# 2
print(fruits.index("date"))# 3

#example: check with 'in' before using .index?() 
if "grape" in fruits: 
    pos = fruits.index("grape")
    print(f"Found at position {pos}")
else: 
    print("Not in tuple") #Not in tuple

#example use try/except 
try: 
    pos = fruits.index("grape")
    print(f"Found at position {pos}")
except ValueError: 
    print("note in tuple")

#example: works on numbers and other tyoes too 
nums = (10, 20, 30, 40)
print(nums.index(30)) #2

#Example: Note Only returns the first occurence 
#if the value appears multiple times .index() returns only the first poistion. the rest is ignored

data = ("a", "b", "a", "c", "a")
print(data.index("a")) #0

#value not found ValueError(crashes)
#print(fruits.index("grape")) #ValueError: tuple.index(x): x not in tuple

#Note: .count which return 0 .index() crashes when value is not found

#example: search starting from a specifc position 
print(data.index("a")) #0
print(data.index("a", 1)) #2 
print(data.index("a", 3)) #4

#example search within a range 
print(data.index("a", 0, 4)) #0 #search only within index 0-3 0th poistion only show 1st occrence 
print(data.index("a", 2, 4)) #2 SEARCH ONLY WITHIN INDEX 2-4 2nd poition only shows the 1st occurnec 
######################################################################
#.index() vs [] indexing 
fruits = ("orange", "kiwi", "Mango")
#[] indexing  - gives value at a poition 
print(fruits[1]) #kiwi #'whats at poition 1? 

#.index() method gives poition of a value 
print(fruits.index("kiwi")) #1 where is kiwi? 
#############################################################################
load_balancer = ("VM-01", "VM-02", "VM-03", "VM-04") 

target = "VM-03"

if target in load_balancer: 
    pos = load_balancer.index(target)
    print(f"{target} is at rotation poistion {pos}")
else: 
    print(f"{target} is not in the pool")
#VM-03 is at rotation poistion 2