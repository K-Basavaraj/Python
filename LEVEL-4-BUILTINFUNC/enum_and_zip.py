"""
enumeratory() and zip() functions in Python are powerful tools for working with iterables.
These bOTH work with any iterable, but you'll use them most with lists. 

when to use: 
use it whenever your loop needs to know 
-> the position of the item in the list ("step3 od 10")
-> To make decisions based on index ("The first one is special")
-> To Produce numbered output in reports/logs
"""
#example1: enumerate() function Loop with index
#you often need both the 'tem' and 'index' while looping. 
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
##########################################
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
##############################################################################################################################
"""
zip() loop two or more list side by side 
The problem it solves sometimes, we have two parallel lists and need to loop through them together.

Note: ZIp() stops at the shortest list 
if your lists are different lengths zip() silenty stops at the end of the shortest one
"""
#example1: 
servers = ["web1", "web2", "web3"]
ips = ["10.0.1.1", "10.0.1.2", "10.0.1.3"]

#old way:
for i in range(len(servers)):
    print(f"{servers[i]} has IP {ips[i]}")
#output:
"""
web1 has IP 10.0.1.1
web2 has IP 10.0.1.2
web3 has IP 10.0.1.3

works but ugly. IF EITHER LIST IS SHORTER, RISK OF INDEX ERROR
"""
#EXAMPLE2: CLEAN WAY: using zip() function
for server, ip in zip(servers, ips):
    print(f"{server} has IP {ip}")  

#output:
"""
web1 has IP 10.0.1.1
web2 has IP 10.0.1.2
web3 has IP 10.0.1.3

pairs up items from the two lists together.
"""
#example3: zip() with more than two lists

names = ["web-01", "web-02", "web-03"]
ips = ["10.0.1.4", "10.0.1.5", "10.0.1.6"]
roles = ["frontend", "database", "backend", "frontend"]

for name, ip, role in zip(names, ips, roles):
    print(f"{name} ({role} at {ip})")
"""
output: 
web-01 (frontend at 10.0.1.4)
web-02 (database at 10.0.1.5)
web-03 (backend at 10.0.1.6)
"""

#example2: 
servers = ["web1", "web2", "web3", "web4"]
ips = ["10.0.1.1", "10.0.1.2"]

for s, i in zip(servers, ips): 
    print(s, i)
"""
output: 
web1 10.0.1.1
web2 10.0.1.2
web3 and web4 are silently skipped No error, no warning. this can hid bugs. always makesure list are same length or check 
"""
if len(servers) != len(ips):
    print("List are in different sizes")

#example5: ZIP() + DICT(): 
names = ["web-01", "web-02", "web-03"]
ips = ["10.0.1.4", "10.0.1.5", "10.0.1.6"]
inventory = dict(zip(names, ips))
print(inventory) #{'web-01': '10.0.1.4', 'web-02': '10.0.1.5', 'web-03': '10.0.1.6'