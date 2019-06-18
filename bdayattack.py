#Wyatt Turner - 100557909
#This program attempts to brute force a matching hash value to the one generated
#in the example. It does so by generating its own random hashes and comparing them to
#the one generated in the example

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"251")
digest.update(b"157")
digest.update(b"191")
tower = digest.finalize()

print(digest)

for i in range(1, 10000000):
    c1 = randint(0, 255)
    c2 = randint(0, 255)
    c3 = randint(0, 255)
    b1 = c1.to_bytes(1, 'big')
    b2 = c2.to_bytes(1, 'big')
    b3 = c3.to_bytes(1, 'big')
    #print(c1)
    digest1 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest1.update(b1)
    digest1.update(b2)
    digest1.update(b3)
    catapult = digest1.finalize()
    
    
    if catapult == (tower):
        print("MATCH FOUND!!!!! ", catapult, "", tower)
        break
        
    else:
        #print("1")
        #print("No Match")
        continue
        #break
