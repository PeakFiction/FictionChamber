#Dog Years Calculator
#The first two years of a dog's life count as 21 human years.

i = int(input("What's the age of the dog? "))
extraLife = i - 2

if i == 1:
    print("The dog is 10.5 years old in human years.")
elif i == 2:
    print("The dog is 21 years old in human years.")
else:
    extraYears = extraLife * 4
    print(f"The dog is {21 + extraYears} years old in human years")




