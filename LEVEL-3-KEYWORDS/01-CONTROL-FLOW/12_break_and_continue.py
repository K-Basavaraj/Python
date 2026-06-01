numbers = [ 1, 2, 3, -1, 5, 6, 7]
for n in numbers:
    if n == -1:
        print("Hit a stop signal - exiting!")
        break  #stop the eniire loop 
    if n % 2 == 0:
        continue #skip even numbers
    print(f"Processing {n}")

"""
output: 
Processing 1
Processing 3
Hit a stop signal - exiting!
"""

#example2: 
inputs = ["Validate", "skip_me", "plan", "Apply", "STOP"]
for item in inputs:
    if item == "skip_me": 
        continue
    if item == "STOP":
        print("encountered stop signal")
        break 
    print(f"processing: {item}")

"""
output: 
processing: Validate
processing: plan
processing: Apply
encountered stop signal
"""