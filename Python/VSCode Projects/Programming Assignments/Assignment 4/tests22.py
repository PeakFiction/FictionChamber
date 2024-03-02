entryData = "123456789101"


class CheckSum: #Function that calculates the checksum
    entryData = "123456789101"
    listedEntryData = list(entryData) #lists the entry
    positionCounter = 0 #counter positions
    evenSum = 0 # initial number for the even sum to be added later on
    oddSum = 0 #multiply oddSum by 3 later
    for x in listedEntryData: #for x in entrydata
        if positionCounter%2 == 0: #if the position is even
            evenSum += int(x) #add that to even sum
            positionCounter += 1 #add the position counter by 1 to move it forward
        else: #otherwise, if odd
            oddSum += int(x) #add said number to the oddsum
            positionCounter += 1 #add the position counter by 1 to move it forward
    checkSumValue = ((oddSum*3)+(evenSum))%10 #counts what will be the checksum in accordance to oddsum and even sum
    if checkSumValue != 0:
        checkSumValue = 10 - checkSumValue
    else:
        checkSumValue = checkSumValue
    listedEntryData.append(str(checkSumValue)) #adds the checksum number to the end of the entry data
    newEntryData = str(listedEntryData) #reconverts it into a string
    print(newEntryData)

CheckSum()
