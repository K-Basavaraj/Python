"""
The four main operations

#each has two ways to call it: 
1. a method             -> a.union(b)
2. an opertor symbol    -> a | b

Both do samething - pick which read better 

1. UNION                    -> |    or  .union()                        everything from BOTH stes 
2. INTERSECTIONS            -> &    or  .intersection()                 only items in both sets 
3. DIFFERENCE               -> -    or  .difference()                   "in A but not in B"
4. SYMMETRIC DIFFERENCE     -> ^    or  .symmetric_difference()         "in either set, but not in both"


note:WHEN TO USE METHOD VS OPERTOR

Operator( | & - ^ ) works only between sets 
methods (.union() etc ) works with any iterable (list, tuple, etc; )

a | [1,2,3] #type error
a.union([1,2,3]) #IT WILL WORK it treats list as set. 

USE METHODS WHEN COMBINING WITH NON-SET DATA 
USE OPER WHEN ITS SET YO SET CLEANER AND SHORTER 

KEY-POINT: 
DIRCTION MATTERS FOR '-' NOT FOR | & ^ 
"""
#example : TWO SETS USES IN ALL EXAMPLES 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

#==================================================================================================
#1. UNION                    -> |    or  .union()                        everything from BOTH stes 
#===================================================================================================
#Give me everything no duplicates. 

print(a | b)    #{1, 2, 3, 4, 5, 6}
print(a.union(b))  #{1, 2, 3, 4, 5, 6}
#BOTH SYNTAX FICES SAME RESULT WHERE AUTOMATICALLY DISAPPER (sets remove them)


#==================================================================================================
#2. INTERSECTIONS            -> &    or  .intersection()                 only items in both sets 
#==================================================================================================
#what do they have in common? 
print(a & b) #{3, 4}
print(a.intersection(b)) #{3, 4}

#==================================================================================================
#3. DIFFERENCE               -> -    or  .difference()                   "in A but not in B"
#==================================================================================================
#WHATS ONLY in A? 

print( a - b )  #{1, 2}            <- only in a 
print(a.difference(b)) #{1, 2}

print(b - a) #{5, 6}                  <- only in b 
print(b.difference(a)) #{5, 6}

#differnce matters ! a -b != b -1 

#===========================================================================================================
#4. SYMMETRIC DIFFERENCE     -> ^    or  .symmetric_difference()         "in either set, but not in both"
#===========================================================================================================
#whats unique to each set (i.e; not shared)? 

print(a ^ b) #{1, 2, 5, 6}
print(a.symmetric_difference(b)) #{1, 2, 5, 6}