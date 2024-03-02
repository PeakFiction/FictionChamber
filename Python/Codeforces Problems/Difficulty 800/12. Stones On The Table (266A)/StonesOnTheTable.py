totalStones = int(input())
stonesOrder = str(input())

listStones = list(stonesOrder)
adder = 0
index = 0

for i in listStones:
    if index == (len(listStones) - 1):
        break
    elif listStones[index] == listStones[index+1]:
        adder += 1
    index += 1

print(adder)