api_response = {
    "status": "suscess", 
    "code": 200,
    "data": {
        "user": {
            "id": 101,
            "name": "Alice", 
            "permission": ["read", "write"],
        },
        "session": {
            "token": "abxx123876zyt",
            "expires_in": 3600,
        },
    },
}

#specific data 
user_name = api_response["data"]["user"]["name"]
session_token = api_response["data"]["session"]["token"]

print(f"user: {user_name}")
print(f"Token: {session_token}")
"""
user: Alice
Token: abxx123876zyt
"""
#################################################################################################################
#config_file with nested settings 

config = {
    "app": {
        "name": "Myapp",
        "Version": "1.0.0"
    },
    "database": {
        "host": "localhost",
        "port": 3306,
        "creds": {
            "user": "admin",
            "password": "secret",
        },
    },
    "logging": {
        "level": "Info",
        "file": "/var/log/myapp.log",
    }
}

db_host = config.get("database", {}).get("host", "localhost")
db_user = config.get("database", {}).get("creds", {}).get("user", "guest")
log_level = config.get("logging", {}).get('level', "WARN")

print(f"DB: {db_user}@{db_host}, log_level: {log_level}")
#DB: admin@localhost, log_level: Info