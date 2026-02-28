def area_of_circle(radius): 
    pi = 3.14
    area = pi * (radius ** 2)
    print("Area of circle is:", area)

user_input = input("Please enter the value of circle to find area: ")

area_of_circle(float(user_input)) 
#input function is always takes as string so we need to convert the str to int to pass.Radius can be decimal values like 4.5, 3.2, etc.
"""
Please enter the value of circle to find area: 45.5
Area of circle is: 6500.585
"""