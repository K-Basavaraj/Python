#scenario1: config merge the classic use case
default_config = {"host": "localhost", "port": 8080, "debug": False}
user_config = {"port": 9090, "debug": True, "user": "admin"}

#merge user config into default config
final = default_config.copy()  # create a copy of the default config
final.update(user_config)  # merge user config into the copy
print(final)  # Output: {'host': 'localhost', 'port': 9090, 'debug': True, 'user': 'admin'}
#===============================================================================================
#scenario2: intalize counter or flags 
#set up counts for a both of items, all starting at 0 
servers = ["server1", "server2", "server3"]

request_counts = dict.fromkeys(servers, 0)  # all servers start with 0 requests
print(request_counts)  # Output: {'server1': 0, 'server2': 0, 'server3': 0}

#then update as you go: 
request_counts["server1"] += 5
request_counts["server2"] += 3
request_counts["server3"] += 1
print(request_counts)  # Output: {'server1': 5, 'server2': 3, 'server3': 1}
