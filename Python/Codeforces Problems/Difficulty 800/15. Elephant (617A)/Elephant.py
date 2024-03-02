distance = int(input())
if distance%5 == 0:
    steps = distance//5
else:
    steps = (distance//5) + 1

print(steps)