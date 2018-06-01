import sys

file = open("list of teams.txt","w")
MyTeams = ['76ers', 'Cleveland', 'Celtics', 'Spurs', 'Lakers']

for n in range(0, len(MyTeams)):
    team = MyTeams[n] + "\n"
    file.write(team)
    
file.close()
