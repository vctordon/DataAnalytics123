
class Restaurant:
    """A class to represent a restaurant and its basic information."""
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Create restaurant objects# Create Olive Garden", "Italian food")
rest1 = Restaurant("Olive Garden", "Italian food")
print()
rest2 = Restaurant("Sushi House", "Japanese food")
print()
rest3 = Restaurant("Taco Fiesta", "Mexican food")


# Call methods for each restaurant
rest1.describe_rest()
print()

rest1.rest_open()
print()

rest2.describe_rest()
print()


rest2.rest_open()
print()


rest3.describe_rest()
print()

rest3.rest_open()
print()



class Restaurant:
    """A class to represent a restaurant and its basic information."""
    
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")



# Create restaurant objects
rest1 = Restaurant("Olive Garden", "Italian food")
rest2 = Restaurant("Sushi House", "Japanese food")
rest3 = Restaurant("Taco Fiesta", "Mexican food")


# Call methods
rest1.describe_rest()
print()
rest1.rest_open()
print()
rest2.describe_rest()
print()
rest2.rest_open()
print()
rest3.describe_rest()
print()
rest3.rest_open()
print()
