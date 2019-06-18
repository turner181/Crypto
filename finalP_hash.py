#Final Project - Group 12
#Hash Functions
def continueGame():
    input1 = input('Press enter to continue... \n')
    return

def getMode():
    while True:
        print('Do you know what Hash Functions are?')
        mode = input().lower()
        if mode in 'yes y no n'.split():
            if mode not in 'yes y'.split():
                getExplanation()
            return mode
        else:
            print('Enter either "yes" or "y" or "no" or "n".')

def getExplanation():
    print('Hash Functions are have many information-security applications, especially in digital signatures, message authentication signatures and other forms of authentication.')
        

def getMessage():
    print('Enter a letter, phrase or sentence to hash:\n')
    return input()

def start():
    print('Welcome to task d. This task provides information about hashes in cryptography.\n')
    print('The main aim of an hash funciton is to convert a variable-length block of data into a fixed-size hash. In this topic we will talk about the Secure Hash Algorithm (SHA). It was originally designed by NIST and published as a federal information processing standard in 1993.\n\nBack in 2002 NIST produced a revised version of the standard that defined three new versions of SHA with hash value length of 256, 384 and 512.')
    continueGame()
    print('In the following, we will use SHA256 to hash an input of your choice.\n')
    mode = getMode()
    message = getMessage()
    #explanation = 
    
    
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    
    
    digest.update(bytes(message, 'utf-8'))
    d= digest.finalize()
    print('The next line shows you the hash of your data \"' + str(message) + '\"')
    print(d)
    continueGame()
    print('By hitting enter you will be redirected to the menu')
    continueGame()
