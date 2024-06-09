# Write a Python program to find gradient of Rosenbrock function using limit of the difference coeffficient method at the point (1,2). Rosenbrock function is defined below. f(x, y) = (1 − x)^2 + 100(y − x^2)^2


def rosenbrock(x, y):
    return (1 - x)**2 + 100 * (y - x**2)**2

def partial_derivative_x(x, y, h=1e-5):
    return (rosenbrock(x + h, y) - rosenbrock(x, y)) / h

def partial_derivative_y(x, y, h=1e-5):
    return (rosenbrock(x, y + h) - rosenbrock(x, y)) / h

def gradient_at_point(x, y):
    df_dx = partial_derivative_x(x, y)
    df_dy = partial_derivative_y(x, y)
    return df_dx, df_dy

x = 1
y = 2
gradient = gradient_at_point(x, y)
print("Gradient of Rosenbrock function at point (1, 2):", gradient)
