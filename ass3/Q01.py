# 1. Find the derivate of using limit of the difference coeffficient method at x = 1. f(x) = e^x^2 + sin(x) − tan(x) + log(x)
import math

def f(x):
    return math.exp(x**2) + math.sin(x) - math.tan(x) + math.log(x)

def derivative_at_1():
    h = 0.0001
    x = 1
    df_dx = (f(x + h) - f(x)) / h
    return df_dx

derivative = derivative_at_1()
print("f(x) = e^x^2 + sin(x) − tan(x) + log(x)")
print("The derivative of f(x) at x = 1 is approximately:", derivative)
