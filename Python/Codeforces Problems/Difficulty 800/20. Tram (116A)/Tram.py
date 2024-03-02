stations = int(input())
totalInside = 0
longTimeMax = 0
temp = 0

for i in range(stations):
    passenger = input()
    passengersSplit = passenger.split()
    passengersInt = [int(x) for x in passengersSplit]
    
    passengersOut = passengersInt[0]
    totalInside = totalInside - passengersOut
    
    passengersIn = passengersInt[1]
    totalInside = totalInside + passengersIn
    
    if totalInside < 0:
        totalInside == 0
    
    if totalInside > longTimeMax:
        longTimeMax = totalInside



print(longTimeMax)
