
# A long word is if it has more than 10 characters
# If a word is too long, it should be changed into a special abbreviation
# Abbreviation: 
# 1. Write down the first and last letter of the word
# 2. Write down the decimal that is the number of letters between the first and last letter of the word
# e.g. If the input is "good", the output will be "good"
# e.g. If the input is "supercalifragilisticexpialidocious", the output will be "s32s"

#Have the user input the word 
inputWord = str(input("Please input the word: "))
checkWord = inputWord.lower()

#Checks if the user's word is considered long
if len(checkWord) < 10:
    print(checkWord)
elif len(checkWord) > 10:
    checkWord = checkWord
    lengthOfWord = len(checkWord)
    firstLetter = checkWord[0]
    lastLetter = checkWord[-1]
    middleLetterQuant = len(checkWord[1:-1])
    print(f"{firstLetter}{middleLetterQuant}{lastLetter}")

