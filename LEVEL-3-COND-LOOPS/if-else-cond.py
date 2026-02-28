#if-else stament check if a condition is true and runs the corresponding code. 
#Example-1 if-else condition
def simple_version():
    user_age = int(input("Enter your age: "))

    if user_age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

###############################################################
# We never trust user input — always validate and handle errors
def safe_version():
    try:
        age = int(input("Enter your age: "))

        # Business logic: Check voting eligibility
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")

    # Handle invalid input (non-numeric values, special characters, etc.)
    except ValueError:
        print("Invalid input. Please enter a valid numeric age.")
    # End of script: Input validation with conditional logic

# Choose which version to run
# safe_version()
###############################################################
# Example-2: if-else condition with proper validation
def exam_score():
    try:
        score = int(input("Enter your exam score (0-100): "))

        # We never trust user input — validate range
        if score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            return # Exit if input is invalid

        if score >= 65:
            print("Congratulations! You passed the exam.")
        else:
            print("Sorry, you did not pass. Better luck next time!")

    except ValueError:
        print("Invalid input. Please enter a numeric score between 0 and 100.")
        return  # Exit the function if input is invalid
    
exam_score()