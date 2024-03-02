wow = input()
uppercaseCounter = 0
lowercaseCounter = 0

for i in range(len(wow)):
    if wow[i].isupper():
        uppercaseCounter += 1
    else:
        lowercaseCounter += 1


if uppercaseCounter > lowercaseCounter:
    newtext = wow.upper()
elif lowercaseCounter > uppercaseCounter or lowercaseCounter == uppercaseCounter:
    newtext = wow.lower()

print(newtext)