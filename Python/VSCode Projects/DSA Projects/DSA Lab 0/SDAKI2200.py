numberOfFriends = 0
while True:
    try:
        numberOfFriends = int(input())
    except ValueError:
        print("Please enter a valid integer 1 - 100 000")
    if numberOfFriends >= 1 and numberOfFriends <=100000:
        break
    else:
        print("His friends must be at least between 1 to 100 000")
        

while True:
    candyPrices = input()
    candyPrices = [int(price) for price in candyPrices.split()]
    if len(candyPrices) == numberOfFriends:
        total = sum(candyPrices)
        print(total)
        break
    else:
        candyPrices = print("The amount of prices have to match the the amount of friends!")
