"""
In python we can swap 2 variables in a single line: 
a,b = b,a 
no temp varibale
this works, because of tuple unpacking - the right side 
because a tuple (b,a) then it gets unpacked into (a,b)

Behind the scens, python does this in 2 steps 
i) build a tuple from the right side (b,a) -> (20, 10)
ii) unpack that tuple into the varibales on the left 
a, b = (20, 10)
a = 20 
b = 10
sp tuple creewation + tuple unpcaking haappen at once


"""
#example1: with temp var 
a = 10
b = 20

temp = a 
a = b 
b = temp
print(a,b) #20 10 

#example2: 
a = 10 
b = 20
a,b = b,a 
print(a,b) #20 10 

#example3: with pranthesis 
a =10 
b =20 
(a,b) = (b,a)
print(a,b) #20 10 

#example3: swap inside a list we can swap elements at specific indexes too 
nums = [10, 20, 30, 40]
#swap 1st and last 
nums[0], nums[-1] = nums[-1],nums[0]
print(nums) #[40, 20, 30, 10]