#your maintaining a list of active servers and one gets decommissioned: 

active_servers = ["web1", "web2", "web3", "web4"]

#web2 gets decommissioned today
decommissined = "web2"

if decommissined in active_servers:
    active_servers.remove(decommissined)
    print(f"{decommissined} has been removed from the list of active servers.")
else:
    print(f"{decommissined} is not in the list of active servers.")

print(f"current active servers: {active_servers}") 
#output: current active servers: ['web1', 'web3', 'web4'] here we have removed web2 from the list of active servers, which means that it is no longer in the list. The remaining active servers are web1, web3 and web4. 

##############################################################################################################
#you want to remove all error logs from a list. remove() only kills the first one so you can use a list compreshension  (the cleanest way): 

#secnario1: 
logs = ["INFO: started", "ERROR: down", "INFO: OK", "ERROR: timeout"]

#keepeverything that doesnt not start with "ERROR
logs = [log for log in logs if not log.startswith("ERROR")] # for each log in logs , if that log does not start with "ERROR" then keep it in the new list. 

print(logs) #output: ['INFO: started', 'INFO: OK'] here we have used a list comprehension to create a new list that only contains the logs that do not start with "ERROR". This way we have effectively removed all the error logs from the original list. The resulting list only contains the info logs.

##############################################################################################################
#scenario2:  Active montoring alerts 
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