#how do you do this in python There are X people going on a tour.
#Charter vans seat 15 passengers each. 
#Vans cost $250 per day to rent (including the driver’s pay). 
#How many vans do you need? How much will it cost to rent vans? 
#What is the cost if you split it per person? 

#How much money did your script say you had to charge per person?
#If you multiply that out, how much did you collect?
#How mcuh were the vans?
#Why do you have leftover money?

#RENTAL 
import math

# Number of people

people = 30

#constants
Seat_per_van = 15
Cost_per_van = 250

#Calculations
vans_needed = math.ceil(people / Seat_per_van)
total_cost = vans_needed * Cost_per_van
Cost_per_person = total_cost / people

#output
print(f"Vans needed: {vans_needed}") 
print(f"Total van cost: ${total_cost:.2f}")
print(f"Cost per person: ${Cost_per_person:.2f}")
