testCaseNumber = int(input())

for i in range(testCaseNumber):
    inputString = input()
    splitInputString = inputString.split()
    intedInputString = [int(x) for x in splitInputString]
    nNumber = intedInputString[0]
    kNumber = intedInputString[1]
    # k + (k // n)
    
    result = kNumber + (kNumber // nNumber)
    print(result)