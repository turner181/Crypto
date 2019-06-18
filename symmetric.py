#Wyatt Turner - 100557909
#This program will take input from the user and encrypt it with AES. After, it will decrypt the ciphertext and display the original input
#Some of this code was taken from https://cryptography.io/en/latest/hazmat/primitives/symmetric‐encryption/

import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

plaintext = input("Please enter the message to encrypt: ").encode()
backend = default_backend() #This code taken from Cryptophrahy.io
key = os.urandom(16)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend=backend)
encryptor = cipher.encryptor()
ct = (encryptor.update(plaintext) + encryptor.finalize())
decryptor = cipher.decryptor()
dt = decryptor.update(ct) + decryptor.finalize()

print('')
print('The encrypted message done with AES is: ', ct)
print('')
print('The original plaintext after being decrypted is: ', dt)
