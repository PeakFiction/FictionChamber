i = input()

digits = [digit for digit in i]

check = True

for digit in digits:
    if digit == "4":
        pass
    elif digit == "7":
        pass
    else:
        check = False
        break

if check == True:
    print("YES")
elif check == False:
    print("NO")