# working with variables and data types: 
"""
variables and restrictions:
-> ensure user inputs are correctly formatted as integer or float before performing calculations.
-> avoid input errors by using functions that convert strings to required data types, such as int() for integers and float() for floating-point numbers.
-> use int() to convert string inputs to integers and float() to convert string inputs to floating-point numbers, allowing for accurate mathematical operations and preventing type-related errors.
"""
#====================================================================================================
#The int() function is used to convert a string or a number to an integer. 
age = int(input("Enter your age: ")) #input function always returns a string, so we need to convert it to int
print("Your age is: " + str(age)) #Your age is: 25


#The float() function is used to convert a string or a number to a floating-point number.
height = float(input("Enter your height in meters: ")) #input function always returns a string, so we need to convert it to float
print("Your height is: " + str(height) + " meters") #Your height is: 1.75 meters

print(f"your are {age} years old and {height} meters tall")