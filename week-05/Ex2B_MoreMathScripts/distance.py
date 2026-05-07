#How do you calculate the distance between coordinates (x1, y1) and (x2, y2)? 
#Hint: You'll need to look up how to calculate a square root in Python, which may involve a function from the math module.
#Code the script for calculating this distance in a file named distance.py

#distance.py
import math

#gather the input 
x1 = 2
y1 = 3
x2 = 6
y2 = 7

#calculate distance 
distance = math.sqrt((x2-x1)** 2 +(y2-y1) ** 2)

print(f"the distance between the two points is {distance:.2f}")