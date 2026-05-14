# Creating variable to use the lambda function to double

doubler = lambda n: n * 2
# print the results all results will be doubled
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

#----------------------------------------------

tripler = lambda n:n * 3
# print the results all results will be tripled
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


def multiplier(factor):
    return lambda n: n * factor


print("Other multiplier tests:")
print()
# Create variables using multiplier()
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


print("String test with quadrupler:")
print(quadrupler('hi'))  # 'hihihihi'

print("string test with sextupler")
print(sextupler("I <3 NY."))

