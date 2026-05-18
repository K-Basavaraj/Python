"""
Lambda is just a tiny one-line function that you can write inline, without giving it a name. 
which means, instead of defining a function with def and giving it a name, you can use lambda to create a function on the fly.

Lambda is "anonymous function" because it does not have a name. which means it exist for a moment 
you use it and immeditly and throw it away.

Function you'll use multiple times -> use def 
Function you'll use once -> use lambda

syntax: key=lambda s: s["filed"]
can take multiple inputs like lambda a, b: a + b
most often used inline with sort(), map(), filter() or similar functions.

servers.sort(key=lambda s: s["cpu"]) #sort the list of dictionaries by the value of the "cpu" key using a lambda function as the key rule to compare 
items
lambda s: s["cpu"] the rule is take each item s, return s["cpu"]

Limts of Lambda: 
only one expression, no multipl elines, no if/else blocks(you can do a one line if, but keep it simple)
No return keyword the exression itself is the return value.

"""
#example1: regular function 
def get_cpu(server): 
    return server["cpu"]

#this above function takes one input called "server" and returns one thing "server['cpu']"
s = {"name": "web-01", "cpu": 45, "memory": 16}
print(get_cpu(s)) #45

#rewrite the above function using lambda same exact function as lambda but without the name and def keyword
get_cpu = lambda server: server["cpu"] #lambda takes the same input and returns the same output as the regular function but without a name
print(get_cpu(s)) #45

#example: side by side comparision of regular function vs lambda function
#regular function
def square(x): 
    return x * x

#lambda function
square = lambda x: x * x # lambda is a keyword and x is a input/parameter and x * x is the return value of the function
print(square(5)) #25

#example2: add two numbers using regular function vs lambda function
#regular function
def add(a, b):
    return a + b

#lambda function
add = lambda a, b: a + b
print(add(3, 4)) #7

#example3: get a key from a dictionary using lambda function
#regular function
def get_name(server):
    return server["name"]

#lambda function
get_name = lambda server: server["name"]
s = {"name": "web-01", "cpu": 45, "memory": 16}
print(get_name(s)) #web-01

#example4: check even or odd using lambda function
#regular function
def is_even(n):
    return n % 2 == 0

#lambda function
is_even = lambda n: n % 2 == 0
print(is_even(4)) #True
print(is_even(5)) #False

#Note: Most often used inside sort(), map(), filter() or similar functions. 

#example5: 
servers = [
    {"name": "web-01", "cpu": 45},
    {"name": "web-02", "cpu": 30},
    {"name": "db-01", "cpu": 80}
]

servers.sort(key=lambda server: server["cpu"]) #sort the list of dictionaries by the value of the "cpu" key using a lambda function as the key
print(servers) #[{'name': 'web-02', 'cpu': 30}, {'name': 'web-01', 'cpu': 45}, {'name': 'db-01', 'cpu': 80}] sorted in ascending order by cpu usage

#or 
servers.sort(key=lambda s: s["cpu"])
print(servers) #[{'name': 'web-02', 'cpu': 30}, {'name': 'web-01', 'cpu': 45}, {'name': 'db-01', 'cpu': 80}] sorted in ascending order by cpu usage
# 'S' is just a varibale/placeholder name. python will pass each list item to the lambda and call it s temporary variable that holds the current item being processed in the sort function.
#Note: you could name it anything 
servers.sort(key= lambda x: x["cpu"])
servers.sort(key= lambda srv: srv["cpu"])

#example5: 
#1. A lamda that takes a number and return it doubled
double = lambda x: x*2
print(double(5)) #10

#2. a LAMDA THAT TAKES A STRING AND RETURN ITS LEANGTH, AND CONVERT IT TO UPPERCASE OR LOWERCASE, OR GET THE FIRST CHARACTER OR lAst CHARACTER
length = lambda s: len(s)
print(length("hello world")) #11

uppercase = lambda s: s.upper()
print(uppercase("hello world")) #HELLO WORLD

lowercase = lambda s: s.lower()
print(lowercase("HELLO WORLD")) #hello world

first_char = lambda s: s[0]
print(first_char("hello world")) #h

last_char = lambda s: s[-1]
print(last_char("hello world")) #d
