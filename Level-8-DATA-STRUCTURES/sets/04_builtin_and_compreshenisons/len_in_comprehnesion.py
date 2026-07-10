"""
Three genral purpose tools that work with sets: 

len(s) -> count of items 
x in s  -> is x in s? 
{x for x in ..}  -> set comprehension (build in one line)

In devops if you check membership often, use a set. 
where lists lookup: slow(check every item)
set lookup: fast(uses hashing - instant)

Key_take aways: 
------------
-> len(s) counts items in a set 
-> 'x in s' is fast much fater than list lookup 
-> set comprhension: {expr for x in iterable if cond}
        -> same shape as list/dict comprehension
        -> duplicates are auto-removed
-> duplicateion trick: list(set(items))
-> if order matters use list(dict.fromkeys(itmes)) insted
"""
#==================================================================================================
#                           .len()
#==================================================================================================

s = {"apple", "banana", "cherry"}
print(len(s)) #3

empty = set() 
print(len(empty)) #0

#same as for lists, tuples, dicts - counts teh items..
 
#==================================================================================================
#                           in / not in 
#==================================================================================================
#sets are much faster at membership checks than lists!

s = {"apple", "banana", "cherry"}

print("apple" in s) #True
print("grape" in s) #False
print("grape" not in s) #True

#==================================================================================================
#                           set comprehension
#==================================================================================================
#Build a set in one line - same like list/dict comprehensions

#synatx: 
#  { expression for item in iterable }
#  { expression for item in iterable if condition }
#notice use like {}, but no colon: (that what makes set)

#example1: 
squares = {n * n for n in range(1,6)}
print(squares) #{1, 4, 9, 16, 25}

#example2: with filter 
even_squares = { n * n for n in range(1, 11) if n % 2 == 0}
print(even_squares) #{64, 100, 4, 36, 16}

#example3: auto duplication in comprehnsion 
words = ["apple", "banana", "apple", "cherry", "banana"]

#set comprehension automatically removes duplicates 
first_letters = {w[0] for w in words}
print(first_letters)

#The duplicateion trick (very common in devops)
#convert list to a set to remove duplicates 
#then convert back to list if we need list features 

items = ["a", "b", "c", "d", "e", "b", "a"]

unique = list(set(items))
print(unique) #['b', 'c', 'e', 'd', 'a']
