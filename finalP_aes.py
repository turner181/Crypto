# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 12:20:01 2018

@author: arndt
"""
def continueGame():
    input1 = input('Press enter to continue... \n')
    return
def start():
    import os
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    import random, os
    import time
    import string
    print()
    print('Now we will use AES to encrypt and decrypt a plaintext you choose. The Advanced Encryption Standard is based on the Data Encryption Standard which was the most widely used symmetric encryption standard until the introduction of AES in 2001.\n\n ')
    #time.sleep(2)
    continueGame()
    print('It processes the entire data block as a single matrix during each round using substitutions and permutation. In total, four different stages are used in one round:\n - Substitute bytes: byte by byte substitution of the block using an S-box\n - ShiftRows: permutation\n - MixColumns: a substitution that makes use of arithmetic over GF(2 to the power 8)\n - AddRoundKey: a bitwise XOR of the current block with a portion of the expanded key')
    #time.sleep(2)
    continueGame()
    def getPlainText():
        inputString = input('Please enter the plaintext that you want to encrypt (16 bytes): ')
        if ((len(inputString) % 16 )!= 0):
            remainder = 16 -(len(inputString) % 16)
            print("As the input\'s length is %i, which is not a multiple of 16, %i characters have been added to plaintext." %(len(inputString), remainder))
            #print('Modified input String: ' + inputString)
            for x in range(remainder):    
                inputString = inputString +random.choice(string.ascii_letters)
            print('Modified input String: ' + inputString)
        else:
            print('Length of input is multiple of 16. So we can start.')
        time.sleep(2)
        return inputString.encode('utf-8')
    backend = default_backend()
    key = os.urandom(32)
    #time.sleep(2)
    #continueGame()
    print('\nA random key is computed, which is: \n', key, '\n')
    #print('Key: ' + key.decode("utf-8"))
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    continueGame()
    print('Now we will get your message and encrypt it using AES in ECB mode (learn more about different modes of operations in task B')
    ct = encryptor.update(getPlainText()) + encryptor.finalize()
    print('\nCongratulations, you have encrypted your message. See the ciphertext in the next line.\n',ct)
    
    continueGame()
    #time.sleep(2)
    print('\n\nNow we are going to decrypt the ciphertext. The decryption algorithm makes use of the expanded key in reverse order. The decryption algorithm is not identical to the encryption algorithm. See your decrypted ciphertext in the next line.\n')
    decryptor = cipher.decryptor()
    pt =decryptor.update(ct) + decryptor.finalize()
    print(pt)
    
    print('\n\nWell done. You are done with task A. If you want to repeat it, you are free to choose it again in main menu. You will get to the main menu in a few secons.')
    #time.sleep(5)
    continueGame()
    

    
#start()