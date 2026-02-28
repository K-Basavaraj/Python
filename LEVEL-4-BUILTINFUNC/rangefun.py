#example1: Basic Usage
for i in range(5):
    print(i)

"""
This for loop will print the value of the incrementer for a range of five.
There'll be five numbers printed,starting from index 0 toPosition 5, 0,1,2,3,4.Overall, 
this loop will print numbers 0-4 due to the range of five
output:
0
1
2
3
4
"""
# example2: iterate over a specific sequence of numbers. using a range of 10 generates numbers 0-9,enabling us to run a loop exactly 10 times.
for i in range(10):
    print(f"Iteration {i}")
    
"""
Iteration 0
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
Iteration 6
Iteration 7
Iteration 8
Iteration 9
"""