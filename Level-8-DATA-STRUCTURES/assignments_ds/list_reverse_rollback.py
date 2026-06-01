"""
You record deployment steps in the order they happened when you need to roll back. 
You reverse them so the last action gets undone first:
"""
deployment_steps = [
    "pull new docker image",
    "stop the container",
    "startrt the container with the new image",
    "update the load balancer to point to the new container"
    "sent slack notification about the deployment"
]

#build the rollback plan by reversing 
rollback_plan = deployment_steps.copy() #dont mess with orginal 
rollback_plan.reverse() #reverse the order of the items in the list

print("rollback_plan: ") #['sent slack notification about the deployment', 'update the load balancer to point to the new container', 'startrt the container with the new image', 'stop the container', 'pull new docker image'] the order of the items in the list is reversed
for i, step in enumerate(rollback_plan, start = 1):
    print(f"{i}. undo: {step}")

#output:
#rollback_plan:
#1. undo: sent slack notification about the deployment
#2. undo: update the load balancer to point to the new container
#3. undo: startrt the container with the new image
#4. undo: stop the container
#5. undo: pull new docker image

#example2: logs 
log_entrioes = [
    "2024-06-01 10:00:00 - User logged in",
    "2024-06-01 10:05:00 - User updated profile",
    "2024-06-01 10:10:00 - User logged out"
]

log_entrioes.reverse() #reverse the order of the items in the list

print("Recent activty (newwest first): ")
for entry in log_entrioes:
    print(f" {entry}") #2024-06-01 10:10:00 - User logged out, 2024-06-01 10:05:00 - User updated profile, 2024-06-01 10:00:00 - User logged in 
