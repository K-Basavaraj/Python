#we seen How we passed the values intop a function as parameters by passing values.  
#What about getting values out of a function? this is where return values comes. which means 
"""
print() → just shows the result on the screen (you see it, but can't reuse it).
return → gives the result back to your program, so you can store it, use it later, or pass it to another function.

The "return keyword in python serves a crucial function, enabling a function to provide outputs after
processing" 

The return values are literal. using incompatible types, such as add(3, 'python) leads to a typo error. 

define parameter types using colon notation(a: int, b: int) for clarity, readabilty and error reduction. 
this ensures that we are passing approriate data making a function call. 
"""

#example1: addition 
def add(a, b): 
    return a + b

result = add(3, 4)
print(result) #7

# result = add(3, "python")
# print(result) #           ~~^~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#example2: 
def sub(a: int, b:int): 
    return a - b

answer = sub(3,5)
print(answer) #-2

#example3: greet function Concatinating string: 
def say_greeting(greeting: str, name: str): 
    return f"{greeting}, {name}!"

greeting_result = say_greeting("Hody", "Python coder!")
print(greeting_result) #Hody, Python coder!!


# """
# None means “no value” in Python.
# A function returns None by default if you don’t use a return statement.
# """
