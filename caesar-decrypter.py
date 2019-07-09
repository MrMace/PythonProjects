
inputFileName = input("Enter the encrypted message file name: ")
key = int(input("Enter the shift key: "))

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
shiftedAlphabetStart = alphabet[len(alphabet) - key:]
shiftedAlphabetEnd = alphabet[:len(alphabet) - key]
shiftedAlphabet = shiftedAlphabetStart + shiftedAlphabetEnd

inputFile = open(inputFileName, 'r')
encryptedMessage = inputFile.readline()

print(encryptedMessage)

decryptedMessage = ''
for character in encryptedMessage.strip():
    letterIndex = shiftedAlphabet.find(character)
    decryptedCharacter = alphabet[letterIndex]
    
    decryptedMessage = decryptedMessage + decryptedCharacter
    
print("The message is: {0} ".format(decryptedMessage))

inputFile.close()