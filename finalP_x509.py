# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:54:29 2018

@author: arndt
"""
from cryptography.hazmat.primitives import serialization
import time
def continueGame():
    input1 = input('Press enter to continue... \n')
    return

def getPlainText(s):
    try:
        infile = open(s, 'rt')
        message = infile.read()
        infile.close()
        return message
    except:
        print('fail')
        return b'None'


def start():
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import dsa
    from cryptography.hazmat.primitives import hashes
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    
      
    print('Welcome to task e. \n\nTask e deals with the X.509 specification.\nX.509 certificates are used to authenticate clients and servers. The most common use case is for web servers using HTTPS.\n')
    continueGame()
    print('When obtaining a certificate from a certificate authority (CA), the usual flow is:\n 1. You generate a private/public key pair.\n 2. You create a request for a certificate, which is signed by your key (to prove that you own that key).\n 3. You give your CSR to a CA (but not the private key).\n 4. The CA validates that you own the resource (e.g. domain) you want a certificate for.\n 5. The CA gives you a certificate, signed by them, which identifies your public key, and the resource you are authenticated for.\n 6. You configure your server to use that certificate, combined with your private key, to server traffic.')
    
    
    
        
    continueGame()
    print('In this task, we will create a Certificate Signing Request. Therefore, we will generate a private/public key pair using DSA, sign the key, and create the CSR. We will not give the CSR to the Certificate Authority.\n\nNow, our private key will be created with the key size 1024')
    
    
    private_key = dsa.generate_private_key(
            key_size=1024,
            backend= default_backend())
    
    print('Now we want to sign the key, to make sure, that we are the owner of it.\n')
    data=bytes(input('Please enter something to sign your private key.\n'), 'utf-8')
    signature = private_key.sign(
            data,
            hashes.SHA256()
            )
    
    public_key = private_key.public_key()
            
    print('In this step, we want to create the request for the certificate. We used some basic values, as it is just an example. But anyway, the programm will ask you to enter the name which will make the CSR more personal for you.')
    
    
    # Generate a CSR
    csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
         # Provide various details about who we are.
         x509.NameAttribute(NameOID.TITLE, u"INFR-3600"),
         x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CANADA"),
         x509.NameAttribute(NameOID.LOCALITY_NAME, u"OSHAWA"),
         x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UOIT"),
         x509.NameAttribute(NameOID.GIVEN_NAME, input('Enter your name:\n')),
         x509.NameAttribute(NameOID.COMMON_NAME, u"FINAL PROJECT"),
     ])).add_extension(
         x509.SubjectAlternativeName([
             # Describe what sites we want this certificate for.
             x509.DNSName(u"test.com"),
             x509.DNSName(u"www.test.com"),
             x509.DNSName(u"subdomain.test.com"),
         ]),
         critical=False,
     # Sign the CSR with our private key.
     ).sign(private_key, hashes.SHA256(), default_backend())
    # Write our CSR out to disk.
    
    print('We will sign the CSR with our private key, to prove that we own that key.\n')
    with open("csr1.pem", "wb") as f:
         f.write(csr.public_bytes(serialization.Encoding.PEM))
    continueGame()
    print('If those steps were succesful you will have created your first CSR. Your CSR will be displayed in the next lines')
    continueGame()
    print(getPlainText("csr1.pem"))
    
    print('\n\n\nCongratulations, you created your CSR. We are not able to give the CSR to a certificate authority as it is just an example. In a real scenario the CA would validate if you own the resource. Then the CA would provide us a certificate which we can use on our server.\nHit enter, whenever you are ready to go back to main menu.')
    continueGame()
    #time.sleep(3)