"""
A function is a piece of code that performs a unit of work. 
print() function, which output the message to the screen.

KeyWords: are reserved words, we should not use this keywords as varible names and function names 
and any other identifers. 
"""

print("Hello world!") #Hello world!

print ("Hello"); print("World")
#output: 
# Hello
# World

#using escape sequence \n)
print("Basava\nRaj") #here \n is a go to next line
#output: 
# Basava 
# Raj

print("Hello\tWorld") 
#output: Hello   World

# Using end=" " to avoid newline
print("Basava", end=" ") #mostly use 
print("Raj")
#output: Hello world 

name = "Basavaraj"
print("Hello "+ name) #Hello Basavaraj

name = "Alex"
print("Hi "+ name) #Hi Alex


x= y= z = "Hello world"
print(x)