#  Program template for Lab Tutorial 8
import string
# string of all lowercase and uppercase letters:
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
lowerupper = string.ascii_letters
def main():
# Gather input from the user:
# keyword, input file name, output file name, kind of operation
    keyword = input("Enter the secret Keyword: ")
    in_name = input("Enter the input file name (including .txt) ")
    out_name = input("Enter the output file name (including. txt) ")
    operation = input("(E)crypt or (D)ecrypt? ")
# Read all of the text out of the file as a string 
    inf = open(in_name)
    text = inf.read()
    inf.close()
# Create dictionaries for encryption and decryption # Put the dictionaries in a list:
# dictioEnc -- list of dictionaries for encryption
# dictioDec -- list of dictionaries for decryption 
    keylen = len(keyword)
    dictioEnc = []
    dictioDec = []
    
    for i in range(0,keylen):
        dictioEnc.append(dict(zip(lowerupper,lowerupper[lowerupper.index(keyword[i]):]+lowerupper[:lowerupper.index(keyword[i])])))
        dictioDec.append(dict(zip(lowerupper[lowerupper.index(keyword[i]):]+lowerupper[:lowerupper.index(keyword[i])],lowerupper)))
# Encrypt or decrypt the text string provided by the user, character # by character, using the dictionaries
    result = "" # accumulate the result of encryption/decryption here 
    for i in range(0, len(text)):
        if operation == "E":
            result += dictioEnc[i % keylen].get(text[i], text[i])
        else:
            mod = i % keylen
            result += dictioDec[i % keylen].get(text[i], text[i])

# Save the result to a file
    print(f"The result has been saved to the file: {out_name}") 
    outf = open(out_name, "w")
    outf.write(result)
    outf.close()

if __name__ == '__main__': 
    main()