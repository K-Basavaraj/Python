"""
---------------------------------------------------------
1) WHAT IS finally?
---------------------------------------------------------
'finally' is an optional block after try/except. 
The finally block ALWAYS executes. - no matter what 
if the try block sucessds -> finally runs and 
if an error happens and is caught ->  finally runs 
if an error happens and is not caught -> finally still runs 
It runs also 
-> Even if return is used
-> Even if break is used

Main purpose:
Cleanup operations such as:
- Closing files
- Closing database connections
- Releasing network resources

summary: Run cleanup code that always executes, wether an error occurred or not. 

syntax: 
try:
    <code> 
except: 
    <handle error> 
finally:
    <cleanup-always runs> 
"""

#example1:  finally always runs (sucess case) 
try: 
    print("trying..")
    result = 10/2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("caught zero division error")
finally: 
    print("Finally block - always runs")
"""
output: 
trying..
Result: 5.0
Finally block - always runs
"""
###################################################################################################################
#example2: finally also runs when error occurs 
try: 
    print("trying..")
    result = 10/0
    print(f"Result: {result}")
except ZeroDivisionError:
    print("caught zero division error")
finally: 
    print("Finally block - always runs")
"""
output: 
trying..
caught zero division error
Finally block - always runs
"""
###################################################################################################################
#example3: finally  without except - still runs 
try: 
    print("Doing work")
finally:
    print("cleanup done")
"""
output: 
Doing work
cleanup done
"""
###################################################################################################################
#EXAMPLE 4 - File handling with finally even if reading the file fails we still want to close it. 
file = open("notes.txt", "r") # Open notes.txt for reading; on Windows, Notes.txt and notes.txt are treated as the same file

try: 
  content = file.read()    # Read the content of the file
except Exception as e:      # Handle any error that occurs while reading the file
    print(f"Error: {e}")
finally:                     # This block always executes, whether an error occurs or not
    print("File closed safely")
    try:
        file.close()     # Attempt to close the file
    except:  # Ignore the error if the file was not opened successfully
        pass

"""
output: 
Traceback (most recent call last):
  File "E:\Python\LEVEL-3-KEYWORDS\02-ERROR-HANDLING\12_finally.py", line 75, in <module>
    file = open("notess.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'notess.txt'

#output: File closed safely

# Note:
# In modern Python, we prefer using 'with' statement 
# instead of finally for file handling.
# Example:
with open("file.txt", "r") as f:
    data = f.read()

# 'with' automatically handles cleanup.
"""
###################################################################################################################
#example5: finally runs even when 'return is used inside try
def divide(a,b): 
    try: 
        return a/b
    except ZeroDivisionError: 
        return  None
    finally: 
        print("Function ending - running cleanup")
    
result = divide(10,2)
print(f"Got: {result}")
"""
output: 
Function ending - running cleanup
Got: 5.0
"""