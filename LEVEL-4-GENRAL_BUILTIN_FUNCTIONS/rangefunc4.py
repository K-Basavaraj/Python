#Slicing Ranges
r = range(10)
print(r[2]) # Output: 2  statement returns the value at index 2, which is 2.
print(r[2:5]) # Output: range(2, 5) statement returns a new range object that represents the slice of the original range from index 2 to index 4 (5 is exclusive). This new range includes the numbers 2, 3, and 4.
print(r[:5]) # Output: range(0, 5) statement returns a new range object that represents the slice of the original range from the beginning (index 0) to index 4 (5 is exclusive). This new range includes the numbers 0, 1, 2, 3, and 4.
r = range(0, 10, 2)
print(6 in r) # Output: True statement checks if the number 6 is present in the range r. Since r represents the numbers 0, 2, 4, 6, and 8, the number 6 is indeed in the range, so the output is True.
print(7 in r) # Output: False statement checks if the number 7 is present in the range r. Since r represents the numbers 0, 2, 4, 6, and 8, the number 7 is not in the range, so the output is False.

b = "Hello, World!"
print(b[2:5])

#Slice From the Start
b = "Hello, World!"
print(b[:5]) # Output: Hello statement returns a substring of b starting from the beginning (index 0) up to index 4 (5 is exclusive). This results in the substring "Hello".

#Slice To the End
b = "Hello, World!"
print(b[2:]) # Output: llo, World! statement returns a substring of b starting from index 2 to the end of the string. This results in the substring "llo, World!".

#Negative Indexing Use negative indexes to start the slice from the end of the string:
#EXAMPLE: 
"""
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
"""
var = "Hello, World!"
print(var[-5:-2]) # Output: orl statement returns a substring of var starting from index -5 (which corresponds to the character "o" in "World!") up to index -2 (which corresponds to the character "d" in "World!"). This results in the substring "orl".

print(var[-5:]) # Output: orld! statement returns a substring of var starting from index -5 (which corresponds to the character "o" in "World!") to the end of the string. This results in the substring "orld!".

print(var[:]) # Output: Hello, World! statement returns a substring of var starting from the beginning to the end of the string. This results in the entire string "Hello, World!".

print(var[-6:]) # Output: World! statement returns a substring of var starting from index -6 (which corresponds to the character "W" in "World!") to the end of the string. This results in the substring "World!".

print(var[-13:]) # Output: Hello, World! statement returns a substring of var starting from index -13 (which corresponds to the character "H" in "Hello, World!") to the end of the string. This results in the entire string "Hello, World!".

print(var[-13:-7]) # Output: Hello, statement returns a substring of var starting from index -13 (which corresponds to the character "H" in "Hello, World!") up to index -7 (which corresponds to the character "," in "Hello, World!"). This results in the substring "Hello,".