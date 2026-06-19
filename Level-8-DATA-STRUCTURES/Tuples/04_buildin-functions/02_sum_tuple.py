"""
sum(tuple) add up all numeric items in the tuple. 

syntax: 
  sum(tuple_name)
  sum(tuple_name, start_value)
returns:  a number (the total) 
only works with numbers will crash on strings 
"""
nums = (10, 20, 30,40)
print(sum(nums)) #100

#example2: sum() works on mixed numeric types (int +float)
prices = (9.99, 4.50, 12.00, 3.75)
print(sum(prices))#30.24

#example3: 
nums = (10, 20, 30)
print(sum(nums)) #60
print(sum(nums, 100)) #160

print(sum(nums)/len(nums)) #20.0