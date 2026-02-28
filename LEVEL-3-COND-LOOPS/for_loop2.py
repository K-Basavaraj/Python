# print("DEBUG: new version running")
# numbers = []

# user_input = input("Enter numbers separated by space: ")

# # Split input into parts
# parts = user_input.split()

# for part in parts:
#     try:
#         num = int(part)
#         numbers.append(num)
#     except ValueError:
#         print(f"'{part}' is not a valid number.")

# # Check even or odd
# for number in numbers:
#     if number % 2 == 0:
#         print(f"{number} is even.")
#     else:
#         print(f"{number} is odd.")

user_input = input("Enter numbers separated by space: ")

try:
    numbers = [int(x) for x in user_input.split()]
except ValueError:
    print("Please enter only numbers.")
    exit()

for number in numbers:
    print(f"{number} is {'even' if number % 2 == 0 else 'odd'}.")
