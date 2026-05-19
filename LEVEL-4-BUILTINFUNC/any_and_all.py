#any() true if at least one item is truthy 

statuses = ["ok", "ok", "ok", "error", "ok"]

has_error = any(s == "error" for s in statuses)
print(has_error) #output: True here we have used the any() function to check if there is at least one item in the statuses list that is equal to "error". The any() function takes an iterable (in this case, a generator expression) as an argument and returns True if at least one item in the iterable is truthy. In this case, since there is one item in the statuses list that is equal to "error", the any() function returns True, so the output is True.

#all() true if all items are truthy
all_good = all(s == "ok" for s in statuses)
print(all_good) #output: False here we have used the all() function to check if all items in the statuses list are equal to "ok". The all() function takes an iterable (in this case, a generator expression) as an argument and returns True if all items in the iterable are truthy. In this case, since there is one item in the statuses list that is equal to "error", the all() function returns False, so the output is False.

#Health gate 
checks = [True, True, False, True]

if all(checks):
    print("All checks passed, system is healthy.")
else:
    print("Some checks failed, system is not healthy.")
#output: Some checks failed, system is not healthy. here we have used the all() function to check if all items in the checks list are True. The all() function takes an iterable (in this case, a list) as an argument and returns True if all items in the iterable are truthy. In this case, since there is one item in the checks list that is False, the all() function returns False, so the else block is executed and the output is "Some checks failed, system is not healthy."
