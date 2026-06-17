"""
1) what is startswith()? 
.startswith() checks wether a string begins with a specific substring, returns True or False. 

syntax: 
  string.startwith(prefix) ]
  string.startswith(prefix, start)
  string.startswith(tuple_of_prefixes) 
"""
#example1: check the start of a string 
text = "Hello world"
print(text.startswith("Hello")) #True
print(text.startswith("world")) #False
print(text.startswith("hello")) #False case-sensitive

#example2: 
log = "ERROR: Database failed"
print(log.lower().startswith("error")) #True

#example3: check multiple prefixes to check multiple at once
log = "WARN: Slow query"
print(log.startswith(("Error", "WARN", "FATAL"))) #TRUE
print(log.startswith(("INFO", "DEBUG"))) #False

#exampl3: check starting from a speciofic position
text = "Hello world"
print(text.startswith("world", 6))

#example4: 
logs = [ 
    "INFO: Service started", 
    "ERROR: DB connection failed",
    "WARN: slow query",
    "ERROR: Timeout", 
    "INFO: Health check ok"
]

errors = [log for log in logs if log.startswith("ERROR")]
print(errors)
#['ERROR: DB connection failed', 'WARN: slow query', 'ERROR: Timeout']

#example: check if a url is secure 
url = "https://example.com"
if url.startswith("https://"):
    print("secure url")
else:
    print("Insecure URL - upgrade to HTTPS")
#########################################################################################################################
"""
2) what is endswith()? 
.endsswith() is the mirror of .startswith(). 
it checks wether a string ENDS with a specific substring.
return TRUE OR False

syntax: 
  string.endswith(prefix) ]
  string.endsswith(prefix, start)
  string.endsswith(tuple_of_prefixes) 
"""
#example1: check the start of a string 
text = "Hello world"
print(text.endswith("Hello")) #False
print(text.endswith("world")) #True
print(text.endswith("hello")) #False case-sensitive

#example2: case sensitive 
filename = "Report.PDF"
print(filename.endswith(".pdf")) #False
print(filename.endswith(".PDF")) #True
print(filename.lower().endswith(".pdf")) #True

#example3: check multiple suffixes at once with a tuple 
filename = "server.log " 
print(filename.endswith((".log", ".txt", ".csv"))) #True
print(filename.endswith((".pdf", ".docx"))) #False

#example4: empty suffix always returns True 
text = "anything "
print(text.endswith("")) #True

#example: idenitify file types 
files = ["report.pdf", "data.csv", "image.png", "server.log", "config.yaml"]

#find all log files 
logs = [ f for f in files if f.endswith(".log")]
print(logs) #['server.log']

#find all data files 
data_files = [ f for f in files if f.endswith((".csv", ".json", ".yaml"))]
print(data_files) #['data.csv', 'config.yaml']
