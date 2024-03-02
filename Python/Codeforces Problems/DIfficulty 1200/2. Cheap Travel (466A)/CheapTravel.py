import math
i = input()

isplit = i.split()
n = int(isplit[0])
# n = Number of rides Ann has planned

m = int(isplit[1])
# m = Number of rides that the special ticket covers

a = int(isplit[2])
# a = Price of one ticket for a normal ride

b = int(isplit[3])
# b = Price of one ticket for a special ride

### Price When Doing Only Normal Rides
NormalOnly = n * a

## Price When Doing Only Special Rides, If the rides is even
Special = (n // m) * b 
RemainderQuant = (n % m)

if RemainderQuant < m or RemainderQuant == m:
    Remainder = b * 1
else:
    Remainder = math.ceil(n/m) * b
SpecialOnly = Special + Remainder

########## Price When Mixing Special and Normal
RemainderFromSpecial = n % m
PriceOfRemainder = RemainderFromSpecial * a

SpecialOnlyNeedQuantity = math.floor(n / m)
SpecialOnlyNeedQuantityPrice = SpecialOnlyNeedQuantity * b

TotalMixed = SpecialOnlyNeedQuantityPrice + PriceOfRemainder

Listings = [NormalOnly, SpecialOnly, TotalMixed]
minimumValue = min(Listings)

print(minimumValue)