#Final Project Group 12
#This module will take a user input and encrypt/decrypt it with RSA. Through messages
#to the user, they will learn about RSA and be able to practice some encryption with it

def continue1():
    input1 = input('Press enter to continue... \n')
    return
	
def start():	
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
    print('Welcome to the RSA encryption/decryption module!!!')
    print('')
    print('In this module we will be exploring RSA, and how it encrypts and decrypts data')
    print('')
    print('Rivest-Sharmir-Adleman(RSA), is a public-key encryption algorithm.\nDeveloped in 1977 at MIT, it is the most ubiquitous public-key encryption algorithm available.')
    print('It makes use of 2 major principals: Prime Factorization and the Diffie-Hellman Key Exchange.')
    print('Prime Factorization, also known as a Trapdoor Function, is a basis for RSA.')
    print('Its the theory that composite numbers, or integers that are non-prime, can be factored down to only primes.')
    print('This is what makes RSA strong, as its extremly difficult to factor large prime numbers.\n\n')
    print('The Diffie-Hellman Key Exchange is another important part of RSA. It allows users to to exchange keys in a way that they both find a common key, and outside listeners cannot compute the message.')
    print('Both sender and reciever know the public-key. Through the use of private keys and exchanging keys, they can encrypt and decrypt messages.')
    continue1()
    print('Now that we understand what makes up RSA, lets look at how RSA actually encrypts our data!')
    
    print('\nIn order to demonstrate this, lets  first start with a plaintext to encrypt with RSA')
    
    #Get input from user to be encrypted
    ptext = input('\nPlease enter the plaintext to be encrypted: ').encode()
    
    print('\nNow that we have the plaintext to be encrypted, we can look at how RSA will encrypt this message.')
    print('First, a key is generated. It is done for you, and is a large number made by the multiplication of 2 large prime numbers.')
    print('The key is large enough that it would take even supercomputers thousands of years to solve.')
    print('In this example a local public-key is created to facilitate the key exchange required in public-key encryption.')
    print('')
    #Creates local public key
    public_key = private_key.public_key()
    
    
    continue1()
    print('Using the public-key created, RSA can be used to encrypt the plaintext.')
    print('It does so, while adding a padding algorithm and a hash.')
    #Encryption
    ciphertext = public_key.encrypt(
    		ptext,
    		padding.OAEP(
    				mgf=padding.MGF1(algorithm=hashes.SHA256()),
    				algorithm=hashes.SHA256(),
    				label=None
    		)
    )
    
    continue1()
    print('We have now taken the plaintext: ', ptext, ' and encrypted it with RSA. This has created a ciphertext; our plaintext, only encrypted with RSA.')
    print('')
    continue1()
    print('The resulting ciphertext after all operations are preformed to RSA is: ')
    print(ciphertext)
    continue1()
    
    print('Now to decrypt the ciphertext we created. RSA does this by using the private key and reversing the padding scheme.')
    #Decryption
    dtext = private_key.decrypt(
    		ciphertext,
    		padding.OAEP(
    				mgf=padding.MGF1(algorithm=hashes.SHA256()),
    				algorithm=hashes.SHA256(),
    				label=None
    			)
    )
    
    continue1()
    print('We have now preformed the decryption process on the ciphertext')
    print('We can now see the decrypted plaintext: ', dtext)
    continue1()
    
    print('\n\n\nWell done, you have successfully encrypted, and decrypted a message using RSA!!')
    print('\n\n\nPress any button to return to menu...')
    continue1()