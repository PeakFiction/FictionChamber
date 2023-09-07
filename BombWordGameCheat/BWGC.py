file = open("words.txt")
data = file.readlines()

newlist = []
for item in data:
    newlist.append(item.replace("\n", ""))

code = input("Type in the letter: ")
newlist2 = []

for i in newlist:
    if code in i:
        newlist2.append(i)

maxWord = ""
for i in newlist2:
    if len(i) > len(maxWord):
        maxWord = i

print(maxWord)
