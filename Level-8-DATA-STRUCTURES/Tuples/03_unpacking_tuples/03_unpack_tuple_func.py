"""
unpacking the result of a function 

functions that return multiple values return a tuple
unpacking lets grab those values clenly 
"""
def get_server_info(): 
   return "web-01", "10.0.0.0", "running"

#old way 
info = get_server_info()
name = info[0]
ip = info[1]
status = info[2]

#clean way of unpacking 
name, ip, status = get_server_info()
print(name) #web-01
print(ip) #10.0.0.0
print(status) #running
##################################################################################
"""
unpacking in a loop 
when looping through a tuple of tuples, we can un pack 
each inner tuple directly in the for loop 
"""
employees = (
   ("Alice", 30, "Engineer"),
   ("Bob", 25, "Designer"),
   ("charle", 35, "Manager")
)

for name, age, role in employees: 
   print(f"{name} ({age}) - {role}")
#Alice (30) - Engineer
#Bob (25) - Designer
#charle (35) - Manager
#######################################################################################
#example: unpacking nested tuples 
point_3d = ((1,2), 3)

(x,y),z = point_3d 
print(x,y,z) # 1 2 3
###############################################################################################
#example: 
db_config = ("local_host", 3306, "admin", "passwords123")
host, port, user, pw = db_config

print(f"{host}:{port} as {user}") #local_host:3306 as admin
###############################################################################################
#EXAMPLE: GET THE 1ST AND LAST ITEM CLEANLY 
items = (10, 20, 30, 40)
first, second, third, last = items
print(first, last) #10 40