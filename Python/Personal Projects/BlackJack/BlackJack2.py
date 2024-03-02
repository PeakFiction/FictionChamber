import random
#Variables ---
deck = []
discardPile = []
dealerHand = []
playerHand = []
roundStart = True
gameStart = True
suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

playername = input("What is your name? ")
print(f"Welcome to BlackJack, {playername} ")
playerMoney = int(input("What's your buy-in going to be? "))
import random

def shuffleDeck(suitsArg, ranksArg):
    global deck
    deck.clear()
    for suit in suitsArg:
        for rank in ranksArg:
            card = {'suit': suit, 'rank': rank}
            deck.append(card)
    random.shuffle(deck)

def drawRandomCard(deckArg):
    global deck
    drawnCard = random.choice(deckArg)
    deck.remove(drawnCard)
    return drawnCard

def valueDetermine(drawnCardArg, currentHandValueArg):
    value = drawnCardArg['rank']
    if value.isdigit():
        return int(value)
    elif value in ['Jack', 'Queen', 'King']:
        return 10
    elif value == 'Ace':
        if currentHandValueArg + 11 <= 21:
            return 11
        else:
            return 1

def endGame():
    global gameStart
    gameStart = False

while gameStart:
    playerTurn = True
    dealerTurn = True
    dealerHandValue = 0
    playerHandValue = 0
    
    ##############
    print("========================================")
    print("ゲームを始めましょう")
    print()
    playerBet = int(input("What Will Be Your Bet? "))
    while playerBet <= 0:
         playerBet = int(input("You can't have 0 or less as a bet. Try again: "))
    print(f"You put {playerBet} on the line")
    playerMoney -= playerBet
    
    print(f"You now have {playerMoney}")
    shuffleDeck(suits, ranks)
    print("The deck has been shuffled")
    print()
    
    ##############
    dealerCard1 = drawRandomCard(deck)
    dealerCard1Value = valueDetermine(dealerCard1, dealerHandValue)
    dealerHandValue += dealerCard1Value
    
    dealerCard2 = drawRandomCard(deck)
    dealerCard2Value = valueDetermine(dealerCard2, dealerHandValue)

    print(f"The Dealer has drawn {dealerCard1['rank']} of {dealerCard1['suit']} and one hidden card")
    
    playerCard1 = drawRandomCard(deck)
    playerCard1Value = valueDetermine(playerCard1, playerHandValue)
    playerHandValue += playerCard1Value
    
    playerCard2 = drawRandomCard(deck)
    playerCard2Value = valueDetermine(playerCard2, playerHandValue)
    playerHandValue += playerCard1Value
    
    print(f"You have drawn {playerCard1['rank']} of {playerCard1['suit']} and {playerCard2['rank']} of {playerCard2['suit']}")
    
    if playerHandValue > 21:
        print("You have drawn a bust")
        print("GAME OVER")
        continue    
    
    while playerTurn:
        playerChoice = input("Hit, Stand, or Double Down?")
        

    
    
    
    