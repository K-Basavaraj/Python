#DRIFT DETECTION 

expected = {"nginx", "docker", "git", "curl"}
installed = {"nginx", "git", "curl", "vim"}

missing = expected - installed   #what should be there but is not 
extra = installed - expected     #whats there that should not be 
common = expected & installed    #whats correctly insatlled 

print(f"Missing: {missing}")  
print(f"unexpected: {extra}")
print(f"OK: {common}")

"""
o/p: 
Missing: {'docker'}
unexpected: {'vim'}
OK: {'git', 'nginx', 'curl'}

THIS PATTERN WORKS FOR 
-EXPECTED VS ACTUAL SERVERS/PACKAGES/RULES ETC; 
"""

#example2: DUPLICATES 2 LISTS INTO ONE 

team_a = ["alice", "bob", "charle"]
team_b = ["bob", "dave", "eve"]

all_members = set(team_a) | set(team_b)
print(all_members)
#o/p: {'charle', 'bob', 'eve', 'dave', 'alice'}

#usecase3: FIND SHARED/EXCLUSIVE USERS
admins = {"aice", "bob"}

editors = {"bob", "charle"}

both_roles = admins & editors   #in both roles 
only_admin  = admins - editors   #admin-only 
exclusive  = admins ^ editors   #only one role, not both 

print(f"Both roles: {both_roles}")
print(f"Only admin: {only_admin}")
print(f"Exclusive:  {exclusive}")

"""
o/p: 
Both roles: {'bob'}
Only admin: {'aice'}
Exclusive:  {'aice', 'charle'}
"""