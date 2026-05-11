
pay_rate = 25.00
hours_worked = 38
filing_status = "single"   # "single" or "joint"

if hours_worked > 40:
    regular_pay = 40 * pay_rate
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    weekly_gross_pay = regular_pay + overtime_pay
else:
    weekly_gross_pay = hours_worked * pay_rate

#-------------------------

# ANNUAL GROSS PAY
weeks_per_year = 52
annual_gross_pay = weekly_gross_pay * weeks_per_year

#-------------------------

# TAX RATING

if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20

#-------------------------


elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20
else:
    tax_rate = 0
    print("Invalid filing status")



if filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.00
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

else: tax_rate = 0
print("Invalid filing status")


# TAX WITHHELD & NET PAY
# -------------------------
weekly_tax_withheld = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - weekly_tax_withheld

# -------------------------
# OUTPUT
# -------------------------
print("You worked", hours_worked, "hours this period.")
print("Because you earn $", pay_rate, "per hour, your gross weekly pay is $", round(weekly_gross_pay, 2))
print("Your filing status is", filing_status)
print("Your tax withholding for the week is $", round(weekly_tax_withheld, 2))
print("Your net pay is $", round(net_pay, 2))
