#adding items 
s = {"apple", "banana"}

s.add("cherry") #add one item 
print(s) #{'cherry', 'apple', 'banana'}

s.update(["date", "fig"])
print(s) #{'date', 'cherry', 'fig', 'apple', 'banana'}

#Note: add() one item and update() many items any iterable 

#Removing items 
s.remove("banana") 

#.remove() - crashes if missing 
#s.remove("mango") #kerError

#.discard() safe (no crash if msising)
s.discard("mango")

#.POP() - REMOVE A RANDOM item, return it 
removed = s.pop() 
print(s) ##{'cherry', 'fig', 'apple'}

#use .discard when your not sure if the item exists 
#use .pop() remove a random item (sets have no order)


#sets are unordered  - no indexing 
s = {"a", "b", "c"}
# s[0] TypeError: 'set' object is not subscriptable
#you can not access items by position. 

#To loop through a set 
for item in s: 
    print(item)
# b c a 