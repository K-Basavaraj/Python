#Lower() - convert the entire string to lowercase for case-insensitive operations. 

email_input = "Basavaraja@email.com"
email_stored = email_input.lower()
print(email_stored)  #basavaraja@email.com

text = "Hello, World!"
print(text.lower())
#hello, world!

##########################################################################################
#upper(). converts all chars in the string to uppercase for consistency 

product_code = "abc123"
print(product_code.upper()) #ABC123
print(text.upper()) #HELLO, WORLD!

##########################################################################################
#replace() - replaces a substring with another within a string 

price = "the total is: $50"
print(price.replace("$", "RS")) #the total is: RS50

print(text.replace("World", "python")) #Hello, python!
##########################################################################################
#split() - split the string into a list based ona specified delimeter 

comment = "this product is amazing, I love it!"
words = comment.split(" ")
print(words) #['this', 'product', 'is', 'amazing,', 'I', 'love', 'it!']

print(text.split(",")) #['Hello', ' World!']
##########################################################################################
