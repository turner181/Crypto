#Wyatt Turner - 100557909
#This program will apply Chinese Remainder THeorm to a set of inputs from the user

#Assuming r s & t are co-primes


a = int(input('Enter integer for a:'))
print('')
b = int(input('Enter integer for b:'))
print('')
c = int(input('Enter integer for c:'))
print('')
r = int(input('Enter integer for r:'))
print('')
s = int(input('Enter integer for s:'))
print('')
t = int(input('Enter integer for t:'))
print('')


M = (r*s*t)
M_1 = (M/r)
M_2 = (M/s)
M_3 = (M/t)

#Fermat
InvM_1 = ((M_1 ** (r-2)) % r)
InvM_2 = ((M_2 ** (s-2)) % s)
InvM_3 = ((M_3 ** (t-2)) % t)


x = ((a*M_1*InvM_1)+(b*M_2*InvM_2)+(c*M_3*InvM_3)) % M

print(x)

