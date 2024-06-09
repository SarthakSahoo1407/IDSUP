# Let X be a binomial random variable with parameters n = 100 and p = 0.6. Write a Python program
# to find the approximate probability that:
# 1. X lies above 60.
# 2. X lies between 50 and 70.
# using normal approximation to binomial distribution


import math

def binomial_mean(n, p):
    return n * p

def binomial_variance(n, p):
    return n * p * (1 - p)

def normal_approximation(x, mean, variance):
    std_deviation = math.sqrt(variance)
    z = (x - mean) / std_deviation
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))  
n = 100
p = 0.6
mean = binomial_mean(n, p)
variance = binomial_variance(n, p)

x_above_60 = 60
prob_above_60 = 1 - normal_approximation(x_above_60, mean, variance)
print("Probability that X lies above 60:", prob_above_60)

x_between_50_and_70 = 70
x_between_50_and_70_lower = 50
prob_between_50_and_70 = normal_approximation(x_between_50_and_70, mean, variance) - normal_approximation(x_between_50_and_70_lower, mean, variance)
print("Probability that X lies between 50 and 70:", prob_between_50_and_70)
