
def Fibonacci(n):
    firstNumber = 0
    secondNumber = 1
    
    for i in range(2, n+1):
        nextNumber = firstNumber + secondNumber
        firstNumber = secondNumber
        secondNumber = nextNumber
    
    return secondNumber

result = Fibonacci(10)
print(result)
