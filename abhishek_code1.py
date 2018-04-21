# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(1,10):
    if i % 2 ==0 :
        print (i)
    elif i % 3==0:
        print (i)   
## to do the conversion
print ( "conversion of miles into kilometers")
def convert(miles):
    return 1.6* miles
    
    
c=convert(2)
print ("miles into kilometers is :")
print (c)
## to again convert meter into centimeter
def mintocm(meters):
    return 100* meters
    
d= mintocm(5)
print ("the meters in the centimetes is:")
print (d)
for i in range(1,10):
    print (i)

# to display prime or composite
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
s = isPrime(7)
print (s)
if s == True :
    print("the number is prime")
else:
    print ("composite")
    








def convert(n):
    return 2*n
r = convert(2)
print (r)

parrot = "Norwegian Blue"

print (parrot.lower())
print (parrot.upper())


day = 6
print ("03 - %day - 2019") % (day)
# 03 - 6 - 2019
print( "03 - %02d - 2019") % (day)
# 03 - 06 - 2019

   
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            