print(0.1 + 0.2 == 0.3) #False
print(0.3) #0.3
print(0.1 + 0.2) #0.30000000000000004

a = 0.1 
b = 0.2 
print(a + b) #0.30000000000000004
#when we print the sum of a  + b this unexpectedly will not equal 0.3 but instead it will be 0.30000000000000004 which is not what we would want or expect
# This happens because 0.1 and 0.2 can not be representd exactly as binary floating point numbers. 
#Their binary represenattions are approximations, and when we add them together, the result is also an approximation, which is why we get 0.30000000000000004 instead of 0.3.

#so By using decimal module we can get more accurate results when working with floating point numbers.
from decimal import Decimal
a = Decimal('0.1')
b = Decimal('0.2')
print(a + b) #0.3   

#handling floating point precision with decimal module set precision using getcontext().prec allows control over 
#mathematical operatios accuracy. useful for applications demanding accuracy eg: account balance calculations, scientific computations, and any scenario where precision is crucial..

from decimal import Decimal, getcontext
getcontext().prec = 1 # Set precision to 1 decimal place
a = Decimal(0.1)
b = Decimal(0.2)
print(a + b) #0.3   

#example2
item1price = 19.9
item2price = 5.7
item3price = 3.5

total_price = item1price + item2price + item3price
print(f"Total price: ${total_price}") #Total price: $29.099999999999998
print(f"Total price: ${round(total_price, 2)}") #Total price: $29.1
print(f"Total price: ${format(total_price, '.2f')}") #Total price: $29.10