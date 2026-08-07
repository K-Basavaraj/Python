"""
################### FUNCTIONS #####################
Functions are like recipes, dividing complex tasks into single, managable steps.
functions can enhance code clarity, reusabilty, and logic flow. 

defining a function with "def" keyword, simplify repetative tasks by encapsulating code steps. 
builtin-functions like pre-defined optimized functions like print, len, sum and type 
do not require user definition.

user-defined functions: created by the programmer to address specific tasks not coverd by built-ins
example: defining greet funtion to print greetings. 

functions use "return", genrating one result per call, 

Note: 
return → gives a value back to the caller.
print → displays a value on the screen.

User-defined functions in Python allow flexibility and control to fulfill specific coding tasks, 
such as custom messages or dynamic interactions.
Key Benefit
Such functionality creates dynamic and individualized outputs, enhancing interactivity and engagement.
"""

#example1: function with no parameter 
def greet():
    print("Hello world!")
greet() #Hello world!

def greeting(name):
    print("welcome: "+ name)

greeting("Basavaraj") #welcome: Basavaraj
#############################################################################################################

#example2:  userdefined function with Single paramenter with return keyword
def greet_input(name):
    return f"Hello, {name}!"

greet_input("Python coder") #No output

#adding numbers 
def add_two(num):
    return num + 2
result = add_two(2)

print(result) #4
#############################################################################################################
#Example3: function with multiple parameters
def greetings(name, department):
    print("welcome, " + name)
    print("your part of " + department + ".")

greetings("Basavaraja", "DevOpsEngineer")
greetings("tyrion Lanister", "SoftwareEngineer")

"""
welcome, Basavaraja
your part of DevOpsEngineer.
welcome, tyrion Lanister
your part of SoftwareEngineer.
"""
#############################################################################################################
