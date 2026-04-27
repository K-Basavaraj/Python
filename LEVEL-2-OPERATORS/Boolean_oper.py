#Not: inverts a Boolean value, if the orginal vcalue is true, not makes it to false, and vice versa. 

#And: Returns true only if all conditions are true, useful for ensuring multiple conditrions meet specific criteria simultaneously. 

#Or: returns true when at least one condition is true, benficial when anyone condition triggers an outcome. 

#example1: Not inverts the value of a boolean expression
a = True
print(not a) #output: False this uses the not operator to invert the value of a, which is true, resulting in false.

b = False
print(not b) #output: True this uses the not operator to invert the value of b, which is false, resulting in true.

#example2: And returns true only if both conditions are true
x = True
y = False
print(x and y) #output: False this uses the and operator to evaluate the conditions x and y. Since y is false, the result is false.

m = True
n = True
print(m and n) #output: True this uses the and operator to evaluate the conditions m and n. Since both are true, the result is true.

#example3: Or returns true if at least one condition is true
p = False
q = False
print(p or q) #output: False this uses the or operator to evaluate the conditions p and q. Since both are false, the result is false.

r = True
s = False
print(r or s) #output: True this uses the or operator to evaluate the conditions r and s. Since r is true, the result is true, even though s is false.  


#example4: combining operators
c = True
d = False
e = not c or d and c 
print(e) #output: False this combines the not, or, and and operators. The expression evaluates to false because d is false, which makes the entire expression false regardless of the value of c.


#example5: another example of combining operators
age = 25
is_student = False
is_eligible_for_discount = (age < 30 and is_student) or (age >= 65)
print(is_eligible_for_discount) #output: False this uses a combination of and and or operators to determine if a person is eligible for a discount based on their age and student status. Since the person is not a student and does not meet the age criteria for a senior discount, the result is false.