# read the octal string from the user's input
octalInput = str(input('Give a positive integer in octal representation: '))
octalPure  = str(octalInput)[2:]
reversedOctalInput = octalPure[ : :-1]



# convert the octal string to a correct decimal integer

for i in range(0, len(octalPure)):
    octalResult = octalResult + ((8 ** i) * int(reversedOctalInput[i]))


print(f'The decimal representation of {octalInput} is {octalResult} ')
