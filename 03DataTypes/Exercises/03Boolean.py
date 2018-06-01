word1=input("Enter name of first animal: ")
word2=input("Enter name of second animal: ")

if word1[0] < word2[0]:
    Word1First = True
else:
    word1First = False

print("Boolean 'animal1High': ",word1First)
if word1First:
    print("%s is before %s!" % (word1, wprd2))
else:
    print("%s is before %s!" % (word2, word1))
