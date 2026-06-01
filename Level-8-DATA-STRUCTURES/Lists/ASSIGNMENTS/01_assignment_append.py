#Building a list of servers as you discover them form an api 

running_servers = []

instances = [              #List of dictionaries representing server instances with their states
    {"id": "i-1234567890abcdef0", "state": "running"},
    {"id": "i-0987654321abcdef0", "state": "stopped"},
    {"id": "i-1122334455667788", "state": "running"},
    {"id": "i-2233445566778899", "state": "terminated"},
    {"id": "i-3344556677889900", "state": "running"},
]

print(instances[0]) #output: {'id': 'i-1234567890abcdef0', 'state': 'running'} this is the first instance in the list, which is a dictionary containing the id and state of the server.
print(instances[0]["id"]) #output: i-1234567890abcdef0 this is the id of the first instance in the list.
print(instances[0]["state"]) #output: running this is the state of the first instance in the list.

for instance in instances: 
    if instance["state"] == "running":
        running_servers.append(instance["id"])

print(running_servers) #output: ['i-1234567890abcdef0', 'i-1122334455667788', 'i-3344556677889900']