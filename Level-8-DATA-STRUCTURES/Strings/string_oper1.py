#concationation 
"""
Joins two strings together using the plus (+) operator, combining them into a single string.
Example: Combining "Hello" and "World" using the + results in "Hello World". Note the insertion of a space for readability.
"""
str1 = "hello"
str2 = "world"

print(str1+str2) #helloworld
print(str1 + " " + str2) #hello world

#Repetition
"""
Repeats a string a specified number of times using the asterisk (*) operator.
Example: Repeating the string "Hello" three times with the * results in "HelloHelloHello" without adding spaces 
between repetitions.
"""
str1 = "Hi"
print(str1 * 3) #HiHiHi

#example2: Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1]) #output: e

#example3: Looping Through a String
for x in "banana":
  print(x) #banana

#example4: String Length
a = "Hello, World!"
print(len(a)) #output: 13

#example5: Check String To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt) #output: True  

#example5: Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") #output: Yes, 'free' is present.

#example6: Check if NOT To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)
#output: True

#example6: Use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #output: No, 'expensive' is NOT present.
