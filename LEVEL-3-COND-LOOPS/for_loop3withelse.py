# Enhancing Loop Functionality with Else in Python
"""
Condistderation for else. 
1) It's important to note that the else clause inloops is not an alternative to using if statements.
It serves as a different purpose by providing a way to execute code after the loop finishes provided it wasn't terminated 
prematurely by a break.

2) Else clause executes after normal loop termination.The else clause only executes if the loop completes all iterations normally.
If the loop is terminated by a break statement,the else clause will not be executed.

Note:
When to Use Else in Loops:
a) Confirmation of Loop Completion: Useful in search algorithms to confirm the loop ran without a break.

b)Searching Within Lists:
-> Break if item is found, preventing else execution.
-> Else executes if the item isn't found.

-> Validating Inputs: Confirms conditions smoothly if no interruptions occur.
-> While Loops: Apply with while loops for continuity checks.

Important Notes:
Else isn't an alternative to if but complements it.
Only activates after a full loop without breaks.
"""
#example1: 
for i in range(5):
    print(i) #This will print numbers from 0 to 4, and then the else block will execute after the loop finishes.
else:
    print("Loop just finished!") #This will print "Loop just finished!" after the loop completes all iterations without encountering a break statement.
"""
output: 
0
1
2
3
4
Loop just finished!
"""
#example2: searching for an item in the list 
fruits = ["apple", "banana", "cherry", "date", "fig"]
search_item = "grapefruit"
for fruit in fruits:
    if fruit == search_item:
        print(f"{search_item} found in the list!")
        break
else:
    print(f"{search_item} not found in the list.")
#output:grapefruit not found in the list.

#example3: validating input data 
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number < 0:
        print("Negative number found, stopping validation.")
        break
else:
    print("All numbers are positive. Validation successful.")
#output: All numbers are positive. Validation successful.