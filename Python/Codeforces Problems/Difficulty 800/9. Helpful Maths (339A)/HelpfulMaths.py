former = input()

formersplitted = former.split("+")

formerInted = [int(element) for element in formersplitted]

sortedList = sorted(formerInted)
finalList = [str(element) for element in sortedList]

print(finalList[0], end="")

for i in range(1, len(finalList)):
    print("+" + finalList[i], end="")