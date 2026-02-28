# action combining of for loops indices and lists.
fruits = ["apple", "cherry", "orange", "banana", "grape"]

for i in range(len(fruits)):
    print(f"index {i} contains {fruits[i]}")

#ANOTHER APPROCH USING FOR INSTED OF RANGE
for fruit in fruits:
    print(f"Fruit: {fruit}")

"""
output: 
index 0 contains apple
index 1 contains cherry
index 2 contains orange
index 3 contains banana
index 4 contains grape
Fruit: apple
Fruit: cherry
Fruit: orange
Fruit: banana
Fruit: grape
"""