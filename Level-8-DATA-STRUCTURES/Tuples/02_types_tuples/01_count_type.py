"""
what is count() 
.count() is one of the only two methods availaible on tuples. 
it counts how many times a specific value appears in the tuple 
returns 0 if not found never crashes 
exact matche only - case-sensitve 
works with only data type(numbers, strings, nested tuples)

Returns: an integer (the count)
synatx: tuple_name.count(value)


.count() vs 'in' operator which to use? 
- use .count() when you need the exact number of matches 
- use 'in' when you only need a yes/no answer 
"""
#example1: 
nums = (1,2,3,2,4,2,5)
print(nums.count(2)) #3 The value appers 3 times in the tuple

#example2: counting strings: 
fruits=("apple", "banana", "cherry", "apple", "apple")
print(fruits.count("apple")) #3 
print(fruits.count("banana")) #1

#example3 value not in tuple returns 0 never crashes 
print(fruits.count("grape")) # output: 0

#cexample: counting items of different types 
mixed = (1,"1", 1, "1", True, 1.0)
#note: python sees True, 1, amd 1.0 as the same numaric value but "!" string is diff
print(mixed.count(1)) #4 counts 1,1, True, 1.0 
print(mixed.count("1")) #2 
#Note: True == 1 and 1.0 == 1 in python 

#counting nesed tuples 
data = ((1,2), (3,4), (5,6), (1,2))
print(data.count((1,2))) #2 

#example: 
log_levels = ("INFO", "ERROR", "INFO", "WARN", "ERROR", "ERROR", "INFO")

print(f"info count: {log_levels.count('INFO')}") #info count: 3
total = len(log_levels)
print(f"Total log {total}") #Total log: 7

#example with 'in opertor 
print("apple" in fruits) #True 
print("grape" in fruits) #False