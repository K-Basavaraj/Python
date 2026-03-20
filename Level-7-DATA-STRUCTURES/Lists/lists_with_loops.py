"""
For loops offer a simple way to cycle through elements in a list, akin to examining items in a shopping cart.

Here's how to use a for loop:
Syntax: Employ the format for item in list: to iterate through each list element.
Naming: Choose any name for the variable representing each element.
Application: Use the loop to sequentially access and manipulate or display list items.

Benefits
Simplicity: For loops simplify processing each list element without manual indexing.
Efficiency: Automatically handles iterations efficiently and neatly.
For loops are a fundamental concept, essential for seamless list manipulation in Python.

Applications:
Geometry: Calculate land areas.
Physics/Engineering: Use squares in equations.
Data Science: Essential in error calculations.
Explore how combining for loops and lists can simplify complex calculations in various fields.
"""
#example1: for loop to print items in a list
grocery_cart = ["veggies", "fruits", "desserts"]
for item in grocery_cart:
    print(item) #output: veggies fruits desserts the for loop iterates through each item in the grocery_cart list and prints it.

#example2: use a loop to calculate the area of each plot and store those areas in the list.
areas = []

for sider_length in range(1,6):
    areas.append(sider_length**2) #this will calculate the area of each plot (assuming it's a square) and append it to the areas list.

print(areas) #output: [1, 4, 9, 16, 25] the areas list now contains the area of each plot from side length 1 to 5.