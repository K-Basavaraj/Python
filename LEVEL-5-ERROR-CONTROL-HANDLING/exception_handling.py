"""
=========================================================
EXCEPTION HANDLING IN PYTHON
try | except | finally | raise
=========================================================

WHAT IS AN EXCEPTION?

An exception is an error that occurs during program execution.
If not handled, it stops the program.

---------------------------------------------------------
1️⃣ WHAT IS try?
---------------------------------------------------------

The try block contains code that might raise an error.
It allows us to test risky code safely.

---------------------------------------------------------
2️⃣ WHAT IS except?
---------------------------------------------------------

The except block handles the error gracefully.
It runs only if an exception occurs inside the try block.

---------------------------------------------------------
3️⃣ WHAT IS finally?
---------------------------------------------------------

The finally block ALWAYS executes.

It runs:
✔ If no error occurs
✔ If an error occurs
✔ Even if return is used
✔ Even if break is used

Main purpose:
Cleanup operations such as:
- Closing files
- Closing database connections
- Releasing network resources

---------------------------------------------------------
4️⃣ WHAT IS raise?
---------------------------------------------------------

The raise keyword is used to manually throw an exception.

It is used when:
✔ You want to enforce validation rules
✔ You detect invalid data
✔ You want to stop execution intentionally

raise does NOT handle errors.
It CREATES errors.

try/except HANDLES errors.
raise THROWS errors.

---------------------------------------------------------
WHY WE USE EXCEPTION HANDLING?
---------------------------------------------------------

In real applications:
- User input may be invalid
- File may not exist
- API may fail
- Division by zero may occur
- Configuration may be wrong

Instead of crashing the program,
we handle errors safely.

=========================================================
SHORTER VERSION
=========================================================

Exception handling in Python is done using try, except, 
finally, and raise. The try block contains risky code, 
the except block handles errors, the finally block runs 
cleanup logic, and raise is used to manually throw 
exceptions when validation fails.

=========================================================
EXAMPLE 1 - Basic try/except
=========================================================
"""

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a valid integer.")


"""
=========================================================
EXAMPLE 2 - Multiple exceptions
=========================================================
"""

try:
    x = int(input("Enter number: "))
    result = 10 / x
    print("Result:", result)
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


"""
=========================================================
EXAMPLE 3 - finally (cleanup demonstration)
=========================================================
"""

print("\n----- Example: finally -----")

try:
    x = int(input("Enter a number: "))
    print("You entered:", x)
except ValueError:
    print("Invalid input.")
finally:
    print("This always runs (cleanup block).")


"""
=========================================================
EXAMPLE 4 - File handling with finally
=========================================================
"""

try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file.")
    try:
        file.close()
    except:
        pass


"""
Note:
In modern Python, we prefer using 'with' statement 
instead of finally for file handling.

Example:
"""

with open("file.txt", "r") as f:
    data = f.read()

# 'with' automatically handles cleanup.


"""
=========================================================
EXAMPLE 5 - raise (Manual Exception)
=========================================================
"""

print("\n----- Example: raise -----")

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")


"""
Why use raise instead of print?

If we only print:
    print("Invalid age")

Program continues with bad data.

If we raise:
    Execution stops immediately.
    Caller must handle the error.

This is safer in real applications.

=========================================================
EXAMPLE 6 - raise inside function (Professional Use)
=========================================================
"""

def validate_age(age):
    if age < 0:
        raise ValueError("Invalid age provided.")
    return age


try:
    validate_age(-1)
except ValueError as e:
    print("Error caught:", e)


"""
=========================================================
WHERE WE SHOULD NOT USE try/except
=========================================================

-> Do NOT use try/except to hide programming mistakes.
-> Do NOT use except: pass (bad practice).
-> Do NOT wrap entire large code blocks unnecessarily.

Bad Practice Example:
"""

try:
    print("undeclared_variable")
except:
    pass   # BAD: hides real bugs


"""
Good practice:
Catch specific exceptions only.

=========================================================
FINAL SUMMARY
=========================================================

try      → Test risky code
except   → Handle errors
finally  → Always run cleanup
raise    → Manually throw error

Design principle:
Low-level functions should raise errors.
High-level code should catch and handle them.

=========================================================
"""
