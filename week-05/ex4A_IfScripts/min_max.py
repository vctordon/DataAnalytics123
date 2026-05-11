# Assigning variables 

a = 50
b = 20
c = 30


#DETERMINE SMALLEST:

if a <= b and a <= c :
    smallest = a 
elif b <= a and b <= c :
    smallest = b
else:
    smallest = c

#-----------------------

#DETERMINE LARGEST: 
if a >= b and a >= c:
    largest = a
elif b >= a and b >=c:
    largest = b
else:
    largest = c

#----------------------
print("the smallest value is", smallest)
print("the largest value is", largest)


