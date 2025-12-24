"""
Four friends are sharing a hotel room that costs Rs2000 per night. The hotel applies a 12% GST (Goods and Services Tax) 
to the room charge. To make the payment fair, they want to calculate the total bill including GST and then split it equally
among all four people.
"""
# Room cost before tax
room_cost = 2000

# GST rate (12%)
gst_rate = 0.12

# Calculate GST amount
gst_amount = room_cost * gst_rate

# Total bill after including GST
total_bill = room_cost + gst_amount

# Number of people sharing the bill
number_of_persons = 4

# Calculate how much each person needs to pay
share_per_person = total_bill / number_of_persons

# Display the result
print(f"Total Room Cost (before GST): Rs{room_cost}") #Total Room Cost (before GST): Rs2000
print(f"GST @ 12%: Rs{gst_amount:.2f}")              #GST @ 12%: Rs240.00
print(f"Total Bill (including GST): Rs{total_bill:.2f}") #Total Bill (including GST): Rs2240.00
print(f"Number of Persons: {number_of_persons}") #Number of Persons: 4
print(f"Each person needs to pay: Rs{share_per_person:.2f}") #Each person needs to pay: Rs560.00


salutaion = "Dr. "
Frist_Name = "Basava"
Middle_Name = "Raj"
Last_Name = "Kuruba"
suffix = "ph.D." 
print(salutaion + " " + Frist_Name + " " + Middle_Name + " " + Last_Name + ", " + suffix) #Dr.  Basava Raj Kuruba, ph.D.
print(salutaion, Frist_Name, Middle_Name, Last_Name, ",", suffix) #Dr.  Basava Raj Kuruba , ph.D.

#print("5 * 3 = " + (5*3)) #string + int get TypeError: can only concatenate str (not "int") to str
print("5 * 3 = "+ str(5*3)) #explicist data type conversion #o/p: 5 * 3 = 15

#Resolve ZeroDivisionError caused by an attempt to divide by 0 error might
"""
1Real-World Example:
This kind of error often happens in situations like:
Looping through data from a database.
Some records might have null or zero values in the denominator.
But you still want to keep the numerator value (not lose it or crash the program).

solution: Use a Default Value
You can avoid the error by checking if the denominator is 0 (or None) and then replace 
it with 1 if needed. That way, the result will just be the numerator.

if not denominator: checks if the denominator is 0 or None.
Setting it to 1 avoids the division by zero.
The result becomes numerator / 1, which equals the numerator itself (8.0).
Use this if you want to preserve the numerator when denominator is missing or zero.
"""
numerator = 8 
denominator = 0 
result = numerator / denominator #ZeroDivisionError: division by zero
print(result)

numerator = 8
denominator = 0

# Fix: If denominator is 0 or None, use 1 instead
if not denominator: #'not' checks for 0, None, or empty
    denominator = 1 # avoid ZeroDivisionError, keep numerator safe

result = numerator / denominator
print(result)  # Output: 8.0
