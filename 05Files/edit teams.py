file = open('list of teams.txt','r')
outfile = ""

MyArray = []

for line in range(10):
    if line % 2 == 0:
        outfile += file.readline()
        MyArray.append(outfile)
    else:
        file.readline()

file = open('edited list of teams.txt','w')
file.write(outfile)
file.close()

print(MyArray)
