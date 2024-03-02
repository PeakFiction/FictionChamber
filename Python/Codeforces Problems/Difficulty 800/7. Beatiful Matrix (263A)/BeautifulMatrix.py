counter = 5
rowCounter = 1
element = "1"

while counter != 0:
    row = str(input())
    newRow = row.split()
    
    if element in newRow:
        YLocation = newRow.index(element) + 1
        XLocation = rowCounter
    
    counter -= 1
    rowCounter += 1

PlacesY = abs(3 - YLocation)
PlacesX = abs(3 - XLocation)

TotalMoves = PlacesY + PlacesX
print(TotalMoves)
