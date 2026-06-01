#finding servers place in rotation 

load_balancer_pool = ["web-01", "web-02", "web-03", "web-04"]

target = "web03"

if target in load_balancer_pool: 
    position = load_balancer_pool.index(target)
    print(f"{target} is at position {position} in the rotation")
else:
    print(f"{target} is not in the LB pool")