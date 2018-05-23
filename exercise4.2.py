##Exercise 4.2

def getTimesTables():
    n = int(input("Enter first number: "))
    o = int(input("Enter second number: "))

    for i in range(1, n+1):
        for j in range(1, o+1):
            print(i,"*",j,"=",i*j)
    return

print("Four times table: ")
for i in range(1,):
    for j in range(1,5):
        print(i,"*",j,"=",i*j)

print("\nFives times table:")
for i in range(1,6):
    for j in range(1,6):
        print(i,"*",j,"=",i*j)

getTimesTables()





