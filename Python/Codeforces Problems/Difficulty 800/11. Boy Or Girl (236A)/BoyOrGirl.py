name = str(input())
reserve = []

nameList = list(name)

for i in nameList:
    if i not in reserve:
        reserve.append(i)
    else:
        pass

if len(reserve) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")