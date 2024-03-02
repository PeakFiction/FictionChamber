# Author: Clayton Ismail Nagle
# NPM: 2206021951
import string
import os.path
from htmlFunctions import *
print(os.path.isfile('banKimoonSpeech.txt'))

# loops for valid input
fileName = (input("File Name: "))
while os.path.isfile(fileName) == False:
    fileName = input('File not found, please try again: ')

# imports files
with open(fileName, 'r') as file:
    speech = file.read().replace('\n', ' ').split()

with open('stopwords.txt', 'r') as file:
    stopwords = file.read().replace('\n', ' ').split()

# removes punctuation from a word
def formatWord(elem):
    for x in string.punctuation:
        elem = elem.replace(x, '').lower()
    return elem
    
# removes punctuation from every word
for word in speech:
    speech[speech.index(word)] = formatWord(word)

# add words to dictionary
pairDict = {}
for word in speech:
    if word in stopwords:
        continue
    else:
        if word not in pairDict.keys() and len(word) > 1:
            pairDict[word] = speech.count(word)

# sorts dictionary as a new list, lambda sorts numerically than alphabetically
pairList = sorted(pairDict.items(), key = lambda x: [x[1], x[0]], reverse=True)
del pairList[60:] # deletes tuples after 60
print()

# table title
print(f'{fileName} :')
print("60 words in frequency order as (count:word) pairs\n")

# table
column_counter = 0
for pair in pairList:
    print(f"{str(pair[1]):>2s}:{pair[0]:20s}", end = "") # joins items in sublist to string
    column_counter += 1
    if column_counter == 3:
        print()
        column_counter = 0

# word cloud
high_count = pairList[0][1] # sets the highest count of a word
low_count = pairList[59][1] # sets the lowest count of a word
body=''

pairList.sort() # resorts list in alphabetical order using anon function
for word,cnt in pairList:
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)

box = make_HTML_box(body)  # creates HTML in a box
print_HTML_file(box,f'A Word Cloud of {fileName}')  # writes HTML to file name 'testFile.html'