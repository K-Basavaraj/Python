#intalize a dict from a list of keys simlar to dict.fromkeys() but each key gets its own mutable values

servers = ["web-01", "web-02", "db-01"]

#each server starts with its own empty list (safe for mutataion)
inventory = {server: [] for server in servers}
print(inventory)
#{'web-01': [], 'web-02': [], 'db-01': []}
#This is the fix for the .frokeys() mutable default tarp we saw in methods list folder file each key gets its own spearte list

#example2: 
servers = ["web-01", "web-02", "db-01", "cache-01"]
statuses = ["running", "stopped", "running", "running"]

status_map = {name: state for name, state in zip(servers, statuses)}
print(status_map)
#{'web-01': 'running', 'web-02': 'stopped', 'db-01': 'running', 'cache-01': 'running'}