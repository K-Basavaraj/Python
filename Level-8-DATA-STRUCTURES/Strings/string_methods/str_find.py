"""
1)what is find()? 
.find() searches for a subsstring inside a string and returns: 
  - The INDEX (POSITION) where it first appears
  - -1 if the substriung is not found 
synatx: 
  string.find(substring)
  string.find(substring, start)
  string.find(substring, start, end)

#Note: returns -1 insted of crashing - safe to use
"""
#example1: 
text = "Hello world"
print(text.find("world")) #6
print(text.find("Hello")) #0
print(text.find("python")) #-1

#example2: How index work in the sring 
text = "Hello World"
print(text.find("W")) #6

#example3: find() vs index() 
text = "Hello"

#find() returns -1 if not found - safe 
print(text.find("xyz")) #-1

#index() raises ValueError if not found - risky 
#print(text.index("xyz")) #ValueError

#example4: find only returns the first occurrence
text = "banana"
print(text.find("a")) #1
#'a' appears at indexes 1 3 4 - find only returns the first

#example6: search from a specific position 
text = "banana"

print(text.find("a")) #1
print(text.find("a", 2)) #3
print(text.find("a", 4)) #5

#example7: search within a range 
print(text.find("a", 0, 4)) #1 search only between index o-4 
print(text.find("a", 0, 1)) #-1 no 'a' in range [0,1)]

#example7: check if a log line contains an error 
log = "2026-01-15 ERROR: Database connection failed"
if log.find("ERROR") != -1:
    print("Log contains an error")

#But for "does it contain x? - use the 'in operator insted"
if "ERROR" in log: 
    print("Clear check using 'in")

#example8: extratct a substri8ng before a delimeter 
log = "ERROR: Database connection failed"

pos = log.find(":")
if pos != -1: 
    severity = log[:pos]
    message = log[pos+1:].strip()
    print(f"severity: {severity}")
    print(f"Message: {message}")
"""
severity: ERROR
Message: Database connection failed

#NOTE: find() vs in opertor which to use? 
use in does it contain x? 
use find() where is x? 
"""
