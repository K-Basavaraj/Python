config = {
    "host": "localhost", 
    "port": 5432,
    #"ssl": xxx  here ssl key is commented which not defined 
}

host = config.get("host", "127.0.0.1")
port = config.get("port", 8080)
ssl = config.get("ssl", False) #deafult false 

print(f"connecting to {host}:{port} (ssl: {ssl})") #connecting to localhost:5432 (ssl: False)
print(config)
