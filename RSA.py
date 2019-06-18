#Wyatt Turner
#100557909

#Question 1 Python RSA Brute Force
#This program brute forces the value of d such that it solves both cases
#of M = C^d mod(n) and C = M^e mod(n), it does so by brute forcing possible
# d values and compares the statements. This is assuming PU = {e, n} ={5, 35}
#and C = 10.



for x in range (1, 35):
    Plaintext = (10**x) % 35
    
    Cipher = (((Plaintext)**5) % 35)
    #print(x)
    if Cipher == 10:
        print("The plaintext value M:" ,Plaintext)
        print("The secret exponent d:",x)
        break
