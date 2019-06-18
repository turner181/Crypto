# -*- coding: utf-8 -*-
"""
Created on Tue Oct  31 22:52:39 2018

@author: arndt
"""
#import symmetric
#import symmetric1
#import symmetric1
import sys, time
exits= False
def quiz():
    print('In this quiz, three questions will be asked, and you have to choose between answer a, b or c in each question.')
    time.sleep(2)
    q1 = q2 =q3 = False
    while True:       
       # if exits == False:
            if q1 == True:
                if q2== True:
                    if q3 == True:
                        return
                    else:
                        q3=question('Tell me %s, which of the following options are not COMPLETELY related to cryptography? [a/b/c]\n' %name, 'A: encryption, hash, signature\n', 'B: plaintext, brute force attack, certificate authority\n','C: cipher, tomography, RSA\n', 'c')
                else:
                    q2 = question('Tell me %s, what is the main difference between symmetric and asymmetric encryption? [a/b/c]\n' %name, 'A: Asymmetric encryption uses SHA512 while symmetric encryption uses SHA256.\n', 'B: Symmetric encryption uses one secret key that has to be kept secure by sender and receiver, while in asymmtric encryption there are two related keys that are used to perform complementary operations.\n','C: While the key is a high prime number in symmetric encryption, the key is a long word in asymmetric encryption.\n', 'b')
            else: 
                q1 =question('Tell me %s, what is a ciphertext? [a/b/c]\n' %name, 'A: The generated key\n', 'B: The original message\n','C: The coded message\n', 'c')
       # else:
        #    print('Exit')
            
    

def question(q, a1, a2, a3, c):
    print(q)
    print(a1)
    print(a2)
    print(a3)
    mode = input().lower()
    if mode == 'exit':
        print('Exit game')
        sys.exit()
        #global exits
       # exits= True
        
    elif mode in 'a b c'.split():
        answer = mode
        correct = c
        if correct == answer:
            print('Correct.\n')
            return True
        else:
            print()
            print('Try again!\n')
           
    else:
        print()
        print('Please enter a, b or c')
            

def isFamiliar():
    while True:
        print('Tell me %s, are you familiar with cryptography? [y/n]' %name)
        mode = input().lower()
        if mode in 'y n'.split():
            return mode
        else:
            print('Please enter "y" or "n"')




# Main Program start  
print()
print('Welcome to our crypto basic tutorial')
#print('')
name = str(input('Please enter your name: '))
print('Fine!. ')

fam = isFamiliar()
if(fam == 'y'):
    print('As you have some knowledge about cryptography, let\'s start with a quiz about basic definitions. Keep in mind, that you can exit with "exit"')

else:
    print('To start, we will define some keywords, you will use dealing with cryptography')
    print('Blabla bla some definitions')
    print('Now we can go on with a little quiz to  test your newly learned stuff')
    
quiz()
print('Alright. This maybe has refreshed your knowledge. Now you will see the main menu')

while(True):
    mode = input("Please choose a task! [a/b/c/d/e] \nOr press 'exit' to leave.\n\nA: Symmetric encryption using AES\nB: Comparison of modes of operations\nC: Encryption & Decryption using RSA\nD: Hash Function using SHA-256\nE: Creating a Certificate Signing Request\n").lower()
    if mode in 'a b c d e exit'.split():
        print("Valid input")
        if mode == "a":
            print(mode)
            import tasks.finalP_aes as finalP_aes
            finalP_aes.start()
            print("\n\nBack to main menu")
            #do Task a
        elif mode == "b":
            print(mode)
            import tasks.finalP_modesOfOperations as finalP_modesOfOperations
            finalP_modesOfOperations.start()
            #do Task b Comparison between modes of operations
            print("\n\nBack to main menu")
        elif mode == "c":
            print(mode)
            import tasks.finalP_rsa as finalP_rsa
            finalP_rsa.start()
            #do Task c RSA
            print("\n\nBack to main menu")
        elif mode == "d":
            print(mode)
            import tasks.finalP_hash as finalP_hash
            finalP_hash.start()
            #do Task d SHA
            print("\n\nBack to main menu")
        elif mode == "e":
            print(mode)
            import tasks.finalP_x509 as finalP_x509
            finalP_x509.start()
            #do Task e DSA, Certificates
            print("\n\nBack to main menu")
        elif mode == "exit":
            sys.exit("Leave the game.")
            #do Task b
    
    else:
        print("Invalid input. Please try again.")


print('Thanks lol')


