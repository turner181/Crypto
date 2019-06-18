# Caesar Cipher Decrypt Brute Force
# Wyatt Turner - 100557909

MAX_SIZE = 26 #sets max key size allowed

#This function will get the users input of the encrypted message
def getCiphertext():   
    print('Please enter the ciphertext:')
    return input()

#This function will pass 2 values. The ciphertext and the 
def getDecryptedText(ciphertext, key):
    key = -key
    translated = ''
    
    for symbol in ciphertext:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
                    
            translated += chr(num)
        else:
            translated += symbol
    return translated
    
ciphertext = getCiphertext()

print('Your translated text is:')
for key in range(1, MAX_SIZE - 1):
        print(key, getDecryptedText(ciphertext, key))





