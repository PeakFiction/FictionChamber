def FibonacciUpToRecursion(n, resultList, firstNumber, secondNumber):
    if secondNumber > n:
        return resultList
    resultList.append(secondNumber)
    
    return FibonacciUpToRecursion(n, resultList, secondNumber, secondNumber + firstNumber)

firstNumber = 0
secondNumber = 1
resultList = [0,]
nInput = int(input("Input Number (Fibonacci): "))

print(f"Fibonacci Recursion: {FibonacciUpToRecursion(nInput, resultList, firstNumber, secondNumber)})")


i = 0
factorial = 1
resultList1 = []
nInput2 = int(input("Input Number (Factorial): "))

def FactorialUpToNRecursion(n, i, factorial, resultList):
    if factorial > n:
        return resultList
    else:
        resultList.append(factorial)
        i += 1
        return FactorialUpToNRecursion(n, i, factorial*i, resultList)

print(f"Factorial Recursion: {FactorialUpToNRecursion(nInput2, i, factorial, resultList1)}")