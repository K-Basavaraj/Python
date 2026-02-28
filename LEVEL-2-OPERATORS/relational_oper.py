"""
Comparision/Realtrional operators return Boolean results. 
we can use comparison operators to compare values. 
Note: Bollean data types are not string data types (Boolean True is not equal to the string "True")
"""
print(10 > 1) #True
print("cat" == "dog") #False
print(1 != 2 ) #True

#'+' operator doesnt work between int and string But here whie comparing also same not supported between instances of 'int' and 'str'
"""
print (1 < "1") #TypeError: '<' not supported between instances of 'int' and 'str'
"""
print (1 == "1") #False in this case the interpreter has no problem telling us that int 1 and str 1 arent the same. 

#The = equal assignment operator is used to assign a value to a variable 
my_var1 = 3*5 
print(my_var1) #15
print(my_var1 == 3*5) #True

#example1 == and !=
print(32 == 30+2) #True
print(5+10 == 6+7) #False
print(10-4 != 10+4) #True
print(9/3 != 3*1) #False 
"""
Why 3.0 != 3 is False in Python
Python compares numeric values, not their data types.
Even though 3.0 is a float and 3 is an integer, both represent the same numeric value.

Therefore:
3.0 == 3 → True
3.0 != 3 → False
 Key Point to Remember
== and != ignore type differences when comparing numbers.
If the numeric values are the same, Python treats them as equal.
"""
#example2 > and <
print(11 > 3*3) #True
print(11 < 3*3 ) #True
print(4/2 > 8-4) #False
print(4/2 < 8-4) #True 2.0 < 4 For <, >, <=, >=: Type difference doesn’t matter — Python compares only the numeric value.


#example2 >= and <=
print(12*2 >= 24) #True 24 >=24
print(12*2 <= 30) #True 24 <=24
print(18/2 >= 15) #False 9.0 >= 15
print(15 <= 18/2) #False 15 <= 9.0

#Comapre operation with strings
print("a string" == "a string") #True
print("4 + 5" == 4 + 5) #False
print("rabbit" != "frog") #True
print("three" == 3) #False two items are not equal
event_city = "shambala"
print(event_city != "shambala") #False
# False because != means "not equal".
# The variable event_city contains the same text as the static string "shambala".
# Since both values match, the "not equal" comparison becomes False.

#operators with > and < 
#Note: ASCI valuys A-7(65-90) a-z(97-122) check the starting char from string 
print("Wednesday" > "Friday") #true W asci value is grester that F 
print("Brown" < "brown") #true B asci value is less than b 
#if the strings have the same first few letters, The comaprision cycle throuigh each letter of each string, from left to right untill it find two letters diff
print("sunbathe" > "suntan") #false b is lessthan t
#if two identical strings are compared using the less than </> comparision opertor this will produce a false result because they are equal.
print("Lima" < "Lima") #False
"""
print("Five" < 6) #TypeError: '<' not supported between instances of 'str' and 'int'
The last example trying to compare two items of different data types using < operator. 
The < and > oprtors can not be used to compare two different data types.
"""
#operators with >= and <= 
print("my computer" >= "my chair") #true o >= h asci value 
print("spring" <= "winter") #true s <= w asci value
# If two identical strings are compared using >= or <=, the result is True
# because these operators allow equality. 
# Identical strings are equal, so >= and <= return True.
print("pineapple" >= "pineapple") #True


var1 = "my computer" >= "my chair"
var2 = "spring" <= "winter"
var3 = "pineapple" >= "pineapple"
print("Is \"my computer\" greater than or equal to \"my chair\"? Result: ", var1)
print("Is \"spring\" less than or equal to \"winter\"? result: ", var2 )
print("Is \"pineapple\" greater than or equal to \"pineapple\"? Result: ", var1)
"""
Is "my computer" greater than or equal to "my chair"? Result:  True
Is "spring" less than or equal to "winter"? result:  True
Is "pineapple" greater than or equal to "pineapple"? Result:  True
"""
"""
When strings are identical:
Comparison	Result
==	True
!=	False
<	False
>	False
<=	True
>=	True
Because:
< and > need one to be smaller/larger → False
<= and >= include equality → True
"""