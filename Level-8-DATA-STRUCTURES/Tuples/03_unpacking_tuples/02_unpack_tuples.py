#example1 works with any iterable (not just tuples!)
#unpacking also works on lists, strings, and other iterables. 

#from a list 
a, b, c = [1,2,3]
print(a,b,c) # 1 2 3

#from a string 
ch1, ch2, ch3 = "ABC"
print(ch1, ch2, ch3) # A B C

#NOTE: VARIBLE COUNT MUST MATCH TUPLE SIZE 
data = (1,2,3)
#a,b = data #ValueError: too many values to unpack (expected 2)

#a, b, c, d = data #ValueError: not enough values to unpack (expected 4, got 3)
###############################################################################

#example2: use _ as a "throwaway" variable
#when we dont care about one of the values, name it _ (underscore)
#its like i am ignoring this. 

person = ("Alice", 30, "engineer")

name, _, role = person 
print(name) #Alice
print(role) #engineer
###############################################################################