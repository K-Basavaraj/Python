"""
---------------------------------------------------------
1)  WHAT IS try?
---------------------------------------------------------

The try block contains code that might raise an error. It allows us to test risky code safely.
"try" lets you attempt code that might fail 

---------------------------------------------------------
2) WHAT IS except?
---------------------------------------------------------

The except block handles the error gracefully. It runs only if an exception occurs inside the try block.
"except" catches the error and decides what to do. 

#without try/except, an error crashes the program 
#with try/except, your script keeps running safely.

syntax: 
try: 
    <code the might fail> 
except: 
    <code to handle the error> 
"""
"""
RULES of try/except and key points: 
-> Catch specifc errors when possible  - not 'EXCEPTION'
-> keep the try block small - only the risky line(s)
-> dont hide errors silently - at minimum, log them 
-> 'else' runs only if no error occurred. 
-> use specifc error types (valueerror, keyerror, etc; )
-> 'except Exception as e' capture the error deatils. 
"""
###########################################################################################################################
#example1: without try/except- program crahses
# x = 10 / 0 
# print("this line never runs")
"""
output: 
    x = 10 / 0
        ~~~^~~
ZeroDivisionError: division by zero
"""
###########################################################################################################################
#example2: with TRY/EXCEPT - caugth gracefully 
try: 
    x = 10/0
except ZeroDivisionError: 
    print("you cant devide by zero!")

print("program continues running")

"""
output: 
you cant devide by zero!
program continues running
"""
###########################################################################################################################
#EXAMPLE 3 - Basic try/except
"""
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

"""
###########################################################################################################################
# #example4: catch specific error 
try: 
    number = int("abc") #can not convert striung to int 
except ValueError: 
    print("That was not a valid number")
    
# output: That was not a valid number
###########################################################################################################################
# EXAMPLE 5 - Multiple exceptions
try:
    x = int(input("Enter number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
"""
output: 
Enter number: abc
Invalid number.
Enter number: 0
Cannot divide by zero.
"""
###########################################################################################################################
#example6: Catch any error using just "except"
try: 
    result = 10/0
except Exception as e: 
    print(f"something went wrong: {e}")
#output: something went wrong: division by zero
###########################################################################################################################
#example7: capturing the actual error with 'as'
#'as e'gives you the error object - useful for loging. 

try: 
    int("not_a_number")
except ValueError as e: 
   print(f"caught error: {e}")
#output: caught error: invalid literal for int() with base 10: 'not_a_number'
###########################################################################################################################
#example7: try/except/else - runs else only if no error 
try: 
  n = int("42")
except ValueError: 
    print("not a number")
else: 
    print(f"sucessfully converted: {n}")

#output: sucessfully converted: 42
###########################################################################################################################