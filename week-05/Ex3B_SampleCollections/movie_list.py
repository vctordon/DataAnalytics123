#Top Movies List
my_top_movies = ["shrek", "shrek2", "shrek3", "shrek4"] 

#the len function includes a count for the amount of movies in my list above 
print(f"The list of my top movies includes my top {len(my_top_movies)} favorite movies.")
# result :"The list of my top movies includes my top 4 favorite movies."


#--------------------------------------------------------------


#Another Top Movie List
top_films =[ "Spider-Man", "Ironman", "Hulk", "CaptainAmerica" ] 

print(top_films)
#Using sort function to sort list of top films in alphabetical order
print(sorted(top_films))

#ordering sort this way provides the same results as above
top_films.sort()
print(top_films)

#adding film using append
top_films.append("Dr.Strange")
# now my top films shows results for 5 movies 
print(f"The list of my favorite movies now includes my {len(top_films)} favorite movies.")
print()
print(top_films)
print()
#sorting in alphabetical order including added film
top_films.sort() 
print(top_films)

#----------------------------------------------------------