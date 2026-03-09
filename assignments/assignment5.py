#Exercise 2: Closing Loops
"""
Part 1: Using break to Exit a Loop Early
Sometimes, we want to stop a loop once a specific condition is met, rather than letting it run to completion. 
The break statement allows us to exit a loop immediately as soon as a certain condition is achieved.

In the below:
 Create a loop that iterates from 0 to 9
 Use break to exit the loop if the iterator variable reaches 7
 Inside the loop, add a print statement so that each number (hint: the iterator variable) is printed before the loop breaks
"""
for i in range(10):
    if i == 7:
        break
    print(i)
  
print("-----------------------------")
"""
Part 2: Using continue to Skip Iterations
In contrast to the break statement, the continue statement allows us to skip the rest of the code inside the loop for 
the current iteration and move directly to the next iteration.

Instead of stopping our code from running, this will allow us to skip "a step" and then continue moving along the loop's 
path of execution.

By combining continue with our modulus operator that we learned about, we can check if a number is odd, or as you'll 
be doing, checking if the numbers we can skip "aren't even" (hint) so we only print even numbers and avoid the odd ones.

In the below:
 Create a loop that iterates from 0 to 9
 Use continue to skip odd numbers
 Print only even numbers in the loop
"""
for j in range(1,10):
    if j % 2 != 0:
      continue
    print(j)   

print("-----------------------------")
#output: 2,4,6,8

"""
Part 3: Preventing Infinite Loops with while
When writing your while loops in Python, it’s essential to ensure that the loop’s condition will eventually become False. 
Otherwise, you risk creating an infinite loop that never ends.

The reason for this is that loops will run when a condition is True, meaning, Python will assume you want to run your code, 
of course. But to prevent it from running indefinitely, you'll need to tell Python when a certain condition is achieved, 
meaing there is no reason to continue running the code until it's invoked again.

In the below:
 Create a variable count and set it equal to 0
 Write a while loop that runs as long as count is less than 20
 Print the value of count in each iteration as an f-string like this: "Count: {count}" where {count} is replaced with the value of the incrementor in your while loop
 Ensure the while loop increments count by 1 to ensure the loop will eventually stop
"""
count = 0

while count < 20:
    print(f"count:{count}")
    count += 1
print("-----------------------------")

"""
Part 4: Practical Use of break and continue
Now that we're more familar with break and continue, let's use these these keywords in a real-world nested loops 
can help control complex loop structures. Here’s an example of how to search for a specific item in a list and stop once 
it’s found.

In the below:
 Create a variable called fruits and set that equal to a list of these 4 fruits (each item as a string): "apple", "banana", "cherry", "grapefruit"
 Write a for loop to iterate over the list of fruits
 Use break to stop the loop if the current fruit is "cherry"
 Inside of the break statement, the loop should print "{fruit_that_was_found} found! Stopping the loop." where fruit_that_was_found is the item that an if statement checks that fruit name against the list of all fruits
 Print each fruit name until the loop breaks.
"""
fruits = ["apple", "banana", "cherry", "grapefruit"]
current_fruit = "cherry"

for fruit in fruits: 
    if fruit == current_fruit:
        print(f"{fruit} found! Stopping the loop.")
        break
    print(fruit)