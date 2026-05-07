#How long will it take a savings account worth X 
#to double in value based on an interest rate of IR? 
#(Hint: Look up the “rule of 72”)
#Your current savings is [number]. 
#At a [number]% interest rate, 
#your savings account will be worth [number] in [number] years


#RULE 72 DEFINITION: 
#The Rule of 72 is a simple mental math shortcut 
#used to estimate how long it will take 
#for an investment, savings, or any value growing 
#at a fixed rate to double in size
#----------------------------------------------------------------

#Rule 72 calculation 
Savings = 5000
interest_rate = 0.06 #6%

years_double = 72 / (interest_rate * 100)
doubled_savings = Savings * 2 


print("Your current savings is {}. At a {} interest rate, your savings account will be worth {} in {} years"
    .format(
        format(Savings, ".2f"),
        format(interest_rate, ".0%"),
        format(doubled_savings, ".2f"),
        format(years_double, ".1f")))
