#checking Number Ranges with Boolean Expressions
#Boolean expressions can check if a value lies within a specific range, which is useful for validating inputs or categorizing data.
#example1: Here's how to use them to verify if a user meets age elgibility criteria: 

total_spent = 120.50 
is_loyalty_member = False 

qulifies_for_discount = (total_spent > 100) or is_loyalty_member
print(qulifies_for_discount) #output: True this checks if the total amount spent is greater than 100 or if the user is a loyalty member. Since the total spent is greater than 100, the result is true, indicating that the user qualifies for a discount.

#example2: 
age = 25
is_elgible = (age >= 18) and (age <= 65)
print(f"User is eligible: {is_elgible}") #output: User is eligible: True this checks if the age is between 18 and 65, inclusive. Since the age is 25, which falls within this range, the result is true, indicating that the user is eligible.

#example3: 
age = 70
has_membership = True
is_eligible_for_senior_discount = (age >= 65) and has_membership
print(f"User is eligible for senior discount: {is_eligible_for_senior_discount}") #output: User is eligible for senior discount: True this checks if the age is 65 or older and if the user has a membership. Since the age is 70 and the user has a membership, the result is true, indicating that the user is eligible for a senior discount.

#============================================================================================================
#Nested Boolean Expressions
#Boolean expressions can be nested within each other to create more complex conditions, allowing for sophisticated decision-making processes.
#example4:
age = 30
total_spent = 150.75
is_loyalty_member = True

qulifies_for_special_offer = (age >=18 and age <= 30) and (total_spent > 100 or is_loyalty_member)

print(f"User qualifies for special offer: {qulifies_for_special_offer}") #output: User qualifies for special offer: True this checks if the age is between 18 and 30, and if either the total spent is greater than 100 or the user is a loyalty member. Since all conditions are met, the result is true, indicating that the user qualifies for the special offer.    