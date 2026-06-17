"""
1) WHAT IS strip()? 
.strip() removes whitespace (spaces, tabs, newlines) 
from both ends of a string. it doesnt  chnage middle spaces

synatx: 
 string.strip() 
 string.strip(chars) 

Note: Returns a NEW string(original is unchnaged - strings are immutable).
"""
#Example1: 
#Remove Whitespace The strip() method removes any whitespace from the beginning or the end:
description = "Hi I 'm Basavaraja"
print(description.strip()) #output: Hi I 'm Basavaraja here it doesnot remove the whitespace in between the string

note = "   Hi I'm Basavaraja   "
print(note.strip()) #output: Hi I 'm Basavaraja  

#example2: orginal string is unchnaged (immutable) 
text = "  hello  "
clean = text.strip() 

print(text) #output:  hello unchanged original string
print(clean) #output: hello new string with whitespace removed

#example3: strip removes all whitespace types 
messy = "\n\t  Hello, World!  \t\n"
print(messy)  
print(messy.strip()) #output: Hello, World! removes all whitespace types (spaces, tabs, newlines) from both ends of the string

#example4: strip specific characters
text = "---hello---"
print(text.strip("-")) #output: hello removes the specified character "-" from both ends of the string

txt="###---hello---###" 
print(txt.strip("#-")) #output: hello removes the specified characters "#" and "-" from both ends of the string


#Remove Whitespace The strip() method removes any whitespace from the beginning or the end:
description = "Hi I 'm Basavaraja"
print(description.strip()) #output: Hi I 'm Basavaraja here it doesnot remove the whitespace in between the string

note = "   Hi I'm Basavaraja   "
print(note.strip()) #output: Hi I 'm Basavaraja  
