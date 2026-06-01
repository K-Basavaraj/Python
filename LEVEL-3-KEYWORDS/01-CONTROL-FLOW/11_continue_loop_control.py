"""
CONTINUE:
--------------------------------------------------------------------------------------------------------------------------

continue statement to control loop execution in Python. The continuous statement skips the rest of the code inside the 
loop for the current iteration and moves to the next iteration.

- Skips the remaining code in the current iteration.
- Moves control back to the loop condition.
- Does NOT stop the loop completely.
---------------------------------------------------------------------------------------------------------------------------
"""
"""
=========================================================
EXAMPLE 1 : continue only - skips certain items example with filtering even numbers
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