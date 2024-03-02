print("Welcome to Duden's Converter")

originalInput = str(input("Where do you want to convert from? "))
originalOutput= str(input("Where do you want to convert to? "))


if originalInput == str("Decimal"):
    decimalInputOrigin= int(input ("Insert the original decimal number: "))
    if originalOutput == str("Binary"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("B"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("O"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("X"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)

if originalInput == str("Dec"):
    decimalInputOrigin= int(input ("Insert the original decimal number: "))
    if originalOutput == str("Binary"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("B"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("O"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("X"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)


if originalInput == str("D"):
    decimalInputOrigin= int(input ("Insert the original decimal number: "))
    if originalOutput == str("Binary"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("B"):
        outputOrigin = bin(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("O"):
        outputOrigin = oct(decimalInputOrigin)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)
    elif originalOutput == str("X"):
        outputOrigin = hex(decimalInputOrigin)
        print(outputOrigin)

#from Binary ------------
elif originalInput == str("Binary"):
    binaryInputOrigin = str(input("Insert the original binary number: "))
    if originalOutput == str("Decimal"):
        outputOrigin = int(binaryInputOrigin, 2)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(binaryInputOrigin, 2)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(binaryInputOrigin, 2)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

elif originalInput == str("Bin"):
    binaryInputOrigin = str(input ("Insert the original binary number: "))
    if originalOutput == str("Decimal"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

elif originalInput == str("B"):
    binaryInputOrigin = str(input ("Insert the original binary number: "))
    if originalOutput == str("Decimal"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(binaryInputOrigin, 10)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(binaryInputOrigin, 2)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

#from Octal --------------------------------

elif originalInput == str("Octal"):
    octalInputOrigin = str(input ("Insert the original octal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

elif originalInput == str("Oct"):
    octalInputOrigin = str(input ("Insert the original octal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

elif originalInput == str("O"):
    octalInputOrigin = str(input ("Insert the original octal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(octalInputOrigin, 8)
        print(outputOrigin)
    if originalOutput == str("Hexa"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Hex"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("X"):
        decimalTemp = int(octalInputOrigin, 8)
        outputOrigin = hex(decimalTemp)
        print(outputOrigin)

#from Hexadecimal ------------

elif originalInput == str("Hexadecimal"):
    hexaInputOrigin = str (input ("Insert the original hexadecimal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(decimalTemp, 16)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(decimalTemp, 16)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(decimalTemp, 16)
        print(outputOrigin)

elif originalInput == str("Hex"):
    hexaInputOrigin = str(input ("Insert the original hexadecimal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)

elif originalInput == str("X"):
    hexaInputOrigin = str (input ("Insert the original hexadecimal number: "))
    if originalOutput == str("Binary"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Bin"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("B"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = bin(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Octal"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("Oct"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    elif originalOutput == str("O"):
        decimalTemp = int(hexaInputOrigin, 16)
        outputOrigin = oct(decimalTemp)
        print(outputOrigin)
    if originalOutput == str("Decimal"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)
    elif originalOutput == str("Dec"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)
    elif originalOutput == str("D"):
        outputOrigin = int(hexaInputOrigin, 16)
        print(outputOrigin)

