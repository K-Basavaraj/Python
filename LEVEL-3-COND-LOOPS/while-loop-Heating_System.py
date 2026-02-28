desired_tenperature = 68
current_temperature = 66

while current_temperature < desired_tenperature:
    print(f"Heating up... Current temperature: {current_temperature}")
    current_temperature += 1  # Simulate heating process

print(f"Desired temperature of {desired_tenperature}°C reached. heating system turned off.")

"""
Understanding while loops is vital in programming, especially for tasks where iteration count is unknown. 
They repeat code execution while a specific condition holds true. When using while loops, 
it's important to be aware of some common pitfalls and considerations to write efficient code.

Highlights:
-> Infinite Loops: Occur when the condition never turns false, causing indefinite execution. 
Similar to a heater without a thermostat, it's crucial to define a stopping condition.

-> Off-By-One Errors: These arise when the loop iterates one time too many or too few. Check conditions carefully to ensure accuracy.

-> Ensuring Termination: Loops should progress toward stopping to avoid hanging indefinitely. 
Ensure variables within the loop are updated correctly.
"""