# Candy store candy list / flavors

Candy_Type = ("Gummy Bears", "Skittles", "Gum Drops")
Candy_Fruit_Flavors = ("grape", "orange", "strawberry")

print(Candy_Type)
print(Candy_Fruit_Flavors)
print()
#------------------------------------------------------------

#Creating candy store variations
#using the add function brings candytype and candy flavor together candy combo using set function creates set
Candy_combos = set()
Candy_combos.add(Candy_Type[0] + "-" + Candy_Fruit_Flavors[0])
Candy_combos.add(Candy_Type[1] + "-" +Candy_Fruit_Flavors[1])
Candy_combos.add(Candy_Type[2] + "-" + Candy_Fruit_Flavors[2])
print(Candy_combos)
print()
# ------------------------------------------------------------
#Output showing candy combo set
print("Todays candy combinations include", (Candy_combos))
#-------------------------------------------------------------