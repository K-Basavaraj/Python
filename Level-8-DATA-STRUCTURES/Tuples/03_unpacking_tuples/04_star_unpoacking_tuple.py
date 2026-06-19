"""
1) what is the star unpacking? 
-> Noraml unpacking requires the EXACT number of varibales to match the tuple leangth. 
But 
-> what if we dont know items the tuple has? or want some specific ones plus "everything else"? 

STAR unpacking (USING *)
LETS ONE VARIBLE COLLECT MULTIPLE VALUES 

synatx: 
 first, *rest = (1,2,3,4)
 *initial, last = (1,2,3,4)
 first, *middle, last = (1,2,3,4,5)

NOTE: THE STARRED VARAIBLE ALAYS BECOME A LIST

-> qUICK rEF: 
a, *b = (1,2,3) -> a=1, b =[2,3]
*a, b = (1,2,3) -> a=[1,2], b =3
a, *b, c =(1,2,3,4) -> a=1, b=[2,3], c=4
a,*_, c =(1,2,3,4) -> a=1, c=4 (middle ignored)
"""
#example1: normal unpacking is strict 
data = (1,2,3,4)
# a, b = data 
#ValueError: too many values to unpack (expected 2)

#example2: *rest at the end - "first + everything else"
data = ("Raj", "Basava", 3, 20.5)
first, *rest = data 
print(first)  #Raj
print(rest) #['Basava', 3, 20.5] a list not a tuple 

#example3: *initial at the start - everything except last 
data = (1,2,3,4,5)
*initial, last = data
print(initial) #[1, 2, 3, 4]
print(last) #5

#example4: *middle - first +last + everything in between 
first, *middle, last = data

print(first)#1
print(middle) #[2, 3, 4]
print(last) #5

#example5: star captures empty if theres nothing left 
data = (1,2)
a,b, *rest = data 
print(a,b) #1 2
print(rest) # [] empty list no error

##################################################################################
#example: HEADER ROW + DATA ROWS 
#common when parsing csv-like data - header is first, rest is data 

csv_data = ("name, age, role", "Alice,30,Engimeer", "Bob,25,Designer", "Charle,35,Manager")
header, *records = csv_data
print(f"Header: {header}") #Header: name, age, role
print(f"records:")

for record in records: 
    print(f" - {record}")
"""
records:
 - Alice,30,Engimeer
 - Bob,25,Designer
 - Charle,35,Manager
"""
#######################################################################################
#example2: 
logs = ("08:00 start", "09:00 ok", "10:00 warn", "11:00 error", "12:00 fixed")

*history, latest = logs 
print(f"Latest: {latest}") #Latest: 12:00 fixed
print(f"History: {history}") #History: ['08:00 start', '09:00 ok', '10:00 warn', '11:00 error']
#####################################################################################
#EXAMPLE COMBINE WITH _ TO INGONE CPATUERD VALUES 
#if we dont care about "the rest", use *_ as a convention 

data = (1,2,3,4,5)
first, *_, last = data 
print(first) #1
print(last)  #5
#*_ CAPTURE THE MIDDLE STUFF BUT I DONT CARE ABOUT IT.
#######################################################
