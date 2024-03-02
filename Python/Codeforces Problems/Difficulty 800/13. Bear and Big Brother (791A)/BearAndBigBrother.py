year = 0
Weight = input()
weightsplit = Weight.split()

WeightList = [int(element) for element in weightsplit]

LimakWeight = WeightList[0]
BobWeight = WeightList[1]

while LimakWeight <= BobWeight:
    year += 1
    LimakWeight = LimakWeight * 3
    BobWeight = BobWeight * 2

print(year)