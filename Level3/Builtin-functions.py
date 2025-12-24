"""
Built-in functions in pythonb including print(), type(), str(), etc; 
these built-in functions can call directly. 
mostly used functions: 
--> sorted(), max(), min(), abs(),  any(), all(), dir(), enumerate(), sum(), round()
int(), float(), list(), tuple(), set(), dict(), map(), reversed(), range() 
"""
#################################################################################################################################
##print() function outputs/print a specified object to the screen. 
month = "October"
print("Investigation failed login attempts during", month, "If more than", 100 )
# Investigation failed login attempts during October If more than 100

##################################################################################################################################
#TYPE() FUNCTION Returns the data type of its argument helps to track of the data-types to avoid errors. it accepts only single argument.
name = "Basavaraj"
print(type(name)) #<class 'str'> this is called passing one function into another 
print(type("this is a string")) #when workinmg with functions often need to pass through print()if you want the output the data type to the screen. It Display str() which means the argmnt passed to the type() functoion is a string. 
#this happend because type() is processed first and its output passed as an argument to the print(). 
##################################################################################################################################
#str() function can be used to convert any data type to string. this str() takes single argument/ which is the value that you want to convert to a string. 
number = 123 
string_representation = str(number)
print(string_representation) #123
##################################################################################################################################
#sorted() function sorts the component of a list. The sorted function also works on any iterable, like a string. and returns the sorted elements in a list. By defult it sorts them in ascending order. An iterable that conatins strings that begin with alphabatical char will be sorected alphabatically. 
time_list = [ 12, 3, 6, 9]
print(sorted(time_list)) #[3, 6, 9, 12]

#The sorted function does not chnage the iterable that it sorts. 
numbers = [ 12, 1, 4, 6, 9, 5 ] 
print(sorted(numbers)) #[1, 4, 5, 6, 9, 12]
print(numbers) #[12, 1, 4, 6, 9, 5]

# sorted function can not take list or strings that have elemenmts of morethan  one data type example: you cant use the list(1, 2, "Hello")
##################################################################################################################################
#max() function returns the largest numeric input passed into it. The min() returns the samllest numeric input passed into it.
#The max() and min() aceept argmnt of either multiple numeric values of an iterable like a list and they return the largest or smallest vlue respectivly. 
time_lists = [ 12, 2, 4, 5, 9, 8, 6, 7 , 1]
print(max(time_lists)) #12
print(min(time_lists)) #1
##################################################################################################################################