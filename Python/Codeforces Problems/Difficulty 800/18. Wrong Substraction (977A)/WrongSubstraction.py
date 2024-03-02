i = input()

isplit = i.split()

number = isplit[0]
minustimesStr = isplit[1]
minustimes = int(minustimesStr)

while minustimes != 0:
    if number[-1] == "0":
        number = number[:-1]
    else:
        number = int(number)
        number = number - 1
        number = str(number)
    minustimes = minustimes - 1

print(number)