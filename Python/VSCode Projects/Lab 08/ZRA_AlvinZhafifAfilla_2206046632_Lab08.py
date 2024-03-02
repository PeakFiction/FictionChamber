# Program template for Lab Tutorial 8
# Alvin Zhafif Afilla
# 2206046632
import string
# string of all lowercase and uppercase letters:
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerupper = string.ascii_letters
def main():
    # Gather input from the user:
    # keyword, input file name, output file name, kind of operation
    keyword = input("Enter Your Keyword : ")  # prompt the user for the keyword
    in_name = input("Enter Your Input File Name(include the .txt) : ") # prompt the user for the requested file
    out_name = input("Enter Your Output File Name(include the .txt) : ") # prompt the user for the name of the outputted file
    operation = input("(E)ncrypt or (D)ecrypt? ") # prompt the user for decryption or encryption
    # Read all of the text out of the file as a string
    inf = open(in_name)
    text = inf.read()
    inf.close()
    # Create dictionaries for encryption and decryption
    # Put the dictionaries in a list:
    # dictioEnc -- list of dictionaries for encryption
    # dictioDec -- list of dictionaries for decryption
    keylen = len(keyword)
    dictioEnc = [] # set the dictionary empty so it can be added later
    dictioDec = [] # set the dictionary empty so it can be added later
    for i in range(0,keylen):
        # we use append here because we need to append the dictionary back to the original empty list, lowerupper.index is used so we can get the precise index of each ascii letters index
        dictioEnc.append(dict(zip(lowerupper,lowerupper[lowerupper.index(keyword[i]):]+lowerupper[:lowerupper.index(keyword[i])])))
        # for decryption dictionary it's the same with encrypting but just reverse their order
        dictioDec.append(dict(zip(lowerupper[lowerupper.index(keyword[i]):]+lowerupper[:lowerupper.index(keyword[i])],lowerupper)))

    # Encrypt or decrypt the text string provided by the user, character
    # by character, using the dictionaries
    result = "" # accumulate the result of encryption/decryption here
    for i in range(0, len(text)) :
        if operation == "E": #equals to E for encrypting
            spec = i % keylen # i % keylen is used because we need every inputted keyword to repeat when it reaches the end of it's length
            result += dictioEnc[spec].get(text[i],text[i]) # add the result back to the empty string 
                                    # .get(text[i],text[i]),is used so we can return the text
        else: # equals to D, but since there are no more inputs i use else
            spec = i % keylen
            result += dictioDec[spec].get(text[i],text[i])
        
# Save the result to a file
    print(f"The result has been saved to the file: {out_name}")
    outf = open(out_name, "w")
    outf.write(result)
    outf.close()
if __name__ == '__main__':
    main()
