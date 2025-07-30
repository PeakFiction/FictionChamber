#RSA Encryption

# How to Use This RSA Program Correctly
# Pick Two Prime Numbers Bigger Than Your Message
# Example: 17 and 23
# Don’t use 1, 4, or any number that’s not prime.

# Enter a Message Smaller Than Prime1 × Prime2
# If you pick 17 and 23, that means your message must be less than 391.

# Use These Sample Keys if You Don’t Know What to Do

# Public Key: 3

# Private Key: 235
# (These only work with primes 17 and 23.)

# Do Not Make Up Random Keys
# The keys only work if they’re paired correctly. Random numbers will break it.

def encryptRSA(message, publicKey, prime1, prime2):
    return (message**publicKey) % (prime1 * prime2)

def decryptRSA(encryptedMessage, privateKey, prime1, prime2):
    return (encryptedMessage**privateKey) % (prime1*prime2)

def startProgram():
    originalMessage = int(input("Input the original Integer: "))
    publicKey = int(input("Input Public Key: "))
    privateKey = int(input("Input Private Key: "))
    prime1 = int(input("Enter 1st Prime Number: "))
    prime2 = int(input("Enter 2nd Prime Number: "))
    print()
    encryptedMessage = encryptRSA(originalMessage, publicKey, prime1, prime2)
    print(f"Encrypted Result: {encryptedMessage}")
    print()
    
    decryptedMessage = decryptRSA(encryptedMessage, privateKey, prime1, prime2)
    
    print(f"Decrypted Message: {decryptedMessage}")

startProgram()

