# Step 1: open file in append mode
f = open("about_me.txt", "a")

# Step 2: close the file
f.close()

#Name: Victoria Ordonez
#Place of birth: New York
#Pets: I had a dog named Princess
#Travel for 1 week: Japan
#Live for a year: Japan


f = open("about_me.txt", "a")

# Add new information
f.write("\nPerfect night out: I would go to a nice dinner and then watch a movie with friends.\n")

# Close the file
f.close()

