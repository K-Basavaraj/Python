"""
using The backslash as an escape character in programming string to: 

include special char: when wanting to incorporate quotes inside a string, 
the backslash can act as an escape char to avoid synatx errors.
Place a blackslash before each internal quote, like this: 
\" or \'
"""
#Example: 
# "After completing the course, you exclaimed: " I love coding in python!""
#without escape char, this results in a syntax error due to unescaped interanl quotes.
#Proper usage: Add backslashes before the internal quotes: 

#example1: 
quote = "After completing the course,  you exclaimed: \"I love coding in python!\""
print(quote) #After completing the course,  you exclaimed: "I love coding in python!"

###########################################################################################
"""
Using quotes, apostrophes inside string, and multi-line strings. 

Understanding quotes and string in python

-> Quotes within strings:
1) single quotes: '****: surround the entire string with single quotes and use double quotes within it without escaping. 

2) Double Quotes: "****: use double quotes to encpasulate the string and include single quotes inside naturallly.

3)When to escape: For mixed quotes within quotes, use a backslash \ to escape the interanl ones.
"""
#example: single quotes warp the entire string and inside use double quotes 
'they said, "Python is amazing!"'

#example2: double quotes wrap the enitre string you can put single apostrophe inside
"It's a great day to code even more!"