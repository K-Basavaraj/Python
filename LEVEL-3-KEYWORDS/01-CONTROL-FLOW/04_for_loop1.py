
#example1 For Loop with Range: Creates a sequence of numbers, allowing iteration across a specified range. Example: for i in range(5) prints numbers 0 through 4.

for i in range(5):
    print("Number:", i)

"""
output:
Number: 0
Number: 1
Number: 2
Number: 3
Number: 4
"""

#example2 - For Loop with Strings:Iterates over each character in a string. Example: for letter in "Python" prints each character of the word.

name = "Python"

for letter in name:
    print("Letter:", letter)

#example3 - For Loop with Lists:Iterates over items in a list (array). Example: Lists of fruits allow each item to be printed: apple, banana, etc.
cart = ["apple", "banana", "cherry", "mango", "strawberry"]

for item in cart:
    print(f"I Like this {item} fruit")

#example4 For Loop with Tuples: Fine for handling immutable sequences of data. Example: Prints coordinates stored in a tuple.
coordinates = (10, 20, 30)
for coord in coordinates:
    print("Coordinate:", coord)

"""
Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:
"""

#example5: or Loop with Sets:Iterates over unordered, unique items.Ensures duplicates are ignored, printing only unique entries.
unique_fruits = {"apple", "banana", "cherry", "apple", "banana"}
for fruit in unique_fruits:
    print("Unique Fruit:", fruit)

#example6 
allowed_users = {"Alice", "Bob", "Charlie"}
users_to_check = ["Alice", "David", "Charlie", "Eve"]
for user in users_to_check:
    if user in allowed_users:
        print(f"{user} is allowed access.")
    else:
        print(f"{user} is NOT allowed access.")

#example7 For Loop with Dictionaries:Iterates over key-value pairs in a dictionary. Example: Prints each student's name and their corresponding grade.
person = {
    "name": "Alice", 
    "age": 30,
    "city": "New York"
}

for key, value in person.items():
    print(f"{key}:{value}")