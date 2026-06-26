db_config = {
    "host": "localhost",
    "port": 5432,
    "user": "admin",
    "password": "secret",
    "ssl": True
}
print(f"connecting to {db_config['host']}:{db_config['port']}") #connecting to localhost:5432

#API RESPONSE 
api_response = {
    "status": "sucess", 
    "code": 200,
    "data": {
        "user_id": 101,
        "username": "alice", 
        "permissions": ["read", "write"],
    },
}

print(api_response["data"]["username"]) #alice