"""
what is ZIP()? 
zip() takes 2 or more iterabvles and pairs them up position by position, like realworld zipper. 
It returns pairs (tuples) one at a time. so you can loop through multiple sequences together. 

in summary: zip() loop two or more list side by side The problem it solves sometimes, we have 
two parallel lists and need to loop through them together.

syntax: zip(iter1, itr2)
zip(iter1, itr2, itr3, ..) #any number of inputs

Note: ZIp() stops at the shortest list 
if your lists are different lengths zip() silenty stops at the end of the shortest one


Key-points: 
-> stops at the shortest iterable(silent- no error)


when to use: 
use it whenever your loop needs to know 
-> the position of the item in the list ("step3 od 10")
-> To make decisions based on index ("The first one is special")
-> To Produce numbered output in reports/logs
"""
##############################################################################################################################

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
##############################################################################################################################

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
web3 and web4 are silently skipped No error, no warning. this can hid bugs. always makesure list are same length or 
check 
"""
if len(servers) != len(ips):
    print("List are in different sizes")

#example5: ZIP() + DICT(): 
names = ["web-01", "web-02", "web-03"]
ips = ["10.0.1.4", "10.0.1.5", "10.0.1.6"]
inventory = dict(zip(names, ips))
print(inventory) #{'web-01': '10.0.1.4', 'web-02': '10.0.1.5', 'web-03': '10.0.1.6'}