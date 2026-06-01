# --------------------
# SLICING
# list[start:stop]
# start = included
# stop  = excluded (not included)
# --------------------

fruits = ["apple", "banana", "cherry", "grapefruit"]

print(fruits[0:2])  # Index 0 to 1 -> ['apple', 'banana']
print(fruits[1:3])  # Index 1 to 2 -> ['banana', 'cherry']

# From a specific index to the end
print(fruits[0:])   # From index 0 to end -> ['apple', 'banana', 'cherry', 'grapefruit']
print(fruits[1:])   # From index 1 to end -> ['banana', 'cherry', 'grapefruit']
# Entire list (commonly used to create a copy)
print(fruits[:])    # Entire list -> ['apple', 'banana', 'cherry', 'grapefruit']

# From beginning up to (but not including) stop index
print(fruits[:3])   # Up to index 2 -> ['apple', 'banana', 'cherry']
print(fruits[:2])   # Up to index 1 -> ['apple', 'banana']


# Using negative indexes in slicing
print(fruits[-2:])  # Last 2 items -> ['cherry', 'grapefruit']
print(fruits[:-2])  # Everything except last 2 items -> ['apple', 'banana']
print(fruits[:-3])  # Everything except last 3 items -> ['apple']

# Reverse slice examples
print(fruits[::-1]) # Reverse list -> ['grapefruit', 'cherry', 'banana', 'apple']

"""
Which one should I use? between [:] and [0:]
a) Use [:] when you want a copy of the entire list 
example: new_list = old_list[:] 

b) Use [0:] when the starting index might change later
example: start = 0
print(fruits[start:]) or print(fruits[2:]) 
"""
#####################################################################################################

"""
list[start:stop:step]

start = where to begin (included)
stop  = where to end (excluded)
step  = how many positions to move

Default values:
start = 0
stop  = end of list
step  = 1
"""
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Every item python sees nums[0:len(nums):1]
# start = 0 (default)
# stop = end of list (default)
# step = 1
# Take every item from beginning to end
print(nums[::1])    # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Every second item
# start = 0 (default)
# stop = end of list (default)
# step = 2
# Take every 2nd item starting from index 0
# Indexes selected: 0, 2, 4, 6
print(nums[::2])    # [10, 30, 50, 70, 90]

# Every third item
# start = 0 (default)
# stop = end of list (default)
# step = 3
# Take every 3rd item starting from index 0
# Indexes selected: 0, 3, 6, 9
print(nums[::3])    # [10, 40, 70, 100]

# Reverse list
# start = end of list (default when step is negative)
# stop = before beginning of list (default)
# step = -1
# Traverse backwards one item at a time
print(nums[::-1])   # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

#step = -2 (backwards, every 2nd item)
# Reverse and take every second item
print(nums[::-2])   # [100, 80, 60, 40, 20]

#example: combining step with start and stop 
# --------------------
# START + STOP + STEP
# --------------------

print(nums[1:8:2])
# start = index 1 -> 20
# stop  = before index 8
# step  = move by 2 positions
nums[1:8:2] 
#start at index 1 (20), stop before index 8 (90), step by 2
#output: [20, 40, 60, 80] here we have sliced the nums list starting from index 1 (which is 20), stopping before index 8 (which is 90), and stepping by 2 (which means we take every second item). So we get the items at index 1 (20), index 3 (40), index 5 (60), and index 7 (80) in the resulting list.

"""
# nums[start:stop:step]

# When step is positive:
# start = 0 (default)
# stop = end of list (default)
# move left to right
"""