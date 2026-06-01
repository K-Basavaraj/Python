"""
BREAK:
--------------------------------------------------------------------------------------------------------------------------
If we want to end our looping logic early or under a certain condition,we can use a brake statement 
to do this efficiently.
The break statement terminates our loop when a specified condition is met,preventing the loop from continuing to execute.

why we want to close a loops? 
We want and need to close loops efficiently to prevent them from running indefinitely,which could lead to endless loops.
Endless loops occur when the loops terminating condition is never met,causing the program to run forever and potentially crash 
or become unresponsive.
---------------------------------------------------------------------------------------------------------------------------
"""
#example1: endless loop using Python and how we can close our loops.
"""
count = 0
while True:  # This creates an infinite loop
    print("this loop will run forever, and ever, and ever unless we break it")
    count += 1

This loop will run indefinitely because the condition is always True.
To prevent this, we can use a break statement to exit the loop when a certain condition is met.
"""
#example2: using break to prevent an infinite loop
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

#example3: break in a for loop
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

#example4: braek only stop at first search 
numbers = [ 1, 3, 5, 7, 9, 11]
for n in numbers: 
    if n > 6: 
      print(f"Found {n} -> stopping")
"""
output: 
Found 7 -> stopping
Found 9 -> stopping
Found 11 -> stopping
"""
###########################################################################################################################

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