"""
four utility methods we will use when comapring sets: 

.copy() make an independent duplicate 
.isdisjoint() True if the two sets have nothing in common 
.issubset() -> True if all my items ate in the other set
.issuperset() -> true if i contain all of the other stes items

QUICK_REF:
--------
METHOD                          OPERATOR                    DESCRIPTION
-------------------------------------------------------------------------
.isdisjoint()                      -                    DO we share NOTHING?
.issubset()                     a <= b                  am i fully inside b? 
.issuperset()                   a >= b                  do i fully contain b? 
.copy()                             -                   make an independent duplicate.

NOTE: ALL ARE READ ONLY THEY DONT MODIFY THE SET 
Coomon uses: permission checks, environment isolation

disjoint     = no overlap 
subset       = inside 
superset     = contains

"""
#=============================================================================
#       .copy()
#=============================================================================

#make an independent copy of a set 

orginal = { 1, 2, 3 }
backup = orginal.copy()

backup.add(99)
print(orginal) #{1, 2, 3}  <- unchange 
print(backup) #{99, 1, 2, 3}

#same as lists/dicts: '=' doesnt copy, .copy() does

#=============================================================================
#       .isdisjoint()
#=============================================================================
#check if two sets have nothing in common 
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4}

print(a.isdisjoint(b)) #True No items in common 
print(a.isdisjoint(c)) #False 3 is in both 

#.disjoint means completely separte. 
#use ful for these two groups mutually exclusive? 

#=============================================================================
#       .issubset()
#=============================================================================
#check a=if all of my items are in another set? 

small = {1, 2}
big = {1,2,3,4,5}

print(small.issubset(big)) #True  every item of small is in big 
print(big.issubset(small)) #False big has items not in small

#equivalent operator: <=
print(small <= big) #True 

#AMI I CONTAINED WITHIN ANOTHER SET?

#=============================================================================
#       .issuperset()
#=============================================================================
big = {1,2,3,4,5}
small = {1, 2}


print(big.issuperset(small)) #True big contains everything in small 
print(small.issuperset(big)) #False  

#equivalent operator: >=
print(big >= small) #True 

#DO I CONTAIN ANOTHER SET?