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
#######################################################################################################################
# import os
# print(os.getcwd())

# Example: Reading a file line-by-line using a while loop.
# The loop continues until the end of file (EOF) is reached.
# readline() returns an empty string ("") when no more lines are available.

# Open the file in read mode ("r")
# 'with' ensures the file is automatically closed after use.
with open("sample_data.txt", "r") as input_file:

    # Read the first line from the file
    line = input_file.readline()

    # Continue looping as long as 'line' contains data
    # When EOF is reached, readline() returns an empty string,
    # which evaluates to False and stops the loop.
    while line:

        # strip() removes leading/trailing whitespace and newline characters
        print(line.strip())

        # Read the next line in each iteration
        line = input_file.readline()

# End of file processing

