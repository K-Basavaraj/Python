#compare two states (drift detection)
expected_state = ["running", "running", "running"]
actual_states = ["running", "stopped", "running"]
server_names = ["web-01", "web-02", "db-01"]

for name, expected, actual in zip(server_names, expected_state, actual_states): 
    if expected != actual:
        print(f"{name}: expected {expected}, got {actual}")

#web-02: expected running, got stopped

#example2: we can use them together whn you need index + multiple lists" 

servers = ["web-01", "web-02", "web-03"]
ips = ["10.0.0.0", "10.0.0.1", "10.0.0.2"]

for i, (servers, ip) in enumerate(zip(servers, ips), start=1):
    print(f"{i}, {servers} -> {ip}")

"""
1, web-01 -> 10.0.0.0
2, web-02 -> 10.0.0.1
3, web-03 -> 10.0.0.2
"""