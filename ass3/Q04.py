# Write a Python program to find the point of minima of Rosenbrock function using Gradient Descent method taking initial solution (0,0). Rosenbrock function is defined below.f(x, y) = (1 − x)^2 + (y − x^2)^2
def rosenbrock(x, y):
    return (1 - x)**2 + (y - x**2)**2

def gradient_rosenbrock(x, y):
    df_dx = -2 * (1 - x) - 4 * x * (y - x**2)
    df_dy = 2 * (y - x**2)
    return df_dx, df_dy

def gradient_descent(x0, y0, learning_rate, epsilon, max_iterations):
    x = x0
    y = y0
    iteration = 0
    while True:
        df_dx, df_dy = gradient_rosenbrock(x, y)
        x_new = x - learning_rate * df_dx
        y_new = y - learning_rate * df_dy
        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon or iteration >= max_iterations:
            break
        x = x_new
        y = y_new
        iteration += 1
    return x, y
x0 = 0
y0 = 0
learning_rate = 0.001
epsilon = 1e-6
max_iterations = 10000
minima_x, minima_y = gradient_descent(x0, y0, learning_rate, epsilon, max_iterations)

print("Point of minimum (x, y):", minima_x, minima_y)
print("Minimum value of the Rosenbrock function:", rosenbrock(minima_x, minima_y))
