# Description: This script tests various numeric 
# conversion techniques 
# Author: Sam Q. Newprogrammer


a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a)
print(type(a)) #String Type
print()
print(b)
print(type(b)) #String Type
print()
print(c)
print(type(c)) #String Type
print()
print(d)
print(type(d)) #String Type
print()


#a) Cast as integer using int()
#b) Cast as float using float()
#c) For variable a,try casting into a float then integer
# like this: int(float(a))
#---------------------------------------------------------------------

#TESTING A
#print(int(a)) #did not work
print(float(a)) #works output 101.1
#STRIP A:
print(a.strip()) #works prints 101.1

#---------------------------------------

#TESTING B
print(int(b)) #works
print(float(b)) #works and outputs 55.0

#---------------------------------------

#TESTING C
#print(int(c)) #did not work
#print(float(c)) #did not work
print(c) #works

#SLICING C:
c_slice = c[0:3]
c_int = int(c_slice)
print(c_int) #works prints 402

#---------------------------------------

#TESTING D
#print(int(d)) #did not work
#print(float(d)) #did not work
print(d) #works 
#STRIP D:
print(d.strip()) #works output Number 5 

#SLICING D:
d_slice = d[-2]
d_int = int(d_slice)
print(d_slice) #works prints 5











