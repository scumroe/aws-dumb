#4.6 Investment

V = int(input("Enter the initial value: "))
dA = float(input("What is your desired amount: "))
r = float(input("Enter the rate of interest: "))
Y = 0

if V<dA:
    while V <= dA:
        print("year",Y,"value",V)
        Y += 1
        V *= 1+(r**-1)
elif V>dA:
    while V >= dA:
        print("year",Y,"value",V)
        Y += 1
        V **= -r

if V == dA:
    print("You need %s years to get £%s." % (Y, dA))

