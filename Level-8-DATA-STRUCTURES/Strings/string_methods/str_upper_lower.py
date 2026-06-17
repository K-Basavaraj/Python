"""
1) what is upper and lower() 
.lower() returns a new string with all letters in lowercase. 
Non-letter charcters(numbers, symbols, spaces) are unchanged 

synatx: string.lower

2) .upper() returns a new string with all letters in upper case 
non-letter charcters (numbers, symbols, spaces are unchnageds. )
its the mirro image of .lower() 

synatx: string.upper() 
"""
#example1: convert to lower case 
Name = "Basavaraja"
#Lower Case
print(Name.lower()) #output: basavaraja

#Note: Already lower case will no chnage 

#example2: case-insensitive comparision 
user_input = "YES"
if user_input.lower() == "yes": 
    print("USER said yes")

#example3: filter case-insensitve
items = ["Apple", "BANANA", "cherry", "APPLE"]
apples = [ item for item in items if item.lower() == "apple"]
print(apples) #['Apple', 'APPLE']
#################################################################################################
#example1:  #Upper Case
Name = "Basavaraja"
print(Name.upper()) #output: BASAVARAJA

#example2: format constants and headers 
status = "active"
header = f"status: {status.upper()}"
print(header) #status: ACTIVE

#example2: convert env names 
env = "production"
print(f"Deploying: {env.upper()}") #Deploying: PRODUCTION