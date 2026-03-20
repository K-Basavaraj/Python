"""
List comprehensions offer a more concise way to generate lists in Python compared to traditional loops.
List comprehensions offer a more concise way to generate lists in Python compared to traditional loops.

Key Concepts:
Automatic List Generators: Create lists by applying mathematical operations and computations.
Syntax: An example of list comprehension syntax: [expression for item in iterable], where expressions can include calculations.

conclusion: 
List comprehensions provide a neat and efficient method for creating and populating lists in Python, immediately placing results within square brackets. 
This process simplifies code and leverages Python's dynamic features for effortless list generation.
"""
#example1: using a for loop to create a list of squares
squares = []
for x in range(10):
    squares.append(x**2) #this will calculate the square of each number from 0 to 9 and append it to the squares list.
print(squares) #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] the squares list now contains the squares of numbers from 0 to 9.

#example2: using a list comprehension to create a list of squares
squares = [x**2 for x in range(10)] #this is a more concise way to create the same list of squares using a list comprehension.
print(squares) #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] the squares list now contains the squares of numbers from 0 to 9, created using a list comprehension.
