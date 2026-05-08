#A colleague has shared the following contact records, 
#but the data is a mess, with inconsistent capitalization and currency 
#symbols that need to be cleaned up before it can be used:
#-----------------------------------------------------------------
name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000"
#---------------------------------------------
#converting names to lowercase using .lower
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())
#-------------------------------------------
#Capitalizing first/last using .title
print(name_1.title())
print(name_2.title())
print(name_3.title())
#--------------------------------------------
#removing $ from salary using .replace
salary_1_fixed = salary_1.replace("$"," ")
print(salary_1_fixed)
print(type(salary_1_fixed)) # result str
salary_2_fixed = salary_2.replace("$"," ")
print(salary_2_fixed)
print(type(salary_2_fixed)) # result str
#--------------------------------------------
#using .replace and int
salary_1_int = int(salary_1_fixed.replace(",",""))
print(salary_1_int) #82500 - code above removed the comma and the replace before removed $
salary_2_int = int(salary_2_fixed.replace(",",""))
print(salary_2_int) #74000 - code above removed the comma and the replace before removed $
#---------------------------------------------
