"""
Adding Matrices and Creating 3D Lists

Adding Matrices:
Define matrix_a and matrix_b of the same size.
Add each corresponding element using loops to achieve a result matrix.
Creating a 3D List (Cube):

Goes beyond 2D by stacking matrices, adding depth.
Data can be accessed similarly to matrices by layer, row, and column identification.
Understanding these foundations in Python can equip learners for advanced data analytics and programming tasks.
"""
matrix_a = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
matrix_b = [ [9, 8, 7], [6, 5, 4], [3, 2, 1] ]

print(len(matrix_a)) #output: 3 this will print the number of rows in matrix_a, which is 3.
print(len(matrix_b)) #output: 3 this will print the number of rows in matrix_b, which is 3.

result = []

for i in range(len(matrix_a)): #this will loop through each row index of matrix_a and matrix_b.
    new_row = [] #this will create an empty list called new_row to store the sum of the corresponding elements from matrix_a and matrix_b for each row.
    for col in range(len(matrix_a[0])): #this will loop through each column index of the current row in matrix_a and matrix_b.
        sum_value = matrix_a[i][col] + matrix_b[i][col] #this will calculate the sum of the corresponding elements from matrix_a and matrix_b for the current row and column, and store it in sum_value.
        new_row.append(sum_value) #this will add the sum of the corresponding elements from matrix_a and matrix_b for the current row and column, and append the result to new_row.
    result.append(new_row) #this will add the new_row to the result matrix.
print(result) #output: [[10, 10, 10], [10, 10, 10], [10, 10, 10]] this will print the result of adding matrix_a and matrix_b, which is a new matrix where each element is the sum of the corresponding elements from matrix_a and matrix_b.

#3D List (Cube)
cube = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[9, 8, 7], [6, 5, 4], [3, 2, 1]],
    [[2, 3, 4], [5, 6, 7], [8, 9, 0]]   
]

print(cube) #output: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]], [[2, 3, 4], [5, 6, 7], [8, 9, 0]]] this will print the original cube which is a nested list containing three matrices as its elements.

print(cube[0]) #output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] this will access the first layer (index 0) of the cube, which is the first matrix.    
print(cube[1]) #output: [[9, 8, 7], [6, 5, 4], [3, 2, 1]] this will access the second layer (index 1) of the cube, which is the second matrix.
print(cube[2]) #output: [[2, 3, 4], [5, 6, 7], [8, 9, 0]] this will access the third layer (index 2) of the cube, which is the third matrix.

#access specific elements in the first layer of the cube
print(cube[0][0][0]) #output: 1 this will access the element in the first layer (index 0), first row (index 0), and first column (index 0) of the cube, which is the number 1.
print(cube[0][0][1]) #output: 2 this will access the element in the first layer (index 0), first row (index 0), and second column (index 1) of the cube, which is the number 2.
print(cube[0][0][2]) #output: 3 this will access the element in the first layer (index 0), first row (index 0), and third column (index 2) of the cube, which is the number 3.

#access specific elements in the second layer of the cube
print(cube[1][0][0]) #output: 9 this will access the element in the second layer (index 1), first row (index 0), and first column (index 0) of the cube, which is the number 9.
print(cube[1][0][1]) #output: 8 this will access the element in the second layer (index 1), first row (index 0), and second column (index 1) of the cube, which is the number 8.
print(cube[1][0][2]) #output: 7 this will access the element in the second layer (index 1), first row (index 0), and third column (index 2) of the cube, which is the number 7.

#access specific elements in the third layer of the cube
print(cube[2][0][0]) #output: 2 this will access the element in the third layer (index 2), first row (index 0), and first column (index 0) of the cube, which is the number 2.
print(cube[2][0][1]) #output: 3 this will access the  element in the third layer (index 2), first row (index 0), and second column (index 1) of the cube, which is the number 3.
print(cube[2][0][2]) #output: 4 this will access the element in the third layer (index 2), first row (index 0), and third column (index 2) of the cube, which is the number 4.