"""
what is indexing? 
each item in a tuple has position number called an index.
indexes start at 0 (same as lists and strings)

synatx: 
tuple_name[index]
use[] to lookup an item by its position

indexing is like "Iknow the the position give me the value
"""
#example1: 
fruits = ("apple", "banana", "cherry", "date")
print(fruits[0]) #apple
print(fruits[3]) #date
#print(fruits[4]) IndexError: tuple index out of range

#example: indexing on a functions return value functions that return values actually return a tuple. 

def get_server_info(): 
    return "web-01", "10.0.0.0", "running"

info = get_server_info()
print(info) #('web-01', '10.0.0.0', 'running')
print(info[0]) #web-01
print(info[1]) #10.0.0.0
print(info[2]) #running

#example: storing the result of an index into a variabe
fruits=("apple", "banana", "cherry")
first_fruit = fruits[0]
print(first_fruit) #apple 
last_listed = fruits[2]
print(last_listed) #cherry

#example
server = ("vm-01", "10.0.0.1", "running")
server_name = server[0]
server_ip = server[1]
server_status = server[2]
print(f"{server_name} at {server_ip} is {server_status}") #vm-01 at 10.0.0.1 is running


###########################################################################################
#negaitive indexing 
fruits = ("apple", "banana", "cherry", "date")
print(fruits[-1]) #date
print(fruits[-2]) #cherry

#EXAMPLE: EACH ITEM HAS TWO VALID INDEXS
print(fruits[0], fruits[-4]) #apple apple
print(fruits[1], fruits[-2]) #banana cherry