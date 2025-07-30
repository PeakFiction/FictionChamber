def FactorialUpToN(n):
    i = 0
    factorial = 1
    resultList = []
    
    while factorial <= n:
        resultList.append(factorial)
        i += 1
        factorial = factorial * i
        
    return resultList


print(FactorialUpToN(10010))

