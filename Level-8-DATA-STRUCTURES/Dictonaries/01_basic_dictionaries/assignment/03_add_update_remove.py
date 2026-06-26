config = {"host": "localhost", "port": 5432}
print(config)
#o/p: {'host': 'localhost', 'port': 5432}

#Add a new key 
config["user"]="admin"
print(config)  
##o/p: {'host': 'localhost', 'port': 5433, 'user': 'admin'}


#update existing key 
config["port"] = 5433
print(config) 
#0/p: {'host': 'localhost', 'port': 5433, 'user': 'admin'}

#remove a key 
del config["host"]
print(config)
#O/P: {'port': 5433, 'user': 'admin'}

#add via .update() 
config.update({"ssl": True, "timeout": 30})
print(config)
#O/P: {'port': 5433, 'user': 'admin', 'ssl': True, 'timeout': 30}

#remove and use the value 
old_port = config.pop("port")
print(f"old port was: {old_port}") #O/P: old port was: 5433

print(config)
#O/P: {'user': 'admin', 'ssl': True, 'timeout': 30}

########################################################################################################
#EXAMPLE: MERGING A DEFULT CONFIG CONFIG WITH USER CONFIG 
default_config = {
    "host": "10.0.0.0",
    "port": 8080,
    "debug": False
}

user_config = {
    "port" : 9090, #override
    "debug": True, #override
    "user": "alice", #new key 
}

#merge user_config 
final_config = default_config.copy()  #start with default
final_config.update(user_config)  #overlay user choices 

print(final_config)
#{'host': '10.0.0.0', 'port': 9090, 'debug': True, 'user': 'alice'}
########################################################################################################
#remove items form a queue 

job_queue = {
    "job-01": "backup-db", 
    "job-02": "restart-nginx",
    "job-003": "rotate-logs", 
}

#process the first job 
job_id = "job-01"
task = job_queue.pop(job_id)
print(f"Processing {job_id}: {task}") #Processing job-01: backup-db   its removing 
print(f"Remaining jobs: {job_queue}") # Remaining jobs: {'job-02': 'restart-nginx', 'job-003': 'rotate-logs'} final after removed 
########################################################################################################
