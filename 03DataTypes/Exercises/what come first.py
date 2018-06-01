#What comes first?

str1=input("Type first word: ")
str2=input("Type second word: ")

str1.UpperBound
if str1[0] < str2[0]:
    print("Alphabetically, '%s' is before '%s'" % (str1, str2))
else:
    print("Alphabetically, '%s' is before '%s'" % (str2, str1))
    
