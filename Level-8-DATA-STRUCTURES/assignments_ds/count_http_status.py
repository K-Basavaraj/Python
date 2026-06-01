#parsing access logs and want to know ho wmany of each status code we got
status_code = [200, 200, 404, 500, 200, 500, 301, 200, 404]

print(f"ok (200): {status_code.count(200)}") 
print(f"Redirect (301): {status_code.count(301)}") 

#detect repted failuers
deploy_results = [
    "auth-service: sucess", 
    "payment-service: failed", 
    "auth-service: failed", 
    "user-service: sucess",
    "payment-service: failed"
]

failures = [r for r in deploy_results if "failed" in r ]
print(f"Total failures: {len(failures)}")

#count how many times "payment-service failed"
payment_failuers = sum(1 for r in deploy_results if r.startswith("payment-service"))
print(f"payment-service failuers: {payment_failuers}")
