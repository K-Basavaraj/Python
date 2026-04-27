#part1: string concatination and repetition
greeting = "Hello" 
name = "python Student"
print(greeting + ", " + name) #Hello, python Student

#part2: basic num opertaions 
a = 10 
b = 3
print(a + b) #13
print(a - b) #7
print(a * b) #30
print(a / b) #3.3333333333333335    
print(a % b) #1
print(a ** b) #1000

# part3: using floor division for whole number results
c = 14 
d = 6 
print(d // c) #0
print(d / c) #0.42857142857142855

#part4: string and arthmatic mixed Operations 
lines_of_code_to_write = 30
print("I have " + str(lines_of_code_to_write) + " lines of code to write today!")

#party5: using conditional statements with modulus 
team_a = []
team_b = []
participants = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for participant in participants:
    if participant % 2 == 0:
        team_a.append(participant)
    else:
        team_b.append(participant)

print("Team A (Even-numbered participants):", team_a) #Team A (Even-numbered participants): [2, 4, 6, 8, 10]
print("Team B (Odd-numbered participants):", team_b) #Team B (Odd-numbered participants): [1, 3, 5, 7, 9]
