"""
range() there are situations where it might not be the best tool for the job. 
Let's explore three common scenarios where using range might not be ideal.
-> First, when working with large ranges,range can consume significant memory and slow down your program.
-> Second, range only works with integers.If you're dealing with floating point numbers or other types,
  a different approach is needed.
-> Third, when your loop needs to run based on a condition rather than a fixed number of iterations,
    a loop might be more appropriate here.
"""
"""
#example1: 
for i in range(100000):
    print(i) #This will print numbers from 0 to 99999, which can be overwhelming and may cause performance issues.
"""
"""
#example2: float with range function 
for i in range(0.0, 1.0, 0.1):
    print(i) #This will raise a TypeError because range does not support floating point numbers.
"""

#example3: insted of using range for a condition-based loop, we can use a while loop to achieve the same result without specifying a fixed number of iterations.
"""
start = 0.0
end = 1.0
step = 0.1

current = start

while current < end:
    print(f"correct use of while loop for floating-point numbers: {current}") #This will print numbers from 0.0 to 0.9 in increments of 0.1, which is a more suitable approach for this scenario.
    current += step
output:
correct use of while loop for floating-point numbers: 0.0
correct use of while loop for floating-point numbers: 0.1
correct use of while loop for floating-point numbers: 0.2
correct use of while loop for floating-point numbers: 0.30000000000000004
correct use of while loop for floating-point numbers: 0.4
correct use of while loop for floating-point numbers: 0.5
correct use of while loop for floating-point numbers: 0.6
correct use of while loop for floating-point numbers: 0.7
correct use of while loop for floating-point numbers: 0.7999999999999999        
correct use of while loop for floating-point numbers: 0.8999999999999999
correct use of while loop for floating-point numbers: 0.9999999999999999

This example demonstrates how to use a while loop to iterate over a range of floating-point numbers, 
which is not possible with the range function. The while loop allows us to control the iteration based on a condition, 
making it more flexible for scenarios where the number of iterations is not predetermined.
But there is a issues in output because of the nature of floating-point arithmetic in Python, which can lead to precision issues. 
How would we fix our code to solve for this? trustee format specification tool:.1f 
to format the floating point numbers withone decimal and avoid the precision issues we just saw here
"""
#example4: using trustee format specification tool:.1f to format the floating point numbers with one decimal and avoid the precision issues we just saw here
start = 0.0
end = 1.0
step = 0.1

current = start

while current < end:
    print(f"correct use of while loop for floating-point numbers: {current:.1f}") #This will print numbers from 0.0 to 0.9 in increments of 0.1, which is a more suitable approach for this scenario.
    current += step

#example5: 
for i in range(10):
    if i < 9:
       print(i, end=", ") #This will print numbers from 0 to 8 followed by a comma and a space, and the last number (9) will be printed without a comma.