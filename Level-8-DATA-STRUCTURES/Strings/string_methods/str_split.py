"""
1) what is split()? 
.split() breaks a string into pieces and returns a list . 
By defult, it splits on whitespaces. we also specify a separetor. 

synatx: 
string.split()
string.split(separtor)
string.split(separtor, maxsplit)
Note: Returns a list of strings. The original string is unchanged - strings are immutable.
"""
#example1: 
sentance = "Hello world python"
words = sentance.split()
print(words) #output: ['Hello', 'world', 'python'] #Split String The split() method splits the string into substrings if it finds instances of the separator: The split() method returns a list where the text between the specified separator becomes the list items.

#example2: split a specific character
name = "Basava, Raja"
print(name.split(",")) #output: ['Basava', ' Raja'] here it splits the string into two parts and returns a list of strings

#example3: split on a longer separtor
text = "one->two->three->four"
parts = text.split("->")
print(parts) #output: ['one', 'two', 'three', 'four'] here it splits the string into four parts and returns a list of strings

#example4: limit the number of splits using maxsplit
text = "a,b,c,d,e"
print(text.split(",", 2)) #output: ['a', 'b', 'c,d,e'] here it splits the string into three parts and returns a list of strings

#example5: splitting new lines 
log = "line1\nline2\nline3"
print(log.split("\n")) #output: ['line1', 'line2', 'line3'] here it splits the string into three parts and returns a list of strings    

#example6: return list even for a single piece string
single_word = "Hello"
print(single_word.split(",")) #output: ['Hello'] here it returns a list with a single string

#example7: 
row = "alice, 30, engineer, USA"
name, age, role, country = row.split(",")
print(name, age, role, country) #output: alice  30  engineer  USA here it splits the string into four parts and returns a list of strings and assigns them to variables

#example8: ext6ract file extension from a file name
filename = "server.log.backup"
last_part = filename.split(".")[-1]
print(last_part) #output: backup here it splits the string into three parts and returns a list of strings and extracts the last part of the list which is the file extension