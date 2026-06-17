#String Concatenation To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c) #output: HelloWorld here it combines the two strings without adding space between them

#example2: To add a space between them, use " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c) #output: Hello World here it combines the two strings with a space between them

########################################################################################
#String Format: we cannot combine strings and numbers like this:
"""
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
#output: TypeError: can only concatenate str (not "int") to str
To fix this error, we can use the str() function to convert the number into a string
But we can combine strings and numbers by using f-strings or the format() method!
"""
#F-Strings: F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
#example1: Using f-strings to combine strings and numbers:
age = 36
txt = f"My name is Basavaraja, I am {age}"
print(txt) #output: My name is Basavaraja, I am 36 here it combines the string with the number using f-string
########################################################################################
#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value.
price = 59
txt = f"The price is {price} dollars"
print(txt) #output: The price is 59 dollars here it combines the string with the number using f-string

#A placeholder can include a modifier to format the value. A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 59
txt = f"price is {price:.2f} dollars" 
print(txt) #output: price is 59.00 dollars here it combines the string with the number using f-string and formats the number to 2 decimal places

#A placeholder can contain Python code, like math operations:
txt = f"The price was doubled to {price * 2} dollars"
print(txt) #output: The price was doubled to 118 dollars here it combines the string with the result of the math operation using f-string

#example: 
a = 5; b = 3
print(f"{a} + {b} = {a + b}") #5 + 3 = 8
print(f"a squared is  {a ** 2}") # squared is 25\

done = 0.756
print(f"progess: {done:.1%}")

#example: 
name = "Raj"
role = "TEACHER"

message = f"""
user Info: 
  name: {name}
  role: {role}
"""
print(message)

#example: build a log message
server = "web-01"
status = "running"
cpu = 45.7

log = f"[{server}] status={status} cpu={cpu:.1f}"
print(log) #[web-01] status=running cpu=45.7

#example: display server health summary 
servers = [
    {"name": "vm-01", "cpu": 45.6, "memory": 78.2},
    {"name": "vm-02", "cpu": 92.1, "memory": 88.7},

]

for s in servers: 
    print(f"{s['name']:10} CPU: {s['cpu']: 5.1f}%  MEM: {s['memory']:5.1f}%")
"""
vm-01      CPU:  45.6%  MEM:  78.2%
vm-02      CPU:  92.1%  MEM:  88.7%
"""