#working with multiple conditional statements using Logic Operators AND,OR, NOT
#======================================================================================================
#WETHER CHECK EXAMPLE
def weather_check(temperature, is_sunny):
    if temperature > 77 and is_sunny:
        print("Go to the beach and enjoy the sun!")
    elif temperature > 50 and not is_sunny:
        print("stay indoors and read a book or watch a movie.")
    elif temperature > 50 and is_sunny:
        print("It's a nice day! You can go for a walk or have a picnic.")
    else:
        print("stay indoors and keep warm.")
    
    return

weather_check(80, True)  # Output: Go to the beach and enjoy the sun!
weather_check(60, False) # Output: stay indoors and read a book or watch a movie.
weather_check(50, True)  # Output: It's a nice day! You can go for a walk or have a picnic.

#example-2 
age = 20 
has_permission = True

if age >= 18 and has_permission:
    print("Access granted. You can enter the event.")
elif age >= 18 and not has_permission:
    print("Access denied. You do not have permission to enter the event. permission is required for entry.")
else: 
    print("Access denied. You must be at least 18 years old to enter the event.")

#======================================================================================================`
# Nested conditions: A condition inside another condition is called a nested condition.
def wether_check_nested(temperature, is_sunny):
    if temperature > 77:
        if is_sunny:
            print("Go to the beach and enjoy the sun!")
        else:
            print("stay indoors and read a book or watch a movie.")
    elif temperature > 50:
        if is_sunny:
            print("It's a nice day! You can go for a walk or have a picnic.")
        else:
            print("stay indoors and keep warm.")
    else:
        print("stay indoors and keep warm.")
    
    return 
wether_check_nested(80, True)  # Output: Go to the beach and enjoy the sun!
wether_check_nested(60, False) # Output: stay indoors and read a book or watch a movie.
wether_check_nested(50, True)  # Output: stay indoors and keep warm.