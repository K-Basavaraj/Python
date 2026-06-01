#scenario: process jobs one at a time from the front of a queue. 
job_queue = ["backup-db", "restart-nginx", "clear-cache", "rotate-logs", "clean-temp-files"]

while job_queue: #keep running while there are jobs
    current_job = job_queue.pop(0) #pop the first job from the queue
    print(f"Processing job: {current_job}") 

#output: Processing job: backup-db, Processing job: restart-nginx, Processing job: clear-cache, Processing job: rotate-logs, Processing job: clean-temp-files here we have used a while loop to keep processing jobs from the queue until there are no more jobs left. We use the pop method with an index of 0 to remove the first job from the queue and store it in the current_job variable. Then we print out a message saying that we are processing that job. This way we can process each job one at a time from the front of the queue.

print("All jobs done!") 
#output: All jobs done! here we have printed a message saying that all jobs are done after the while loop has finished processing all the jobs in the queue. This indicates that there are no more jobs left to process.

print(f"Remaining jobs in the queue: {job_queue}") #output: Remaining jobs in the queue: [] here we have printed out the remaining jobs in the queue after the while loop has finished processing all the jobs. Since we have processed all the jobs, the queue is now empty, which is why we see an empty list as the output.
###########################################################################################################################

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
###########################################################################################################################
