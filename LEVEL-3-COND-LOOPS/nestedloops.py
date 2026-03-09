"""
Nested loops allow incorporating a loop within another loop, enabling more complex data processing. 
This concept is crucial for Python programming when handling tasks that involve repeated actions on datasets.
"""
#example1: without nested loop
for i in range(1,5):  
    print(f"itetration: {i}") #This will print the current iteration number from 1 to 4.
"""
output:
itetration: 1
itetration: 2
itetration: 3
itetration: 4
"""
#example2: 
fruits = ["apple", "banana", "cherry", "grapefruit"]
for i in range(1,5):  #This outer loop will iterate 4 times, with i taking values from 1 to 4.
    for fruit in fruits: #This inner loop will iterate over each fruit in the fruits list for every iteration of the outer loop.
        print(f"iteration: {i}, fruit: {fruit}") #This will print the current iteration number along with each fruit in the list for every iteration of the outer loop.
"""
output: 
iteration: 1, fruit: apple
iteration: 1, fruit: banana
iteration: 1, fruit: cherry
iteration: 1, fruit: grapefruit
iteration: 2, fruit: apple
iteration: 2, fruit: banana
iteration: 2, fruit: cherry
iteration: 2, fruit: grapefruit
iteration: 3, fruit: apple
iteration: 3, fruit: banana
iteration: 3, fruit: cherry
iteration: 3, fruit: grapefruit
iteration: 4, fruit: apple
iteration: 4, fruit: banana
iteration: 4, fruit: cherry
iteration: 4, fruit: grapefruit

How Nested Loops Work
Outer Loop iterates over a sequence, such as a range of numbers.

Example: for i in range(1, 5)
Inner Loop runs for each iteration of the outer loop, further iterating over another dataset.

Example: for fruit in ['apple', 'banana', 'cherry', 'grapefruit']
Execution: The outer loop completes one cycle, and within each cycle, the inner loop completes its full cycle.

Iteration Example:
First, i = 1, inner loop iterates over all fruits.
Then, i = 2, inner loop reiterates over all fruits.
Output
For an outer loop range of 1 to 4 and four fruits, expect outcomes like:
Iteration 1: apple, banana, cherry, grapefruit
Iteration 2: apple, banana, cherry, grapefruit
"""