#Wyatt Turner - 100557909
#This program will take input from the user, and test whether or not the numbers are congruent


print('Welcome to the Congruency Tester! Please enter numbers for variables: a, b, and n')
print('The program will determine if the numbers are congruent, and the values of a mod n, and b mod n')


 
a = int(input('Enter integer for a:'))
print('')
b = int(input('Enter integer for b:'))
print('')
n = int(input('Enter integer for n:'))
print('')

#Run calculation
amod = a % n
bmod = b % n

#Check congruency
if (((b % n) == 0) and ((a % n) == 0)):
    print('True')
else:
    print('False')

print('')


print('The value of a mod n is:',amod,'The value of b mod n is:', bmod)
