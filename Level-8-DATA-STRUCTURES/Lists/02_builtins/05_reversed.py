"""
Reversed Function in Python

Purpose:
Helps reverse the order of elements in a sequence.

Real-world example:
Useful for displaying recent transactions first,
reversing a playlist, showing the latest messages first,
or processing data from last to first.

Practical application:
Allows viewing items in reverse order without modifying
the original list.

The reversed() function returns a reverse iterator,
so it is commonly converted into a list using list().

Syntax:
reversed(sequence):
reversed() is a built-in function.
Works with lists, tuples, strings, and other sequences.
Returns a reverse iterator.
Usually used with list().
Does not modify the original sequence.

Difference from reverse():
reversed() is a built-in function that returns a reversed view
of the sequence and keeps the original list unchanged.

reverse() is a list method that directly modifies the original list.

The reversed() function returns a reverse iterator,
so it is commonly converted into a list using list().
"""
# Example 1: Reverse a List
fruits = ["apple", "banana", "cherry"]

reversed_fruits = list(reversed(fruits))

print(reversed_fruits)
# output: ['cherry', 'banana', 'apple']
# reversed() returns the items in reverse order.

print(fruits)
# output: ['apple', 'banana', 'cherry']
# The original list remains unchanged.

#Example 2: Reverse Numbers
numbers = [10, 20, 30, 40, 50]

reversed_numbers = list(reversed(numbers))

print(reversed_numbers)
# output: [50, 40, 30, 20, 10]
# reversed() returns the elements from last to first.

#Example 3: Reverse a String
name = "python"

reversed_name = ''.join(reversed(name))

print(reversed_name)
# output: nohtyp
# reversed() can also work with strings.
