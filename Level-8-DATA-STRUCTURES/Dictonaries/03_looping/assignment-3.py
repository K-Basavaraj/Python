#pattern4: get index while looping (with enumarator)

config = {
    "hosts": "local-host", 
    "port": 5432,
    "user": "admin"
}

#enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
for i, (key, value) in enumerate(config.items(), start=1):
    print(f"{i}, {key} =  {value}")

"""
1, hosts =  local-host
2, port =  5432
3, user =  admin
"""