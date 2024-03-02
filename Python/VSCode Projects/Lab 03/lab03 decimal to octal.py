print('Lab 03 -- 2022\n')
print('From decimal to octal')
print('----------------------')

# read the user's input
decimalInput = int(input('Give a positive integer in decimal representation: '))

# convert the integer given by the user stored in decimalInput to a octal representation
octString = ''
quotient = decimalInput

while quotient > 0:
    octString = octString + str(quotient % 8)
    quotient = quotient // 8

octalResult = octString[: : -1]

# accumulator for binary digits, start with empty
print(f'The octal representation of {decimalInput} is 0c{octalResult}')