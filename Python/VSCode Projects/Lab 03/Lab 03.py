print('Lab 03 -- 2022\n')
print('From decimal to octal')
print('----------------------')

# read the user's input
decimalInput = int(input('Give a positive integer in decimal representation: '))

# convert the integer given by the user stored in decimalInput to a octal representation

#have python tell the octString as a string, and quotient as decimalInput to make it easier
octString = ''
quotient = decimalInput

#have python divide quotient by 8 with % while keeping it in its string form and combine it while 
while quotient > 0:
    octString = octString + str(quotient % 8)
    #have python keep on dividing the quotient and keeping only except the remainder of the division
    quotient = quotient // 8

#reverses the octString so that it becomes a proper octal form after adding "0o" at the start
octalResult = octString[: : -1]

# prints the result of the conversion
print(f'The octal representation of {decimalInput} is 0o{octalResult}')
print()

print('From octal to decimal')
print('----------------------')

# read the octal string from the user's input
octalInput = str(input('Give a positive integer in octal representation: '))

# remove '0o' using string slicing
octalPure  = str(octalInput)[2:]

# get the reversed octal digit
reversedOctalInput = octalPure[ : :-1]


# convert the octal string to a correct decimal integer
# add the appropriate power
octalResult = 0
for i in range(0, len(octalPure)):
    octalResult = octalResult + ((8 ** i) * int(reversedOctalInput[i]))


print(f'The decimal representation of {octalInput} is {octalResult} ')
print()
print('Thank you for using this program.')
print()
input('Press Enter to continue ...')