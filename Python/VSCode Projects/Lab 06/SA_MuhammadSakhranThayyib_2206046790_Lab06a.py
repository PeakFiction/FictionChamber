def main():
    words = input("Please give a sequence of words: ") 
    listOfWords = words.split() 
    showDigits(listOfWords)

# Recursive function for translating a list of numeric words 
# into a sequence of digits and print them
def showDigits(listOfWords):
    if len(listOfWords) == 1: # base case
        print(printDigit(listOfWords[0]))
    else: # recursive case
        print(printDigit((listOfWords[0])), end = "") 
        showDigits(listOfWords[1:])


# Function for translating one word and printing the digit 
def printDigit(word):
    番号翻訳 = {
"one": "1",
"two": "2",
"three": "3",
"four": "4",
"five": "5",
"six": "6",
"seven": "7",
"eight": "8",
"nine": "9",
"zero": "0"
    }
    return 番号翻訳.get(word)

if __name__ == '__main__':
    main()