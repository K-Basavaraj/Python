"""
enumarator(tup) gives (index, item) pairs 
Loops through a tuple and gives us the poistion(index) too. 

synatx: 
for i, item in enumerate(tup):
for i, item in enumerate(tup, start=N):
"""

#example: old way manul counter 
fruits = ("apple", "banana", "cherry")
i = 0 
for fruit in fruits: 
    print(i, fruit)
    i += 1
"""
0 apple
1 banana
2 cherry
"""
#example2: 
fruits = ("apple", "banana", "cherry")
for i, fruit in enumerate(fruits):
    print(i, fruit)
"""
0 apple
1 banana
2 cherry
"""
#example3: start counting from 1 or any number by defult enumerate starts at 0 
steps = ("login", "navigate", "click", "logout")
for i, step in enumerate(steps, start=1): 
    print(f"step{i}: {step}")

"""
step1: login
step2: navigate
step3: click
step4: logout
"""