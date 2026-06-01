"""
Min and Max Functions in Python

Purpose:
Helps find the smallest and largest values in a list.

Real-world example:
Useful for finding the lowest and highest marks,
cheapest and most expensive products,
youngest and oldest ages, or minimum and maximum temperatures.

Practical application:
Quickly identifies the minimum and maximum values
without manually checking every element.

The min() function returns the smallest value.
The max() function returns the largest value.
"""
#Example 1: Finding Lowest and Highest Marks 
marks = [85, 92, 78, 96, 88]

lowest_mark = min(marks)
highest_mark = max(marks)

print(lowest_mark)
# output: 78
# min() finds the smallest value in the list.

print(highest_mark)
# output: 96
# max() finds the largest value in the list.

#Example 2: Finding Cheapest and Most Expensive Product
prices = [500, 1200, 300, 750, 2000]

print(min(prices))
# output: 300
# min() returns the lowest price.

print(max(prices))
# output: 2000
# max() returns the highest price.

#Example 3: With Strings
fruits = ["banana", "apple", "cherry", "grape"]

print(min(fruits))
# output: apple
# Alphabetically first value.

print(max(fruits))
# output: grape
# Alphabetically last value.

#example4: 
numbers = [10, 50, 20, 90, 30]

print(min(numbers))  # 10
print(max(numbers))  # 90

# Find the range of values
print(max(numbers) - min(numbers))
# output: 80