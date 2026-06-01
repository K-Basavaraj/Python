#while loops are essentially a way to repeatedly execute a block of code until a specified condition becomes false. 
# where to use while loops: commonly used when the number of iterations is not known in advance. like user input handling,
#data processing, and situations where you want to keep executing a block of code until a certain condition is met.

# Example 1: Counting from 1 to 5 using a while loop
counter = 0
while counter < 5: 
    print("count:", counter)
    counter += 1  # Increment the counter by 1
"""
output:
count: 0
count: 1
count: 2    
count: 3
count: 4
"""

# Example 2: User input handling using a while loop

# Initialize variable with empty string to enter the loop the first time
user_input = ""

# Continue looping until user types "exit" (case-insensitive check)
while user_input.lower() != "exit":

    # Take input from the user
    user_input = input("Enter a command (type 'exit' to quit): ")

    # Display what the user entered
    # Note: If user types 'exit', it will print once before loop stops
    print(f"You entered: {user_input}")

# Loop ends when user_input.lower() becomes "exit"
# Program terminates after this point

#example3 even or odd number check using while loop 
count = 1 
while count <= 5:
    if count % 2 == 0:
        print(f"{count} is an even number.")
    else:
        print(f"{count} is an odd number.")
    
    count += 1  # Increment the counter by 1