"""
1) what is join()? 
.join is the opposite of split().
it takes an iterable (list, tuple) of strings and combines them into one string, with a separtor between each. 

syntax: 
"separator".join(iterable) #iterable	Required. Any iterable object where all the returned values are strings
Note: Returns a new string. The original string is unchanged - strings are immutable.
The separtor comes first(the string you call .join() on). 
The list goes inside the parantheses. 
"""
#example1: Basic join with comma 
words = ["Hello", "world", "python"]
result = ",".join(words)
print(result) #output: Hello,world,python here it joins the list of strings into a single string with a comma as the separator

#example2: join with space
words = ["Hello", "world", "python"]
sentance = " ".join(words)
print(sentance)
#output: Hello world python here it joins the list of strings into a single string with a space as the separator

#example3: join with no seprator 
chars = ["H", "e", "l", "l", "o"]
result = "".join(chars)
print(result) #output: Hello here it joins the list of strings into a single string with no separator

#example4: join with newline (build multi-line text)
lines = ["Line 1", "Line 2", "Line 3"]
text = "\n".join(lines)
print(text)
#output:
#Line 1
#Line 2
#Line 3 here it joins the list of strings into a single string with a newline as the separator

#example4: Join() only works with strings, not numbers. If you have a list of numbers, you need to convert them to strings first:
"""
numbers = [1, 2, 3, 4, 5]
result = ",".join(numbers) 
#output: TypeError: sequence item 0: expected str instance, int found here it
"""
#convert numbers to strings first 
numbers = [1, 2, 3, 4, 5]
num_As_str = [str(n) for n in numbers]
result = ",".join(num_As_str)
print(result) #output: 1,2,3,4,5 here it joins the list of strings into a single string with a comma as the separator

#example5:
user_ids = ["1001", "1002", "1003"]
sql_in = "("+", ".join(user_ids) + ")"
print(sql_in) #(1001, 1002, 1003)

cmd_parts = ["docker", "run", "-d", "--name", "web", "nginx"]
command = " ".join(cmd_parts)
print(command)
#output: docker run -d --name web nginx

#example6: 
myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)
print(x) #nameTESTcountry
#Note: When using a dictionary as an iterable, the returned values are the keys, not the values

#example7: Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x) #John#Peter#Vicky