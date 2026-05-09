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

##############################

#scenario: you have a deployment queue and a critical hotfix comes in. it needs to go the front of the queue. not the back of the queue. how do you do that?

deployment_queue = ["app-feature-A", "app-feature-B", "app-feature-C"]

deployment_queue.insert(0, "app-hotfix-CRITICAL")

print(deployment_queue) #output: ['app-hotfix-CRITICAL', 'app-feature-A', 'app-feature-B', 'app-feature-C'] here we have inserted the critical hotfix at index 0, which means that it is now the first item in the list. The rest of the items have been shifted to the right to make room for the new item. So app-feature-A is now at index 1, app-feature-B is now at index 2 and app-feature-C is now at index 3.
##############################
#scenario2: inserting a maintanance step in the middle of a runbook: 

runbook = [
    "1. stop the application",
    "3. apply the patch",
    "4. start the application"
    "5. verify health checks"
]

#Oops we forgot to add step 2, which is to take a backup of the application before applying the patch. We can use the insert method to add this step at the correct index.
runbook.insert(1, "2. take a backup of the application")

for step in runbook:
    print(step)

#output:
#1. stop the application
#2. take a backup of the application
#3. apply the patch
#4. start the application
#5. verify health checks here we have inserted the backup step at index 1, which means that it is now the second item in the list. The rest of the items have been shifted to the right to make room for the new item. So step 3 is now at index 2, step 4 is now at index 3 and step 5 is now at index 4.

#######################################################################################################################

#your maintaining a list of active servers and one gets decommissioned: 

active_servers = ["web1", "web2", "web3", "web4"]

#web2 gets decommissioned today
decommissined = "web2"

if decommissined in active_servers:
    active_servers.remove(decommissined)
    print(f"{decommissined} has been removed from the list of active servers.")
else:
    print(f"{decommissined} is not in the list of active servers.")

print(f"current active servers: {active_servers}") #output: current active servers: ['web1', 'web3', 'web4'] here we have removed web2 from the list of active servers, which means that it is no longer in the list. The remaining active servers are web1, web3 and web4. 

#you want to remove all error logs from a list. remove() only kills the first one so you can use a list compreshension  (the cleanest way): 

logs = ["INFO: started", "ERROR: down", "INFO: OK", "ERROR: timeout"]

#keepeverything that doesnt not start with "ERROR
logs = [log for log in logs if not log.startswith("ERROR")] # for each log in logs , if that log does not start with "ERROR" then keep it in the new list. 

print(logs) #output: ['INFO: started', 'INFO: OK'] here we have used a list comprehension to create a new list that only contains the logs that do not start with "ERROR". This way we have effectively removed all the error logs from the original list. The resulting list only contains the info logs.

#scenario: Active montoring alerts 
alerts = ["disk-full", "cpu-high", "memory-leak", "cpu-high", "network-down"]

# remove memory-leak
alerts.remove("memory-leak")
print(alerts) #output: ['disk-full', 'cpu-high', 'cpu-high', 'network-down'] here we have removed the first occurrence of "memory-leak" from the alerts list using the remove method. 

#remove cpu-high but there are two of them in the list, so we need to use a loop or a list comprehension to remove all occurrences of cpu-high.
alerts = [alert for alert in alerts if alert != "cpu-high"] # for each alert in alerts, if that alert is not equal to "cpu-high" then keep it in the new list.
print(alerts) #output: ['disk-full', 'memory-leak', 'network-down'] here we have used a list comprehension to create a new list that only contains the alerts that are not equal to "cpu-high". This way we have effectively removed all the occurrences of "cpu-high" from the original list. The resulting list only contains the remaining alerts.

#safely try to remove "service-crashed" which is not in the list, use the if statement to check if it exists before trying to remove it.
if "service-crashed" in alerts:
    alerts.remove("service-crashed")
    print("service-crashed has been removed from the alerts list.")
else:
    print("service-crashed is not in the alerts list, cannot remove it.") #output: service-crashed is not in the alerts list, cannot remove it. here we have checked if "service-crashed" is in the alerts list before trying to remove it. Since "service-crashed" is not in the list, we print a message saying that it cannot be removed. This way we avoid the ValueError that would have been raised if we had tried to remove "service-crashed" without checking for its existence first.
    

#scenario: process jobs one at a time from the front of a queue. 
job_queue = ["backup-db", "restart-nginx", "clear-cache", "rotate-logs", "clean-temp-files"]

while job_queue: #keep running while there are jobs
    current_job = job_queue.pop(0) #pop the first job from the queue
    print(f"Processing job: {current_job}") #output: Processing job: backup-db, Processing job: restart-nginx, Processing job: clear-cache, Processing job: rotate-logs, Processing job: clean-temp-files here we have used a while loop to keep processing jobs from the queue until there are no more jobs left. We use the pop method with an index of 0 to remove the first job from the queue and store it in the current_job variable. Then we print out a message saying that we are processing that job. This way we can process each job one at a time from the front of the queue.

print("All jobs done!") #output: All jobs done! here we have printed a message saying that all jobs are done after the while loop has finished processing all the jobs in the queue. This indicates that there are no more jobs left to process.

print(f"Remaining jobs in the queue: {job_queue}") #output: Remaining jobs in the queue: [] here we have printed out the remaining jobs in the queue after the while loop has finished processing all the jobs. Since we have processed all the jobs, the queue is now empty, which is why we see an empty list as the output.

#example: docker 
deployment_steps = []

deployment_steps.append("pulled new docker image")
deployment_steps.append("stopped old container")
deployment_steps.append("started new container")
deployment_steps.append("updated load balancer")

#Now imaginer deployment failed at the end -> need to roll back
print("Rolling back deployment...")

while deployment_steps:
    last_step = deployment_steps.pop() #pop the last step from the list
    print(f"Undoing step: {last_step}") #output: Undoing step: updated load balancer, Undoing step: started new container, Undoing step: stopped old container, Undoing step: pulled new docker image here we have used a while loop to keep undoing the deployment steps until there are no more steps left. We use the pop method without an index to remove the last step from the list and store it in the last_step variable. Then we print out a message saying that we are undoing that step. This way we can roll back the deployment by undoing each step in reverse order.