"""
List comprehensions offer a more concise way to generate lists in Python compared to traditional loops.

Key Concepts:
Automatic List Generators: Create lists by applying mathematical operations and computations.
Syntax: An example of list comprehension syntax: [expression for item in iterable], where expressions can 
include calculations.

syyntax: universal formula for list comprehensions: [ output for item in list if condition ]


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

#example3: [ x * 2 for x in nums if x > 10 ] for each 'x' in nums. if x > 10 give me x * 2 
#[ output for item in list ]
ports = [ 20, 80, 443 ]
labels = [f"port: {p}" for p in ports] #this will create a new list called labels that contains the string "port: " followed by the value of each port in the ports list. The f-string is used to format the string with the value of p.
print(labels) #output: ['port: 20', 'port: 80', 'port: 443'] the labels list now contains the formatted strings for each port in the ports list, created using a list comprehension.

#[item for item in list if condition]
ports = [ 22, 8080, 3306 ]
high_ports = [p for p in ports if p > 1000 ]
print(high_ports) #output: [8080, 3306] the high_ports list now contains only the ports from the ports list that are greater than 1000, created using a list comprehension with a condition.