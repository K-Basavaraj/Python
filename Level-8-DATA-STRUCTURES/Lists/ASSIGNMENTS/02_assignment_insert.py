#scenario: you have a deployment queue and a critical hotfix comes in. it needs to go the front of the queue. 
# not the back of the queue. how do you do that?

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

#oops we forgot to add step 2, which is to take a backup of the application before applying the patch. We can use the insert method to add this step at the correct index.
runbook.insert(1, "2. take a backup of the application")

for step in runbook:
    print(step)

#output:
#1. stop the application
#2. take a backup of the application
#3. apply the patch
#4. start the application
#5. verify health checks here we have inserted the backup step at index 1, which means that it is now the second item in the list. The rest of the items have been shifted to the right to make room for the new item. So step 3 is now at index 2, step 4 is now at index 3 and step 5 is now at index 4.
