#4.5 Vowels

word = str(input("Enter your word."))
vowels = ['a','e','i','o','u','A','E','I','O','U']
i = int(0)

for i in range(len(word)):
    for char in word:
        if char == vowels[i]:
            vowelsFound=i

print("There are %s vowels in %s" % (vowelsFound, word))


