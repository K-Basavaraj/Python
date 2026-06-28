#example: LIST of Dict - very common in real data 
#Many APis return a list where each item is a dict 

servers = [
    {
        "vm_name": "vm1",
        "ip_adress": "10.0.0.0"
    }, 
    {
        "vm_name": "vm2",
        "ip_adress": "10.0.0.1"
    }, 
    {
        "vm_name": "vm3",
        "ip_adress": "10.0.0.2"
    }, 
]

#Access one item 
print(servers[0])  #{'vm_name': 'vm1', 'ip_adress': '10.0.0.0'}
print(servers[2]) #{'vm_name': 'vm3', 'ip_adress': '10.0.0.2'}

print(f"Vm_name is: {servers[1]["vm_name"]}") #Vm_name is: vm2

#loop through and access nested data 
for server in servers:
    print(f"{server['vm_name']} -> {server["ip_adress"]}")
"""
vm1 -> 10.0.0.0
vm2 -> 10.0.0.1
vm3 -> 10.0.0.2
"""
############################################################################################################################
#example: dict of list 
team = {
    "frontend": ["Raj", "BOB"],
    "backend": ["Charli", "Deva"],
    "Devops": ["Ramesh"],
}

#access values which are list 
print(team["frontend"]) #['Raj', 'BOB']

#access an item insdie the list (using [] twice - diff meaning each time!)
print(team["frontend"][0]) #Raj  here 'frontedn' is a dict key and '[0]' is a list index

#Loop both lvels 
for dept, memebers in team.items():
    print(f"{dept}:")
    for memebr in memebers: 
        print(f" - {memebr}")
"""
frontend:
 - Raj
 - BOB
backend:
 - Charli
 - Deva
Devops:
 - Ramesh
"""
############################################################################################################################
#example: list of dicts containing dict 
virtual_machines = [
    {
        "name": "web-01",
        "ip_adress": "10.0.0.0",
        "spec": {
            "cpu": 4,
            "memory_gb": 16
          },
        "tags": ["frontend", "Prod"]
    }, 
    {
        "name": "db-01",
        "ip_adress": "10.0.0.1",
        "spec": {
            "cpu": 8,
            "memory_gb": 64
          },
        "tags": ["database", "Prod"]
    }, 
]

#pull nested data 
for machine in virtual_machines: 
    name = machine["name"]
    cpu = machine["spec"]["cpu"]
    #tags = machine["tags"] which gives dict of list example #(['frontend', 'Prod'])
    tags = ", ".join(machine["tags"]) #gives as dict
    print(f"{name}: {cpu} CPUs ({tags})")
"""
web-01: 4 CPUs (frontend, Prod)
db-01: 8 CPUs (database, Prod)
"""