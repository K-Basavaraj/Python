#CHECK REUIRED PERMISSION

required_perms = { "read", "write" }
user_perms = {"read", "write", "delete"}

if required_perms.issubset(user_perms):
    print("Access Granted")
else: 
    print("Access deanied")
#o/p: Access Granted

#CHECK NO OVERLAP BETWEEN ENVIRONMENTS 
prod_servers = {"web-01", "web-02"}
dev_servers = {"dev-01", "dev-02"}

if prod_servers.isdisjoint(dev_servers):
    print("Environments are properly isolted")

#o/p:  Environments are properly isolted