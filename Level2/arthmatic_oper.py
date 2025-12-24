"""
Python can calculate numbers using common mathamatical operators along with 
special operators too.
x+y, x-y, x*y, x/y
x ** y exponent operator returns the result of raising x to the power of y. 
x ** 2 squere expresion returns x squad
x ** 3 cube expression return x cubed.
x**(1/2) square root(1/2) or 0.5 fractional exponent operator returns the square root of x 
x //y floor division opertor returns the integer part of the integer division of x by y.
"""
#====================================================================================================
                                    # Addition: #
#====================================================================================================
print(4+5) #9
#case2: Breaking line without continuation symbol
x = 1 +    2
+3 
print(x)
#output: 3  #`+3` is treated as a separate statement and ignored here
#case3: Using backslash '\' to continue expression
y = 1+   2 \
+3 
print(y)
#output: 6 

#example1 with intalize
a = 1; b=2.5
c=a+b
print(c)                 # int + float  = float type ans is 3.5

#example2 Insert the correct syntax to assign values to multiple variables in one line:
x , y = 4, 8
print(x+y) #12

#example3 Insert the correct syntax to assign the same value to all three variables in one code line.
x = y = z = 5
print(x+y)
#====================================================================================================
                                    # substraction: #
#====================================================================================================
#basic without intalize 
print(1-2.5)  # here int + float the ans is float type -1.5

#example1
a=0; b=.5
c=a-b
print(c)      # here also same int +float is float ans is -0.5
#====================================================================================================
                                    # Multiplication: #
#====================================================================================================
print(9*7) #63

#example4
a=9.8; b=7.6; c=4.5
d=(a*b*c)
print(d)  #335.16

#example1
a=5; b=4.0
c=a*b
print(c) #int * float = float ans 20.0

#====================================================================================================
                                    #Division: #
#====================================================================================================
# A Division operation is always results in a floating pount numbers
print(2/4) #ans is 0.5 here int/int = float is the answer there is no decimal lose value                          while in java we loose .5 value.

print(-1/4) #-0.25
print(1/3) #0.3333333333333333

"""
#Note: as you observer above example annswer always your getting float you need int as answers  
there is a special symbol called "  Floor Division (//)  " 
if you want as integaer value the use "// insted /"
it works only int/int values and  not in float/int values or int/float values

"""
#example6: 
a = 4 ; b = 2
c=(a//b)
print(c)  # int/int = int value ans is 2 Returns the quotient of the division, removing the decimal part.

#example7: compare with example 6 and read the above note
print(4.0//2) #see it doesnt work for here it doesnt work float/int

#====================================================================================================
                                    #Modulus: #
#====================================================================================================
#this opertion is used to find the reminder the value present on the left side of the operation                 acts as a dividend and the one right side is divisior 

# in division where there is an option "//" to make int value as answer but in modules operator                 there is no such type so, you need to make is as "type casting"

# Keynote: when numerator < denominator then answer is numerator. because the numerator doesn't have            enough value to be divided by the denominator even once, leaving the remainder equal to the                     value of the numerator. 

#The reminder will be '+ve' if the dividend is '+ve' Even if the Divisor is '-ve' But                       the Divided is '+ve' then Reminder will be '+ve'

#example1:
print(5%100)  #as i mentioned in note whenever numerator is less than greter then the answer is                 numarator which is 5

#example2:
a=438; b=5
print(a%b)  # lets calculate manually 438÷5=87  87×5=435  so here, 438−435= 3 so the ans reminder is 3

#example5:
a=5; b=40.5 
c=(a%b)
print(c) #here also same if the the num < den where value is int/float then ans is float which is 5.0

#example6: sample type cast how we can make it int from abover example5 ans 
a=5; b=40.5 
c=(int(a%b)) #or just c=int(a%b)
print(c)     #here ans is int/float where ans is int 5

#====================================================================================================
                                    #Exponentiation: #
#====================================================================================================
print(2 ** 3) #8 2 power 3 2 * 2 *2 is 8 

#example1:
a=4.8; b=5.3
print(a**b) #here floatnum power floatnum 4.8 power of 5.3 the answer is 4079.2334300067487

#example2: 
a= 4.7; b=5
c=(a**b)
print(c)  #here floatnum power of int num which is 4.7 power of 5 ans is 2293.4500700000003
#====================================================================================================
"""
order of operations: can be calculated from left to right
-----------------
1. paranthesis (), {}, []
2. exponents (x**y)
3. multiplications and divisions and 
4 Addition and substraction.
"""
print(((2050/5)-32)/9) #42.0 

