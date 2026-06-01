"""
1) WHAT IS assert?
assert is used for debugging purposes. It checks whether a condition is True. 
If the condition is False:
→ Python raises AssertionError.
→ Program stops (unless handled).

Simple meaning:
assert = "This condition must be True."

syntax: 
a) assert <condition>
b) assert <condition>, "Optional error message"

2) WHEN TO USE assert?
->  verify assumptions testing assumptions you know should be true
->  For internal testing sanity checks during devlopemnt 
->  To catch programming mistakes early

NOT recommended for:
->  User input validation (use raise insted)
->  Production error handling 

3) WHY NOT USE assert FOR USER VALIDATION?
When Python is run in optimization mode: python -O script.py assert statements can be disabled. 

Python removes all assert statements.
That means:
→ Assertions will NOT execute.
→ Validation will be skipped.

So assert should NOT be used for critical validation.
Use raise instead for production validation.

Note: 
assert(x>0, "must be possitive) wrong (silently bug - always passes!) 
why beacsue? 
(x>0, "must be possitive) is a TUPLE
and a non-empty tuple is always truthy -> assertion always passes 
so always make sure when using assert #NO OUTER PARENS
"""
# EXAMPLE 1- Normal assert behavior
x = -1
assert x > 0, "x must be positive"
print("Program continues")

"""
Since x > 0 is False:
→ Python raises AssertionError
→ Program stops
→ "Program continues" does NOT print
"""
######################################################################################################################
#example2: Assertion with a custom message
age = 25 
assert age >= 18, "Age must be 18 or older"

# age = 15
# assert age >= 18, "Age must be 18 or older" #output: AssertionError: Age must be 18 or older
######################################################################################################################

#example3: validate function inputs (development time)
def divide(a, b):
    assert b != 0, "Can not divide by zero"
    return a/b 
print(divide(10,2)) #5.0 
#print(divide(10,0)) #AssertionError: Cannot divide by zero 
######################################################################################################################

#example4: confirm a type before processing 
def calculate_total(items): 
    assert isinstance(items, list), "items must be a list"
    return sum(items)

print(calculate_total([1,2,3])) #6



"""
---------------------------------------------------------
EXAMPLE 5- assert in optimization mode
---------------------------------------------------------
If you run:
    python -O script.py
Python removes assert statements internally.
So the code behaves like this:
"""

x = -1
# assert x > 0, "x must be positive"   (Removed in -O mode)
print("Program continues")

"""
Output:
Program continues

Because assert was ignored.
"""
