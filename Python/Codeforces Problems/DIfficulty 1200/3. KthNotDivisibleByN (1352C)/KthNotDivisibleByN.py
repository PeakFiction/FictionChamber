numberOfTestCase = int(input())
outputlist = []

for i in range(numberOfTestCase):
    notDivisibleList = []
    query = input()
    queryListed = query.split()
    queryInput = [int(element) for element in queryListed]
    n = queryInput[0]
    k = queryInput[1]
    
    Counter = 1
    
    while len(notDivisibleList) != k:
        if Counter % n != 0:
            notDivisibleList.append(Counter)
        else:
            pass
        Counter = Counter + 1
    lastnumber = notDivisibleList[-1]
    outputlist.append(lastnumber)


for i in outputlist:
    print(i)