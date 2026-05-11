# If basics 

#starting variables 
x=100
y=20

# A)

if x/y == 5:
    print("x divided by y is 5")
    x = 1 
else: print("are the variables set up correctly?") # output: "X divided by y is 5"
#----------------------------------------------------------------------------------
# B)

if x*y == y:
    print("now x times y is y")
    x = 10
else: print("whoops,x equals", x) # output: "now x times y is y"
#----------------------------------------------------------------------------------
# C)

if x < y:
    print("x is less than y")
    x = x*2
else: print("uh oh, x is not less than y") # output: uh oh, x is not less than y
#-----------------------------------------------------------------------------------
#D)

if x > y:
    print("how is x greater than y??")
else: print("x is NOT greater than y") # output: "x is NOT greater than y"
#-----------------------------------------------------------------------------------
#E)

print("The final value of x is", x, "and the final value of y is", y)

#------------------------------------------------------------------------------------
