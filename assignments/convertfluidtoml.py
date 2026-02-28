# Program: Convert fluid ounces (fl oz) to milliliters (mL)

def convert_volume(fluid_ounce):
    # 1 fluid ounce = 29.5 milliliters
    ml = fluid_ounce * 29.5
    return ml

# ---- User Input ----
user_input = float(input("Enter fluid ounces to convert: "))

# Requirement 1:
# Convert user input and print the result
print("Converted volume in milliliters: " + str(convert_volume(user_input)))

# Requirement 2:
# Call the conversion again and double the value
print("Doubled converted volume: " + str(convert_volume(user_input) * 2))
