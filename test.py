newWord = []
for i in input():
    if i.islower():
        word = i.upper()
        newWord.append(word)
    else:
        word = i.lower()
        newWord.append(word)
print(''.join(newWord))
