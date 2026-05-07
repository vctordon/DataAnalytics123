#The diameter of a given circle is the same as the 
# day of your birthday (not the month, just the day). Figure out the formula, refresh your recollection of the difference between diameter and radius, 
#and figure out what the script should look like.


#The area of a circle with radius [number] is [number]
#------------------------------------------------
Diameter = 21 #Diameter is day of dob
Radius = Diameter / 2 #Radius equals half of the diameter

import math
area = math.pi * Radius ** 2

print(f'The area of a circle with radius {Radius} is {area:.2f}')

#f"" → allows variables inside { }
#:.2f → shows two decimal places
#Always import math before using math.pi

