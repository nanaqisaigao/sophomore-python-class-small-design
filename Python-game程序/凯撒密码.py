#This is the program on pages 43 to 45, up to and including step 8.

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrypt: ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key:"))
encryptedString = ""

for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    encryptedString = encryptedString + alphabet[newPosition]

print("Your encrypted message is", encryptedString)

#To decrypt, type the encrypted message and make the shift negative (a minus number)

