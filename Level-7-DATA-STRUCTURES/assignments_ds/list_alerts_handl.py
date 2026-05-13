#pending alerts to hanbdle, oldest first

alerts = ["disk-full", "high-cpu", "memory-leak", "network-latency"]

oldest = alerts.pop(0) #this will remove the first item from the alerts list, which is "disk-full", and store it in the variable oldest. The pop method with an index argument removes the item at the specified index and returns it, so we can use it to get the oldest alert from the list.
print(f"Handling oldest alert: {oldest}") #output: Handling oldest alert: disk-full here we have printed the value of oldest, which is "disk-full", to indicate that we are handling this alert first since it is the oldest one in the list.

newest = alerts.pop() #this will remove the last item from the alerts list, which is "network-latency", and store it in the variable newest. The pop method without an index argument removes the last item from the list and returns it, so we can use it to get the newest alert from the list.
print(f"Handling newest alert: {newest}") #output: Handling newest alert: network-latency here we have printed the value of newest, which is "network-latency", to indicate that we are handling this alert last since it is the newest one in the list.

print(f"Remaining alerts to handle: {alerts}") #output: Remaining alerts to handle: ['high-cpu', 'memory-leak'] here we have printed the remaining items in the alerts list, which are "high-cpu" and "memory-leak", to indicate that these are the alerts that still need to be handled after we have handled the oldest and newest alerts.

try: 
    alerts.pop(99)
except IndexError:
    print("No more alerts to handle.") #output: No more alerts to handle. here we have used a try except block to handle the IndexError that would be raised if we tried to pop an item from the alerts list at an index that is out of range. Since there are only 2 items left in the list, trying to pop at index 99 will raise an IndexError, which we catch and print a message indicating that there are no more alerts to handle.