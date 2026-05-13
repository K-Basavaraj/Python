#FIFO (First In, First Out) Queue Example
job_queue = ["backup", "restart-nginx", "rotate-logs", "cleanup-temp-files"]

while job_queue:
    current_job = job_queue.pop(0)
    print(f"Processing job: {current_job}")

print("All jobs have been processed.")
print(f"Remaining jobs in queue: {job_queue}")

#LIFO (Last In, First Out) Stack Example
deploment_steps = []

deploment_steps.append("pulled new docker image")
deploment_steps.append("stopped old container")
deploment_steps.append("started new container")
deploment_steps.append("updated load balancer")

#Now imaging deployment failed at the end we need to roll back 
print("Rolling back deployment steps...")
while deploment_steps:
    last_step = deploment_steps.pop()
    print(f"Undoing: {last_step}")    