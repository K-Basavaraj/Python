"""
1) what is replace()? 
.replace() finds and replaces text in a string. 

returns a new string(orginal is unchnaged - strings are immutable)

synatx: 
 string.replace(old, name)
 string.replace(old, new, count) 
"""
#example1: replace one word with another 
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) #Hello Python
#if new_text = text.replace(" ", "Python") #HelloPythonworld  /or new_text = text.replace("wor", "Python") # Hello Pythonld
#Note: orginal string is unchnaged 
print(text) #Hello world

#example2: Replace all occurrences by default 
text = "cat cat cat"
print(text.replace("cat", "dog")) #dog dog dog

#example3: limit replace with the count argument
text = "cat cat cat cat"
print(text.replace("cat", "dog", 2)) #output: dog dog cat cat count means only replace first 2 occrence 

#example4: replace with empty string = remove text 
text = "Hello World"
print(text.replace("o", "")) #Hell Wrld

#example5: replace speacil charcters / white spaces 
text = "line1\nline2\nline3"
print(text.replace("\n", " | ")) #line1 | line2 | line3

#EXAMPLE6:MASK SENSITVE DATA 
secret = "API_KEY=ABC123XYZ"
MASKED = secret.replace("ABC123XYZ", "******") #API_KEY=******
print(MASKED)

#Replace String The replace() method replaces a string with another string:
rupees = "1000"
print(rupees.replace(("1000"), ("2000"))) #output: 2000

name = "Basavaraja"
print(name.replace("Basavaraja", "Basava")) #output: Basava
print(name.replace("B", "b")) #output: basavaraja here it replaces the first letter B with b