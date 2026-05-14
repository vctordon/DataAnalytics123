
class Restaurant:
    """A class to represent a restaurant and track customers and ratings."""
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []
        
    def add_num_served(self):
        num = int(input("How many customers served today? "))
        self.number_served += num
        
    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")
        
    def customer_rating(self):
        while True:
            rating = input("Rate your experience (1-5): ")
            
            # check if input is integer
            if rating.isdigit():
                rating = int(rating)
                
                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating)
                    
                    avg = sum(self.customer_ratings) / len(self.customer_ratings)
                    
                    print(f"Your rating was {rating}. The average rating for this restaurant is {avg:.2f}")
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            else:
                print("Invalid input. Please enter a whole number (1-5).")


# Create restaurants
rest1 = Restaurant("Olive Garden", "Italian")
rest2 = Restaurant("Sushi House", "Japanese")
rest3 = Restaurant("Taco Fiesta", "Mexican")


# TEST number served
print("\n--- Testing number served ---")
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()


# TEST ratings
print("\n--- Testing ratings ---")
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()



