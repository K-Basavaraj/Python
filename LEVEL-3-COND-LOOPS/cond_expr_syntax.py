################################################################################################
                            # Part 3: Conditions & Statements Syntax
################################################################################################
"""
name = "Basavaraj"
if name == "Basavaraj" :
print(name)

 print(name)
    ^^^^^
IndentationError: expected an indented block after 'if' statement on line 5

You have to use the same number of spaces in the same block of code, otherwise 
Python will give you an error:
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
"""
################################################################################################
# case1: if statement
name = "Basavaraja"
if name == "Basavaraja":
    print(name)
#output: Basavaraja

# case2: if-else statement
x = 3
if x > 5:
    print( x, " is greater than 5")
else:
    print( x, " is not greater than 5")

# case3: Nested if
x = 15
if x > 10:
    if x < 20:
        print( x, " is between 10 and 20")

# case4: Single-line if (short-hand)
x = 7
if x > 5: print( x, " is greater than 5")

# case5: Short-hand if-else (ternary expression)
x = 4
result = "Even" if x % 2 == 0 else "Odd"
print(result)  # Output: Even
################################################################################################
# case6: pass statement (do nothing placeholder)
# Python does not allow empty blocks (if, for, while, def, class).
# pass is used when you want the block to do nothing but still be valid.
"""
Error example (empty if block)
x = 10
if x > 5:
    # nothing here
print("After if")

# Output:
# IndentationError: expected an indented block
"""
x = 10
if x > 5:
    pass   # placeholder, does nothing
print("After if")

# Output:
# After if
################################################################################################
