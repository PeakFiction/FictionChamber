import math

i = input()
isplit = i.split()
integermade = [int(x) for x in isplit]
n = integermade[0]
m = integermade[1]

a = integermade[2]

nSize = n/a
mSize = m/a

nSizeUp = math.ceil(nSize)
mSizeUp = math.ceil(mSize)

finalNeed = nSizeUp * mSizeUp

print(finalNeed)