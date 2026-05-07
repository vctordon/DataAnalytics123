#How do you calculate your net worth given your assets and debts? 

#A: Start by brainstorming: What are “assets” that would need to be included in this calculation? What about “debts”?

#B: Discuss and figure out the formula and what the script would look like, making up example values as needed

#Your total assets are [number]
#Your total debts are [number]
#Your net worth is [number]

#-----------------------------------------------------------------------
#VALUES: 
#ASSETS 
Cash = 3000
Investment = 10000
Homevalue = 200000

Total_Assets = Cash + Investment + Homevalue


#DEBTS
Mortgagebalance = 150000
Creditcard = 2000

Total_Debts = Mortgagebalance + Creditcard

#NETWORTH
Net_Worth = Total_Assets - Total_Debts


print('Your total assets are', (Total_Assets))
print('Your total debts are', (Total_Debts))
print('Your total networth is', (Net_Worth))
#-----------------------------------------------------------------------

