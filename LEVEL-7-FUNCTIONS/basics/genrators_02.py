"""
################### GENERATORS: #####################

are special type of functions that generetaes values one at a time using "yield" keyword. 
memory-effecincy, pausing after each value is produced and resuming as needed 
ideal for managing large datasets or sequences, siumilar to baking batches of cookies as needed insted of all at once. 

example:  a gernatror "count_up_to", to count up incrementally. 

genrators use "yield" fo sequence.

==> Why Use Generators?
Memory Efficiency: Conserve memory by processing data in chunks.
Convenience: Pause and resume a process, yielding batches as needed.

==> Function to Implement Generators
Use the yield keyword instead of return to allow continuity.
batch_size defines the size of each batch.
Optional max_batches limits the number of iterations.
"""
#example1: 
def count_up_to(max):
    count = 1
    while count <= max:
        yield count 
        count += 1

counter = count_up_to(5)
print(next(counter)) #1
print(next(counter)) #2
print(next(counter)) #3 
print(next(counter)) #4
print(next(counter)) #5
#print(next(counter)) # StopIteration


#example2a: 
def bake_cookies(batch_size, max_batches=None):
  batch_count = 0
  total_cookies = 0
  while max_batches is None or batch_count < max_batches:
    total_cookies += batch_size
    yield total_cookies
    batch_count += 1

# limited_cookie_batches = bake_cookies(100, max_batches=3)
# for cookies in limited_cookie_batches:
#     print(f"Baked {cookies} cookies in total.")
"""
Baked 100 cookies in total.
Baked 200 cookies in total.
Baked 300 cookies in total.
"""
#Example2b:
#Run in iterations with the next() function to yield cookies up to the defined limit.
#Stop after reaching the batch limit to avoid overproduction.
#Takeaway: Generators offer efficient, controlled sequence handling in programming tasks.
limited_cookie_batches = bake_cookies(100, max_batches=3)
print(next(limited_cookie_batches)) #100 
print(next(limited_cookie_batches)) #200 
print(next(limited_cookie_batches)) #300 
#print(next(limited_cookie_batches)) # print(next(limited_cookie_batches)) ~~~~^^^^^^^^^^^^^^^^^^^^^^^^StopIteration

#example2c: 
#for unlimeted cokkies insted of limited we use like this 
unlimited_cookie_batches = bake_cookies(100)
print(next(unlimited_cookie_batches)) #100 
print(next(unlimited_cookie_batches)) #200
print(next(unlimited_cookie_batches)) #300 
print(next(unlimited_cookie_batches)) #400 