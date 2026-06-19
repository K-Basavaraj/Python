""""
sorted() returns a new sorted list from the tuple the orginal tuple is unchnaged (tuples are immutable)

synatx: 
sorted(tuple_name)
sorted(tuple_name, reverse=True)
sorted(tuple_name, key=function)
"""
nums = (45, 92, 30, 75,88)
result = sorted(nums)
print(result) #[30, 45, 75, 88, 92]
print(type(result)) #<class 'list'>
#even though we sorted a tuple the reuslt is a list why bcz sorting needs a mutable contaiuner internally.

#if we need a tuple back, convert it 
result_tuple = tuple(sorted(nums))
print(result_tuple) #(30, 45, 75, 88, 92)
print(type(result_tuple)) #<class 'tuple'>

#example: sort in descending order 
print(sorted(nums, reverse=True)) #[92, 88, 75, 45, 30]

#example sported string 
fruits = ("banana", "apple", "cherry")
print(sorted(fruits)) #['apple', 'banana', 'cherry']
print(sorted(fruits, reverse=True)) #['cherry', 'banana', 'apple']

#example: 
employees = (
    ( "Alice", 30),
    ("Bob", 25),
    ("charle", 35),
)
#sort by ascending 
by_age = sorted(employees, key=lambda emp:emp[1])
print(by_age) #[('Bob', 25), ('Alice', 30), ('charle', 35)]

#sort by descending 
oldest_first=sorted(employees, key=lambda emp:emp[1], reverse=True)
print(oldest_first) #[('charle', 35), ('Alice', 30), ('Bob', 25)]

#example: 
servers = (
    ("VM-1", 45),
    ("VM-2", 92)
)
most_loaded = max(servers, key=lambda s:s[1])
print(f"Most loded: {most_loaded[0]} ({most_loaded[1]}% cpu)")
#Most loded: VM-2 (92% cpu)

