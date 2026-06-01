def grading(): 
    try:
        score = int(input("Enter your score: "))

        if score < 0 or score > 100:
             print("Score must be between 0 and 100.")
             return # Exit if input is invalid
        
        elif score >= 90:
             print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        else:
             print("Grade: F")
    except ValueError:
        print("Invalid input. Please enter a numeric score between 0 and 100.")
        return  # Exit the function if input is invalid

grading()