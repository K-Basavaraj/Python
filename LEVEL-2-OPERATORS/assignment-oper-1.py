a = 5 
b = 3 
print( a == b) #False
print( a != b) #True
print( a > b) #True
print( a < b) #False
print( a >= b) #True
print( a <= b) #False
#=========================================
#accuracy of floating point numbers 
num1 = 0.1 
num2 = 0.2
sum = num1 + num2
print(sum == 0.3) #False
print(sum) #0.30000000000000004

#import the decimal class from the decimal module create a variable called num1_decimal and convert num1 to a string.
#import the decimal class from the decimal module create a variable called num2_decimal and convert num2 to a string.
from decimal import Decimal
num1_decimal = Decimal(str(num1))
num2_decimal = Decimal(str(num2))
sum_decimal = num1_decimal + num2_decimal
print(sum_decimal) #0.3
#=========================================
#type casting 
p = "123"
q = int(p) #type casting string to integer
print(type(q)) #<class 'int'>
print(q) #123

r = "123.45"
s = float(r) #type casting string to float
print(type(s)) #<class 'float'>
print(s) #123.45
#=========================================
c = "15"
d = int(c) #type casting string to integer
print(d+5) #20

myvariable = False 
if myvariable:
    print("yes")
else:
    print("no") 