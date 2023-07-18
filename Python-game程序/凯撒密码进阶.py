alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter the message you want to encrypt: ")
stringToEncrypt = stringToEncrypt.upper() 
shiftAmount = int(input("Please enter a whole number from 1-25:"))
encryptedString = ""

print(alphabet[52])

for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]
        print(alphabet[newPosition]+str(newPosition))
    else:
        encryptedString = encryptedString + currentCharacter

print("Your encrypted message is", encryptedString)

#To decrypt, type the encrypted message and make the shift negative (a minus number)

