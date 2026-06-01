"""
Pass is a unique statement that essentially does nothing.Think of it like a box of error that occupies space.
when you're writing Python code.It serves as a placeholder allowing you to define blocks of code that you plan to implement later on.
By using pass, you can avoidsyntax errors that occur when Python expects a block of code,but you're not ready to write it just yet.
Frequently, pass is used in loops, functions, classes,and conditional statements, when you want to outline the structure of your 
code without filling in all of the details immediately.

This is especially useful in incremental development,where you may want to keep certain parts ofyour code empty 
while you work on other sections.

In summary, Pass is a simple,yet effective way to maintain the flow of your code and prevent errors as you build out 
your functions and scripts.


The pass function in Python plays a critical role in writing code efficiently:

-> Purpose: It serves as a placeholder in programming, performing no action while occupying space.
-> Syntax Error Prevention: Pass helps avoid syntax errors by acting as a substitute when code blocks are required 
but not yet ready to be written.
-> Usage:
Often utilized in loops, functions, classes, and conditional statements.
Ideal for outlining code structure without immediate implementation.
-> Development Aid:
Especially beneficial during incremental development, allowing focus on different parts of code as needed.
In essence, the pass function is a straightforward yet powerful tool, enabling a smooth coding process by maintaining code 
flow and preventing errors until the full script is developed.

pass is a null operation.

It does NOTHING.

It is used as a placeholder when Python requires a block 
of code syntactically, but no action is needed.

pass = "Do nothing."
pass does NOT:
Stop execution
Skip next line
Exit loop
Raise error
It literally does nothing.

--------------------------------------------------------
WHEN TO USE pass?
---------------------------------------------------------
✔ Creating empty functions
✔ Creating empty classes
✔ Placeholder during development
✔ Required when block cannot be empty
"""
# ---------------------------------------------------------
# EXAMPLE 1- pass inside condition
# ---------------------------------------------------------
value = 10
if value > 5:
    pass   # No action needed
else:
    print("Value is small")

print("Program continues normally.")
print("---------------------------------------------------------")
# ---------------------------------------------------------
# EXAMPLE 2- pass inside loop with condition
# ---------------------------------------------------------
for i in range(5):
    if i == 3:
        pass  # No action needed when i is 3
    else:
        print("Number:", i)
print("---------------------------------------------------------")
# ---------------------------------------------------------
# EXAMPLE 3- pass inside function with condition
# ---------------------------------------------------------
def process_numbers():
    for i in range(5):
        if i == 3:
            pass 
        else:
            print("Processing number:", i)
process_numbers()
print("---------------------------------------------------------")
# ---------------------------------------------------------
# EXAMPLE 4- pass inside function
# ---------------------------------------------------------
def future_feature():
    pass   # To be implemented later
print("Function defined successfully.")
print("---------------------------------------------------------")
# ---------------------------------------------------------
# EXAMPLE 5- pass inside class
# ---------------------------------------------------------
class MyClass:
    pass
print("Class defined successfully.")