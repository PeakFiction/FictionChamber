def main():
    try:
        n = int(input("Enter the number of friends: "))
        if n < 1 or n > 100000:
            raise ValueError("Invalid input for number of friends")
        
        prices = list(map(int, input("Enter the prices of each friend's favorite candy: ").strip().split()))
        if len(prices) != n:
            raise ValueError("The number of prices should be the same as the number of friends")
        
        for price in prices:
            if price < 1 or price > 1000000:
                raise ValueError("Invalid input for price of candy")
        
        total_cost = sum(prices)
        print("The total cost is: ", total_cost)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
