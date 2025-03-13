emptyInput = input()
resultInput = input()
AntonCount = 0
DanikCount = 0

result = list(resultInput)

for i in result:
    if i == "D":
        DanikCount += 1
    elif i == "A":
        AntonCount += 1

if DanikCount > AntonCount:
    print("Danik")
elif AntonCount > DanikCount:
    print("Anton")
elif AntonCount == DanikCount:
    print("Friendship")


