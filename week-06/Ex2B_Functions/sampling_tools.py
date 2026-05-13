import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp','Surge Protector']

#4A)Goal: Pick ONE random product.
product_of_the_day = random.choice(products)
print("Product of the Day: ", product_of_the_day)
#this code selects 1 product at random using random.choice

#4B)Goal: Pick 3 different products, with no repeats.
survey_products = random.sample(products,3)
print("Products selected for usability survery:", survey_products)
#this code selects 3 products at random with no duplicates and uses random.sample 

#4C)Shuffle the entire list randomly
random.shuffle(products)
print("Shuffled product list for presentation:", products)
#this code randomly shuffles results 

#4D)Goal: Generate a random number between 50 and 300 (inclusive).
daily_transactions = random.randint(50,300)
print("Simulated daily transaction count:", daily_transactions)
#this code will pick a point from 50 - 300 as a possible value

