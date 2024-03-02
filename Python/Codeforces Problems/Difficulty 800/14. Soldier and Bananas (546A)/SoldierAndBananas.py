i = input()

isplit = i.split()

isplitwow = [int(element) for element in isplit]

initialbananaprice = isplitwow[0]
cashinwallet = isplitwow[1]
totalbananaers = isplitwow[2]
countup = 0
temporary = 0
total = 0


for i in range(totalbananaers):
    if totalbananaers == countup:
        break
    else:
        temporary = initialbananaprice * countup
        total = temporary + total
        countup += 1

moneyNeed = cashinwallet - total
if moneyNeed < 0:
    moneyNeed = 0

print(moneyNeed)