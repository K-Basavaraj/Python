#example1: Get the characters from position 2 to position 5 (not included):
a = "Hello, world!"
print(a[2:5]) #output: llo

#example2: Slice From the Start By leaving out the start index, the range will start at the first character:Get the characters from the start to position 5 (not included):
print(a[:5])  #output: Hello

#example3: Slice To the End By leaving out the end index, the range will go to the end of the string:Get the characters from position 2, and all the way to the end:
print(a[2:]) #output: llo, world!

#example4: Negative Indexing Use negative indexes to start the slice from the end of the string:
#Get the characters: From: "o" in "World!" (position -5) To, but not included: "d" in "World!" (position -2):
print(a[-5:-2]) #output: orl