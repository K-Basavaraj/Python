"""
A dict comprehension builds a dict in a single line. 
its like a list compreshension, but produce a dict. 

synatx: 
{key_expr: value_expr for item in iterable }
{key_expr: value_expr for item in iterables if condition}

mental_map(same shape as list comprehension)
{what_key: what_avlue for item in source if filter}
"""
#example1: the long way vs the short way 
squares = {}
for n in range(1,6):
    squares[n] = n * n
print(squares) #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#short way 
squares = {n: n * n for n in range(1,6)}
print(squares) ##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
#-------------------------------------------------------------------------------
#example2: with a filter if condition 

evens = {n: n * n for n in range(1, 11) if n % 2 == 0}
print(evens) #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
#-------------------------------------------------------------------------------
#example3: convert two list into a dict 
keys = ["name", "age", "city"]
values = ["Alice", 30, "Pune"]

person = {k: v for k, v in zip(keys, values)}
print(person) #{'name': 'Alice', 'age': 30, 'city': 'Pune'}
#-------------------------------------------------------------------------------
#example4: transform an exsiting dict 
prices = {"apple": 50, "banana": 30, "cherry": 70}

#apply 10% discount on all prices 
discounted = {name: price * 0.9 for name, price in prices.items()}
print(discounted)
#{'apple': 45.0, 'banana': 27.0, 'cherry': 63.0}
#-------------------------------------------------------------------------------
#example5: filter an existing dict 
scores = {"india": 250, "england": 150}

#keep only who won the match 
won = {name: score for name, score in scores.items() if score >= 200}
print(f"{won} the match") #{'india': 250} the match
#-------------------------------------------------------------------------------
#example6: swap keys and values 
person = {"name": "Raj", "role": "Doctor"}

swapped = {v: k for k, v in person.items()}
print(swapped) #{'Raj': 'name', 'Doctor': 'role'}
#-------------------------------------------------------------------------------
#example7: with a conditional value (inline if/else)

scores = {"Raj": 90, "rajesh": 40, "charli": 92}

#label each score as pass or fail 
results = {name: ("pass" if score >=50 else "faill") for name, score in scores.items()}
print(results)
#{'Raj': 'pass', 'rajesh': 'faill', 'charli': 'pass'}
#-------------------------------------------------------------------------------
#example8: normalize keys (all lowercase)
config = {"HOST": "local-host", "PORT": 5432, "USER": "admin"}

lower_config = {k.lower(): v for k, v in config.items()}
print(lower_config)
#{'host': 'local-host', 'port': 5432, 'user': 'admin'}
#-------------------------------------------------------------------------------
