#find max and min value in a dict using loop

cpu_usage = {"server1": 75, "server2": 60, "server3": 90}

#which server has the highest CPU usage? and which has the lowest?
max_server = ""
max_cpu  = 0 

for name, cpu in cpu_usage.items():
    if cpu > max_cpu:
        max_cpu = cpu
        max_server = name

print(f"Highest CPU: {max_server} at {max_cpu}%")
#output: Highest CPU: server3 at 90%

#cleaner one liner using max() with a key function
top = max(cpu_usage.items(), key=lambda kv:kv[1])
print(top) #('server3', 90)