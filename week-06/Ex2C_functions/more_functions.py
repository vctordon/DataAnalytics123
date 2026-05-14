def display_mailing_label(name,address,city,state,zip):

    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
    print()  # blank line for spacing


display_mailing_label("Victoria Ordonez", "123 Main St", "Charlotte", "NC", "28202")

display_mailing_label("Jane Doe", "123 Oak Ave", "Atlanta", "GA", "30303")

#-----------------------------------------------------

def add_numbers(*numbers):
    result = sum(numbers)

    expression = " + ".join(str(num) for num in numbers)

    print(f"{expression} = {result}")

add_numbers(5)
add_numbers(2 , 3)
add_numbers(1 , 2 , 3 , 4 , 5)

# ------------------------------------------------------------

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")

    elif amount_paid == total_due:
        print("Change Due: $0")

    else:
        remaining = total_due - amount_paid
        print(f"Remaining Balance: ${remaining}")

    print()  # spacing

display_receipt(50, 80)
display_receipt(40, 40)
display_receipt(60, 30)