# Write a Python program to find the point of minima of function using Gradient Descent method taking initial solution x0 = 2.f(x) = x^2 + sin(x)

import math
def f(x):
    return x**2 + math.sin(x)
def df(x):
    return 2*x + math.cos(x)

def gradient_descent(x0, learning_rate, epsilon, max_iterations):
    x = x0
    iteration = 0
    while True:
        x_new = x - learning_rate * df(x) 
        if abs(x_new - x) < epsilon or iteration >= max_iterations:
            break 
        x = x_new
        iteration += 1
    return x
x0 = 2
learning_rate = 0.1
epsilon = 1e-6
max_iterations = 1000
minima = gradient_descent(x0, learning_rate, epsilon, max_iterations)

print("Point of minimum:", minima)
print("Minimum value of the function:", f(minima))
