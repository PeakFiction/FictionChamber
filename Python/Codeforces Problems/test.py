inputString = input()
splitInputString = inputString.split()

print(splitInputString)
newIntString = [int(x) for x in splitInputString ]
print(newIntString)
print(newIntString[0])
print(newIntString[1])