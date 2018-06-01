number1=input("Enter your first number: ")
number2=input("Enter your second number: ")

if number1>number2:
    number1bigger = True
else:
    number1bigger=False

print("number1 bigger: ",number1bigger)

if number1bigger:
    print("number1 bigger")
else:
    print("number1 not bigger")
