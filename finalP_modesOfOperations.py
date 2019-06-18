# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:02:16 2018

@author: arndt
"""

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import random
import string
import time
import msvcrt as m

def getPlainText(s):
    try:
        infile = open(s, 'rb')
        message = infile.read()
        infile.close()
        #print('hello')
        return message
    except:
        print('fail')
        return b'None'
    
    
def continueGame():
    input1 = input('Press enter to continue... \n')
    return


def start():
    print()
    print('In this task you will learn about different modes of operations and how they impact the encryption. We will use the Advanced Encryption standard from task a to demonstrate the modes.\n')
    print('In 2001 the NIST standardized five modes of operation which apply to AES: \n - ECB (Electronic Code Book)\n - CBC (Cipher Block Chanining)\n - CFB (Cipher FeedBack)\n - OFB (Output FeedBack)\n - CTR (Counter)')
    print('\nThe mode of operation may provide application of the block cipher on a stream of plaintext and make the algorithm more efficient. Additionally, mode of operation may convert the block cipher into a stream cipher and strengthen the effect of the encryption algorithm.\nIn this task information about the modes will be provided and the time for encryption will be compared.')
    print('')
    #modes1 = ("ECB", "CBC", "CFB","OFB","CTR")    
    a = 10
    #time.sleep(10)
    #os.system('pause')
    continueGame()
    # ECB
    print('We will start with the encryption of a file with AES in ECB mode. It is the simplest of all and it divides the plaintext message in blocks (P1, P2, Pn), where each block is encrypted seperately with the same key. The result of the encryption are the encrypted messages C1, C2 and Cn. Identical blocks P will produce identical C blocks. It is not recommended to use this mode for encryption of data that is larger than one block.\n')
    timeECB = 0
    for i in range(a):
        padder= padding.PKCS7(128).padder()
        backend = default_backend()
        key = os.urandom(32)
        iv = os.urandom(16)
        mode = modes.ECB()
        cipher = Cipher(algorithms.AES(key), mode, backend=backend)
        encryptor = cipher.encryptor()
        plaintext = padder.update(getPlainText('Ch06-AES.pptx'))
        plaintext+= padder.finalize()
        start = time.time()
        ct = encryptor.update(plaintext) + encryptor.finalize()
        end= time.time()
        timeECB+= end-start
    timeECB = timeECB/(a)
    
    continueGame()
    
    #print("Time for encryption "  + str(end-start))
    
    
    # CBC
    print('As every encryption of the same plaintext should result in a different ciphertext the CBC mode uses an initialization vector (IV). The IV has the same size as the block that is encrypted. First an  XOR operation is applied to the plaintext block (P1) with the IV, and then an encryption with the key (K) is performed. Then, the results of the encryption performed on each block (C1, C2, … , CN-1) is used in an XOR operation of the next plaintext block PN which results in CN. The same key K is used in each of the encryption blocks.\n')
    timeCBC=0
    for i in range(a):
        
        padder= padding.PKCS7(128).padder()
        backend = default_backend()
        key = os.urandom(32)
        iv = os.urandom(16)
        mode = modes.CBC(iv)
        cipher = Cipher(algorithms.AES(key), mode, backend=backend)
        encryptor = cipher.encryptor()
        plaintext = padder.update(getPlainText('Ch06-AES.pptx'))
        plaintext+= padder.finalize()
        start = time.time()
        ct = encryptor.update(plaintext) + encryptor.finalize()
        end= time.time()
        timeCBC += end- start
    timeCBC= timeCBC/a
    continueGame()
    #print("Time for encryption "  + str(end-start))
    
    # CFB
    print('The CFB mode of operation allows the block encryptor be used as a self-synchronizing stream cipher. As it is close to CBC, it also uses an IV and a Key. Then, an XOR is performed between the encryption result and the plaintext block. Afterwards, another XOR is performed with corresponding plaintext block, while the IV is placed in a shift register that can be e.g. 64 bits.\n')
    #padder= padding.PKCS7(128).padder()
    timeCFB =0
    for i in range(a):  
        backend = default_backend()
        key = os.urandom(32)
        iv = os.urandom(16)
        mode = modes.CFB(iv)
        cipher = Cipher(algorithms.AES(key), mode, backend=backend)
        encryptor = cipher.encryptor()
        plaintext = (getPlainText('Ch06-AES.pptx'))
        #plaintext+= padder.finalize()
        start = time.time()
        ct = encryptor.update(plaintext) + encryptor.finalize()
        end= time.time()
        timeCFB += end- start
    timeCFB = timeCFB/a
    continueGame()
    
    # OFB
    print('The Output Feedback (OFB) mode makes a block cipher into a synchronous stream cipher. It generates keystream blocks, which are then XORed with the plaintext blocks to get the ciphertext. Just as with other stream ciphers, flipping a bit in the ciphertext produces a flipped bit in the plaintext at the same location. This property allows many error correcting codes to function normally even when applied before encryption.\n')
    timeOFB = 0
    for i in range(a):
        
        backend = default_backend()
        key = os.urandom(32)
        iv = os.urandom(16)
        mode = modes.OFB(iv)
        cipher = Cipher(algorithms.AES(key), mode, backend=backend)
        encryptor = cipher.encryptor()
        plaintext = (getPlainText('Ch06-AES.pptx'))
        #plaintext+= padder.finalize()
        start = time.time()
        ct = encryptor.update(plaintext) + encryptor.finalize()
        end= time.time()
        timeOFB += end- start
    timeOFB = timeOFB /a
    continueGame()
    
    # CTR
    print('At the CTR mode of operation as an input block to the encryptor (e.g. an IV), the value of a counter is used. Like OFB, Counter mode turns a block cipher into a stream cipher. It generates the next keystream block by encrypting successive values of a "counter". The counter can be any function which produces a sequence which is guaranteed not to repeat for a long time, although an actual increment-by-one counter is the simplest and most popular.\n')
    
    timeCTR = 0
    for i in range(a):
        
        key = os.urandom(32)
        nonce = os.urandom(16)
        mode = modes.CTR(iv)
        cipher = Cipher(algorithms.AES(key), mode, backend=backend)
        encryptor = cipher.encryptor()
        plaintext = (getPlainText('Ch06-AES.pptx'))
        #plaintext+= padder.finalize()
        start = time.time()
        ct = encryptor.update(plaintext) + encryptor.finalize()
        end= time.time()
        timeCTR += end- start
    timeCTR = timeCTR/a
    continueGame()
    
    print('\n\n\nFinally, the encryption times of the mode will be compared. The same file has been used for encryption. Additionally, the average of 10 times of encryptions have been taken.\n - Time for encryption using ECB: ',timeECB,'s\n - Time for encryption using CBC: ', timeCBC, 's\n - Time for encryption using CFB: ', timeCFB,'s\n - Time for encryption using OFB: ', timeOFB, 's\n - Time for encryption using CTR: ', timeCTR,'s')
    print('\n\nIt can be seen that CTR mode is one of the fastes modes. In order to obtain a proper and secure AES implementation, the CTR mode should be used.\n\n')
    
    print('Well done. Hopefully you could improve your knowledge about the modes of operation.\nYou will be redirected to the main menu to choose the next task by hitting enter.\n')
    #time.sleep(5)



