"""
count(): it tells how many times a specific value appers in the list. 
Note: count() is the method that does not stop at the first match it count all of them. 

synatx: list_name.count(value)
 matches exactly it doesnt do partial natching, case-insensitive, or pattern matching 
"""
#example1: 
logs = ["error", "db down", "error", "timeout", "info-ok"]

print(logs.count("error")) #2
print(logs.count("info-ok")) #1

#example2: what if the value is not there? unlike index() and remove(), count() does not crash if the value is missing it returns 0 
log_levels = ["INFO", "ERROR", "warn"]
print (log_levels.count("DEBUG")) #0

#example3: 
servers = ["web-01", "web-02", "web-03"]

if servers.count("web-01") > 0:
    print("web-01 is in the pool")

# #(or) in operator is faster and more readble 
# if "web-01" in servers: 
#     print("web-01 is in the pool")

#example4: if we need count items that "startwith" or "contain" something use a list comprhnsion 
logs = ["ERROR-DBDOWN", "DB-DOWN", "ERROR-TIMEOUT", "INFO-OK"]

error_count = len([log for log in logs if log.startswith("ERROR")])
print(error_count) #2