# SCRIPT
# Defining known values
# food_cost = 79.25 
# tax = 6.54 
# tip = 12.00 
# Calculate the unknown total_due = food_cost + tax + tip 
# Display the results print("The total due is " + str(total_due))
#----------------------------------------------------------------
# Defining known values 
food_cost = 79.25
tax = 6.54
tip = 12.00

total = food_cost + tax + tip
print("The total amount due is " + str(total))

#the str() function is used to convert a value into a string
#----------------------------------------------------------------
#print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip)) 
#print("Total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + str(tip))
print("Total due is " + str(total))

#Adding second decimal to tip print statement 
#print("Tip is " + format(tip, ".2f"))
print("Tip is " + format(tip, ".2f"))

print(f"The tip on a ${food_cost:.2f} restaurant bill is ${tip:.2f}")
#------------------------------------------------------------------------

