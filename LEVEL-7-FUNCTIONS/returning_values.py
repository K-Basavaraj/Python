#we seen How we passed the values intop a function as parameters by passing values.  
#What about getting values out of a function? this is where return values comes. which means 
"""
print() → just shows the result on the screen (you see it, but can't reuse it).
return → gives the result back to your program, so you can store it, use it later, or pass it to another function.
"""
def area_traingle(base, height):
    return base*height/2 #The return sends that value back to wherever the function was called.

area_a = area_traingle(4, 5) #10.0 #Because of return, thoEe values are stored in the variables.
area_b = area_traingle(5, 5) #12.5 #Because of return, these values are stored in the variables.
sum = area_a + area_b  #Adds both (10.0 + 12.5 = 22.5)
print("sum of both areas is: " + str(sum)) #sum of both areas is: 22.5 
#he value 22.5 (which came through return) is converted to string using str(sum)

"""
None means “no value” in Python.
A function returns None by default if you don’t use a return statement.
"""
def greeting(name): 
    print("welcome, " + name)

result = greeting("Basavaraj") #welcome, Basavaraj
print(result) #None