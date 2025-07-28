testCaseInputs = int(input())

def mainAlgo(n, k):
    counter = 0
    notDivisibleList = []
    for i in range(n*k):
        if counter % n != 0:
            notDivisibleList.append(counter)
        counter += 1
    
    return notDivisibleList

for i in range(testCaseInputs):
    mainInput = input()
    mainInputSplit = mainInput.split()
    mainInputQuery = [int(element) for element in mainInputSplit]
    
    n = mainInputQuery[0]
    k = mainInputQuery[1]
    
    print(mainAlgo(n, k)[k-1])




