"""
how to quickly verify whether items exist within lists using the powerful in and not in operators. 
These tools streamline searches and enhance efficiency by alleviating the need to manually sift through extensive lists.

Key Points:
Understanding Operators:

in Operator: Checks if an item exists in a list. Use for confirming presence.

not in Operator: Checks if an item is absent in a list. Use for confirming absence.
"""
#example1: in operator
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("banana is in the fruits list") #output: banana is in the fruits list this checks if "banana" is present in the fruits list and prints a message confirming its presence.

#example2: not in operator
if "grape" not in fruits:
    print("grape is not in the fruits list") #output: grape is not in the fruits list this checks if "grape" is absent from the fruits list and prints a message confirming its absence.

#example3: using in operator with a loop to check for multiple items
items_to_check = ["apple", "grape", "cherry"]
for item in items_to_check:
    if item in fruits:
        print(f"{item} is in the fruits list") #output: apple is in the fruits list cherry is in the fruits list this loop iterates through each item in the items_to_check list and uses the in operator to check if it exists in the fruits list, printing a message for each item found.

#example4: using not in operator with a loop to check for multiple items
for item in items_to_check:
    if item not in fruits:
        print(f"{item} is not in the fruits list") #output: grape is not in the fruits list this loop iterates through each item in the items_to_check list and uses the not in operator to check if it is absent from the fruits list, printing a message for each item not found.

#example5:
colors = ["red", "blue", "yellow"]
if "green" in colors:
    print("green is in the colors list")
else:
    print("green is not in the colors list") #output: green is not in the colors list this checks if "green" is present in the colors list and prints a message confirming its absence since it is not found.