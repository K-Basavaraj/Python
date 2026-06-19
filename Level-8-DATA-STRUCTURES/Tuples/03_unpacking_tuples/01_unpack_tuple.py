"""
what is tuple unpacking? 
-> unpacking means taking a tuples itmes and assigning each one to its own varible, all in a single line 
syntax: 
  a, b, c = (1,2,3)

this feature use it consestenly - especially with functions that returns tuples 
"""
#example1: The clumsy way 
#without unpacking we have to do it one at a time 

point = (10, 20)
x = point[0]
y = point[1]
print(x,y) #10 20 which is noisy and repetative

#example2: the claen way - unpacking 
#assign all varibales in one line 
x, y = (10,20)
print(x) #10
print(y) #20

#example3: works without paranthese troo 
x, y = 10, 20 
print(x,y) #10 20

#example4: UNPACKING WITH 3+values 
name, age, city = ("Alice", 30, "Hyderabad")
print(name) #Alice
print(age) #30
print(city) #Hyderabad

