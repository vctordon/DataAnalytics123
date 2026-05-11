#SAVING VARIABLES

bank_balance = 100.00
saving_goal = 500.00
weekly_saving = 50.00

#SAVING LOOP
while bank_balance < saving_goal:
    bank_balance += weekly_saving

if bank_balance >= saving_goal * 0.75:
    treat_cost = 20.00
    bank_balance -= treat_cost

print("So close! after treating myself, my balance is up to ", round(bank_balance,2))

elif bank_balance >= savings_goal / 2:
        print("Almost there! This week my balance is up to", round(bank_balance, 2))

    else:
        print("This week my balance increased to", round(bank_balance, 2))

# -------------------------
# GOAL MET
# -------------------------
print("Goal met! My current balance is", round(bank_balance, 2))
