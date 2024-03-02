def yes(checkWord):
    if len(checkWord) <= 10:
        print(checkWord)
    elif len(checkWord) > 10:
        checkWord = checkWord
        lengthOfWord = len(checkWord)
        firstLetter = checkWord[0]
        lastLetter = checkWord[-1]
        middleLetterQuant = len(checkWord[1:-1])
        print(f"{firstLetter}{middleLetterQuant}{lastLetter}")

okay = int(input())

for i in range(okay):
    yes(str(input())) 
