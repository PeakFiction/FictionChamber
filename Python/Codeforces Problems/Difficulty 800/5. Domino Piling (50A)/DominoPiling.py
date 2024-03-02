boardsize = str(input())
boardsize2 = boardsize.split()

boardsizeX = int(boardsize2[0])
boardsizeY = int(boardsize2[1])

boardsizeTotal = boardsizeX * boardsizeY

possibleDomino = boardsizeTotal // 2

print(possibleDomino)