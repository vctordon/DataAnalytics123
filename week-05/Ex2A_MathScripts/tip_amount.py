#Figure out the formula and what the script would look like
# # making up example values as needed. 
# (If you need inspiration
#  what was your approximate restaurant bill the last time you ate at a restaurant?)

#The tip on a $[number] restaurant bill is $[number]
#-----------------------------------------------------------------------------------
#Calculating script
bill_amount = 40.00
tip_percent = .18

#Calculate tip
tip_amount = bill_amount * tip_percent

print('The tip on a $',bill_amount,'bill is $',round(tip_amount,2))
print(f"The tip on a ${bill_amount:.2f} restaurant bill is ${tip_amount:.2f}")