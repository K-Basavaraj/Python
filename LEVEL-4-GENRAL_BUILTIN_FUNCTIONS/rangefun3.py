#Custom Start and End: Specify both starting and ending points with range(start, end).

for i in range(1,7):
    print(f"Number {i}")

"""
Number 1
Number 2
Number 3
Number 4
Number 5
Number 6
"""
for i in range(0, 10):
    print(i) #it prints 0-9 because the end point is exclusive, meaning it stops before reaching 10.

for i in range(5,10):
    print(i) #it prints 5-9 because the end point is exclusive, meaning it stops before reaching 10.
#=========================================================================================================================
#Incorporating Steps: Add a step value to control the increment between numbers. Example: range(0, 20, 5) generates 0, 5, 10, 15.
for i in range(0,10, 2):
    print(i) #it prints 0,2,4,6,8 because the step value of 2 means it increments by 2 each time, starting from 0 and stopping before 10.

for i in range(1, 10, 2):
    print(i) #it prints 1,3,5,7,9 because the step value of 2 means it increments by 2 each time, starting from 1 and stopping before 10.

for i in range(0, 10, 5):
    print(i, end=" ") #it prints 0,5 because the step value of 5 means it increments by 5 each time, starting from 0 and stopping before 10.
#=========================================================================================================================
x = range(6)
for n in x:
  print(n)

print(list(range(5))) #it prints [0, 1, 2, 3, 4] because range(5) generates numbers starting from 0 up to but not including 5, resulting in a list of the first five non-negative integers.
print(list(range(1, 6))) #it prints [1, 2, 3, 4, 5] because range(1, 6) generates numbers starting from 1 up to but not including 6, resulting in a list of the first five positive integers.
print(list(range(5, 20, 3))) #it prints [5, 8, 11, 14, 17] because range(5, 20, 3) generates numbers starting from 5 up to but not including 20, incrementing by 3 each time. This results in the sequence of numbers: 5, 8, 11, 14, and 17.