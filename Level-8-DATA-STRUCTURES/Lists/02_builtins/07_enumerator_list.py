"""
what is enumerator()? 
enumertor() is a builtin function that adds a counter(index)  to anything you can loop through. 

insted of just getting the item you get a (index, item) pair on every iteration 

syntax: enumerate(iterable)
enumerate(iterable, start=N) #WHERE CHNAGE STARTING INDEX

Key-points: 
-> enumerator() give you(index, item) pairs wile looping 
-> default index starts at 0 - use start=N to chnage it
-> cleaner than manual using a counter varibale
-> works on ANY iterable

when to use: 
use it whenever your loop needs to know 
-> the position of the item in the list ("step3 od 10")
-> To make decisions based on index ("The first one is special")
-> To Produce numbered output in reports/logs
"""
#old way: 
servers = ["web1", "web2", "web3", "db-01"]
i = 0 
for server in servers: 
    print(f"{i}: {server}")
    i += 1

#or even worse using range(len(..))
for i in range(len(servers)):
    print(f"{i}: {servers[i]}")

#Both work, but theyre noisy and not very pythonic. 

###########################################################################################
#new way: using enumerate() function
server = ["web1", "web2", "web3", "db-01"]
for i, serv in enumerate(servers):
    print(f"{i}: {serv}")
#output:
"""
0: web1
1: web2 
2: web3
3: db-01
#enumerate() function  gives (index, item) pairs for each item in the iterable.
"""

#example2: starting with a different number instead of 0 By defult, indexes starts at 0, we can chnage with start=:
instances = ["ec2-01", "ec2-02", "ec2-03"]

for i, instance in enumerate(instances, start=1):
    print(f"{i}: {instance}")

#output:
"""
1: ec2-01
2: ec2-02
3: ec2-03

USE START=1, WHENEVER YOUR PRINTING HUMAN-READABLE LIST(DONT COUNT FROM ZERO)
"""
#EXAMPLE3: 
steps = [
    "Build Docker image",
    "push to registry",
    "Apply Kubernetes manifest",
    "Run smoke tests"
]

print("Deployment plan:")
for i, step in enumerate(steps, start=1):
    print(f"{i}. {step}")   

#output:
"""
Deployment plan:
1. Build Docker image
2. push to registry
3. Apply Kubernetes manifest
4. Run smoke tests
"""


#example4: find postion of first problem 
checks = ["pass", "pass", "fail", "pass"]

for i, status in enumerate(checks):
    if status == "fail":
        print(f"First failure at check {i}") #output: First failure at check 2 here we have used the enumerate function to loop through the checks list and find the position of the first failure. The enumerate function gives us both the index (i) and the value (status) for each item in the list. When we find a status that is "fail", we print out the index of that failure, which is 2 in this case since the first failure occurs at index 2 in the checks list.
        break #we can use break to stop the loop after finding the first failure, since we only care about the position of the first failure and not any subsequent failures.   

#output:
"""
First failure at check 2
"""