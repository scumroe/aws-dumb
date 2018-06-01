#float function stores input as floating point integer
#OPERATORS
# '+' is Addition
# '-' is Subtraction
# '*' is multiplication
# '/' is division
# '%' is modulus (remainder of)
# '**' is exponent (i.e a**b where a is 2 and b = 3 will output 8)

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
result = number1**number2
print("%s ** %s = %s" % (number1, number2, result))
