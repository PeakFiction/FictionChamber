problemtotal = int(input())
okay = 0

for i in range(problemtotal):
    problemDivision = str(input())
    splitter = problemDivision.split()
    problemDivisionFinal = []
    for x in splitter:
        intConv = int(x)
        problemDivisionFinal.append(intConv)
    if sum(problemDivisionFinal) >= 2:
        okay = okay + 1

print(okay)


#A problem can be solved when the there's at two people or more that