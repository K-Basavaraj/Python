cpu_usage = {
    "web-01": 45,
    "web-02": 92,
    "db-01": 30
}

print(sum(cpu_usage.values())) #167
print(max(cpu_usage.values())) #92
print(min(cpu_usage.values())) #30
#====================================================================================================
#server inventory summary 
servers = {
    "web-01": "running", 
    "web-02": "stopped", 
    "db-01": "running"
}

#how many of each status? 
running_count = list(servers.values()).count("running")
print(f"Running: {running_count}") #Running: 2

#find which server are stoped 
stopped = [ name for name, status in servers.items() if status == "stopped"]
print(f"stopped: {stopped}") #stopped: ['web-02']

for key, value in servers.items():
    print(f"({key}) = {value}")
"""
(web-01) = running
(web-02) = stopped
(db-01) = running
"""