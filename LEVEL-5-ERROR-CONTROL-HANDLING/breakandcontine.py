"""
=========================================================
BREAK & CONTINUE IN PYTHON
=========================================================
BREAK:
--------------------------------------------------------------------------------------------------------------------------
If we want to end our looping logic early or under a certain condition,we can use a brake statement 
to do this efficiently.
The break statement terminates our loop when a specified condition is met,preventing the loop from continuing to execute.

why we want to close a loops? 
We want and need to close loops efficiently to prevent them from running indefinitely,which could lead to endless loops.
Endless loops occur when the loops terminating condition is never met,causing the program to run forever and potentially crash 
or become unresponsive.
"""
#example1: break in a for loop
for i in range(10):
    if i == 5:
        break   # Exit the loop immediately when i is 5
    print("Current value of i:", i)
"""
output: 
Current value of i: 0
Current value of i: 1
Current value of i: 2
Current value of i: 3
Current value of i: 4
"""
#example2: endless loop using Python and how we can close our loops.
"""
count = 0
while True:  # This creates an infinite loop
    print("this loop will run forever, and ever, and ever unless we break it")
    count += 1

This loop will run indefinitely because the condition is always True.
To prevent this, we can use a break statement to exit the loop when a certain condition is met.
"""
#example3: using break to prevent an infinite loop
count = 0
while True:  # This creates an infinite loop
    print("this loop will run forever")
    count += 1
    if count > 10:  # Break the loop after 10 iterations
        print("Breaking the loop to prevent it from running indefinitely.")
        break
"""
output: 
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
this loop will run forever
Breaking the loop to prevent it from running indefinitely.
"""

#EXAMPLE 4 : This example keeps asking the user for input. The loop runs forever (while True). When user types "exit", break stops the loop.
while True:
    user_input = input("Type 'exit' to stop: ")

    if user_input.lower() == "exit":
        print("Breaking loop...")
        break   # Exit the loop immediately

    print("You typed:", user_input)

print("Loop ended.")


"""
EXPECTED BEHAVIOR:

If user types:
hello
You typed: hello

If user types:
exit
Breaking loop...
Loop ended.

Notice:
After break runs, the loop stops completely.
Execution continues after the loop.
"""
#=========================================================================================================================
"""
CONTINUE:
--------------------------------------------------------------------------------------------------------------------------

continue statement to control loop execution in Python. The continuous statement skips the rest of the code inside the 
loop for the current iteration and moves to the next iteration.

- Skips the remaining code in the current iteration.
- Moves control back to the loop condition.
- Does NOT stop the loop completely.
"""
"""
=========================================================
EXAMPLE 1 : continue with filtering even numbers
=========================================================

This example prints only odd numbers between 1 and 10.
Even numbers are skipped using continue.
"""

for number in range(10):

    # If number is even, skip this iteration
    if number % 2 == 0:
        continue

    # This runs only for odd numbers
    print("Odd number:", number)


"""
EXPECTED OUTPUT:

Odd number: 1
Odd number: 3
Odd number: 5
Odd number: 7
Odd number: 9

Explanation:

When number is even:
- Condition becomes True
- continue executes
- Remaining code is skipped
- Loop moves to next number

When number is odd:
- Condition becomes False
- continue does NOT run
- print statement executes
"""


"""
=========================================================
EXAMPLE 2 : continue
=========================================================

This example prints numbers from 1 to 5.
When number is 3, continue skips that iteration.
"""

for i in range(1, 6):

    if i == 3:
        print("Skipping 3")
        continue   # Skip the rest of this iteration

    print("Number:", i)

"""
output:
Number: 1
Number: 2
Skipping 3
Number: 4
Number: 5
"""

"""
=========================================================
KEY DIFFERENCE BETWEEN break AND continue
=========================================================

break:
→ Stops the entire loop immediately.

continue:
→ Skips current iteration only.
→ Loop continues with next value.

=========================================================
SUMMARY
=========================================================

break is used to terminate a loop early when a condition is met.

continue is used to skip specific iterations without stopping the loop.

=========================================================
"""

