#using append() with a list 
a  = ["web1", "web2"]
a.append(["web3", "web4"])
print(a) 
#output: ['web1', 'web2', ['web3', 'web4']] here we have a list of two items, which are web1 and web2. When we use the append method to add another list, which contains web3 and web4, it adds the entire list as a single item to the original list. So the original list now contains three items: web1, web2, and the new list ['web3', 'web4'].  a list inside a list! Not what we wanted.

#using extend() with a list
b = ["web1", "web2"]
b.extend(["web3", "web4"])
print(b)
#output: ['web1', 'web2', 'web3', 'web4'] here we have a list of two items, which are web1 and web2. When we use the extend method to add another list, which contains web3 and web4, it adds each item in the new list as separate items to the original list. So the original list now contains four items: web1, web2, web3, and web4. This is what we wanted!

"""
append() adds the things as a single item (even if its a list)
extend() unpacks the items and adds each element as a separate item to the list.
"""
#######################################################################################################################
#scenario:  your collecting ec2 instnaces from multiple aws regions and want one combine list: 

all_instances = []

us_east_instances = ["i-1234567890abcdef0", "i-0987654321abcdef0"]
us_west_instances = ["i-1122334455667788", "i-2233445566778899"]
ap_southeast_instances = ["i-3344556677889900", "i-4455667788990011"]

all_instances.extend(us_east_instances)
all_instances.extend(us_west_instances)
all_instances.extend(ap_southeast_instances)

print(all_instances) 
#output: ['i-1234567890abcdef0', 'i-0987654321abcdef0', 'i-1122334455667788', 'i-2233445566778899', 'i-3344556677889900', 'i-4455667788990011'] here we have a list of all the instances from the three regions, which is what we wanted. If we had used append instead of extend, we would have ended up with a list of three items, which are the three lists of instances, instead of a single list of all the instances.