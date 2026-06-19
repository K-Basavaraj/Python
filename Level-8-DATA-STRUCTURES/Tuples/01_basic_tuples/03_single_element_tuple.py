"""
-> The famous "Comma trick for single element tuples"
-> To create a tuple with one element, you must include a comma, without comman, python thinks your just using parantheses. 
#around a value - which doesnt make a tuple, just a value in parantheses

-> why? because parantheses are also used for grouping expressions, 
so python needs a way to distinguish between a single value in parantheses and a tuple with one element. 
The comma is what tells python that it is a tuple, even if it has only one element.
python uses () for math grouping too: 
(5+3) * 2 #just grouping, not a tuple, the result is 16 not (8,)
the comman is what creates the tuple, not the parantheses.

Note: always use parantheses + comma 
example: (5, )
not just 5, because 5 is just an integer, not a tuple.
"""
#example1: wrongway to create a single element tuple its not a tuple. 
not_a_tuple = ("hello") #this will create a string variable called not_a_tuple, which contains the value "hello". The parentheses around "hello" do not create a tuple, they are just used for grouping the expression. So not_a_tuple is just a string, not a tuple.
print(type(not_a_tuple)) #output: <class 'str'> this will print the type of the variable not_a_tuple, which is a string.
print(not_a_tuple) #output: hello this will print the value of not_a_tuple, which is "hello".

not_a_tuple2 = (5) #this will create an integer variable called not_a_tuple2, which contains the value 5. The parentheses around 5 do not create a tuple, they are just used for grouping the expression. So not_a_tuple2 is just an integer, not a tuple.
print(type(not_a_tuple2)) #output: <class 'int'> this will print the type of the variable not_a_tuple2, which is an integer.
print(not_a_tuple2) #output: 5 this will print the value of not_a_tuple2, which is 5.
#########################################################################################################################
#example2: correct way to create a single element tuple
single_element_tuple = ("hello",) #this will create a tuple variable called single_element_tuple, which contains one element "hello". The comma after "hello" is what makes it a tuple, even though there is only one element. So single_element_tuple is a tuple containing the string "hello".
print(type(single_element_tuple)) #output: <class 'tuple'> this will print the type of the variable single_element_tuple, which is a tuple.
print(single_element_tuple) #output: ('hello',) this will print the contents of the single_element_tuple, which is a tuple containing one element "hello". The comma is included in the output to indicate that it is a tuple, even though it has only one element.

single_element_tuple2 = (5,) #this will create a tuple variable called single_element_tuple2, which contains one element 5. The comma after 5 is what makes it a tuple, even though there is only one element. So single_element_tuple2 is a tuple containing the integer 5.
print(type(single_element_tuple2)) #output: <class 'tuple'> this will print the type of the variable single_element_tuple2, which is a tuple.
print(single_element_tuple2) #output: (5,) this will print the contents of the single_element_tuple2, which is a tuple containing one element 5. The comma is included in the output to indicate that it is a tuple, even though it has only one element.
#########################################################################################################################
