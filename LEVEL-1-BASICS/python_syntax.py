################################################################################################
                                 # Part 1: Print & String Syntax 
################################################################################################

"""
case1: Two print statements on same line without separator
print("Hello") print("world")
output:
   print("Hello") print("world")
                   ^^^^^
SyntaxError: invalid syntax

case2: 
print("Hello
World")
This will give an error → because Python doesn't allow breaking a string like this directly.
"""
################################################################################################
#case3: Correct ways to print on next line
print ("Hello")
print("world")

# OR (two statements in one line using ;)
print ("Hello"); print("World")

# OR (using escape sequence \n)
print("Hello\nWorld") #here \n is a go to next line

#output: 
# Hello 
# world

# Example with tab \t
print("Hello\tWorld") 
#output: Hello   World
################################################################################################
#case4: Printing with and without custom end
print("Hello world")   
#output: Hello world 

# OR Using end=" " to avoid newline
print("Hello", end=" ") #mostly use 
print("World")
#output: Hello world 
################################################################################################
# case5: Using triple quotes for multi-line strings
print("""Hello
World
Python""")

# Output:
# Hello
# World
# Python

# Note: Triple quotes preserve line breaks and spaces exactly as written.
################################################################################################

                           # Part 2: Operator Syntax & Line Continuation
################################################################################################
#case:1 Spaces around operators don't matter
x = 1+2 
#or 
x = 1 +    2  
print(x)
#output: 3
################################################################################################
#case2: Breaking line without continuation symbol
x = 1 +    2
+3 
print(x)
#output: 3  #`+3` is treated as a separate statement and ignored here
################################################################################################
#case3: Using backslash '\' to continue expression
x = 1+   2 \
+3 
print(x)
#output: 6 
################################################################################################
# case4: Using parentheses to continue expression
x = (1 +
     2 +
     3)
print(x)
#output: 6 
################################################################################################

################################################################################################
                        #Part3 : Many Values to Multiple Variables 
          ##In the print() function, you output multiple variables, separated by a comma:
################################################################################################
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)  #Python is awesome

#you can also use the + operator to output multiple variables:
x = "Python " #here we givin space after python as well as is 
y = "is "
z = "awesome"
print(x + y + z) #Python is awesome 

#Notice above and below the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python"
y = "is"
z = "awesome"
print(x + y + z) #Pythonisawesome

x = "Python "
y = "is"
z = "awesome"
print(x + y + z) #Python isawesome
################################################################################################