
#example4: Differnt error types of different situations 
def get_user(users, user_id):
    if not isinstance(user_id, int): 
        raise TypeError("user_id must be integer")
    if user_id < 0: 
        raise ValueError("user_id must be non negative")
    if user_id not in users: 
        raise KeyError(f"user {user_id} not fount")
    return users[user_id]

users = {1: "Alice", 2: "Bob"}

print(get_user(users, 1))
print(get_user(users, "Hello"))
print(get_user(users, -5))
print(get_user(users, 99))
"""
output: 
Alice
Traceback (most recent call last):
  File "e:\Python\LEVEL-3-KEYWORDS\02-ERROR-HANDLING\12_raise.py", line 82, in <module>
    print(get_user(users, "Hello"))
          ~~~~~~~~^^^^^^^^^^^^^^^^
  File "e:\Python\LEVEL-3-KEYWORDS\02-ERROR-HANDLING\12_raise.py", line 72, in get_user
    raise TypeError("user_id must be integer")
TypeError: user_id must be integer
"""
######################################################################################################################
#catch, log, and RE-Raise
#sometimes you want to log an error and let it propagate up.

def risky_operation():
    try:
        result = 10/0
    except ZeroDivisionError as e: 
        print(f"Logging error: {e}")
        raise #re-raise the same error 

risky_operation()
"""
output: 
Loggig error: divison by zero
(Then ZeroDivisionError crashes the program)
"""
######################################################################################################################
#raise + try/except -manual error + catch 
def process_data(data): 
    if not data: 
        raise ValueError("Data cannot be empty")
    return data.upper() 

try: 
    process_data("")
except ValueError as e: 
    print(f"caught: {e}")

"""
output: 
Data cannot be empty
"""