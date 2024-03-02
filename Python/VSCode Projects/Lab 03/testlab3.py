
octalInput = int(input('Give a positive integer in octal representation: '))
octalPure  = str(octalInput)[2:]

for i in range(1, int(octalPure)):
    print(i)
