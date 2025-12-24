"""
Imagine you have a timer app that measures time only in seconds, but you want to show it in a human-friendly way
 — hours, minutes, and seconds.

For example:
If the total time is 7000 seconds, you want the app to show it as

“1 hour, 56 minutes, and 40 seconds.”
"""
# Function to convert total seconds into hours, minutes, and remaining seconds
def converting_seconds(seconds):
    # Step 1: Convert total seconds to hours using integer division
    # There are 3600 seconds in an hour, so this gives full hours only
    hours = seconds // 3600

    # Step 2: Calculate how many seconds are left after removing full hours
    # Then divide by 60 to get the number of full minutes
    # (seconds - hours * 3600) removes seconds used for hours
    minutes = (seconds - hours * 3600) // 60

    # Step 3: Calculate the remaining seconds after removing both hours and minutes
    remaining_seconds = seconds - hours * 3600 - minutes * 60

    # Step 4: Return all three values so we can use them outside the function
    return hours, minutes, remaining_seconds


# Scenario: Our timer counted 7000 seconds, now we want to convert that
hours, minutes, seconds = converting_seconds(7000)

# Step 5: Display the result in a readable way
print("Converted Time:")
print(hours, "hours,", minutes, "minutes,", seconds, "seconds")
