"""
Exercise 1: Loops
In this exercise, you'll practice writing loops in Python with various scenarios, focusing on the range() function, 
controlling loop flow with else, and using break and continue.

Part 1: Basic Use of range()
The range() function in Python generates a sequence of numbers, which is very useful when working with loops.
It simplifies the process of iterating over a sequence, such as printing a range of numbers or running a loop 
for a set number of times.

In the cell below:
 Write a for loop for number that uses the range() function to print numbers from 0 to 4
 Write a for loop for i that uses the range() function to print "Iteration: i" over 10 iterations as 
 an f-string with i being passed in dynamically for each iteration

An f-string is way to write a string with data in it dynamically. An example of what this could look like is: 
f"The file to use is: {file_name}" and the {file_name} is how we pass in the value of another variable into the entire string. 

If file_name = "report.pdf", then the string would read: `"The file to use is: report.pdf"
"""
#part1: Write a for loop for number that uses the range() function to print numbers from 0 to 4
for i in range(5):
    print(i)

#part1.1: Write a for loop for i that uses the range() function to print "Iteration: i" over 10 iterations as an f-string with i being passed in dynamically for each iteration
for i in range(10):
    print(f"Iteration: {i}")

"""
Part 2: Using range() with Start, End, and Step Arguments
The range() function is very versatile and can take optional arguments to specify a start, an end, and a step size (increment) in Python.

All of these options allow you to control where your sequence begins, ends, and how much it increments by in each step.

In the cell below:
 Write a for loop for i that uses the range() function to print numbers from 2 to 6
 Write a for loop for i that uses the range() function with a step of 2 to print the numbers from 0 to 10
"""
#part2: write a for loop for i that uses the range() function to print numbers from 2 to 6
for i in range(2,7):
    print(i)
print('---------')
#part2.1: Write a for loop for i that uses the range() function with a step of 2 to print the numbers from 0 to 10
for i in range(0, 10, 2):
    print(i)

"""
Part 3: Using else with Loops
Python loops can include an else clause, which executes when the loop completes all iterations without encountering a break.

This nifty else clause can be very useful for confirming that a loop ran successfully or for running final code 
after a loop has processed all items, such as all the iterations defined by the range() as you'll practice in a moment.

In the cell below:
 Write a for loop for i that iterates over range(5) and prints each iteration i
 Add an else clause that prints "Loop just finished!" once the loop completes
"""
#part3: Write a for loop for i that iterates over range(5) and prints each iteration i
for i in range(5):
    print(i)
#part3.1: Add an else clause that prints "Loop just finished!" once the loop completes
else:
    print("Loop just finished!")

"""
Part 4: Using break and continue in Loops
In Python, break and continue are powerful statements for controlling loop execution.

break ends the loop early once a certain condition is met (i.e. a condition is True)
continue skips the rest of the current loop iteration and moves to the next one
In the cell below:
 Write a for loop for i with range(10)
 Add a condition to break the loop when i == 5
 Print each number before the loop breaks
 Create another for loop for i with range(10)
 Use continue to skip i == 5 instread of breaking at i == 5 like before
"""
#part4: Write a for loop for i with range(10)
print("Loop with break:")
for i in range(10):
    if i == 5:
        break
    print(i)
#part4.1: Create another for loop for i with range(10)
print("Loop with continue:") 
for i in range(10):
    if i == 5:
        continue
    print(i)