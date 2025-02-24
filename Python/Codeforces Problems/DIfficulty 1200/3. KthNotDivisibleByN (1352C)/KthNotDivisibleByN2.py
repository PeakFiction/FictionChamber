totalQuery = int(input())

output = []

for i in range(totalQuery):
    
    initialInput = input()
    splitInput = initialInput.split()
    intedInput = [int(element) for element in splitInput]
    n = intedInput[0]
    k = intedInput[1]
    
    if k < n:
        output.append(k)
    else:
        quotient = k // n
        remainder = k % n 
        finalK = k + quotient + remainder
        output.append(finalK)
        
print("________________")
for _ in output:
    print(_)