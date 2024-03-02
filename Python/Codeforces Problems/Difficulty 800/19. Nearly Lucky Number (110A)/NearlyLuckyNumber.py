i = input()

digits = [digit for digit in i]

counter = 0

for i in digits:
    if i == "4" or i == "7":
        counter = counter + 1
    else:
        pass

if counter == 4 or counter == 7:
    print("YES")
else:
    print("NO")