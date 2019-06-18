#Final Project Group 12
#This module will take a user input and encrypt/decrypt it with RSA. Through messages
#to the user, they will learn about RSA and be able to practice some encryption with it


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#Generate a private key
private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
)

#Welcome messages. Explains module and asks for user input
print('Welcome to the RSA encryption/decryption module')
print('')
print('In this module we will be exploring RSA, and how it encrypts and decrypts data')
print('')
print('First, lets start with a plaintext')
print('-------------------------------------------------')


#Get input from user to be encrypted
ptext = input('Please enter the plaintext to be encrypted: ').encode()

#Creates local public key
public_key = private_key.public_key()

#Encryption
ciphertext = public_key.encrypt(
        ptext,
        padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
        )
)

print('We have now taken the plaintext: ', ptext, ' and encrypted it with RSA.')
print('')
print('The resulting output after all operations are preformed to RSA is: ')
print('')
print(ciphertext)

#Decryption
dtext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
)

print('')
print('We have now preformed the decryption process on the ciphertext')
print('We can now see the decrypted plaintext: ', dtext)