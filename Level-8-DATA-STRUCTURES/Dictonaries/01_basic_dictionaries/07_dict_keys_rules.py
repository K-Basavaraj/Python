"""
The RULE FOR DICT KEYS (WHAT CAN AND CAN NOT BE USED AS A KEY)

2 imp rule: 
R1-> Keys must be immutable ( can not change)
R2-> keys must be UNIQUE ( no duplicates allowed)

These rules are exist because dicts use the Key's "fingerprint"
(called a HASH) to find data instantly. 

If Key could chnage or be duplicate, the dict keep track of anything.
"""

"""
Not allowed mutable types 

1)
List are mutable so not allowed inside dict. 
which means a list can not be key inside dict but it can be value in the dict 
it gives error if you try 
TypeError: unhashable type: 'list'

2)
Dict - not allowed (dict inside dicts as keys - not values)
TypeError: unhashable type: 'dict'

3) 
sets- Not allowed as key in dict 
gives error TypeError: unhashable type: 'set'
All three are mutable (can chnage), so they cant be keys.
"""

"""
Why does python rejects mutable keys? 

python uses a Key's Hash (a number "fingerprint") to find data instantly inside the dict.

If the key Could chnage after being added: 
-> The Hash would chnage too 
-> The dict would lose track of where the data is? 
-> you could never find you data again.

By only allowing immutbale keys, python gurantees: 
-> stable hash 
-> relaible lookups
-> No "lost" data

Python uses the word "HASABLE" for things that can be keys: 
-> immutable -> hashable -> usable as key 
-> mutable -> not hashable -> not allwoed

"""

"""
Why key must be unique in dict? 
Dicts use the key as unique "lable" to find the data. 
Two entries with same label would confuse the dict 
so python keeps the most recent one 
"""

"""
TUPLES AS KEYS - the special power 

Tuples are the only immutable container - so they're the only 
multi value type we can use as key 
example: 
servers = {
  ("us-east-1", "Zone-a"): "server A",
  ("us-east-2", "Zone-b"): "server B"
 }

The whole tuple (...) is one key, no two separte keys - one combined key with two parts. 

#sometimes we need to look up by more that one thing. 
Tuples let us bundle [multiple values into a single key]

example: 
cache = {
 ("auth", "india"): "healthy",
 ("auth", "usa" ): "degarde"
}
print(cache[("auth", "India")]) #healthy 
print(cache[("auth", "usa")]) #degarde
"""

"""
But Tuples must be conatin only imutable items 

a TUPLE IS HASHABLE ONLY IF EVERYTHING INSIDE IT IS ALSO HASHABLE 

A tuple of immutable items works 
"""
#example: 
good_key = ("usa", 3386, True)
d = {good_key: "value"}
print(d) #{('usa', 3386, True): 'value'}

"""
Tuple conatining a list - will fails
example 
bad_key = ("usa", [3386, True])
d ={bad_key: "value"}
TypeError: unhashable type: 'list

EVEN though the tuple itself is immutable, 
The list inside is not so the whole thing becomes unhashable. 
"""