#RSA Encryption

# m = message
# c = encrypted message
# e = public key component
# d = private key component
# n = prime1 * prime2, product of two secret primes

#To Encrypt = 
# c == m^e mod n

#To Decrypt = 
# m == m^d mod n

def encryptRSA(message, publicKey, prime1, prime2):
    return (message**publicKey) % (prime1 * prime2)

def decryptRSA(encryptedMessage, privateKey, prime1, prime2):
    return (encryptedMessage**privateKey) % (prime1*prime2)

def startProgram():
    originalMessage = int(input("Input the original Integer: "))
    publicKey = int(input("Input Public Key "))
    privateKey = int(input("Input Private Key: "))
    primesNumber = input("Input Prime Number: ")
    primesNumber.split()
    prime1 = primesNumber
