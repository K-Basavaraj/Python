fruits = ["apple", "banana", "cherry", "grapefruit"]
print(fruits[0]) #output: apple
print(fruits[1]) #output: banana
print(fruits[2]) #output: cherry

print(fruits[0:2]) #output: ['apple', 'banana']
print(fruits[1:3]) #output: ['banana', 'cherry']
print(fruits[0:]) #output: ['apple', 'banana', 'cherry', 'grapefruit']
print(fruits[:3]) #output: ['apple', 'banana', 'cherry']
print(fruits[:]) #output: ['apple', 'banana', 'cherry', 'grapefruit']
print(fruits[:2]) #output: ['apple', 'banana']
print(fruits[-2:]) #output: ['cherry', 'grapefruit']
print(fruits[:-2]) #output: ['apple', 'banana']

"""
#list[ start : stop : step ]
#start where to begin (included) 
#stop where to end (not included/excluded)
#step the interval between elements
"""
#example: 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#step = 1 (default, every item)
nums[::1] #output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#step = 2 (every 2nd item)
nums[::2] #output: [10, 30, 50, 70, 90]
#step = -1 (backwards, every item)
nums[::-1] #output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
#step = -2 (backwards, every 2nd item)
nums[::-2] #output: [100, 80, 60, 40, 20]

#example: combining step with start and stop 
nums[1:8:2] 
#start at index 1 (20), stop before index 8 (90), step by 2
#output: [20, 40, 60, 80] here we have sliced the nums list starting from index 1 (which is 20), stopping before index 8 (which is 90), and stepping by 2 (which means we take every second item). So we get the items at index 1 (20), index 3 (40), index 5 (60), and index 7 (80) in the resulting list.