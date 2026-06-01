"""
A list can, in fact,even contain other lists within it. This is known as a nested list. 
A nested list is a list that contains one or more lists as its elements.

Lists in Python can contain other lists to create complex data structures.

Why Nested Lists Matter:
Nested lists are pivotal in crafting data structures like matrices (2D lists) and cubes (3D lists).
Useful for grids, tables, and essential in areas like machine learning, gaming, and animations.

Creating a 2D Matrix:
A matrix can be initialized using list comprehension.
Example:
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
- The matrix has three rows and columns.
Manipulating Matrices:
Access elements directly using index locators.
Retrieve whole rows or specific elements (e.g., third row, second column).
Use loops to traverse through the matrix.
"""
#example1: creating a nested list (2D matrix)
matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print(matrix) #output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] this is the original matrix which is a nested list containing three lists as its elements.

#access only the rows of the matrix
print(matrix[0]) #output: [1, 2, 3] this will access the first row (index 0) of the matrix, which is the list [1, 2, 3].
print(matrix[1]) #output: [4, 5, 6] this will access the second row (index 1) of the matrix, which is the list [4, 5, 6].
print(matrix[2]) #output: [7, 8, 9] this will access the third row (index 2) of the matrix, which is the list [7, 8, 9].

#access specific elements in the first row of the matrix
print(matrix[0][0]) #output: 1 this will access the element in the first row (index 0) and first column (index 0) of the matrix, which is the number 1.
print(matrix[0][1]) #output: 2 this will access the element in the first row (index 0) and second column (index 1) of the matrix, which is the number 2.
print(matrix[0][2]) #output: 3 this will access the element in the first row (index 0) and third column (index 2) of the matrix, which is the number 3.

#ACCESS specific elements in the second row of the matrix
print(matrix[1][0]) #output: 4 this will access the element in the second row (index 1) and first column (index 0) of the matrix, which is the number 4.
print(matrix[1][1]) #output: 5 this will access the element in the second row (index 1) and second column (index 1) of the matrix, which is the number 5.
print(matrix[1][2]) #output: 6 this will access the element in the second row (index 1) and third column (index 2) of the matrix, which is the number 6.

#access specific elements in the third row of the matrix
print(matrix[2][0]) #output: 7 this will access the element in the third row (index 2) and first column (index 0) of the matrix, which is the number 7.
print(matrix[2][1]) #output: 8 this will access the element in the third row (index 2) and second column (index 1) of the matrix, which is the number 8.
print(matrix[2][2]) #output: 9 this will access the element in the third row (index 2) and third column (index 2) of the matrix, which is the number 9.

#example2: using loops to access elements in the matrix
for row in matrix: #this will loop through each row in the matrix and print it.
    print(row) #output: [1, 2, 3] [4, 5, 6] [7, 8, 9] this will print each row of the matrix on a new line.

#example3: using loops to access ONLY 2ND AND 3RD rows in the matrix
for row in [1,2]:
    print(matrix[row]) #output: [4, 5, 6] [7, 8, 9] this will loop through the second and third rows of the matrix (index 1 and index 2) and print them on a new line.

#example4: using loops to access ONLY 1ST AND 2ND rows in the matrix
for row in [0,1]:
    print(matrix[row]) #output: [1, 2, 3] [4, 5, 6] this will loop through the first and second rows of the matrix (index 0 and index 1) and print them on a new line.

#example5: using loops to access ONLY 1ST AND 3RD rows in the matrix
for row in [0,2]:
    print(matrix[row]) #output: [1, 2, 3] [7, 8, 9] this will loop through the first and third rows of the matrix (index 0 and index 2) and print them on a new line.