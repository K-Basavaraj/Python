# common pattern - config with defaults 
config = {"host": "localhost", "port":3386}

host    = config.get("host", "10.0.0.0")
port    = config.get("port", 8080)
ssl     = config.get("ssl", False) #not in config false
timeout = config.get("timeout", 30)

print(f"{host}:{port} ssl-{ssl} timeout={timeout}")
#localhost:3386 ssl-False timeout=30