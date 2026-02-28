# This program converts years, months, and days into total number of days.
# Assumptions:
#   - 1 year  = 365 days
#   - 1 month = 30 days

def find_total_days(years, months, days):
    total_days = (years * 365) + (months * 30) + days
    return total_days


# ---- Taking input from the user ----
years_input = int(input("Enter number of years: "))
months_input = int(input("Enter number of months: "))
days_input = int(input("Enter number of days: "))

# ---- Store return value in a variable ----
result = find_total_days(years_input, months_input, days_input)

# ---- Print a clear message ----
print("Total number of days is:", result)

"""Enter number of years: 3
Enter number of months: 1
Enter number of days: 5
Total number of days is: 1130
"""