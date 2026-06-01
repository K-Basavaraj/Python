"""
The else clause is not limited to for loops.It can also be used with while loops.
This can be useful for scenarios where you want to ensure that a condition was met throughout the entire loop,such as 
counting up to the limit and then printing a message at the end as while completes.
"""
#example1: 
count = 0
while count < 5:
    print(count) #This will print numbers from 0 to 4, and then the else block will execute after the loop finishes.
    count += 1
else:
    print("while loop completed with out Break") #This will print and after the loop completes all iterations without encountering a break statement.
"""
output:
0
1
2
3
4
while loop completed with out Break
"""
