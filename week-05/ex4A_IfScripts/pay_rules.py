# setting pay variables 

pay_rate = 12.50
hours_worked = 20

# calculating pay
if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else: gross_pay = hours_worked * pay_rate

print ("hourly pay", pay_rate)
print()
print("your total gross pay is", round(gross_pay,2))

