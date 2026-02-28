#List of Participant numbers
participants = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]

team_A = []
team_B = []

for participant in participants:
    if participant % 2 == 0:
        team_A.append(participant)
    else:
        team_B.append(participant)

print("Team A:", team_A) #Team A: [2, 4, 6, 8, 8, 10]
print("Team B:", team_B) #Team B: [1, 3, 5, 7, 9]