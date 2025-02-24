totalQuery = int(input())
xNumo = 0
yNumo = 0
zNumo = 0

#Create a for loop for how many times a Query is made
for i in range(totalQuery):
    #Takes input depending on how many times there are
    ren = input()
    splitRen = ren.split()
    otherRen = [int(splitRen) for splitRen in splitRen]
    xCoordinate = otherRen[0]
    yCoordinate = otherRen[1]
    zCoordinate = otherRen[2]
    
    xNumo = xNumo + (xCoordinate)
    yNumo = yNumo + (yCoordinate)
    zNumo = zNumo + (zCoordinate)

if xNumo == 0 and yNumo == 0 and zNumo == 0:
    print("YES")
else:
    print("NO")
