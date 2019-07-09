encodedString = '80 121 116 104 111 110 32 51'
encodedTokens = encodedString.split(" ")

decodedStr = []
for numberString in encodedTokens:
    decodedChar = chr(int(numberString))
    #decodedStr = decodedStr + decodedChar
    decodedStr.append( decodedChar)
    
print(decodedStr)
print("".join(decodedStr))