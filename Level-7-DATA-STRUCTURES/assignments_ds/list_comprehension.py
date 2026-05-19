instances = [
    {"name": "server1", "state": "running"},
    {"name": "server2", "state": "stopped"},
    {"name": "server3", "state": "running"},
    {"name": "server4", "state": "stopped"},
]
#name of running servers 
running = [i["name"] for i in instances if i["state"] == "running"]

#convert all server names to uppercase 
upper = [s.upper() for s in running]

#only error logs  
logs = ["error: disk full", "info: backup completed", "error: network timeout", "warning: high memory usage"]
errors = [log for log in logs if log.startswith("error")]


servers  = [
    {"name": "server1", "cpu": 75},
    {"name": "server2", "cpu": 85},
    {"name": "server3", "cpu": 90},
    {"name": "server4", "cpu": 60},
]
#double cpu values for high cpu servers 
high_cpu_doubled = [s["cpu"] * 2 for s in servers if s["cpu"] > 80]

print(high_cpu_doubled)
print(errors)
print(upper)
print(running)
