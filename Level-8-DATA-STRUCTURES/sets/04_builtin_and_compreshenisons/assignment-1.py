#remove duplicate log entries 
logs = ["ERROR: DB down", "INFO: started", "ERROR: started", "ERROR: DB down", "WARN: slow"]

unique_logs = set(logs)
print(f"Unique logs: {len(unique_logs)}") #Unique logs: 4

#fast lookup with 'in
#faster than list when we check membership repeatedly 

allowed_users = {"alice", "bob", "charlie"}

def is_allowed(user):
    return user in allowed_users
 
print(is_allowed("alice")) #True
print(is_allowed("dave")) #False
#example: if allowed_users has 10k items: list is slow and set is fast just one hash lookup 

#example3: count unique vistors: 
vistor_logs = ["alice", "bob", "alice", "charle", "bob", "alice"]

unique_vistors = len(set(vistor_logs))
print(f"Unique vistors: {unique_vistors}") #Unique vistors: 3
