enter = input()
enter2 = input()
maxDifference = 0

entersplit = enter.split()
enterlist = [int(x) for x in entersplit]

enter2split = enter2.split()
enter2list = [int(x) for x in enter2split]
enter2list.sort()

numberOfLanterns = enterlist[0]
streetLength = enterlist[1]

firstLantern = enter2list[0]
secondLantern = enter2list[-1]

startToFirstLen = firstLantern
endToLastLen = abs(streetLength - secondLantern)

def DifferenceFinder(listName, maximum):
    for i in range(len(listName) - 1):
        difference = listName[i + 1] - listName[i]
        if difference > maximum:
            maximum = difference
    
    return maximum

if len(enter2list) == 0:
    print("0.0000000000")
else:
    DifferenceResult = DifferenceFinder(enter2list, maxDifference)
    maximumDifferenceFinal = DifferenceResult/2
    
    resulted = [maximumDifferenceFinal, startToFirstLen, endToLastLen]
    final = max(resulted)
    
    print("{:.10f}".format(final))


