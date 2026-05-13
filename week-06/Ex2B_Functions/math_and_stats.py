
import random
import math
import statistics

#----------------------------------------------


vals_1_100 = range(1,100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k = 200)
radius = random.randint(3,10)
pi = math.pi

# what each variable is doing 
#vals_1_100: numbers 1–99
#vals_sample: 75 unique values (no repeats)
#vals_choices: 200 values with repeats allowed
#radius: random circle radius
#pi: π value from math module

#----------------------------------------------
# Experimenting with a subset of integers 1-100
sample_sum = sum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)


# Experimenting with a superset of 200 values, integers 1-100

choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

circle_area = pi * (radius ** 2)
area_rounded_up = math.ceil(circle_area)
area_rounded_down = math.floor(circle_area)

print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:",sample_sum)
print("average of 75 sample values:",sample_avg)
print("median of 75 sample values", sample_median)

print("\n")


print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_avg)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_stdev)
print("Variance of 200 values:", choices_variance)

print('\n')


print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_up}")
print(f"Radius = {radius}, area = {area_rounded_down}")
