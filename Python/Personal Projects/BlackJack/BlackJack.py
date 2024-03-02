import random

suits = ['Diamond', 'Heart', 'Spade', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = []
discardPile = []
dealerHand = []
playerHand = []
roundStart = True

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

currentHandValue = 1
shuffleDeck(suits, ranks)
drawnCard = drawRandomCard(deck)
print(drawnCard['rank'])
print(f"Current Value Before:{currentHandValue}")

determinedResult = valueDetermine(drawnCard, currentHandValue)

if drawnCard['rank'] == 'Ace':
    if  determinedResult <= 11:
        print(f"Hand's Value at {currentHandValue+determinedResult} OR {currentHandValue+1}")
    else:
        print(f"Hand's Value at {currentHandValue+1}")
else:
    print(currentHandValue+determinedResult)