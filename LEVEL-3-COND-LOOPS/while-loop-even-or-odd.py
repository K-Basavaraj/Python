# Example: Even or Odd number check with proper user input validation

while True:
    try:
        # Ask user for upper limit
        limit = int(input("Enter a positive number limit: "))

        # Validate that number is greater than 0
        if limit <= 0:
            print("Please enter a number greater than 0.")
            continue

        # If valid input, exit validation loop
        break

    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter a valid integer.")


# Process even/odd numbers from 1 up to user-defined limit
number = 1

while number <= limit:
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    number += 1


# End of program
print("Processing completed successfully.")
