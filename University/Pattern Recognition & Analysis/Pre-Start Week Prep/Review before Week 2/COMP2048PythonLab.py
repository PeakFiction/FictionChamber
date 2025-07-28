nInput = input()
nInputInteger = int(nInput)

def Fibonacci(n):
    firstNumber = 0
    secondNumber = 1
    resultList = [0, 1, ]
    
    for i in range(2, n+1):
        nextNumber = firstNumber + secondNumber
        resultList.append(nextNumber)
        firstNumber = secondNumber
        secondNumber = nextNumber
    
    return resultList

print(Fibonacci(nInputInteger))



