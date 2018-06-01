file = open("list of teams.txt","r")

print("First four items: ")
for n in range (4):
    print(file.readline())
    
print("Contents of rest of file:\n")
print(file.readline())

