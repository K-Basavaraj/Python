"""
Escape Character
To insert characters that are illegal in a string, use an escape character.
An escape character is a backslash \ followed by the character you want to insert.
An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
"""
#example1: 
#txt = "We are the so-called "Vikings" from the north." output: SyntaxError: invalid syntax here it gives an error because of the double quotes inside the string
#To fix this problem, use the escape character \":
txt = "We are the so-called \"Vikings\" from the north."
print(txt) #output: We are the so-called "Vikings" from the north. here it uses the escape character to include the double quotes inside the string

#example2: 
txt = "This will insert one \\ (backslash)."
print(txt) 

#example3: 
txt = "Hello\nWorld!"
print(txt) #output: Hello
           #World! here it uses the escape character \n to insert a new line between Hello and World! 

#example4: 
txt = "Hello\tWorld!"
print(txt) #output: Hello   World! here it uses the escape character \t to insert a tab between Hello and World!

##This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 