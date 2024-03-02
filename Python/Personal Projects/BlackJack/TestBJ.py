gameStart = True
playerHand = 1000

while gameStart:
    playerHand += 1
    print(playerHand)
    playerInput = input("Finish? Y/N/P ")
    if playerInput  == "Y":
        break
    elif playerInput == "N":
        continue
    elif playerInput == "P":
        pass
    print("FINISH")

print(playerHand)