"""
=========================================================
BREAK & CONTINUE IN PYTHON
=========================================================

BREAK:
---------------------------------------------------------
- Used only inside loops (for / while).
- Immediately exits the nearest loop.
- Stops further iterations completely.

CONTINUE:
---------------------------------------------------------
- Used only inside loops.
- Skips the remaining code in the current iteration.
- Moves control back to the loop condition.
- Does NOT stop the loop completely.

=========================================================
EXAMPLE 1 : break
=========================================================

This example keeps asking the user for input.
The loop runs forever (while True).
When user types "exit", break stops the loop.
"""

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
EXPECTED OUTPUT:

Number: 1
Number: 2
Skipping 3
Number: 4
Number: 5

Explanation:

When i == 3:
- "Skipping 3" prints
- continue runs
- print("Number:", i) is skipped
- Loop moves to next iteration

continue does NOT stop the loop.
It only skips one iteration.
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
INTERVIEW SUMMARY
=========================================================

break is used to terminate a loop early when a condition is met.

continue is used to skip specific iterations without stopping the loop.

=========================================================
"""

"""
=========================================================
EXAMPLE 3 : continue with filtering even numbers
=========================================================

This example prints only odd numbers between 1 and 10.
Even numbers are skipped using continue.
"""

for number in range(1, 11):

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
