Word = input("Enter a Word: ")
if Word == Word[::-1]:
    print(Word, "is a palindrom")
else:
    print(Word,"is not a palindrom")
