"""
1) WHAT IS raise?
The raise keyword is used to manually throw an exception.

It is used when:
-> You want to enforce validation rules
-> You detect invalid data
-> You want to stop execution intentionally

raise does NOT handle errors. It CREATES errors.

try/except HANDLES errors. where as raise THROWS errors.

synatx: raise <ErrorType>("optional message")
"""
#example1: Raise a Basic error 
# raise ValueError("this is a manual error"
"""
output: if uncommented: 
ValueError: This is a manual error 
program crashes 
"""
#######################################################################################################################             
# EXAMPLE 2 - raise inside function (Professional Use)

def validate_age(age):
    if age < 0:
        raise ValueError("Invalid age provided.")
    return age

try:
    validate_age(-1)
except ValueError as e:
    print("Error caught:", e)  

#output: Error caught: Invalid age provided.

####################################################################################################################### 
# Example 3: Raise and handle a custom error message

def withdraw(balance, amount):

    # Raise a ValueError if the withdrawal amount exceeds the available balance
    if amount > balance:
        raise ValueError(
            f"CAN NOT WITHDRAW {amount} - ONLY {balance} AVAILABLE"
        )

    # Return the remaining balance after a successful withdrawal
    return balance - amount

try:
    # Attempt to withdraw more than the available balance
    print(withdraw(100, 150))

except ValueError as e:
    # Catch and display the custom error message raised by withdraw()
    print(e)
"""
output: 
CAN NOT WITHDRAW 150 - ONLY 100 AVIALBLE

ValueError → indicates an invalid value was provided.
except ValueError as e → catches the exception and stores the error message in e.
Without the try-except block, Python would display a traceback and stop the program.
"""
####################################################################################################################### 
