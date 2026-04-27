#Basic Assignment: Assigns a value to a variable 
#example1: 
x = 10 

#Addition Assignment (+=): Adds and reassigns (e.g., X += 5 makes X from 10 to 15).
x += 5 #which means x = x + 5 here x is 10 for this 10 we are adding +5 
print(x) #15 

#Subtraction Assignment (-=): Subtracts and reassigns (e.g., X -= 3 makes X from 15 to 12).
x -= 3 #which means x = x - 3 here becomes 15 in that 15 we are sub -3 
print(x) #12

#Multiplication Assignment (*=): Multiplies and reassigns (e.g., X *= 2 changes X from 12 to 24).
x *= 2 #whicxh is equalent to x = x * 2 where x values is now 12 we are mul with 2 
print(x) #24 

#====================================================================================
y = 3

#Exponentiation Assignment (**=): Raises to a power and reassigns (e.g.,X** = 2turnsX from 3 into 9).
y **= 2 #this is equlanet to x = x ** 2 which means 3 ** 2 = 3 × 3 = 9
print(y) #9

z = 24
#Division Assignment (/=): Divides and reassigns 
z /= 4 #equalent to z = z/4 now 
print(z) #6.0

#Floor Division Assignment (//=): Floors division and reassigns 
z //= 2
print(z) #3.0

#If any operand is float → result is float

a = 30 
# a /= 10 
# print(a) #3.0 
a //= 10 
print(a) #3 
#======================================================================================================
# Modulus Assignment (%=): Modulus result reassigned (e.g.,b=6 then b %= 5 leaves b as 1).
b = 6
b %= 5 
print(b) #1
#===========================================================================================
#Unary Operator (Negative Sign) Used to change a positive number to a negative.
trasaction = 100 
refund = - trasaction
print(refund) #-100

#Binary Operator (positive sign)
cart_item1_price = 20 
cart_item2_price = 30 
total_price = cart_item1_price + cart_item2_price
print(total_price)