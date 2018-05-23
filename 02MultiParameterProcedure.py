#MultipleParameterProcedure

def addition(num1, num2):
    print("%d + %d = %d" % (num1, num2, num1+num2))

def multiplication(num1, num2):
    print("%d * %d = %d" % (num1, num2, num1*num2))
    
for i in range(3):
    for j in range(4):
        addition(i,j)
        multiplication(i,j)
