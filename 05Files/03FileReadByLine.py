import sys

file = open("list of teams.txt","r")
sizeoffile = str(sys.getsizeof(file))
print(sizeoffile)
print("First line:")
print(file.readline())
    
print("First line again")
print(file.readline())
