#collect items into a buffer process them, then clear the buffer for the nest batch 

log_buffer = []
batch_size = 3

incomming_logs = [
    "INFO: user login", 
    "WARN: slow query", 
    "ERROR: db timeout",
    "INFO: bakcup done",
    "INFO: user logout",
    "ERROR: Disk Full"
]

for log in incomming_logs:
    log_buffer.append(log)

    if len(log_buffer) == batch_size:
        print(f"Sending batch to mintoring: {log_buffer}")
        log_buffer.clear() #empty the buffer for next batch 


#example2: buffer collecting metrics before sending cloudwatch 
metrics_buffer  = ["cpu=45", "mem=78", "disk=90"]
print(f"Buffer has {len(metrics_buffer)} items: {metrics_buffer}") #Buffer has 3 items: ['cpu=45', 'mem=78', 'disk=90']

metrics_buffer.clear()
print(f"Buffer has {len(metrics_buffer)} items: {metrics_buffer}") #Buffer has 0 items: []

new_metric = ["net=120", "load=2.5"]
for log in new_metric:
    metrics_buffer.append(log)
print(f"Buffer has {len(metrics_buffer)} items: {metrics_buffer}") #Buffer has 2 items: ['net=120', 'load=2.5']