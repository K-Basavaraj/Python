"""
1) what is slicing? 
slicing lets you grab a slice (a range) of items from a tuple. 
return a new tuple the original is unchnaged

synatx: tuple_name[start:stop:step]
start: where to begin(included)
stop: where to end (excluded)
step: how big a jump between picks 
"""
#example1: 
fruits =("apple", "banana", "cherry", "date", "fig")
print(fruits[1:4]) #('banana', 'cherry', 'date')
print(fruits[:3])  #('apple', 'banana', 'cherry')
print(fruits[2:]) #('cherry', 'date', 'fig')
print(fruits[:]) #('apple', 'banana', 'cherry', 'date', 'fig')

print(fruits[-3: ]) ##('cherry', 'date', 'fig')
print(fruits[:-2]) # ('apple', 'banana', 'cherry')
# [:-2] means "everything except the last 2 items"

#example: adding step 
nums = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

#every 2nd item from the start 
print(nums[::2]) #(10, 30, 50, 70, 90)

#EVERY THIRD ITEM 
print(nums[::3]) #(10, 40, 70, 100)

print(nums[1:8:2]) #(20, 40, 60, 80)

