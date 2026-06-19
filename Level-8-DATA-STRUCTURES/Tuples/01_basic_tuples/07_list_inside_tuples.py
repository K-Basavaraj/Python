"""
Tuples are immutable we can not replace items inside them. 
But 
if a tuple contains a mutable object(list a list), we can still modify that object. 
The tuple is locked. But Objects inside the tuple follow their own rules. 

Key-point: 
---------
Tuple containing a list -> tuple locked list flexible 
List containing a tuple -> list flexible, tuple locked
"""
#example: a tuple containing a list 
data = ("config", [1,2,3])
print(data) #('config', [1, 2, 3])

#example: replacing an item in the tuple - fails 
# data[0] = "new-config"
 #    ~~~~^^^TypeError: 'tuple' object does not support item assignment

#Example: Modifying the list inisde the tuple it will work 
result = ("numbers", [1,2,3])
result[1].append(4)
print(result) #('numbers', [1, 2, 3, 4])
result[1][0] = 99
print(result) #('numbers', [99, 2, 3, 4])

"""
Why does this happen? 
A tuple store the reference to its items, not copies.

when the tuple points to a list, the tuple itself is locked, but the list it points to is a separte object that can change. 
result --> tuple 
           [0] -> "numbers"
           [1] -> [1,2,3] <- the list is still mutable
result[1].append(4)  doesnt replace the list it modfies it. 
Thats why the tuple still "conatins" the same list refrnec, but the list itself has grow. 
"""
"""
#example: replacing the list eniterly will fails 
data = ("config", [1,2,3])
data[1] = [9,9,9]
#TypeError: 'tuple' object does not support item assignment ()
You can modify the existing list but can not swap it out for a different list
"""
