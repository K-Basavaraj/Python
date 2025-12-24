name = "Basava"
number = len(name) * 9 
print("Hello " + name + ". Your Lucky number is " + str(number))

name = "Raj"
number = len(name) * 9 
print("Hello " + name + ". Your Lucky number is " + str(number))

"""
Hello Basava. Your Lucky number is 54
Hello Raj. Your Lucky number is 27
"""
##################################################################################################################################
def your_name(name): 
    number = len(name) * 9 
    print("Hello " + name + ". Your Luky number is: " + str(number))
    
# Taking input from the user
user_input = input("Enter your name: ")

your_name(user_input)

"""
Enter your name: Rajesh
Hello Rajesh. Your Luky number is: 54
"""
##################################################################################################################################
