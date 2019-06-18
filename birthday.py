#Wyatt Turner - 100557909
#This program generates a list of 16 sets of 4 numbers, 3 primes and a hash of the 3.
#It then generates random sets of numbers, and compares the hashes generated to those
#from the original list of primes


from sympy import randprime, isprime
import os
from random import *

#3a list of 3 random numbers below 25
prime_set = ([])
print("16 valid messages: ")
for i in range(0,16):
    
    p1= randprime(1,257)
    p2= randprime(1,257)
    p3= randprime(1,257)
    
    h1 = p1^p2^p3
    
    numset = ([p1,p2,p3,h1])
    
    prime_set.append(numset)
	
    print(prime_set[i][0], prime_set[i][1], prime_set[i][2],"    || ", prime_set[i][3])
    
    
#Composite Numbers
t1 = 0

while t1 == 0:
    c1 = randint(1, 256)
    c2 = randint(1, 256)
    c3 = randint(1, 256)
    #print(c1)
    
    
    h2 = c1^c2^c3
    numset2 = ([c1,c2,c3,h2])
    
    for i in range(0,16):
        #print(prime_set[i])
        if h2 == (prime_set[i][3]):
            print("Looking for fraudulent message that matches valid hash...")
            print("Collision found after", i , "attempts:")
            print("Original set and hash: ")
            print(prime_set[i][0], prime_set[i][1], prime_set[i][2],"    || ", prime_set[i][3])
            print("Fraudulent Message set and hash:")
            print(c1, "", c2, "", c3, "   ||  ", h2)
            t1 += 1
        else:
            #print(prime_set[i][3])
            #print("1")
            continue
    

    
        
        
    
        