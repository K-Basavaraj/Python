"""
Bitwise Operators in Programming
Bitwise operators are essential tools for manipulating data at the binary level across different programming environments. 

Here's a concise overview:
Purpose: Used predominantly in low-level programming tasks. They are vital for manipulating bits to control the behavior of 
various software features and are crucial in resource-constrained environments like embedded systems.

Common Uses:
Managing feature flags: Toggle functionalities in applications by setting bit values.
Optimizing performance: For tasks requiring efficient data storage and manipulation.

Key Operations:
OR (|): Activates bits by evaluating where any operand is 1. Example: Turning on specific feature bits.
AND (&), XOR (^): Other operators for different bit-level manipulations.

Bitwise operators offer significant advantages for directly manipulating memory, optimizing software performance, and 
improving efficiency in programming environments where resource management is critical. Mastering them can enhance overall 
programming proficiency.
"""
#Binary opertor
features = 0b0000 #all features are off 

#turn on features 1 and 3 
features = features | 0b0101
print(features) #5
print(bin(features)) #0b101

#Not (~): Inverts all bits. Converts positive to negative by flipping each bit (e.g., 0101 becomes 1010, yielding -6).
a = 5 #0101
print(~a) #-6 inverst binary from 0101 to 1010 

#And (&): Results in 1 only if both bits are 1. For 0101 and 0011, the outcome is 0001.
p = 5 #0101
q = 3  #0011
print(p & q) #1 

#Or (|): Produces 1 if at least one bit is 1. Given 0101 or 0011, results in 0111.
p = 5 #0101
q = 3  #0011
print(p | q) #7

#Xor (^): Returns 1 if bits differ. 0101 and 0011 become 0110.
p = 5 #0101
q = 3  #0011
print(p ^ q) #6

#Left Shift (<<): Moves bits left, filling with zeros. Shifting 0101 one place results in 1010 (decimal 10).
p = 5 #0101
print(p << 1) #10 

#Right Shift (>>): Shifts bits right, reducing size. Moving 0101 right delivers 0010 (decimal 2).
p = 5 #0101
print(p >> 1) #2

#note: in left shift you gain the bits but (in right shift you will loose the bits)